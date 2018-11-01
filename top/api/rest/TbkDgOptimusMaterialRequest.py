'''
Created by auto_sdk on 2018.10.29

http://open.taobao.com/api.htm?docId=33947&docType=2

taobao.tbk.dg.optimus.material( 淘宝客物料下行-导购 )
￥免费不需用户授权
通用物料推荐，传入官方公布的物料id，可获取指定物料
'''
from top.api.base import RestApi


class TbkDgOptimusMaterialRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.content_id = None
        self.content_source = None
        self.device_encrypt = None
        self.device_type = None
        self.device_value = None
        self.material_id = None
        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'taobao.tbk.dg.optimus.material'
