#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


from topic import *

topic = Topic()
for x in topic.topics:
  print x[0] + " " + str(x[1])