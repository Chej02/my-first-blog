from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'Empleame_app.urls', name='www'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
)
