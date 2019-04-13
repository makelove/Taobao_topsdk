# -*- coding: utf-8 -*-
'''

http://open.taobao.com/docs/api.htm?apiId=31127
'''

from top.api.base import RestApi


class TbkTpwdCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.ext = None

        self.logo = None
        self.text = None
        self.url = None

        self.user_id = None

    def getapiname(self):
        return 'taobao.tbk.tpwd.create'
