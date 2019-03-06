# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 18:33
# @Author  : play4fun
# @File    : 淘宝客商品关联推荐查询1.py
# @Software: PyCharm

"""
淘宝客商品关联推荐查询1.py:
可以用
还是没有佣金

返回 列表
"""

from top.api import TbkItemRecommendGetRequest
from top import appinfo

from config import appkey, secret

req = TbkItemRecommendGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url"
req.num_iid = "568659766675"
req.platform = 2  # 链接形式：1：PC，2：无线，默认：１
req.count = 40

try:
    resp = req.getResponse()
    import json

    ds = json.dumps(resp)
    print(ds)
except Exception as e:
    print(e)
    '''
     {
        "item_url": "http://h5.m.taobao.com/awp/core/detail.htm?id=572151163766",
        "num_iid": 572151163766,
        "pict_url": "https://img.alicdn.com/tfscom/i1/587451667/TB23sxjrviSBuNkSnhJXXbDcpXa_!!587451667.jpg",
        "provcity": "浙江 杭州",
        "reserve_price": "598.00",
        "small_images": {
            "string": [
                "https://img.alicdn.com/tfscom/i3/587451667/TB2eGONiY3nBKNjSZFMXXaUSFXa_!!587451667.jpg",
                "https://img.alicdn.com/tfscom/i3/587451667/TB2AR.DtRyWBuNkSmFPXXXguVXa_!!587451667.jpg",
                "https://img.alicdn.com/tfscom/i1/587451667/TB2LKAUCYuWBuNjSszgXXb8jVXa_!!587451667.jpg",
                "https://img.alicdn.com/tfscom/i2/587451667/TB2jf3qvm8YBeNkSnb4XXaevFXa_!!587451667.jpg"
            ]
        },
        "title": "2018夏季新款女装时尚黑色V领拼接收腰A字裙中长款雪纺显瘦连衣裙",
        "user_type": 0,
        "zk_final_price": "168.00"
    },
    '''
