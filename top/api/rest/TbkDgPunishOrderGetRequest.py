# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 18:55
# @Author  : play4fun
# @File    : TbkDgPunishOrderGetRequest.py
# @Software: PyCharm

"""
TbkDgPunishOrderGetRequest.py:
taobao.tbk.dg.punish.order.get( 处罚订单查询 -导购-私域用户管理专用 )
https://open.taobao.com/api.htm?docId=42050&docType=2
新增处罚订单查询API，提供媒体调用查询能力。这个是给媒体自己用的
"""

from top.api.base import RestApi


class TbkDgPunishOrderGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)

        self.af_order_option = None
        self.span = None  # 查询时间跨度，不超过1小时，单位是秒

        self.relation_id = None  # 渠道管理id, 父订单号/子订单号/relation_id/special_id 至少传一个
        self.tb_trade_id = None  # 子订单号,父订单号/子订单号/relation_id/special_id 至少传一个
        self.tb_trade_parent_id = None  # 父订单号,父订单号/子订单号/relation_id/special_id 至少传一个
        self.special_id = None  # 会员运营id,父订单号/子订单号/relation_id/special_id 至少传一个

        self.violation_type = None  # 处罚类型：1 店铺淘客，2其他
        self.punish_status = None  # 处罚状态，0 正常，1 待处罚，2冻结

        self.start_time = None  # 2018-10-10 00:00:00 查询开始时间，以taoke订单创建时间开始
        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'taobao.tbk.dg.punish.order.get'
