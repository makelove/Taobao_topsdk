# -*- coding: utf-8 -*-
'''

'''

from top.api.base import RestApi


class TbkUatmEventItemGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None  # 推广位id，需要在淘宝联盟后台创建；且属于appkey对应的备案媒体id（siteid），如何获取adzoneid，请参考：http://club.alimama.com/read-htm-tid-6333967.html?spm=0.0.0.0.msZnx5
        self.event_id = None  # 招商活动id
        self.fields = None
        self.page_no = None
        self.page_size = None
        self.platform = None
        self.unid = None

    def getapiname(self):
        return 'taobao.tbk.uatm.event.item.get'
