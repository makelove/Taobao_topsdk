'''
Created by auto_sdk on 2020.07.09

https://open.taobao.com/api.htm?source=search&docId=43317&docType=2
淘宝客-推广者-淘礼金发放及使用报表

淘礼金实例维度相关报表数据查询
'''
from top.api.base import RestApi
class TbkDgVegasTljInstanceReportRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.rights_id = None

	def getapiname(self):
		return 'taobao.tbk.dg.vegas.tlj.instance.report'
