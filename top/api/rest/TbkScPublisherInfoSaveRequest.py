'''
Created by auto_sdk on 2020.10.30

https://open.taobao.com/api.htm?source=search&docId=37988&docType=2
淘宝客-公用-私域用户备案
通过入参渠道管理或会员运营管理的邀请码，生成渠道id或会员运营id，完成渠道或会员的备案。

'''
from top.api.base import RestApi
class TbkScPublisherInfoSaveRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.info_type = None
		self.inviter_code = None
		self.note = None
		self.offline_scene = None
		self.online_scene = None
		self.register_info = None
		self.relation_from = None

	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.save'
