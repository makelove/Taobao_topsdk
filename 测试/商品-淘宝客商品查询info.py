# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 20:32
# @Author  : play4fun
# @File    : 淘宝客商品查询info.py
# @Software: PyCharm

"""
没有权限
淘宝客商品查询info.py:
http://open.taobao.com/api.htm?docId=24518&docType=2
用处不大,返回的信息太少

基本信息
"""

from top.api import TbkItemInfoGetRequest
from top import appinfo
import json
from config import appkey, secret

req = TbkItemInfoGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.num_iids = "605650440548"
req.platform = 2  # 链接形式：1：PC，2：无线，默认：１

try:
    resp = req.getResponse()

    it = resp['tbk_item_info_get_response']['results']['n_tbk_item'][0]
    print(it)

    # ds = json.dumps(resp)
    # print(ds)
except Exception as e:
    print(e)

'''
{'cat_leaf_name': '调和油', 'cat_name': '粮油米面/南北干货/调味品', 'item_url': 'https://detail.m.tmall.com/item.htm?id=530672343155', 'material_lib_type': '', 'nick': '天猫超市', 'num_iid': 530672343155, 'pict_url': 'https://img.alicdn.com/bao/uploaded/i2/725677994/TB2Zg7sc3TqK1RjSZPhXXXfOFXa_!!725677994-0-sm.jpg', 'provcity': '上海', 'reserve_price': '199.9', 'seller_id': 725677994, 'small_images': {'string': ['https://img.alicdn.com/i3/725677994/TB2lrBCpAKWBuNjy1zjXXcOypXa_!!725677994.jpg', 'https://img.alicdn.com/i2/725677994/TB2cDTdpDlYBeNjSszcXXbwhFXa_!!725677994.jpg', 'https://img.alicdn.com/i3/725677994/TB2eepSprGYBuNjy0FoXXciBFXa_!!725677994.jpg', 'https://img.alicdn.com/i1/725677994/TB2ZWfaeQZmBKNjSZPiXXXFNVXa_!!725677994.jpg']}, 'title': '金龙鱼 葵花籽清香食用油调和油5L*4 食用油', 'user_type': 1, 'volume': 10831, 'zk_final_price': '199.9'}
'''

'''
{
    "tbk_item_info_get_response": {
        "results": {
            "n_tbk_item": [
                {
                    "cat_leaf_name": "半身裙",
                    "cat_name": "女装/女士精品",
                    "item_url": "https://item.taobao.com/item.htm?id=569885087264",
                    "nick": "lee官方旗舰店",
                    "num_iid": 569885087264,
                    "pict_url": "https://img.alicdn.com/bao/uploaded/i1/928622636/TB1WI44ueuSBuNjy1XcXXcYjFXa_!!0-item_pic.jpg",
                    "provcity": "上海",
                    "reserve_price": "990",
                    "seller_id": 928622636,
                    "small_images": {
                        "string": [
                            "https://img.alicdn.com/i3/928622636/TB2hmPNXQT85uJjSZFgXXcZvVXa_!!928622636.jpg",
                            "https://img.alicdn.com/i3/928622636/TB2QtCRobsTMeJjSsziXXcdwXXa_!!928622636.jpg",
                            "https://img.alicdn.com/i2/928622636/TB2zArNXOP85uJjSZFKXXcw7FXa_!!928622636.jpg",
                            "https://img.alicdn.com/i2/928622636/TB2R3_CobsTMeJjSszhXXcGCFXa_!!928622636.jpg"
                        ]
                    },
                    "title": "Lee女装 2017秋冬新品双口袋时尚休闲牛仔背带短裙 L29975Z02898",
                    "user_type": 1,
                    "volume": 29,
                    "zk_final_price": "449"
                }
            ]
        },
        "request_id": "10fclulaghcir"
    }
}
'''
