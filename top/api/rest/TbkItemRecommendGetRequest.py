'''
Created by auto_sdk on 2017.06.17
'''
from top.api.base import RestApi
class TbkItemRecommendGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.fields = None
		self.num_iid = None
		self.platform = None

	def getapiname(self):
		return 'taobao.tbk.item.recommend.get'
