import re

def add_param_or_remove_it_if_exist(url, key, value):
    """Add a parameter to the URL or remove it if it already exists.
    
    It is used to htmx_facet_list.html to help with the URL attribute
    of the selected facet.
    """
    value = value.replace(" ", "%20")
    # regex to match key=value or &key=value
    pattern = f"([&?]){key}={value}"
    active = False
    match = re.search(pattern, url)
    if match:
        active = True
        url = re.sub(pattern, "", url)
    else:
        url += '&' + key + '=' + value
    # check if the parameter was added at the end of the URL
    if '?' not in url:
        url = url.replace('&', '?', 1)
    return url, active


def remove_param_if_exist(url, key, value):
    """Remove a parameter from the URL if it exists.
    
    This is user in htmx_search.html to remove the `q` and `sort` parameter from
    the URL. For some reason, htmx does not remove the `q` parameter from the
    URL when a new search is done, causing the `&q=search_term` to be appended 
    each time a user does a query.

    This may be a bug in htmx, but I am not sure.
    """
    value = value.replace(" ", "%20")
    pattern = f"([&?]){key}={value}"
    match = re.search(pattern, url)
    if match:
        url = re.sub(pattern, "", url)
    # check if the parameter was added at the end of the URL
    if '?' not in url:
        url = url.replace('&', '?', 1)
    return url
