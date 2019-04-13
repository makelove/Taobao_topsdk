# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 20:15
# @Author  : play4fun
# @File    : 渠道-淘宝客邀请码生成-社交.py
# @Software: PyCharm

"""
渠道-淘宝客邀请码生成-社交.py:
"""
import traceback
from datetime import datetime

from top.api import TbkScInvitecodeGetRequest
from top import appinfo
import config

req = TbkScInvitecodeGetRequest()
req.set_app_info(appinfo(config.appkey, config.secret))

req.session = config.session
req.relation_id = 112343
req.relation_app = "common"
req.code_type = 1

try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
    '''
    errorcode=11 message=Insufficient isv permissions subcode=isv.permission-api-package-limit submsg=scope ids is 11655 381 application_host=11.1.181.93 service_host=top011001181093.center.na62

    '''
