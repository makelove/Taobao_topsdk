# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 17:02
# @Author  : play4fun
# @File    : 创建淘口令2.py
# @Software: PyCharm

"""
创建淘口令2.py:

过期了？不能用
下线了?

submsg=不合法ApiName，ApiName = taobao.wireless.share.tpwd.create
"""

from top.api import WirelessShareTpwdCreateRequest
from top import appinfo
import config,json
req=WirelessShareTpwdCreateRequest()
req.set_app_info(appinfo(config.appkey,config.secret))

text='2018夏季新款女装时尚黑色V领拼接收腰A字裙中长款雪纺显瘦连衣裙'
url='https://uland.taobao.com/coupon/edetail?e=JBuZPm5JWqEGQASttHIRqZL3pImL%2FJh1HZ6yD2Py5i%2Fg4lUqifPvH9x2%2FlD7wOdrVxl2CHuUpj1uWNE2q%2FyjycWKxy1EFPIVsSKwS%2F%2FvFcFma4VUO7VGBlZrtTOLgXkcjDppvlX%2Bob%2BBtHA6T8TZnVBPfopb7LXvu8n6e%2B0RLoCEsG9BMdsVqA%3D%3D&traceId=0bb6999515405448411741149e&union_lens=lensId:0b0ad4b4_0bf5_166afa0c5f0_c4b9'
logo='https://img.alicdn.com/bao/uploaded/i1/587451667/TB23sxjrviSBuNkSnhJXXbDcpXa_!!587451667.jpg_220x220_.webp'
d={'url':url,'text':text,'logo':logo}
param=json.dumps(d)
req.tpwd_param=param

try:
    resp= req.getResponse()
    import json

    ds = json.dumps(resp)
    print(ds)
    print(resp['wireless_share_tpwd_create_response']['model'])
except Exception as e:
    print(e)
    '''
    {'wireless_share_tpwd_create_response': 
    {'model': '€bzp3b3xUpDI€',
  'request_id': '3qxi481xxgei'}}
    '''