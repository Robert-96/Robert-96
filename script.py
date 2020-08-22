import json
from collections import defaultdict

import requests
import requests_cache

requests_cache.install_cache('cache/github')

USER = 'Robert-96'
README_TEMPLATE = 'README-TEMPLATE.md'


def get_languages():
    repos_raw = requests.get('https://api.github.com/users/{}/repos'.format(USER))
    repos = repos_raw.json()

    total = 0
    languages = defaultdict(int)

    for repo in repos:
        repo_languages_raw = requests.get(repo['languages_url'])
        repo_languages = repo_languages_raw.json()

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
    return top_languages


def generate_language_markdown(top_languages):
    markdown = ''

    for language in top_languages:
        markdown += '* {}: {}%\n'.format(language.get('name'), language.get('percentage'))

    return markdown


def update_readme():
    top_languages = compute_top_languages(*get_languages())
    top_languages_markdown = generate_language_markdown(top_languages)

    with open(README_TEMPLATE, 'r') as fp:
        readme = fp.read()

    with  open('README.md', 'w') as fp:
        fp.write(readme.format(TOP_LANGUAGES=top_languages_markdown))


if __name__ == "__main__":
    update_readme()