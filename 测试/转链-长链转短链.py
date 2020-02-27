# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 21:19
# @File    : 转链-长链转短链.py


"""
不能使用
转链-长链转短链.py:
https://open.taobao.com/api.htm?docId=27832&docType=2

top.api.base.TopException: errorcode=41 message=Invalid arguments:requests subcode=None submsg=None application_host=11.141.25.108 service_host=top011141025108.center.na62

Invalid arguments:requests
非法参数？

不知道搞什么
"""

import traceback

from top.api import TbkSpreadGetRequest
from top import appinfo

from config import appkey, secret, pid

req = TbkSpreadGetRequest()
req.set_app_info(appinfo(appkey, secret))

# 长链
req.requests = ["https://s.click.taobao.com/t?e=m%3D2%26s%3DSZrG7lN%2BR70cQipKwQzePOeEDrYVVa64K7Vc7tFgwiHjf2vlNIV67n%2FF6Mpn%2F%2FyrdgpT%2Fnt4ZAilldgrEKAMDfvtTsPa%2Bvw8FDXjhIkoffd7RTQd3LKg2nJi6DFpZGNc" \
           "%2Bht3wBcxEojXtv8oC884TT3gpsjoB0xH39doH8m%2FXrme7iFIr8Ii0c9kxRRHfUqm&scm=null&pvid=null&app_pvid=59590_11.26.37.213_531_1582801824591&ptl=floorId%3A17741&originalFloorId%3A17741&app_pvid%3A59590_11.26.37.213_531_1582801824591&union_lens=lensId%3APUB%401582801818%400b579756_0ee6_17086571260_b054%40025TMjT3NVuU9iOPDBPFeS83"]

try:
    resp = req.getResponse()
    import json

    print(resp)

    ds = json.dumps(resp)
    print(ds)  # 以前 成功
    '''
   
    '''
except Exception as e:
    print(e)
    traceback.print_exc()
