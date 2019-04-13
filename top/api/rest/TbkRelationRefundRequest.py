# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 18:36
# @Author  : play4fun
# @File    : TbkRelationRefundRequest.py
# @Software: PyCharm

"""
TbkRelationRefundRequest.py:
文档
taobao.tbk.relation.refund( 淘宝客维权退款订单查询-私域用户管理专用 )
https://open.taobao.com/api.htm?spm=a219a.7386797.0.0.120a669aJKTj8X&source=search&docId=40121&docType=2
渠道管理和会员运营管理专用


"""

from top.api.base import RestApi


class TbkRelationRefundRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)

        self.search_option = None
        self.search_type = None  # 1-维权发起时间，2-订单结算时间（正向订单），3-维权完成时间，4-订单创建时间

        self.biz_type = None  # 1代表渠道关系id，2代表会员关系id
        self.refund_type = None  # 1 表示2方，2表示3方
        self.start_time = None  # 2018-10-10 00:00:00	开始时间

        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'taobao.tbk.relation.refund'
