'''
Created by auto_sdk on 2017.06.17
'''
from top.api.base import RestApi
class TbkShopGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_auction_count = None
		self.end_commission_rate = None
		self.end_credit = None
		self.end_total_action = None
		self.fields = None
		self.is_tmall = None
		self.page_no = None
		self.page_size = None
		self.platform = None
		self.q = None
		self.sort = None
		self.start_auction_count = None
		self.start_commission_rate = None
		self.start_credit = None
		self.start_total_action = None

	def getapiname(self):
		return 'taobao.tbk.shop.get'
