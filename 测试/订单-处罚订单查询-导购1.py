# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 19:01
# @Author  : play4fun
# @File    : 处罚订单查询-导购1.py
# @Software: PyCharm

"""
处罚订单查询-导购1.py:
"""
import traceback
from datetime import datetime

from top.api import TbkDgPunishOrderGetRequest
from top import appinfo

from config import appkey, secret

req = TbkDgPunishOrderGetRequest()
req.set_app_info(appinfo(appkey, secret))

# req.af_order_option = ''
req.span = 60 * 60 * 24 * 30  # 1个月

req.relation_id = 1
req.tb_trade_id = 2
req.tb_trade_parent_id = 2
req.special_id = 2
req.violation_type = 2
req.punish_status = 0

req.start_time = "2019-03-23 00:00:00"
req.page_no = 1
req.page_size = 20

try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
    '''无权限
    errorcode=11 message=Insufficient isv permissions subcode=isv.permission-api-package-limit submsg=scope ids is 11655 381 application_host=11.11.166.75 service_host=top011011166075.na62
    '''
