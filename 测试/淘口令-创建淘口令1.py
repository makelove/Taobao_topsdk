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
req.url 要https开头
"""

from top.api import TbkTpwdCreateRequest
from top import appinfo
import config

req = TbkTpwdCreateRequest()
req.set_app_info(appinfo(config.appkey, config.secret))

# req.text='半身裙套装女2018新款时尚潮 港风省心搭配女装上衣短裙两件套夏'
req.text = '雾妆上衣 清水溪原创女装改良汉服刺绣交领上衣复古针织棉外套春'
# req.url='https://item.taobao.com/item.htm?id=567873872517'
req.url = 'https://s.click.taobao.com/t?e=m%3D2%26s%3DhcQz%2FVJ3mhwcQipKwQzePOeEDrYVVa64lwnaF1WLQxlyINtkUhsv0PmZ6XtpHWZAPYSlF0lm7fJHatIorvhTnDBUxNsqx3L7njzwEGq%2FDRvSkx9ROi4DlKXezsSnMpj3SD99OVE0eUhnZEISIab18DnpmhTObRx2eAkx3bKOzfsSDRAhaLK2V7ee%2FAGi314VtHLIDNbvfQeiZ%2BQMlGz6FQ%3D%3D&scm=null&pvid=100_11.139.186.102_1598_771555678262154878&app_pvid=59590_11.21.18.24_8144_1555678262148&ptl=floorId:2836;pvid:100_11.139.186.102_1598_771555678262154878;app_pvid:59590_11.21.18.24_8144_1555678262148&xId=Tpu3TQSqmxUd5GdBaMFSPAyNttSCsp8TTpxwNRUxhLiiFBGXHtMLHEtsEH6NaA3VZUS4ZiLmobC6WhwRIFeHvn&union_lens=lensId:0b151218_0c17_16a35a673bf_5a05'
req.logo = 'https://img.alicdn.com/bao/uploaded/i4/113740699/TB2aYQ8b41YBuNjy1zcXXbNcXXa_!!113740699.jpg_220x220_.webp'

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
