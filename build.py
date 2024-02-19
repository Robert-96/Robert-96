"""A python script for generating a new profile README file."""

import os

import requests
from profile_readme import ProfileGenerator, get_github_context


def get_blog_posts():
    """Fetches the latest 5 blog posts from my blog."""

    url = "https://www.dezmereanrobert.com/posts/index.json"

    response = requests.get(url)
    data = response.json()

    return data["posts"][:5]


if __name__ == "__main__":
    user = os.getenv("GITHUB_ACTOR", default="Robert-96")

    context = get_github_context(user)
    context["POSTS"] = get_blog_posts()
    context["SOCIAL"] = {
        "Twitter": "https://twitter.com/dezmereanrobert",
        "LinkedIn": "https://www.linkedin.com/in/robert-dezmerean",
        "DEV.to": "https://dev.to/robert96",
        "Resume": "https://resume.dezmereanrobert.com",
        "Blog": "https://www.dezmereanrobert.com",
    }

    ProfileGenerator.render(
        template_path="README.jinja", output_path="README.md", context=context
    )
