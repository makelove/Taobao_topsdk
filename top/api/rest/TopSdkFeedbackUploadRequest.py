'''
Created by auto_sdk on 2016.08.19
'''
from top.api.base import RestApi
class TopSdkFeedbackUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None
		self.type = None

	def getapiname(self):
		return 'taobao.top.sdk.feedback.upload'
