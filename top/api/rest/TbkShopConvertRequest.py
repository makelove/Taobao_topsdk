'''
Created by auto_sdk on 2018.07.25
https://open-doc.dingtalk.com/docs/api.htm?apiId=24523

淘宝客店铺链接转换
'''
from top.api.base import RestApi


class TbkShopConvertRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.fields = None
        self.platform = None
        self.unid = None
        self.user_ids = None

    def getapiname(self):
        return 'taobao.tbk.shop.convert'
