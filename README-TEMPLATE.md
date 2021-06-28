<h2>Hi there 👋</h2>

<!-- This is just the base template, feel free to change it. -->

<p>
    I'm a developer based in <i>{{ USER.location }}</i>
    and I'm on GitHub since {{ USER.created_at|datetimeformat('%Y') }}
    with <a href="https://github.com/{{ USER.login }}?tab=repositories">{{ USER.public_repos }} public repositories</a>
    and <a href="https://github.com/{{ USER.login }}?tab=followers">{{ USER.followers }} followers</a>.
</p>

<h3>Top Languages</h3>

<ul>
{% for language in TOP_LANGUAGES %}
    <li><a href="https://github.com/search?q=user%3A{{ USER.login }}&l={{ language.name }}">{{ language.name }}</a>: {{ language.percentage }}%</li>
{% endfor %}
</ul>

{% if DEVTO %}
<h3>DEV.TO Posts</h3>

<ul>
{% for post in DEVTO[:5] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
{% endif %}

{% if GISTS %}
<h3>Pupular Gists</h3>

<ul>
{% for gist in GISTS[:5] %}
    {% if gist.description %}
        <li><a href="{{ gist.html_url }}">{{ gist.description }}</a></li>
    {% endif %}
{% endfor %}
</ul>
{% endif %}

<p><strong>Updated</strong>: <i>{{ TIME_STAMP|datetimeformat }}</i></p>
