# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 16:52
# @Author  : play4fun
# @File    : 创建淘口令1.py
# @Software: PyCharm

"""
有权限
创建淘口令1.py:
http://open.taobao.com/docs/api.htm?apiId=31127

平时用这个

这个能转换【优惠券-长链接】
req.url 要https开头
"""

from top.api import TbkTpwdCreateRequest
from top import appinfo
import config

req = TbkTpwdCreateRequest()
req.set_app_info(appinfo(config.appkey, config.secret))

# req.text='半身裙套装女2018新款时尚潮 港风省心搭配女装上衣短裙两件套夏'
# req.text = '雾妆上衣 清水溪原创女装改良汉服刺绣交领上衣复古针织棉外套春'
req.text = '韩国东大门2019春夏新款复古民族风编织包头深口低跟平底半拖鞋'
# req.url='https://item.taobao.com/item.htm?id=567873872517'
req.url = 'https://s.click.taobao.com/t?e=m%3D2%26s%3D8F43%2BjiTfWMcQipKwQzePOeEDrYVVa64lwnaF1WLQxlyINtkUhsv0FSvxYuis1LoGcvgIVjTTAdHatIorvhTnDBUxNsqx3L7njzwEGq%2FDRvSkx9ROi4DlKXezsSnMpj3SD99OVE0eUi%2FsSjYM%2FueLAcJF%2FlBkX5m5UwZupjob08v3l3uT7Tftfr%2BRoxyUbBMDdFDrVj%2B9kW8ByuoqNuRlUadTiDOGWxEcSpj5qSCmbA%3D&scm=null&pvid=100_11.229.171.161_1616_5161582806071608228&app_pvid=59590_11.88.143.71_522_1582806071604&ptl=floorId:2836;originalFloorId:2836;pvid:100_11.229.171.161_1616_5161582806071608228;app_pvid:59590_11.88.143.71_522_1582806071604&xId=2xRsRttYBIo8lY84NtvmwZBcR5Jud5K369knvYqsvhgL6UQz2tqJSoTdr5b73KQPeiQ0YPtaTtauhqn6zPGGYaOB7lwTElWz39os07hxc8pS&union_lens=lensId%3AMAPI%401582806071%400b588f47_0dd4_1708697f96d_2233%4001'
req.logo = 'https://img.alicdn.com/i1/394693657/O1CN01o1tFvd1cswvDv2Qea_!!394693657.jpg'

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
