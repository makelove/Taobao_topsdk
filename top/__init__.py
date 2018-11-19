# -*- coding: utf-8 -*-
'''
Created on 2012-6-29

@author: lihao
'''

__version__ = '18.11.18'
__author__ = 'play4fun <play4fun@foxmail.com>'

from top.api.base import sign


class appinfo(object):
    def __init__(self, appkey, secret):
        self.appkey = appkey
        self.secret = secret


def getDefaultAppInfo():
    pass


def setDefaultAppInfo(appkey, secret):
    default = appinfo(appkey, secret)
    global getDefaultAppInfo
    getDefaultAppInfo = lambda: default
