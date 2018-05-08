'''
Created by auto_sdk on 2018.04.09
'''
from top.api.base import RestApi
class TbkDgNewuserOrderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.end_register_time = None
		self.page_no = None
		self.page_size = None
		self.start_register_time = None

	def getapiname(self):
		return 'taobao.tbk.dg.newuser.order.get'
