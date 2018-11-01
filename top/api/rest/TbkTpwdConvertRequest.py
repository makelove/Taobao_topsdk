'''
Created by auto_sdk on 2018.08.31

https://open-doc.dingtalk.com/docs/api.htm?apiId=32932

taobao.tbk.tpwd.convert (淘口令转链)
￥免费
不需要授权
支持通过淘口令解析商品id，并提供对应的淘客转链接


反向解析：淘口令-->s.click.taobao.com链接

把别人的淘口令转成自己的淘口令
'''
from top.api.base import RestApi


class TbkTpwdConvertRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.dx = None  # 1表示商品转通用计划链接，其他值或不传表示优先转营销计划链接
        self.password_content = None  # 需要解析的淘口令

    def getapiname(self):
        return 'taobao.tbk.tpwd.convert'
