import os

from profile_readme import get_github_context, ProfileGenerator


user = os.getenv('GITHUB_ACTOR', default='Robert-96')

context = get_github_context(user)
filters = {}


if __name__ == "__main__":
    ProfileGenerator.render(
        template_path="README-TEMPLATE.md",
        output_path="README.md",
        context=context,
        filters=filters
    )
