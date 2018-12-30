# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 16:52
# @Author  : play4fun
# @File    : 创建淘口令1.py
# @Software: PyCharm

"""
创建淘口令1.py:
http://open.taobao.com/docs/api.htm?apiId=31127

平时用这个

这个能转换【优惠券-长链接】
"""

from top.api import TbkTpwdCreateRequest
from top import appinfo
import config

req = TbkTpwdCreateRequest()
req.set_app_info(appinfo(config.appkey, config.secret))

# req.text='半身裙套装女2018新款时尚潮 港风省心搭配女装上衣短裙两件套夏'
req.text = '雾妆上衣 清水溪原创女装改良汉服刺绣交领上衣复古针织棉外套春'
# req.url='https://item.taobao.com/item.htm?id=567873872517'
req.url = 'https://s.click.taobao.com/t?e=m%3D2%26s%3Dea3gZ6NOUrscQipKwQzePOeEDrYVVa64LKpWJ%2Bin0XLjf2vlNIV67ozKWyu6bnIwRku8%2Bpj6eJalldgrEKAMDXnQOo8damCBj2X6i1GYASI3b1dKfLeFUEg0aHp6CeiCqnVeK%2FmooCGS4mRUfswfBlsIB3jWKyiYxgxdTc00KD8%3D&pvid=10_114.244.180.148_65971_1546169008143'
req.logo = 'https://img.alicdn.com/bao/uploaded/i4/113740699/TB2aYQ8b41YBuNjy1zcXXbNcXXa_!!113740699.jpg_220x220_.webp'
# req.tpwd_param

try:
    resp = req.getResponse()
    import json

    ds = json.dumps(resp)
    print(ds)
    print(resp['tbk_tpwd_create_response']['data']['model'])
    # {"tbk_tpwd_create_response": {"data": {"model": "\uffe5cqtQbS9y8gR\uffe5"}, "request_id": "41yh5cdyclhc"}}
    # ￥cqtQbS9y8gR￥
except Exception as e:
    print(e)
    '''
    {"tbk_tpwd_create_response": 
        {"data": 
             {'model': '￥8fNsbpXtbyr￥'},
            "request_id": "53m2arr978ek"
        }
    }
    '''
