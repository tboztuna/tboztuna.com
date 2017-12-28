#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tolga Boztuna'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR

SITENAME = u'Software Engineering Blog by Tolga Boztuna'
SITEURL = 'http://tboztuna.com'
FEED_DOMAIN = 'http://tboztuna.com'

FAVICON = '/images/favicon.ico'

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

THEME = './themes/flex'

PATH = 'content'

ROBOTS = 'index, follow'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'en'

I18N_TEMPLATES_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/tboztuna'),
          ('github', 'https://github.com/tboztuna'),
          ('google', 'https://plus.google.com/109527849290886664803'),
          ('twitter', 'https://twitter.com/tboztuna'),
          ('rss', '//tboztuna.com/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = ''
ADD_THIS_ID = ''

STATUSCAKE = {
    'trackid': '',
    'days': 7,
    'rumid': 0,
    'design': 6,
}

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GOOGLE_ADSENSE = {
    'ca_id': '',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
