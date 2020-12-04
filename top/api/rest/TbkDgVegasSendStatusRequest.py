'''
Created by auto_sdk on 2020.11.03

https://open.taobao.com/api.htm?source=search&docId=52958&docType=2
淘宝客-推广者-超级红包领取状态查询
淘宝客传入用户标识的信息，查询该用户是否有当前阶段待核销的红包（淘客接入前需签署协议 https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin）

'''
from top.api.base import RestApi
class TbkDgVegasSendStatusRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.device_type = None
		self.device_value = None
		self.relation_id = None
		self.special_id = None

	def getapiname(self):
		return 'taobao.tbk.dg.vegas.send.status'
