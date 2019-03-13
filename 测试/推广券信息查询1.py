# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 15:58
# @Author  : play4fun
# @File    : 推广券信息查询1.py
# @Software: PyCharm

"""
推广券信息查询1.py:

不知道怎样使用
"""

from top.api import TbkCouponGetRequest
from top import appinfo
from pprint import pprint
from config import appkey, secret

req = TbkCouponGetRequest()
req.set_app_info(appinfo(appkey, secret))

# req.me="nfr%2BYTo2k1PX18gaNN%2BIPkIG2PadNYbBnwEsv6mRavWieOoOE3L9OdmbDSSyHbGxBAXjHpLKvZbL1320ML%2BCF5FRtW7N7yJ056Lgym4X01A%3D"
req.item_id = 42245811160  # http://item.taobao.com/item.htm?spm=a219t.7900221/10.1998910419.d5d3d3cdd.392075a5HRxzk9&id=42245811160
# req.activity_id="sdfwe3eefsdf"

# 入参为空 ???

try:
    resp = req.getResponse()
    pprint(resp)

    # it = resp['tbk_item_info_get_response']['results']['n_tbk_item'][0]
    # pprint(it)

    # import json

    # ds = json.dumps(resp)
    # print(ds)
except Exception as e:
    print(e)
