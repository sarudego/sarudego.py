#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/voce'

AUTHOR = 'Sarudego'
SITENAME = 'Sarudego\'s Web'
SITESUBTITLE = 'A personal blog.'
SITEURL = ''

DEFAULT_METADATA = {}
KEYWORDS = ''

PATH = 'content'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'

# FAVICON = 'images/favicon.ico'
STATIC_PATHS = ['images']
# PAGE_PATHS = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
    ('INDEX', 'https://sarudego.es'),
    ('ABOUT ME', 'pages/about'),
    ('PROJECTS', '/projects'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Email', 'mailto:sruizdegopegui[at]gmail[dot]com'),
    ('GitHub', 'https://github.com/sarudego'),
)

# PLUGINS_PATHS = ['plugins']
PLUGINS = ['themes.voce.plugins.assets']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
