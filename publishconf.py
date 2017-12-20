#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *


SITEURL = 'http://swarna.info'
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico'
RELATIVE_URLS = False

FEED_ALL_ATOM =	'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True