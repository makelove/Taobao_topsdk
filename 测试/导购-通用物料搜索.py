# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 18:37
# @Author  : play4fun
# @File    : 导购信息搜索1.py
# @Software: PyCharm

"""
有权限
导购信息搜索1.py:通用物料搜索
参考：
https://doc.alidayu.com/docs/api.htm?apiId=35896

佣金
优惠券

'commission_rate': '1550',
商品信息-佣金比率。1550表示15.5%
commission_rate = commission_rate / 10000
-
'commission_type': 'MKT'
商品信息-佣金类型。MKT表示营销计划，SP表示定向计划，COMMON表示通用计划
MKT 佣金不高?!!
"""
from pprint import pprint
import traceback, json

from top.api import TbkDgMaterialOptionalRequest
from top import appinfo

from config import appkey, secret, pid

req2 = TbkDgMaterialOptionalRequest()
req2.set_app_info(appinfo(appkey, secret))

# req2.start_dsr = 10 #店铺dsr评分

req2.page_size = 10
req2.page_no = 1
req2.platform = 1
# req.end_tk_rate = 1234 #TODO 设置一个区间
# req.start_tk_rate = 1234
#
# req2.end_price = 10
# req2.start_price = 20
#
# req.is_overseas = False#报错
# req.is_tmall = False
req2.sort = 'tk_total_commi'  # "tk_rate_des"#
# req.itemloc = "杭州"
# req2.cat = "16,18"
# req2.q = "亮片刺绣T恤 夏装韩版宽松大码女装中长款下衣失踪休闲上衣服潮"  # https://detail.tmall.com/item.htm?id=588009231660
req2.q = "2019春夏新款复古民族风"  # https://detail.tmall.com/item.htm?id=575317425603
# req2.q = "10000毫安充电宝女小巧迷你可爱苹果安卓通用大容量移动电源快充"
# req2.q = "植护本色抽纸面巾纸巾餐巾纸抽卫生纸家用实惠家庭装整箱批发10包"
# "宝宝吃饭罩衣围兜春夏薄款防水耐脏男女孩儿童画画围裙饭衣反穿衣"
# req2.q = "紫外线杀菌灯"
# req2.material_id = 2836#默认

# req2.has_coupon = True# Invalid arguments

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
    # pprint(resp)
    # print('\n')
    # ds = json.dumps(resp)
    # print(ds)  # 成功
    print('-' * 40)
    result_list = resp['tbk_dg_material_optional_response']['result_list']['map_data']
    print('长度', len(result_list))
    for item in result_list:
        pprint(item)
        # if item['coupon_remain_count'] > 0:
        #     break
        # else:
        #     print('No')
        print('-' * 40)
    titles = [item['title'] for item in result_list]
    print(titles)
except Exception as e:
    print(e)
    '''
    {'category_id': 121434057,
 'category_name': '干鞋器',
 'commission_rate': '5000',
 'commission_type': 'COMMON',
 
 'coupon_amount': '10',
 'coupon_end_time': '2019-05-10',
 'coupon_id': '1c8791f3c0e842efa85e1a6200d15b4e',
 'coupon_info': '满11.00元减10元',
 'coupon_remain_count': 96084,
 'coupon_share_url': '//uland.taobao.com/coupon/edetail?e=%2F0fFmuCj6gkNfLV8niU3RwXoB%2BDaBK5LQS0Flu%2FfbSog%2BeE%2BjpQFGNpsAmOX0u61tVNRlA%2Fi6pDhowMfyAmukaF4WPfmYkkXY4aTwv%2BuJfjZ14W3Mirj8mVujRnwwY9pAdwGVw25uD4%2FYjzBQAW7hC2rdv8UL3t5yXj7JdOCXY4sYE%2BO7Xaulytm02CsHt1k1LeEfNPJT5MM1L%2FmEra8u1kT%2Burs3qO2&&app_pvid=59590_11.11.147.214_31021_1551960729750&ptl=floorId:2836;app_pvid:59590_11.11.147.214_31021_1551960729750;tpp_pvid:100_11.178.152.226_69696_4801551960729755733&xId=ThRL7gmx1DkJFNB6BJ7vK5v1cn6LwgKNXWl2K9HhV4HHqmWbCOl1XT2ffFDe63EF941nL46VZGOylzei4zz44&union_lens=lensId:0b0b93d6_0ca0_169581168d7_bfca',
 'coupon_start_fee': '11.00',
 'coupon_start_time': '2019-02-10',
 'coupon_total_count': 100000,
 
 
 'include_dxjh': 'false',
 'include_mkt': 'false',
 'info_dxjh': '{}',
 'item_description': '',
 'item_id': 564357848871,
 'item_url': 'https://item.taobao.com/item.htm?id=564357848871',
 'level_one_category_id': 50012100,
 'level_one_category_name': '生活电器',
 'nick': '试试8888',
 'num_iid': 564357848871,
 'pict_url': 'http://img.alicdn.com/imgextra/i4/1763136390/TB2NH1_XDka61Bjy0FgXXbPpVXa_!!1763136390.jpg',
 'provcity': '广东 深圳',
 'reserve_price': '120.51',
 'seller_id': 793802970,
 'shop_dsr': 44028,
 'shop_title': '轴心外设店',
 'short_title': '紫光灯消毒除臭杀菌暖鞋机烘鞋器',
 'small_images': {'string': ['https://img.alicdn.com/i8/TB2hwakabnA11Bjy0FjXXapoFXa_!!1763136390.jpg',
                             'https://img.alicdn.com/i8/TB2961oajzB11BjSspaXXcJ0VXa_!!1763136390.jpg',
                             'https://img.alicdn.com/i8/TB2P6GcbF_AQeBjSZFvXXbnKXXa_!!1763136390.png',
                             'https://img.alicdn.com/i8/TB2kyaBaoHB11BjSspeXXan0FXa_!!1763136390.png']},
 'title': '紫光灯烘鞋器 消毒烤鞋器 除臭杀菌干鞋器暖鞋机烘干机安全电热',
 'tk_total_commi': '0',
 'tk_total_sales': '0',
 'url': '//s.click.taobao.com/t?e=m%3D2%26s%3DgsZsZTj1OpccQipKwQzePOeEDrYVVa64lwnaF1WLQxlyINtkUhsv0PJg2A3RWGYJqqacliaqsdBwe9WqVoWbK6cpCeoIkU8NSlFUVq0truStrs69PUsRSCQjO9J4i5qlSD99OVE0eUj%2BDRZRaf%2FcEDEwlqBIbLFMkRIxIi9Kdk7qS%2FXCXzX7tY5oHZ1V5zdkwS%2BtB%2BvBHo7GJe8N%2FwNpGw%3D%3D&scm=null&pvid=100_11.178.152.226_69696_4801551960729755733&app_pvid=59590_11.11.147.214_31021_1551960729750&ptl=floorId:2836;pvid:100_11.178.152.226_69696_4801551960729755733;app_pvid:59590_11.11.147.214_31021_1551960729750&xId=ThRL7gmx1DkJFNB6BJ7vK5v1cn6LwgKNXWl2K9HhV4HHqmWbCOl1XT2ffFDe63EF941nL46VZGOylzei4zz44&union_lens=lensId:0b0b93d6_0ca0_169581168d7_bfca',
 'user_type': 0,
 'volume': 0,
 'white_image': '',
 'x_id': 'ThRL7gmx1DkJFNB6BJ7vK5v1cn6LwgKNXWl2K9HhV4HHqmWbCOl1XT2ffFDe63EF941nL46VZGOylzei4zz44',
 'zk_final_price': '120.27'}  
 
 
 
 {'category_id': 50012478,
 'category_name': '抽纸',
 'commission_rate': '45',
 'commission_type': 'ZX',
 'coupon_id': '',
 'coupon_info': '',
 'coupon_remain_count': 0,
 'coupon_total_count': 0,
 'include_dxjh': 'false',
 'include_mkt': 'false',
 'info_dxjh': '{}',
 'item_description': '',
 'item_id': 588287384841,
 'item_url': 'https://item.taobao.com/item.htm?id=588287384841',
 'level_one_category_id': 50025705,
 'level_one_category_name': '洗护清洁剂/卫生巾/纸/香薰',
 'nick': 'm841995082',
 'num_iid': 588287384841,
 'pict_url': 'https://img.alicdn.com/bao/uploaded/i2/2734800840/O1CN01ZlpLVR1I4lCOQ4G1J_!!2734800840.jpg',
 'provcity': '广东 广州',
 'reserve_price': '16.8',
 'seller_id': 2734800840,
 'shop_dsr': 47877,
 'shop_title': '匠心Miss you生活馆',
 'short_title': '植护本色面巾纸巾抽家用实惠卫生纸',
 'small_images': {'string': ['https://img.alicdn.com/i3/2734800840/O1CN01SKblRC1I4lCNXhhjP_!!2734800840.jpg',
                             'https://img.alicdn.com/i4/2734800840/O1CN018SeA5C1I4lCNQLJsB_!!2734800840.jpg',
                             'https://img.alicdn.com/i3/2734800840/O1CN01xmIrbG1I4lCNQMG4d_!!2734800840.jpg',
                             'https://img.alicdn.com/i2/2734800840/O1CN0185ZmQl1I4lCNX0Ja6_!!2734800840.jpg']},
 'title': '植护本色抽纸面巾纸巾餐巾纸抽卫生纸家用实惠家庭装整箱批发10包',
 'tk_total_commi': '1.02',
 'tk_total_sales': '5',
 'url': '//s.click.taobao.com/t?e=m%3D2%26s%3DUI22P%2FB2AhIcQipKwQzePOeEDrYVVa64lwnaF1WLQxlyINtkUhsv0DwRP6v6RZjKklPFOsnCtMVHatIorvhTnDBUxNsqx3L7njzwEGq%2FDRvSkx9ROi4DlKXezsSnMpj3SD99OVE0eUhwGilLG1DZrfqmGxzdfRI0%2FVJqtNeEg5OyAilzVYVmIivXtY%2B2Lf8rch%2F%2BlwyD3uE74r98KLXqNsYl7w3%2FA2kb&scm=null&pvid=100_11.182.100.47_108984_9981555725553411118&app_pvid=59590_11.21.18.24_11158_1555725553404&ptl=floorId:2836;pvid:100_11.182.100.47_108984_9981555725553411118;app_pvid:59590_11.21.18.24_11158_1555725553404&xId=U2xxkk6FPNMYdlBbMwPA7bFWzj3uFzZjt9kdTQGpj2c8xuciWbggFYzkq6H9N1j74YJLYNoTanhnu6ayz7R6Y1&union_lens=lensId:0b151218_0c17_16a38780f2f_c1be',
 'user_type': 0,
 'volume': 8,
 'white_image': '',
 'x_id': 'U2xxkk6FPNMYdlBbMwPA7bFWzj3uFzZjt9kdTQGpj2c8xuciWbggFYzkq6H9N1j74YJLYNoTanhnu6ayz7R6Y1',
 'zk_final_price': '13.8'}
 
   
    '''
