const csrfToken = $('meta[name=_csrf_token]').attr('content')

htmx.on('htmx:configRequest', (event) => {
  if (csrfToken) {
    event.detail.headers['x-csrftoken'] = csrfToken;
  }
});
