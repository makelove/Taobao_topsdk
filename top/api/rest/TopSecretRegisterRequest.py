'''
Created by auto_sdk on 2016.08.16
'''
from top.api.base import RestApi
class TopSecretRegisterRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.user_id = None

	def getapiname(self):
		return 'taobao.top.secret.register'
