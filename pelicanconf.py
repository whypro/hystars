#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'whypro'
SITENAME = 'hystars'
SITEURL = ''
SITESUBTITLE = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

DATE_FORMATS = {
    'zh': '%Y-%m-%d',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/whypro'),
    ('OSChina', 'http://my.oschina.net/apoptosis'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
# GITHUB_URL = 'http://github.com/whypro/'
DISQUS_SITENAME = 'hystars'

STATIC_PATHS = ['images']

PLUGIN_PATHS = ['/home/whypro/tools/pelican-plugins']
PLUGINS = ['better_figures_and_images']
RESPONSIVE_IMAGES = True
