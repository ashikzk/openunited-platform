from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

from product_management.filters import display_role
from talent.templatetags.custom_filters import expertise_filter, get_ids


def environment(**options):
    env = Environment(**options)
    env.filters["get_ids"] = get_ids
    env.filters["expertise_filter"] = expertise_filter
    env.globals.update(
        {
            "static": staticfiles_storage.url,
            "url": reverse,
        }
    )

    env.filters["display_role"] = display_role
    return env
