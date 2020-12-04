'''
Created by auto_sdk on 2020.10.27

https://open.taobao.com/api.htm?source=search&docId=52700&docType=2
淘宝客-推广者-权益物料精选

推广者使用。支持入参推广者对应的“推广位”和官方提供的“权益物料id”，获取指定权益物料。

'''
from top.api.base import RestApi
class TbkDgOptimusPromotionRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.page_num = None
		self.page_size = None
		self.promotion_id = None

	def getapiname(self):
		return 'taobao.tbk.dg.optimus.promotion'
