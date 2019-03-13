# -*- coding: utf-8 -*-
'''
Created by auto_sdk on 2017.06.17

https://open.taobao.com/api.htm?docId=24517&docType=2

pict_url 商品主图
reserve_price 商品一口价格
zk_final_price 商品折扣价格
volume 30天销量
provcity 宝贝所在地  发货地
user_type | 卖家类型，0表示集市，1表示商城
'''
from top.api.base import RestApi


class TbkItemRecommendGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.count = None  # 返回数量，默认20，最大值40
        self.fields = None
        self.num_iid = None
        self.platform = None

    def getapiname(self):
        return 'taobao.tbk.item.recommend.get'
