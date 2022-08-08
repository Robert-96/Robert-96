<h2>Greetings, traveler! 👋</h2>

<!-- This is just the base template, feel free to change it. -->

<p>
    I'm a <strong>Software Developer</strong> based in <em>{{ USER.location }}</em>
    and I'm on GitHub since {{ USER.created_at|datetimeformat('%Y') }}.
</p>

<p>I'm a big fan of open source. My work is focused on developing tools that help developers and testers be more productive.</p>

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

----

<h4>Where you can to find me?</h4>

<p>
{% for title, url in social.items() %}
    {% if loop.index is ne(1) %}<span> <strong>•</strong> <span>{% endif %}<a href="{{ url }}">{{ title }}</a>
{% endfor %}
</p>

----

<p><strong>Updated</strong>: <em>{{ TIME_STAMP|datetimeformat }}</em></p>
