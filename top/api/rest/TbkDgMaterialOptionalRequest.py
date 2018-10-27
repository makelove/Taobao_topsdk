# -*- coding: utf-8 -*-
'''
Created by auto_sdk on 2018.04.02
参考：
https://doc.alidayu.com/docs/api.htm?apiId=35896
'''
from top.api.base import RestApi


class TbkDgMaterialOptionalRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None  # mm_xxx_xxx_xxx的第三位
        self.material_id = None  # 官方的物料Id(详细物料id见：https://tbk.bbs.taobao.com/detail.html?appId=45301&postId=8576096)，不传时默认为2836
        self.cat = None  # 后台类目ID，用,分割，最大10个，该ID可以通过taobao.itemcats.get接口获取到
        self.end_price = None
        self.ip = None  # ip参数影响邮费获取，如果不传或者传入不准确，邮费无法精准提供

        self.start_tk_rate = None
        self.end_tk_rate = None  # 淘客佣金比率上限，如：1234表示12.34%

        self.has_coupon = None
        self.is_overseas = None  # 是否海外商品，设置为true表示该商品是属于海外商品，设置为false或不设置表示不判断这个属性
        self.is_tmall = None
        self.itemloc = None  # 所在地
        self.page_no = None
        self.page_size = None
        self.platform = None  # 链接形式：1：PC，2：无线，默认：１
        self.q = None  # 查询词
        self.sort = None  # 排序_des（降序），排序_asc（升序），销量（total_sales），淘客佣金比率（tk_rate）， 累计推广量（tk_total_sales），总支出佣金（tk_total_commi），价格（price）
        self.start_dsr = None  # 店铺dsr评分，筛选高于等于当前设置的店铺dsr评分的商品0-50000之间
        self.start_price = None
        self.npx_level = None  # 牛皮癣程度，取值：1:不限，2:无，3:轻微

    def getapiname(self):
        return 'taobao.tbk.dg.material.optional'
