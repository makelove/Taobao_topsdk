# -*- coding: utf-8 -*-
'''
枚举定向招商列表,taobao.tbk.uatm.event.get
http://open.taobao.com/doc2/apiDetail.htm?spm=a219a.7395905.0.0.xyzraZ&apiId=26449
网址失效了！

'''
from top.api.base import RestApi


class TbkUatmEventGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'taobao.tbk.uatm.event.get'
