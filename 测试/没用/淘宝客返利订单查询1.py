# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 17:20
# @Author  : play4fun
# @File    : 淘宝客返利订单查询1.py
# @Software: PyCharm

"""
淘宝客返利订单查询1.py:
activity_id

errorcode=40 message=Missing required arguments:activity_id subcode=None submsg=None application_host=11.11.49.179 service_host=top011011049179.na62

"""
from top.api import TbkDgNewuserOrderGetRequest
import top,config
req=TbkDgNewuserOrderGetRequest()
req.set_app_info(top.appinfo(config.appkey, config.secret))

req.fields = "tb_trade_parent_id,tb_trade_id,num_iid,item_title,item_num,price,pay_price,seller_nick,seller_shop_title,commission,commission_rate,unid,create_time,earning_time"
req.start_time = "2019-03-15 00:00:00"
req.span = 600
req.page_no = 1
req.page_size = 100

try:
    resp= req.getResponse()
    import json

    ds = json.dumps(resp)
    print(ds)
except Exception as e:
    print(e)