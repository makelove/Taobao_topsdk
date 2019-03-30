# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 16:13
# @Author  : play4fun
# @File    : 淘宝客商品链接转换1.py
# @Software: PyCharm

"""
淘宝客商品链接转换1.py:
http://open.taobao.com/api.htm?docId=24516&docType=2
有权限了

现在可以


"""
import traceback

from top.api import TbkItemConvertRequest
from top import appinfo

from config import appkey, secret, pid

req = TbkItemConvertRequest()
req.set_app_info(appinfo(appkey, secret))
# req.set_app_info(appinfo("24728514",'847aff038c548e44adeeb7fd634d6cc2'))#也没有权限

req.fields = "num_iid,click_url"
# https://detail.tmall.com/item.htm?id=572473824056
req.num_iids = "588009231660"  # ,566807961895"# 商品ID串，用','分割，从taobao.tbk.item.get接口获取num_iid字段，最大40个

# req.adzone_id=adzone_id#只能是【网站广告位】
# req.adzone_id=1814028435#成功 #广告位ID，区分效果位置
req.adzone_id = pid  ##24921350189 adzone_id不正确

req.platform = 2  # 链接形式：1：PC，2：无线，默认：１
# req.unid="demo"#自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道
# req.dx="1"

try:
    resp = req.getResponse()
    import json

    print(resp)

    ds = json.dumps(resp)
    print(ds)  # 成功
    '''
    {'tbk_item_convert_response': 
    {'request_id': 'sbotxvt1as81',
  'results': 
  {'n_tbk_item': 
  [{'click_url': 'https://s.click.taobao.com/t?e=m%3D2%26s%3DuvdckrSoU18cQipKwQzePOeEDrYVVa64XoO8tOebS%2BdRAdhuF14FMd2%2BYEKtRXLMMMgx22UI05aUZR70%2BlK9qVurOGJDe30MkDfIHRGCqXtWah4BbUeGMu%2FBas0tvb4eZz42eVlqqJTf1lozC%2BSXTPdFsh68tKJt%2FNI%2BDXrnOcZv%2FEPE%2FQzyzwtRW0nH3Ls%2BVJ%2B%2BVg%2FftcXcNzTJORRJBj2l4PysJx%2FP',
  
     'num_iid': 572935458344}]}}}
    '''
except Exception as e:
    print(e)
    traceback.print_exc()
