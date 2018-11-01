'''
Created by auto_sdk on 2018.07.20

https://jaq-doc.alibaba.com/docs/api.htm?scopeId=11655&apiId=36836

taobao.tbk.dg.newuser.order.sum (拉新活动汇总API--导购)
'''
from top.api.base import RestApi


class TbkDgNewuserOrderSumRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.activity_id = None
        self.adzone_id = None
        self.page_no = None
        self.page_size = None
        self.settle_month = None
        self.site_id = None

    def getapiname(self):
        return 'taobao.tbk.dg.newuser.order.sum'
