# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 15:50
# @Author  : play4fun
# @File    : 淘口令转链1.py
# @Software: PyCharm

"""
淘口令转链1.py:
把别人的淘口令转成自己的淘口令

很有用，可以用来获取商品ID
"""

from top.api import TbkTpwdConvertRequest
from top import appinfo

from config import appkey, secret,pid

req = TbkTpwdConvertRequest()
req.set_app_info(appinfo(appkey, secret))

# req.password_content = "￥dAEYbi4KO4D￥"#原链接
# req.password_content = "￥G1FEbk599bL￥"#别人的导购淘口令
# req.password_content = "￥TvFnbi4rS28￥"#转链之后的，优惠券
# req.password_content = "【冬季外套女2018新款韩版流行毛呢大衣中长款秋冬女装修身呢子外套】https://m.tb.cn/h.3Ox4kp0 点击链接，再选择浏览器咑閞；或復·制这段描述￥cZqJbk7JyoR￥后到👉淘♂寳♀👈"#淘宝 有返利
# req.password_content = "【小巴士新款老人四轮电动代步车接送孩子长跑电瓶车成人观光车】https://m.tb.cn/h.3m5PFm3 点击链接，再选择浏览器咑閞；或復·制这段描述￥23pObk7tAKi￥后到👉淘♂寳♀👈"#非淘客宝贝
msg='【复古网红行李箱女皮箱拉杆箱男潮旅行箱韩版密码箱子万向轮大学生】https://m.tb.cn/h.3rSpRWc?sm=1f3ea1 点击链接，再选择浏览器咑閞；或復·制这段描述￥09WvbKVt9HB￥后到👉淘♂寳♀👈'
#该item_id对应宝贝已下架或非淘客宝贝

# req.password_content = "【轻薄羽绒服女短款立领连帽时尚韩版修身秋冬大码女装外套反季促销】https://m.tb.cn/h.3n52vLA 点击链接，再选择浏览器咑閞；或復·制这段描述￥E1UAbOaNcwP￥后到👉淘♂寳♀👈"#有券

msg='￥i9CMbz0hLPo￥'
req.password_content = msg
req.adzone_id = pid
req.dx = "1"

try:
    resp = req.getResponse()

    # it=resp['tbk_item_info_get_response']['results']['n_tbk_item'][0]
    # print(it)

    import json

    ds = json.dumps(resp)
    print(ds)
except Exception as e:
    print(e)#errorcode=15 message=Remote service error subcode=10000 submsg=该item_id对应宝贝已下架或非淘客宝贝 application_host=11.0.173.162 service_host=top011000173162.center.na62

    '''
{
    "tbk_tpwd_convert_response": {
        "data": {
            "click_url": "https://s.click.taobao.com/t?e=m%3D2%26s%3DlPB%2BIFlTXXYcQipKwQzePOeEDrYVVa64XoO8tOebS%2BdRAdhuF14FMQPx4A86vneat4hWD5k2kjOUZR70%2BlK9qVurOGJDe30Mi4iGkEp3vhY1bHXFwOOwIlnifR7TequSVbyFvQb68TVhzIPRUbx8%2FC%2FoxewA8MDczd4sm6IVoF5BvG9Dt0tL1PUA8sxeHPJeLm7IGu8cWyae94Djkt%2FJYSGFCzYOOqAQ&union_lens=lensId:0b177a9d_0c35_166ce44e330_566b",
            
            "num_iid": "576016341093"
        },
        "request_id": "81f43dtpbscl"
    }
}


把别人的淘口令转成自己的淘口令
{
    "tbk_tpwd_convert_response": {
        "data": {
            "click_url": "https://s.click.taobao.com/t?e=m%3D2%26s%3Dsnn8QvJbTiwcQipKwQzePOeEDrYVVa64XoO8tOebS%2BdRAdhuF14FMZ6IEgctIxHz1aH1Hk3GeOiUZR70%2BlK9qVurOGJDe30Mi4iGkEp3vhY1bHXFwOOwIlnifR7TequSVbyFvQb68TVhzIPRUbx8%2FC%2FoxewA8MDczd4sm6IVoF5BvG9Dt0tL1PUA8sxeHPJeLm7IGu8cWyae94Djkt%2FJYSGFCzYOOqAQ&union_lens=lensId:0b01eedb_0d43_166ce482533_5605",
            "num_iid": "576016341093"
        },
        "request_id": "64ifmu0jz018"
    }
}


#2
{
    "tbk_tpwd_convert_response": {
        "data": {
            "click_url": "https://s.click.taobao.com/t?e=m%3D2%26s%3D4LKtvJ%2F69yAcQipKwQzePOeEDrYVVa64yK8Cckff7TVRAdhuF14FMdXE8COXJQ681aH1Hk3GeOiUZR70%2BlK9qVurOGJDe30Mi4iGkEp3vhY1bHXFwOOwIlnifR7TequSVbyFvQb68TVhzIPRUbx8%2FC%2FoxewA8MDclshKYK6%2BA%2BDcmblpIxbswhXtVrfbdkOIqX9lXiHwDJPkX12FW3F1BXEqY%2Bakgpmw&union_lens=lensId:0bb082ba_0202_167394f70ab_61ad",
            "num_iid": "561566817370"
        },
        "request_id": "631vor0uoktc"
    }
}

    '''
