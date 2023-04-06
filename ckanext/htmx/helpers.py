import re

def add_param_or_remove_it_if_exist(url, key, value):
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
    """Remove a parameter from the URL if it exists."""
    value = value.replace(" ", "%20")
    pattern = f"([&?]){key}={value}"
    match = re.search(pattern, url)
    if match:
        url = re.sub(pattern, "", url)
    # check if the parameter was added at the end of the URL
    if '?' not in url:
        url = url.replace('&', '?', 1)
    return url
