# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from .views import home_page, robots_page, load_services
from .sitemaps import StaticSitemap

sitemaps = {
	'static': StaticSitemap
}

urlpatterns = [
	url(r'^$', home_page, name='index'),
	url(r'^load-services/$', load_services, name='load_services'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	url(r'^robots\.txt$', robots_page, name='robots')
]
