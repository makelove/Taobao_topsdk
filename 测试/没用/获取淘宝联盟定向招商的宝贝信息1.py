# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 18:27
# @Author  : play4fun
# @File    : 获取淘宝联盟定向招商的宝贝信息1.py
# @Software: PyCharm

"""
获取淘宝联盟定向招商的宝贝信息1.py:
没用
"""

from top.api import TbkUatmEventItemGetRequest
from top import appinfo

from config import appkey, secret

req = TbkUatmEventItemGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.num_iids = "575968998243"
req.adzone_id = 34567  # 推广位id，需要在淘宝联盟后台创建；且属于appkey对应的备案媒体id（siteid），如何获取adzoneid，请参考：http://club.alimama.com/read-htm-tid-6333967.html?spm=0.0.0.0.msZnx5

req.platform = 1
req.page_size = 20
req.page_no = 1

req.unid = "3456"  # TODO
req.event_id = 123456  # 招商活动id

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick,shop_title,zk_final_price_wap,event_start_time,event_end_time,tk_rate,type,status"
try:
    resp = req.getResponse()
    import json

    ds = json.dumps(resp)
    print(ds)
except Exception as e:
    print(e)
