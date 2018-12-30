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
        self.num_iids = None  # 商品ID串，用','分割，从taobao.tbk.item.get接口获取num_iid字段，最大40个
        self.platform = None  # 链接形式：1：PC，2：无线，默认：１
        self.adzone_id = None  # 只能是【网站广告位】
        self.unid = None  # 自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道
        self.dx = None

    def getapiname(self):
        return 'taobao.tbk.item.convert'
