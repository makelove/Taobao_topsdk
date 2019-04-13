# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 11:19
# @Author  : play4fun
# @File    : 获取佣金和优惠券1.py
# @Software: PyCharm

"""
获取佣金和优惠券1.py:
使用2个api去查

不建议用
"""

from top.api import TbkItemInfoGetRequest, TbkDgMaterialOptionalRequest
from top import appinfo

from config import appkey, secret

req = TbkItemInfoGetRequest()
req.set_app_info(appinfo(appkey, secret))

req2 = TbkDgMaterialOptionalRequest()
req2.set_app_info(appinfo(appkey, secret))

req.num_iids = "577221455881"
req.platform = 2  # 链接形式：1：PC，2：无线，默认：１

try:
    resp = req.getResponse()

    it = resp['tbk_item_info_get_response']['results']['n_tbk_item'][0]
    print(it)
    '''
{'cat_leaf_name': '大码女装',
 'cat_name': '女装/女士精品',
 'item_url': 'https://h5.m.taobao.com/awp/core/detail.htm?id=577221455881',
 'material_lib_type': '',
 'nick': '广州柔星专业大码女装',
 'num_iid': 577221455881,
 'pict_url': 'https://img.alicdn.com/bao/uploaded/i2/3013701358/O1CN011Lu0JUOoBV9CpWD_!!3013701358.jpg',
 'provcity': '广东 广州',
 'reserve_price': '65',
 'seller_id': 3013701358,
 'small_images': {'string': ['https://img.alicdn.com/i2/3013701358/O1CN011Lu0JVlIA3JxtKV_!!3013701358.jpg',
   'https://img.alicdn.com/i2/3013701358/O1CN011Lu0JWKHHkqVdjm_!!3013701358.jpg',
   'https://img.alicdn.com/i4/3013701358/O1CN011Lu0JWt91aSzSWa_!!3013701358.jpg',
   'https://img.alicdn.com/i4/3013701358/O1CN011Lu0JWWMFP8TxNM_!!3013701358.jpg']},
 'title': '秋冬新款羽绒棉大码中年女装时尚休闲拼接夹棉中长棉衣长袖连衣裙',
 'user_type': 0,
 'volume': 44,
 'zk_final_price': '65'}    
    '''

    import json

    # ds = json.dumps(resp)
    # print(ds)

    #
    # req2.start_dsr = 10

    req2.page_size = 20
    req2.page_no = 1
    req2.platform = 1
    # req.end_tk_rate = 1234 #TODO 设置一个区间
    # req.start_tk_rate = 1234
    req2.end_price = it['zk_final_price']
    req2.start_price = it['zk_final_price']
    # req.is_overseas = False#报错
    # req.is_tmall = False
    req2.sort = "tk_rate_des"
    # req.itemloc = "杭州"
    req2.cat = "16,18"
    req2.q = it['title']
    req2.material_id = 2836
    # req.has_coupon = True
    # req.ip = "13.2.33.4"
    req2.adzone_id = 26807050116
    # req.need_free_shipment = True
    # req.need_prepay = True
    # req.include_pay_rate_30 = True
    # req.include_good_rate = True
    # req.include_rfd_rate = True
    # req.npx_level = 2
    # req.end_ka_tk_rate = 1234
    # req.start_ka_tk_rate = 1234
    # req.device_encrypt = "MD5"
    # req.device_value = "xxx"
    # req.device_type = "IMEI"
    try:
        resp = req2.getResponse()
        print(resp)
        print('\n')
        ds = json.dumps(resp)
        # print(ds)  # 成功
        print('----------')
        for item in resp['tbk_dg_material_optional_response']['result_list']['map_data']:
            if item['coupon_remain_count'] > 0:
                print(item)
            else:
                print('No')
    except Exception as e:
        print(e)

except Exception as e:
    print(e)
