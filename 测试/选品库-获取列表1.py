# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 12:06
# @Author  : play4fun
# @File    : 选品库-获取列表1.py
# @Software: PyCharm

"""
选品库-获取列表1.py:

为空
"""

from top.api import TbkUatmFavoritesGetRequest
from top import appinfo
from pprint import pprint
from config import appkey, secret

req = TbkUatmFavoritesGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.page_no = 1
req.page_size = 20
req.fields = "favorites_title,favorites_id,type"
req.type = 1

try:
    resp = req.getResponse()
    pprint(resp)
except Exception as e:
    print(e)

'''
{'tbk_uatm_favorites_get_response': 
    {'request_id': '8kzm0avbswbh',
      'results': {
                'tbk_favorites': 
                    [
                        {'favorites_id': 19485269,
                         'favorites_title': 'T1',
                         'type': 1}
                     ]
            },
      'total_results': 1
    }
}
'''
