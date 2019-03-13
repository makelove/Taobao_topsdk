# -*- coding: utf-8 -*-
'''
Created by auto_sdk on 2018.01.05
https://doc.alidayu.com/docs/api.htm?spm=a3142.7395905.4.32.7cd71239B99Oix&apiId=31106


阿里妈妈推广券信息查询
阿里妈妈推广券信息查询。传入商品ID+券ID，或者传入me参数，均可查询券信息
'''
from top.api.base import RestApi


class TbkCouponGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.activity_id = None
        self.item_id = None
        self.me = None

    def getapiname(self):
        return 'taobao.tbk.coupon.get'
