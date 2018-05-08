'''
Created by auto_sdk on 2017.06.17
'''
from top.api.base import RestApi
class TbkJuTqgGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.end_time = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.tbk.ju.tqg.get'
