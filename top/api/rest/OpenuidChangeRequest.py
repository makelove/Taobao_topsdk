'''
Created by auto_sdk on 2018.01.11
'''
from top.api.base import RestApi
class OpenuidChangeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.open_uid = None
		self.target_app_key = None

	def getapiname(self):
		return 'taobao.openuid.change'
