# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 12:11
# @Author  : play4fun
# @File    : 选品库-获取宝贝信息1.py
# @Software: PyCharm

"""
选品库-获取宝贝信息1.py:
"""

from top.api import TbkUatmFavoritesItemGetRequest
from top import appinfo
from pprint import pprint
from config import appkey, secret, pid

req = TbkUatmFavoritesItemGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.adzone_id = pid  # 网站推广位
# req.unid = "3456" #可无
req.favorites_id = 19491050  # 从 选品库-获取列表1.py

req.platform = 1
req.page_size = 20
req.page_no = 2
req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick,shop_title,zk_final_price_wap,event_start_time,event_end_time,tk_rate,status,type"

try:
    resp = req.getResponse()
    pprint(resp)
except Exception as e:
    print(e)
    '''
    不知道是怎么回事??
    
    errorcode=15 message=Remote service error subcode=isv.invalid-parameter:favorites_id submsg=该favorite_id下没有宝贝 application_host=11.131.81.98 service_host=top011131081098.na62
    '''
