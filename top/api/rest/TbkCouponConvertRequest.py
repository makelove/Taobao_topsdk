# -*- coding: utf-8 -*-
'''
Created by auto_sdk on 2018.07.25
【导购】链接转换-根据商品ID获取该商品的优惠券
参考
http://open.taobao.com/api.htm?docId=29289&docType=2&scopeId=12486

'''
from top.api.base import RestApi


class TbkCouponConvertRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.item_id = None
        self.me = None  # 营销计划链接中的me参数
        self.platform = None

    def getapiname(self):
        return 'taobao.tbk.coupon.convert'
