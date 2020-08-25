from script import compute_top_languages, generate_language_markdown

import pytest


@pytest.mark.parametrize(
    "total,languages,expected",
    [
        (100, {'Py': 0}, [{'name': 'Py', 'percentage': 0}]),
        (100, {'Py': 50}, [{'name': 'Py', 'percentage': 50}]),
        (100, {'Py': 100}, [{'name': 'Py', 'percentage': 100}]),
        *[(100, {'Py': x}, [{'name': 'Py', 'percentage': x}]) for x in range(100)],
        (200, {'Py': 0}, [{'name': 'Py', 'percentage': 0}]),
        (200, {'Py': 100}, [{'name': 'Py', 'percentage': 50}]),
        (200, {'Py': 200}, [{'name': 'Py', 'percentage': 100}]),
        *[(200, {'Py': 2 * x}, [{'name': 'Py', 'percentage': x}]) for x in range(100)],
        (100, {'Py': 100, 'JS': 0}, [{'name': 'Py', 'percentage': 100}, {'name': 'JS', 'percentage': 0}]),
        (100, {'Py': 0, 'JS': 100}, [{'name': 'JS', 'percentage': 100}, {'name': 'Py', 'percentage': 0}]),
        (100, {'Py': 50, 'JS': 50}, [{'name': 'Py', 'percentage': 50}, {'name': 'JS', 'percentage': 50}]),
        (200, {'Py': 100, 'JS': 100}, [{'name': 'Py', 'percentage': 50}, {'name': 'JS', 'percentage': 50}]),
    ]
)
def test_compute_top_languages(total, languages, expected):
    top_languages = compute_top_languages(total, languages)

    assert top_languages == expected


@pytest.mark.parametrize(
    "top_languages,expected",
    [
        ([{'name': 'Py', 'percentage': 0}], '* Py: 0%\n'),
        ([{'name': 'Py', 'percentage': 100}], '* Py: 100%\n'),
        *[([{'name': 'Py', 'percentage': x}], '* Py: {}%\n'.format(x)) for x in range(100)],
        ([{'name': 'JS', 'percentage': 0}], '* JS: 0%\n'),
        ([{'name': 'JS', 'percentage': 100}], '* JS: 100%\n'),
        *[([{'name': 'JS', 'percentage': x}], '* JS: {}%\n'.format(x)) for x in range(100)],
        ([{'name': 'Py', 'percentage': 100}, {'name': 'JS', 'percentage': 0}], '* Py: 100%\n* JS: 0%\n'),
        ([{'name': 'JS', 'percentage': 100}, {'name': 'Py', 'percentage': 0}], '* JS: 100%\n* Py: 0%\n')
    ]
)
def test_generate_language_markdown(top_languages, expected):
    markdown = generate_language_markdown(top_languages)

    assert markdown == expected
