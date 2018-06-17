# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from rest_framework import routers

from earth.views import DealViewSet, LocationViewSet

admin.autodiscover()

# router = routers.SimpleRouter()
# router.register(r'earth/deal', DealViewSet)
# router.register(r'earth/location', LocationViewSet)


urlpatterns = [
    url(r'^admin/',  include(admin.site.urls)),
    # url(r'^', include(router.urls)),
]
