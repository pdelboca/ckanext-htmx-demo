from flask import Blueprint

from ckan.plugins import toolkit

htmx = Blueprint('htmx', __name__, url_prefix='/htmx')

@htmx.route('/dataset/')
def dataset():
    extra_vars = {}
    return toolkit.render('package/search.html', extra_vars=extra_vars)


@htmx.route('/search/')
def search():
    context = {}
    q = toolkit.request.args.get('search', '*:*')
    print(q)
    data_dict = {
        'q': q,
        'rows': 10,
    }
    results = toolkit.get_action('package_search')(context, data_dict)
    extra_vars = {
        "packages": results["results"],
    }
    if toolkit.request.headers.get('HX-Request') == 'true':
        return toolkit.render('snippets/package_list.html', extra_vars=extra_vars)
    return toolkit.render('package/search.html', extra_vars=extra_vars)