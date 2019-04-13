# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 07:22
# @Author  : play4fun
# @File    : 获取淘宝联盟选品库列表1.py
# @Software: PyCharm

"""
获取淘宝联盟选品库列表1.py:
没有权限

top.api.base.TopException:
errorcode=11
message=Insufficient isv permissions
subcode=isv.permission-api-package-limit
submsg=scope ids is 11655 381

application_host=11.1.241.156 service_host=top011001241156.center.na62


"""

import traceback

from top.api import TbkUatmFavoritesGetRequest
from top import appinfo

from config import appkey, secret

req = TbkUatmFavoritesGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.page_no = 1
req.page_size = 20
req.fields = "favorites_title,favorites_id,type"
req.type = 1

try:
    resp = req.getResponse()
    import json

    print(resp)

    ds = json.dumps(resp)
    print(ds)
except Exception as e:
    print(e)
    print(traceback.format_exc())
