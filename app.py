#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys

VERSION = '0.0.1'

class UI_Form(object):
  '''
  App's controller
  '''
  def setupUi(self, Form):
    Form.setObjectName("Form")
    Form.resize(600,400)

def main():
  app = QtWidgets.QApplication(sys.argv)
  Form = QtWidgets.QWidget()
  ui = UI_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
