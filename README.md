# ckanext-htmx-demo

This is a small extension to Demo how to integrate [HTMX](https://htmx.org/) and an [Hypermedia](https://hypermedia.systems/) approach to CKAN.

After adding it to the plugins, navigate to `/htmx/search` for a faceted search implemented with HTMX. 

Note: You can still navigate to `/dataset/` to have a comparison with current CKAN search implementation.


## Installation

To install ckanext-htmx:

1. Activate your CKAN virtual environment

2. Clone the source and install it on the virtualenv

    git clone https://github.com/pdelboca/ckanext-htmx.git
    cd ckanext-htmx
    pip install -e .

3. Add `htmx` to the `ckan.plugins` setting in your CKAN config file


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
