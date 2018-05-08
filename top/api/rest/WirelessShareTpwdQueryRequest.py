'''
Created by auto_sdk on 2017.12.20
'''
from top.api.base import RestApi
class WirelessShareTpwdQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.password_content = None

	def getapiname(self):
		return 'taobao.wireless.share.tpwd.query'
