'''
Created by auto_sdk on 2020.10.30

https://open.taobao.com/api.htm?source=search&docId=37989&docType=2
淘宝客-公用-私域用户备案信息查询
查询已生成的渠道id或会员运营id的相关信息。

'''
from top.api.base import RestApi
class TbkScPublisherInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.external_id = None
		self.info_type = None
		self.page_no = None
		self.page_size = None
		self.relation_app = None
		self.relation_id = None
		self.special_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.get'
