#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raveendra Swarna'
SITENAME = u"Swarna's Blog"
SITETITLE = AUTHOR
SITEURL = 'http://swarna.info'
SITESUBTITLE = 'Data Scientist / Cloud Specialist'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings on Statistics, Data Science, Programming, and Economics' % AUTHOR
SITELOGO = '//s.gravatar.com/avatar/5dc5ba59a94eeab2106ad9d397361b2c?s=120'
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico' 
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'America/Chicago'

I18N_TEMPLATES_LANG = 'en'
PATH = 'content'
STATIC_PATHS = ['images', 'figures']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

DEFAULT_DATE = 'fs'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Social widget
SOCIAL = (('twitter',   'https://twitter.com/swarnaravi'),
   ('github',   'https://github.com/swarnaravi'),
   ('linkedin',   'https://www.linkedin.com/in/swarnaravi'))

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
      ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10