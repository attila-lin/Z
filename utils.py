#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import json
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def getList(url):
  req = urllib2.urlopen(url)
  jsonstr = req.read()
  return json.loads(jsonstr)

