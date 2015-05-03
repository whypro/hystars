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
DEFAULT_CATEGORY = 'Misc'
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

PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_headings', 'niux2_lazyload_helper']

# extract_headings settings
import md5
def my_slugify(value, sep):
    m = md5.md5(value.encode('utf-8'))
    return m.digest().encode('hex')[:6]
MY_SLUGIFY_FUNC = my_slugify
MY_TOC_LIST_TYPE = 'ol'

# niux2_lazyload_helper settings
NIUX2_LAZY_LOAD = False
NIUX2_LAZY_LOAD_TEXT = 'orz 努力加载中'
NIUX2_LAZY_LOAD_ICON = 'icon-spin icon-spinner2'

def my_img_url_2_path(url):
    new_url = url.replace('{filename}', 'content')
    return new_url

MY_IMG_URL2PATH_FUNC = my_img_url_2_path


# better_figures_and_images plugin settings
RESPONSIVE_IMAGES = True

# THEME = 'themes/elegant'
# THEME = 'themes/niu-x2'
THEME = 'themes/niu-x2-sidebar'

# niu-x2 theme settings
JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension', ]
DISQUS_SITENAME = 'hystars'
NIUX2_FAVICON_URL = '/favicon.ico'

# notmyidea theme settings
# SITESUBTITLE = ''
# GITHUB_URL = 'http://github.com/whypro/'
# DISQUS_SITENAME = 'hystars'
# Blogroll
# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
# )
# Social widget
# SOCIAL = (
#     ('github', 'http://github.com/whypro'),
#     ('oschina', 'http://my.oschina.net/apoptosis'),
# )
