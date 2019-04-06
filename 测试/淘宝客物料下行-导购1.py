# -*- coding: utf-8 -*-
# @Time    : 2019-04-06 15:20
# @Author  : play4fun
# @File    : 淘宝客物料下行-导购1.py
# @Software: PyCharm

"""
淘宝客物料下行-导购1.py:



"""
from pprint import pprint
import traceback
from datetime import datetime
from top.api import TbkDgOptimusMaterialRequest
from top import appinfo

from config import appkey, secret, pid

req = TbkDgOptimusMaterialRequest()
req.set_app_info(appinfo(appkey, secret))

req.page_no = 1
req.page_size = 20
req.adzone_id = pid
req.item_id = 575317425603  # http://item.taobao.com/item.htm?id=575317425603

req.material_id = 3767#TODO 女装 3767

# req.device_value = "xxx"
# req.device_encrypt = "MD5"
# req.device_type = "IMEI"
#
# req.content_id = 323
# req.content_source = "xxx"


try:
    resp = req.getResponse()
    # print(resp)
    l = resp['tbk_dg_optimus_material_response']['result_list']['map_data']
    for it in l:
        pprint(it)
        print('-'*50)
except:
    print(traceback.format_exc())
    '''
    errorcode=15 message=Remote service error subcode=30001 submsg=非法的物料id 
    '''
'''
{'category_id': 50010850,
 'category_name': '连衣裙',
 'click_url': '//s.click.taobao.com/t?e=m%3D2%26s%3DzFlR4%2BEBXAVw4vFB6t2Z2ueEDrYVVa64Dne87AjQPk9yINtkUhsv0L4lM4GcrElNwZFsYLsVxmxHatIorvhTnDBUxNsqx3L7njzwEGq%2FDRvSkx9ROi4DlKXezsSnMpj3LrHGZgcOhECoyauY3EQuvVg2udsK8%2Fy5OemaFM5tHHYxZyjQcbVDhcnjRDTsxzJ6F9vcx87ZOorFxpfIaQw05sYOae24fhW0&scm=1007.15023.81719.0&pvid=fc0d76a5-b58a-4efb-849b-7e1a87aa8f87&app_pvid=59590_11.11.34.86_640_1554536012902&ptl=floorId:3767;pvid:fc0d76a5-b58a-4efb-849b-7e1a87aa8f87;app_pvid:59590_11.11.34.86_640_1554536012902&union_lens=lensId:0b0b2256_0cc3_169f1911ca1_0cc7',
 'commission_rate': '9.0',
 
 
 'coupon_amount': 40,
 'coupon_click_url': '//uland.taobao.com/coupon/edetail?e=iQk1qXVTzasNfLV8niU3R5TgU2jJNKOfNNtsjZw%2F%2FoI%2BPoLd9Z8OEFfkZwfQqR5NLspxGy3zBjap%2B7s0sowtFAwO1rtt%2FBLcKV87J25RfhQ9x3wfD33383sK1eK%2BmoM1bONkAIHspTroh%2BlW9XNZLsz%2BqQ6G6CH%2BBUu%2FPoKQNGRa6uwQqw6QIlzLQtwepDDS4ORKM8hl%2BPx%2BOHfs5nLQGA%3D%3D&&app_pvid=59590_11.11.34.86_640_1554536012902&ptl=floorId:3767;app_pvid:59590_11.11.34.86_640_1554536012902;tpp_pvid:fc0d76a5-b58a-4efb-849b-7e1a87aa8f87&union_lens=lensId:0b0b2256_0cc3_169f1911ca1_0cc7',
 'coupon_end_time': '1554825599000',
 'coupon_info': '满69.00元减40元',
 'coupon_remain_count': 87000,
 'coupon_share_url': '//uland.taobao.com/coupon/edetail?e=iQk1qXVTzasNfLV8niU3R5TgU2jJNKOfNNtsjZw%2F%2FoI%2BPoLd9Z8OEFfkZwfQqR5NLspxGy3zBjap%2B7s0sowtFAwO1rtt%2FBLcKV87J25RfhQ9x3wfD33383sK1eK%2BmoM1bONkAIHspTroh%2BlW9XNZLsz%2BqQ6G6CH%2BBUu%2FPoKQNGRa6uwQqw6QIlzLQtwepDDS4ORKM8hl%2BPx%2BOHfs5nLQGA%3D%3D&&app_pvid=59590_11.11.34.86_640_1554536012902&ptl=floorId:3767;app_pvid:59590_11.11.34.86_640_1554536012902;tpp_pvid:fc0d76a5-b58a-4efb-849b-7e1a87aa8f87&union_lens=lensId:0b0b2256_0cc3_169f1911ca1_0cc7',
 'coupon_start_fee': '69.0',
 'coupon_start_time': '1554480000000',
 'coupon_total_count': 100000,
 
 'item_description': '长袖/短袖任选  法式复古碎花雪纺连衣裙',
 'item_id': 589127310615,
 'level_one_category_id': 16,
 'level_one_category_name': '女装/女士精品',
 
 'nick': '云美莎服饰旗舰店',
 'pict_url': '//img.alicdn.com/bao/uploaded/i1/3012579599/O1CN01AwUCxb2KmOLD2ktbO_!!0-item_pic.jpg',
 'seller_id': 3012579599,
 'shop_title': '云美莎服饰旗舰店',
 
 'small_images': {'string': ['//img.alicdn.com/i3/3012579599/O1CN01Mh8l6Z2KmOL9l7tvb_!!3012579599.jpg',
   '//img.alicdn.com/i3/3012579599/O1CN01dPNIJB2KmOLD1yQ2Y_!!3012579599.jpg',
   '//img.alicdn.com/i2/3012579599/O1CN01NB6Zy42KmOLDfsnhN_!!3012579599.jpg',
   '//img.alicdn.com/i4/3012579599/O1CN01CupHFB2KmOLEQOV8Z_!!3012579599.jpg']},
 'title': '法式复古山本过膝初恋桔梗超仙很仙的法国小众碎花雪纺连衣裙春秋',
 'user_type': 1,
 'volume': 5518,
 'zk_final_price': '99.9'}

'''
