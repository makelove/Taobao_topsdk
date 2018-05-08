'''
Created by auto_sdk on 2018.04.02
'''
from top.api.base import RestApi
class TbkScMaterialOptionalRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.cat = None
		self.end_price = None
		self.end_tk_rate = None
		self.has_coupon = None
		self.is_overseas = None
		self.is_tmall = None
		self.itemloc = None
		self.page_no = None
		self.page_size = None
		self.platform = None
		self.q = None
		self.site_id = None
		self.sort = None
		self.start_dsr = None
		self.start_price = None
		self.start_tk_rate = None

	def getapiname(self):
		return 'taobao.tbk.sc.material.optional'
