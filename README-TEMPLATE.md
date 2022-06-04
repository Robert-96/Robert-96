<h2>Hi there 👋</h2>

<!-- This is just the base template, feel free to change it. -->

<p>
    I'm a Softwere Developer based in <i>{{ USER.location }}</i>
    and I'm on GitHub since {{ USER.created_at|datetimeformat('%Y') }}
    with <a href="https://github.com/{{ USER.login|urlencode }}?tab=repositories">{{ USER.public_repos }} public repositories</a>
    and <a href="https://github.com/{{ USER.login|urlencode }}?tab=followers">{{ USER.followers }} followers</a>.
</p>

<p>
    I made <a href="https://gitlab.com/altom/altwalker/altwalker">AltWalker</a> - an open source Model-Based Testing framework that supports running tests written in python3 and .NET/C#.
</p>

<h3>Top Languages</h3>

<ul>
{% for language in TOP_LANGUAGES %}
    <li><a href="https://github.com/search?q=user%3A{{ USER.login|urlencode }}&l={{ language.name|urlencode }}">{{ language.name }}</a>: {{ language.percentage }}%</li>
{% endfor %}
</ul>

{% if DEVTO %}
<h3>DEV.TO Posts</h3>

<ul>
{% for post in DEVTO %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
{% endif %}

<p><strong>Updated</strong>: <i>{{ TIME_STAMP|datetimeformat }}</i></p>
