# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 18:44
# @Author  : play4fun
# @File    : 淘宝客维权退款订单查询1.py
# @Software: PyCharm

"""
淘宝客维权退款订单查询1.py:
"""
import traceback
from datetime import datetime


from top.api import TbkRelationRefundRequest
from top import appinfo

from config import appkey, secret

req = TbkRelationRefundRequest()
req.set_app_info(appinfo(appkey, secret))


# req.search_option = ''
req.search_type = 1

req.biz_type = 1
req.refund_type = 2

req.start_time = "2019-03-23 00:00:00"
req.page_no = 1
req.page_size = 20

try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
    '''无权限
    errorcode=11 message=Insufficient isv permissions subcode=isv.permission-api-package-limit submsg=scope ids is 11655 381 application_host=11.11.13.104 service_host=top011011013104.na61
    '''