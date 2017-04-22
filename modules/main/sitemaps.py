#-*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'

	def items(self):
		return ['index']

	def location(self, item):
		return reverse(item)
