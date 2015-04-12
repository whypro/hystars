#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'whypro'
SITENAME = 'hystars'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

DATE_FORMATS = {
    'zh': '%Y-%m-%d',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
# REVERSE_CATEGORY_ORDER = True
DEFAULT_CATEGORY = 'uncategorized'
DEFAULT_PAGINATION = 7

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
# disable author pages
# AUTHOR_SAVE_AS = ''
# AUTHORS_SAVE_AS = ''

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['/home/whypro/tools/pelican-plugins']
PLUGINS = ['better_figures_and_images']

# better_figures_and_images plugin settings
RESPONSIVE_IMAGES = True

# THEME = '/home/whypro/tools/pelican-themes/elegant'
THEME = 'notmyidea'

# notmyidea theme settings
SITESUBTITLE = ''
# GITHUB_URL = 'http://github.com/whypro/'
DISQUS_SITENAME = 'hystars'
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
