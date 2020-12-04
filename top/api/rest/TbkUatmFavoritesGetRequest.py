# -*- coding: utf-8 -*-
'''
taobao.tbk.uatm.favorites.get( 获取淘宝联盟选品库列表 )
￥免费不需用户授权
枚举出淘宝客在淘宝联盟超级搜索，特色频道中，创建的选品库列表

https://open.taobao.com/api.htm?docId=26620&docType=2
失效

创新大赛可开放API列表
https://open.taobao.com/docV3.htm?source=search&docId=118419&docType=1
'''
from top.api.base import RestApi


class TbkUatmFavoritesGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.page_no = None
        self.page_size = None
        self.type = None

    def getapiname(self):
        return 'taobao.tbk.uatm.favorites.get'
