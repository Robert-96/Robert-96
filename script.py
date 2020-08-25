import os
import json
import logging
from collections import defaultdict

import requests
import requests_cache
from dotenv import load_dotenv

load_dotenv()

LOG_FILE = os.getenv("LOG_FILE", None)
LOG_LEVEL = os.getenv("LOG_LEVEL", 'INFO')
LOG_FORMAT = os.getenv("LOG_FORMAT", '%(name)s:%(funcName)s:%(levelname)s - %(message)s')

USER = 'Robert-96'
README_TEMPLATE = 'README-TEMPLATE.md'

logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger()

requests_cache.install_cache('cache/github')


def get_languages():
    repos_raw = requests.get('https://api.github.com/users/{}/repos'.format(USER))
    repos = repos_raw.json()

    total = 0
    languages = defaultdict(int)

    for repo in repos:
        repo_languages_raw = requests.get(repo['languages_url'])
        repo_languages = repo_languages_raw.json()

        logger.info("{}: {}".format(
            repo['name'],
            json.dumps(repo_languages, sort_keys=True, indent=4)
        ))

        for language, value in repo_languages.items():
            total += value
            languages[language] += value

    return total, languages


def compute_top_languages(total, languages):
    top_languages = []

    for language, value in languages.items():
        top_languages.append({
            'name': language,
            'percentage': round(total / value, 2)
        })

    top_languages.sort(key=lambda x: x.get('percentage', 0), reverse=True)
    logger.info(json.dumps(top_languages, sort_keys=True, indent=4))

    return top_languages


def generate_language_markdown(top_languages):
    markdown = ''

    for language in top_languages:
        markdown += '* {}: {}%\n'.format(language.get('name'), language.get('percentage'))

    logger.info(markdown)

    return markdown


def get_latest_repo():
    repos_raw = requests.get('https://api.github.com/users/{}/repos'.format(USER))
    repos = repos_raw.json()
    repos = filter(lambda x: x.get('name') != USER, repos)

    latest_repo = max(repos, key=lambda x: x.get('updated_at'))
    logger.info(latest_repo['name'])

    return latest_repo


def update_readme():
    top_languages = compute_top_languages(*get_languages())
    top_languages_markdown = generate_language_markdown(top_languages)

    latest_repo = get_latest_repo()

    with open(README_TEMPLATE, 'r') as fp:
        readme = fp.read()

    with  open('README.md', 'w') as fp:
        fp.write(readme.format(
            TOP_LANGUAGES=top_languages_markdown,
            LATEST_REPO=latest_repo.get('name'),
            LATEST_REPO_URL=latest_repo.get('html_url'),
            LATEST_LANGUAGE=latest_repo.get('language', 'Python')
        ))


if __name__ == "__main__":
    update_readme()