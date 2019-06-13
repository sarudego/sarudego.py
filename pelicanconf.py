#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/voce'

AUTHOR = 'Sarudego'
SITENAME = 'Sarudego'
SITESUBTITLE = 'A personal blog.'
SITEURL = ''
# SITEURL = 'www.sarudego.es'
# ABSOLUTE_URL = SITEURL

DEFAULT_METADATA = {}
KEYWORDS = ''

PATH = 'content'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'

# USER_LOGO_URL = 'sazut.jpg'
USER_LOGO_URL = '/pictures/sazut.jpg'
# FAVICON = 'images/favicon.ico'
STATIC_PATHS = ['pictures', 'extra/favicon-16x16.png', 'extra/sazut.jpg']
EXTRA_PATH_METADATA = {
    'extra/favicon-16x16.png': {
        'path': 'favicon-16x16.png'
    },
    'extra/sazut.jpg': {
        'path': 'sazut.jpg'
    }
}
# PAGE_PATHS = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

# Voce theme config
GLOBAL_KEYWORDS = ''
FUZZY_DATES = True
GOOGLE_ANALYTICS_ID = ''
USER_LOGO_URL = ''
MANGLE_EMAILS = ''

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

# Blogroll
LINKS = (
    ('INDEX', 'localhost:8000'),
    # ('ABOUT ME', 'pages/about'),
    ('PROJECTS', SITEURL + '/pages/projects'),
)

# Social widget
SOCIAL = (
    ('Email', 'mailto:sruizdegopegui[at]gmail[dot]com'),
    ('GitHub', 'https://github.com/sarudego'),
)

# PLUGINS_PATHS = ['plugins']
PLUGINS = ['themes.voce.plugins.assets']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = ''
