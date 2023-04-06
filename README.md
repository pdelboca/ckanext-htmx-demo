[![Tests](https://github.com/pdelboca/ckanext-htmx/workflows/Tests/badge.svg?branch=main)](https://github.com/pdelboca/ckanext-htmx/actions)

# ckanext-htmx-demo

This is a small extension to Demo how to integrate [HTMX](https://htmx.org/) and an [Hypermedia](https://hypermedia.systems/) approach to CKAN.


## Installation

To install ckanext-htmx:

1. Activate your CKAN virtual environment

2. Clone the source and install it on the virtualenv

    git clone https://github.com/pdelboca/ckanext-htmx.git
    cd ckanext-htmx
    pip install -e .
	pip install -r requirements.txt

3. Add `htmx` to the `ckan.plugins` setting in your CKAN
   config file

## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini ckanext/htmx/tests


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
