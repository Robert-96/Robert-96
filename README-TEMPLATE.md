<h2>Greetings, traveler! 👋</h2>

<!-- This is just the base template, feel free to change it. -->

<p>
    I'm a <strong>Software Developer</strong> based in <em>{{ USER.location }}</em>
    and I'm on GitHub since {{ USER.created_at|datetimeformat('%Y') }}
    with <a href="https://github.com/{{ USER.login|urlencode }}?tab=repositories">{{ USER.public_repos }} public repositories</a>
    and <a href="https://github.com/{{ USER.login|urlencode }}?tab=followers">{{ USER.followers }} followers</a>.
</p>

<p>I'm a big fan of open source. My work is focused on developing tools that helps developers and testers be more productive.</p>

<p>
    I made <strong><a href="https://gitlab.com/altom/altwalker/altwalker">AltWalker</a></strong> - an open source Model-Based Testing framework that supports running tests written in python3 and .NET/C#.
</p>

<p>
    When I'm not coding, I love drawing, reading and cooking.
</p>

<h3>Most Used Languages</h3>

<ul>
{% for language in TOP_LANGUAGES %}
    <li><a href="https://github.com/search?q=user%3A{{ USER.login|urlencode }}&l={{ language.name|urlencode }}">{{ language.name }}</a>: {{ language.percentage }}%</li>
{% endfor %}
</ul>

{% if DEVTO %}
<h3>Blog Posts</h3>

<ul>
{% for post in DEVTO %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
{% endif %}

<p><strong>Updated</strong>: <i>{{ TIME_STAMP|datetimeformat }}</i></p>
