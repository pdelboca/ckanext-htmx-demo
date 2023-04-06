from collections import OrderedDict
from flask import Blueprint
from werkzeug.datastructures import MultiDict

from ckan import plugins
from ckan.plugins import toolkit

htmx = Blueprint('htmx', __name__)

@htmx.route('/htmx/search/')
def search():
    context = {}
    q = toolkit.request.args.get('q', '*:*')
    sort = toolkit.request.args.get(u'sort', None)
    facets = _get_search_facets()
    details = _get_search_details()
    data_dict = {
        'q': q,
        'rows': 10,
        'sort': sort,
        'facet.field': list(facets.keys()),
        'fq': details['fq'].strip(),
        'extras': details['search_extras'],
    }
    results = toolkit.get_action('package_search')(context, data_dict)
    extra_vars = {
        "packages": results["results"],
        "search_facets": results["search_facets"],
        "count": results["count"],
    }
    if toolkit.request.headers.get('HX-Request') == 'true':
        return toolkit.render('package/htmx_search.html', extra_vars=extra_vars)
    return toolkit.render('package/htmx_index.html', extra_vars=extra_vars)



def _get_search_facets():
    """Return the search facets.
    
    This function will return all the facets that are available for the search in the
    secondary block.
    """
    facets = OrderedDict()

    org_label = toolkit.h.humanize_entity_type(
        'organization',
        toolkit.h.default_group_type('organization'),
        'facet label') or toolkit._('Organizations')

    group_label = toolkit.h.humanize_entity_type(
        'group',
        toolkit.h.default_group_type('group'),
        'facet label') or toolkit._('Groups')

    default_facet_titles = {
        'organization': org_label,
        'groups': group_label,
        'tags': toolkit._('Tags'),
        'res_format': toolkit._('Formats'),
        'license_id': toolkit._('Licenses'),
    }

    for facet in toolkit.h.facets():
        if facet in default_facet_titles:
            facets[facet] = default_facet_titles[facet]
        else:
            facets[facet] = facet

    for plugin in plugins.PluginImplementations(plugins.IFacets):
        facets = plugin.dataset_facets(facets, "dataset")

    return facets


def _get_search_details():
    """Copied from ckan/views/dataset.py"""
    fq = ''

    # fields_grouped will contain a dict of params containing
    # a list of values eg {'tags':['tag1', 'tag2']}

    fields = []
    fields_grouped = {}
    search_extras = MultiDict()

    for (param, value) in toolkit.request.args.items(multi=True):
        if param not in ['q', 'page', 'sort'] \
                and len(value) and not param.startswith('_'):
            if not param.startswith('ext_'):
                fields.append((param, value))
                fq += ' %s:"%s"' % (param, value)
                if param not in fields_grouped:
                    fields_grouped[param] = [value]
                else:
                    fields_grouped[param].append(value)
            else:
                search_extras.update({param: value})

    extras = dict([
        (k, v[0]) if len(v) == 1 else (k, v)
        for k, v in search_extras.lists()
    ])
    return {
        'fields': fields,
        'fields_grouped': fields_grouped,
        'fq': fq,
        'search_extras': extras,
    }