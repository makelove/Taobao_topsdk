# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 18:37
# @Author  : play4fun
# @File    : 导购信息搜索1.py
# @Software: PyCharm

"""
导购信息搜索1.py:
参考：https://doc.alidayu.com/docs/api.htm?apiId=35896

佣金
优惠券
"""

import top.api

# req = top.api.TbkDgMaterialOptionalRequest(url, port)
# req.set_app_info(top.appinfo(appkey, secret))

import traceback, json

from top.api import TbkDgMaterialOptionalRequest
from top import appinfo

from config import appkey, secret,pid

req2 = TbkDgMaterialOptionalRequest()
req2.set_app_info(appinfo(appkey, secret))

req2.start_dsr = 10

req2.page_size = 20
req2.page_no = 1
req2.platform = 1
# req.end_tk_rate = 1234 #TODO 设置一个区间
# req.start_tk_rate = 1234
req2.end_price = 10
req2.start_price = 20
# req.is_overseas = False#报错
# req.is_tmall = False
req2.sort = "tk_rate_des"
# req.itemloc = "杭州"
req2.cat = "16,18"
req2.q = "女装"
req2.material_id = 2836
# req.has_coupon = True
# req.ip = "13.2.33.4"
req2.adzone_id = pid
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
        if item['coupon_remain_count']>0:
            print(item)
        else:
            print('No')
except Exception as e:
    print(e)
    '''
{
    "category_id": 50010850,
    "category_name": "连衣裙",
    "commission_rate": "7000",
    "commission_type": "ZX",
    "coupon_id": "",
    "coupon_info": "",
    "coupon_remain_count": 0,
    "coupon_total_count": 0,
    "include_dxjh": "false",
    "include_mkt": "false",
    "info_dxjh": "{}",
    "item_url": "https://item.taobao.com/item.htm?id=578808249791",
    "level_one_category_id": 16,
    "level_one_category_name": "女装/女士精品",
    "num_iid": 578808249791,
    "pict_url": "https://img.alicdn.com/bao/uploaded/i4/833450195/O1CN011DJLhEdyid51HxL_!!0-item_pic.jpg",
    "provcity": "浙江 杭州",
    "reserve_price": "10",
    "seller_id": 833450195,
    "shop_dsr": 50000,
    "shop_title": "店主VX: zzq518899",
    "short_title": "微商女装一手货源招代理一件代发",
    "title": "微商女装一手货源招代理一件代发欧泰货服装加盟厂家直销韩版高端",
    "tk_total_commi": "0",
    "tk_total_sales": "0",
    "url": "//s.click.taobao.com/t?e=m%3D2%26s%3DemdAmL8lW2McQipKwQzePOeEDrYVVa64lwnaF1WLQxlyINtkUhsv0GqskRXq8a9LngqExHzB0EJwe9WqVoWbK6cpCeoIkU8NSlFUVq0truStrs69PUsRSCQjO9J4i5qlSD99OVE0eUgdcoJn23In8lUM%2FAmuI%2FSW5UwZupjob08v3l3uT7Tftfr%2BRoxyUbBM3IwrKPeZEd%2FfkS3Jgs7fdqJn5AyUbPoV&scm=null&pvid=100_11.182.80.100_19664_4071540466096948180&app_pvid=59590_11.11.60.245_338_1540466096944&ptl=floorId:2836;pvid:100_11.182.80.100_19664_4071540466096948180;app_pvid:59590_11.11.60.245_338_1540466096944&union_lens=lensId:0b0b3cf5_0c79_166aaef3c4e_361d",
    "user_type": 0,
    "volume": 0,
    "white_image": "",
    "zk_final_price": "10"
}    
    '''
