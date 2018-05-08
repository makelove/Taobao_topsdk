'''
Created by auto_sdk on 2017.04.14
'''
from top.api.base import RestApi
class JuItemsSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_top_item_query = None

	def getapiname(self):
		return 'taobao.ju.items.search'
