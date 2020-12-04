'''
Created by auto_sdk on 2020.10.19

https://open.taobao.com/api.htm?source=search&docId=48340&docType=2
淘宝客-推广者-官方活动转链

支持入参推广位和官方活动会场ID，获取活动信息和推广链接，包含推广长链接、短链接、淘口令、微信推广二维码地址等。改该API支持二方、三方类型的转链。官方活动会场ID，从淘宝客后台“我要推广-活动推广”中获取。

'''
from top.api.base import RestApi
class TbkActivityInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_material_id = None
		self.adzone_id = None
		self.relation_id = None
		self.sub_pid = None
		self.union_id = None

	def getapiname(self):
		return 'taobao.tbk.activity.info.get'
