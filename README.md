# ckanext-htmx-demo

This is a small extension to Demo how to integrate [HTMX](https://htmx.org/) and an [Hypermedia](https://hypermedia.systems/) approach to CKAN.

After adding it to the plugins, navigate to `/htmx/search` for a faceted search implemented with HTMX. 

Note: You can still navigate to `/dataset/` to have a comparison with current CKAN search implementation.


## Errors with `request.endpoint`

So far, this is an unstable for-demo purposes extension. If you encounter errors when trying to parse `request.endpoint` you can comment the code
in CKAN's core `flask_app.py`. (I'll fix this later):

```python
    # Disable CSRF protection if user was logged in via the Authorization
    # header
    if g.get("login_via_auth_header"):
        # Get the actual view function, as it might not match the endpoint,
        # eg "organization.edit" -> "group.edit", or custom dataset types
        endpoint = request.endpoint or ""
        #view = current_app.view_functions.get(endpoint)
        #dest = f"{view.__module__}.{view.__name__}"     # type: ignore
        #csrf.exempt(dest)

    # Set the csrf_field_name so we can use it in our templates
    g.csrf_field_name = config.get("WTF_CSRF_FIELD_NAME")

    # Provide g.controller and g.action for backward compatibility
    # with extensions
    #set_controller_and_action()

```


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
