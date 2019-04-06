# -*- coding: utf-8 -*-
'''
https://open.taobao.com/api.htm?docId=24515&docType=2
淘宝客商品查询
'''
from top.api.base import RestApi


class TbkItemGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.cat = None  # 后台类目ID，用,分割，最大10个，该ID可以通过taobao.itemcats.get接口获取到
        self.end_price = None
        self.end_tk_rate = None
        self.fields = None  # num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick
        self.is_overseas = None
        self.is_tmall = None
        self.itemloc = None  # 所在地
        self.page_no = None
        self.page_size = None
        self.platform = None
        self.q = None
        self.sort = None  # 排序_des（降序），排序_asc（升序），销量（total_sales），淘客佣金比率（tk_rate）， 累计推广量（tk_total_sales），总支出佣金（tk_total_commi）
        self.start_price = None
        self.start_tk_rate = None  # 淘客佣金比率上限，如：1234表示12.34%

    def getapiname(self):
        return 'taobao.tbk.item.get'
