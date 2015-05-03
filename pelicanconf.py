#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import OrderedDict

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
DEFAULT_DATE = 'fs' # use filesystem's mtime

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

# niu-x2 theme translating settings
NIUX2_AUTHOR_TRANSL = '作者'
NIUX2_404_TITLE_TRANSL = '404'
NIUX2_404_INFO_TRANSL = '请求页面未找到!'
NIUX2_TAG_TRANSL = '标签'
NIUX2_ARCHIVE_TRANSL = '存档'
NIUX2_ARCHIVE_UPDATEDATE_TRANSL = '存档 (按修改时间)'
NIUX2_CATEGORY_TRANSL = '分类'
NIUX2_TAG_CLEAR_TRANSL = '清空'
NIUX2_TAG_FILTER_TRANSL = '过滤标签，不妨试试[0-9]{3}'
NIUX2_HEADER_TOC_TRANSL = '目录'
NIUX2_SEARCH_TRANSL = '搜索'
NIUX2_SEARCH_PLACEHOLDER_TRANSL = '按回车开始搜索...'
NIUX2_COMMENTS_TRANSL = '评论'
NIUX2_PUBLISHED_TRANSL = '发布时间'
NIUX2_LASTMOD_TRANSL = '最后修改'
NIUX2_PAGE_TITLE_TRANSL = '页面'
NIUX2_RECENT_UPDATE_TRANSL = '最近修改'
NIUX2_HIDE_SIDEBAR_TRANSL = '隐藏侧边栏'
NIUX2_SHOW_SIDEBAR_TRANSL = '显示侧边栏'
NIUX2_REVISION_HISTORY_TRANSL = '修订历史'
NIUX2_VIEW_SOURCE_TRANSL = '查看源文件'

NIUX2_CATEGORY_MAP = {
    'python': ('Python', 'icon-code'),
    'she-ying': ('摄影', 'icon-briefcase'),
    'shu-mei-pai': ('树莓派', 'icon-leaf'),
    'misc': ('其他', 'icon-coffee'),
}

NIUX2_HEADER_SECTIONS = [
    ('关于', 'about me', '/about.html', 'icon-anchor'),
    ('标签', 'tags', '/tag/', 'icon-tag'),
    ('存档', 'archives', '/archives.html', 'icon-archive'),
]

NIUX2_FOOTER_LINKS = [
    ('关于', 'about me', '/about.html', ''),
]

NIUX2_FOOTER_ICONS = [
    ('icon-envelope-o', 'my email address', 'mailto: whypro@live.com'),
    ('icon-github-alt', 'my github page', 'http://github.com/whypro'),
    # ('icon-rss', 'subscribe my blog', '/feed.xml'),
]

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
