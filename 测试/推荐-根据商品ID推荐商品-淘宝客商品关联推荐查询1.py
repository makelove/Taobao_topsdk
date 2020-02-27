# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 18:33
# @Author  : play4fun
# @File    : 淘宝客商品关联推荐查询1.py
# @Software: PyCharm

"""
没有权限
淘宝客商品关联推荐查询1.py:

还是没有佣金，佣金率
还是没有优惠券

返回 列表

#不一定会有推荐
商品ID不存在，返回 {'tbk_item_recommend_get_response': {'request_id': '3qx1vn2sd259'}}
"""
from pprint import pprint
from top.api import TbkItemRecommendGetRequest
from top import appinfo

from config import appkey, secret

req = TbkItemRecommendGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,volume"
req.num_iid = "605650440548"
req.platform = 2  # 链接形式：1：PC，2：无线，默认：１
req.count = 10

try:
    resp = req.getResponse()
    import json

    # ds = json.dumps(resp, indent=2)
    # print(ds)
    pprint(resp, indent=2)
    #
    list1 = resp['tbk_item_recommend_get_response']['results']['n_tbk_item']
    pprint(list1[0])
except Exception as e:
    print(e)
    '''
{'item_url': 'http://h5.m.taobao.com/awp/core/detail.htm?id=41704016130',
 'num_iid': 41704016130,
 'pict_url': 'https://img.alicdn.com/tfscom/i1/TB1jhfqIVXXXXXEXpXXXXXXXXXX_!!0-item_pic.jpg',
 'provcity': '广东 广州',
 'reserve_price': '388.00',
 
 'small_images': {'string': ['https://img.alicdn.com/tfscom/i4/1883687207/TB2L4.iaFXXXXbzXXXXXXXXXXXX_!!1883687207.jpg',
                             'https://img.alicdn.com/tfscom/i2/1883687207/TB208UcaFXXXXX3XpXXXXXXXXXX_!!1883687207.jpg',
                             'https://img.alicdn.com/tfscom/i4/1883687207/TB2rbcdaFXXXXXZXpXXXXXXXXXX_!!1883687207.jpg',
                             'https://img.alicdn.com/tfscom/i2/1883687207/TB2jk3OvJRopuFjSZFtXXcanpXa_!!1883687207.jpg']},
                             
 'title': '韩语琳空间春夏2019女装韩版修身名媛OL包臀打底连衣裙时尚礼服裙',
 'user_type': 1,
 'volume': 10,
 'zk_final_price': '199.00'}
    '''
