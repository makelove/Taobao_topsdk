# -*- coding: utf-8 -*-
'''

https://open.taobao.com/api.htm?docId=27832&docType=2

taobao.tbk.spread.get( 淘宝客-公用-长链转短链 )
￥免费 不需用户授权
输入一个原始的链接，转换得到指定的传播方式，如二维码，淘口令，短连接； 现阶段只支持短连接。

'''
from top.api.base import RestApi


class TbkSpreadGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.requests = None
        self.url = None

    def getapiname(self):
        return 'taobao.tbk.spread.get'
