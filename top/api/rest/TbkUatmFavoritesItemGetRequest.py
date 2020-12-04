# -*- coding: utf-8 -*-
'''
taobao.tbk.uatm.favorites.item.get( 获取淘宝联盟选品库的宝贝信息 )
￥免费不需用户授权
指定选品库id，获取该选品库的宝贝信息

https://open.taobao.com/api.htm?docId=26619&docType=2
失效！

'''
from top.api.base import RestApi


class TbkUatmFavoritesItemGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None #推广位id，需要在淘宝联盟后台创建；且属于appkey备案的媒体id（siteid），如何获取adzoneid，请参考，http://club.alimama.com/read-htm-tid-6333967.html?spm=0.0.0.0.msZnx5
        self.favorites_id = None #选品库的id
        self.fields = None
        self.page_no = None
        self.page_size = None
        self.platform = None #链接形式：1：PC，2：无线，默认：１
        self.unid = None #自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道

    def getapiname(self):
        return 'taobao.tbk.uatm.favorites.item.get'
