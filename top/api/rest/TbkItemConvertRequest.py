# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 16:08
# @Author  : play4fun
# @File    : TbkItemConvertRequest.py
# @Software: PyCharm

"""
TbkItemConvertRequest.py:
taobao.tbk.item.convert (淘宝客商品链接转换)
文档 http://open.taobao.com/doc2/apiDetail.htm?apiId=24516&scopeId=11653
要申请权限才能调用
"""

from top.api.base import RestApi

class TbkItemConvertRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.num_iids = None
        self.platform = None
        self.adzone_id = None
        self.unid = None
        self.dx = None

    def getapiname(self):
        return 'taobao.tbk.item.convert'