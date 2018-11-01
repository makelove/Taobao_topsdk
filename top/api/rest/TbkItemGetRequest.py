'''
Created by auto_sdk on 2016.07.25
'''
from top.api.base import RestApi


class TbkItemGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.cat = None
        self.end_price = None
        self.end_tk_rate = None
        self.fields = None
        self.is_overseas = None
        self.is_tmall = None
        self.itemloc = None
        self.page_no = None
        self.page_size = None
        self.platform = None
        self.q = None
        self.sort = None
        self.start_price = None
        self.start_tk_rate = None

    def getapiname(self):
        return 'taobao.tbk.item.get'
