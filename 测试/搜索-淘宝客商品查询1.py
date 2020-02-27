# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 16:06
# @Author  : play4fun
# @File    : 淘宝客商品查询1.py
# @Software: PyCharm

"""
淘宝客商品查询1.py:
搜索商品
返回列表

errorcode=22 message=Invalid method subcode=None submsg=不合法ApiName，ApiName = taobao.tbk.item.get application_host=11.1.185.92 service_host=top011001185092.center.na62
"""

from top.api import TbkItemGetRequest
from top import appinfo
from pprint import pprint
from config import appkey, secret

req = TbkItemGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"  # ,tk_rate"#没用

# req.q="女装"
# req.q = "韩都衣舍2019韩版女装夏装网纱仙女印花气质蛋糕裙连衣裙EK9095囡"
# req.q = "舒客舒克儿童电动牙刷B32男女宝宝小孩防水声波自动2-3-6-12岁"
req.q = "10000毫安充电宝女小巧迷你可爱苹果安卓通用大容量移动电源快充"
# req.q="http://item.taobao.com/item.htm?id=569885087264"

# req.cat="16,18"
#
# req.itemloc = "杭州"
#
req.sort ='tk_total_sales'# "tk_rate_des"  #
#
# req.is_tmall=False
# req.is_overseas=False
#
# req.start_price=400
# req.end_price=500
#
# req.start_tk_rate = 500  #
# req.end_tk_rate = 700
#
# req.platform=1
req.page_no = 1
req.page_size = 10

try:
    resp = req.getResponse()
    # pprint(resp)
    result_list = resp['tbk_item_get_response']['results']['n_tbk_item']
    for it in result_list:
        pprint(it)
        print('-'*30)
    # import json
    #
    # ds = json.dumps(resp)
    # print(ds)
except Exception as e:
    print(e)
'''
{'tbk_item_get_response': {'request_id': '7ju6x3yuq9mb',
                           'results': {'n_tbk_item': [{'item_url': 'http://item.taobao.com/item.htm?id=561817433242',
                                                       'nick': 'keaidexixi2017',
                                                       'num_iid': 561817433242,
                                                       'pict_url': 'https://img.alicdn.com/tfscom/i3/1612016151/TB2X7XtbNhmpuFjSZFyXXcLdFXa_!!1612016151.jpg',
                                                       'provcity': '浙江 金华',
                                                       'reserve_price': '147.00',
                                                       'seller_id': 3519956009,
                                                       'title': '松宝UV-009，007鱼缸杀菌灯 '
                                                                'UVC-9W,7W杀菌灯灯管 '
                                                                '消毒灯 除藻灯',
                                                       'user_type': 0,
                                                       'volume': 0,
                                                       'zk_final_price': '147.00'}
'''