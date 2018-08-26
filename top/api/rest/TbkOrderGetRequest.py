# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 11:23
# @Author  : play4fun
# @File    : TbkOrderGetRequest.py
# @Software: PyCharm

"""
TbkOrderGetRequest.py:
需要申请权限，否则不能用
"""

from top.api.base import RestApi


class TbkOrderGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        # self.adzone_id = None
        # self.site_id = None
        #
        self.fields = None#需返回的字段列表
        self.start_time = None#订单查询开始时间
        self.span = None#订单查询时间范围,单位:秒,最小60,最大600,默认60
        self.page_no = None
        self.page_size = None
        self.tk_status = None#非必须，订单状态，1: 全部订单，3：订单结算，12：订单付款， 13：订单失效，14：订单成功； 订单查询类型为‘结算时间’时，只能查订单结算状态
        self.order_query_type = None#订单查询类型，创建时间“create_time”，或结算时间“settle_time”

    def getapiname(self):
        return 'taobao.tbk.order.get'
