'''
Created by auto_sdk on 2017.09.05

http://open.taobao.com/api.htm?docId=24518&docType=2

'''
from top.api.base import RestApi


class TbkItemInfoGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.num_iids = None
        self.platform = None

    def getapiname(self):
        return 'taobao.tbk.item.info.get'
