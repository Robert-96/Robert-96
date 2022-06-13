import os

import requests
from profile_readme import get_github_context, ProfileGenerator


def get_devto_posts(user):
    url = 'https://dev.to/api/articles?username={}'.format(user)

    response = requests.get(url)
    data = response.json()
    posts = []

    for post in data[:5]:
        posts.append({
            'title': post.get('title'),
            'url': post.get('url')
        })

    return posts


if __name__ == "__main__":
    user = os.getenv('GITHUB_ACTOR', default='Robert-96')
    devto_user = os.getenv('DEVTO_USER', default='robert96')

    context = get_github_context(user)
    context["DEVTO"] = get_devto_posts(devto_user)
    context["social"] = {
        "Twitter": "https://twitter.com/dezmereanrobert",
        "LinkedIn": "https://www.linkedin.com/in/robert-dezmerean"
    }
    filters = {}

    ProfileGenerator.render(
        template_path="README-TEMPLATE.md",
        output_path="README.md",
        context=context,
        filters=filters
    )
