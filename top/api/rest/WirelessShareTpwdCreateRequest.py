'''
Created by auto_sdk on 2017.12.18

下线了！
淘口令API在开放平台下线公告
发布于: 2018-9-10 13:40:35

尊敬的开发者

      您好。基于综合考虑，淘口令接口taobao.wireless.share.tpwd.create计划在开放平台下线，ISV对该接口的调用申请也将关闭。具体下线计划：该接口新申请入口关闭时间为2018年9月11日24:00。针对已有权限者，该接口关闭的时间为2018年9月27日24:00。为免影响您的业务，请已有权限者及时停止使用该接口功能，由此造成的不便深表歉意 。

--阿里巴巴.开放平台

2018年9月10日

submsg=不合法ApiName，ApiName = taobao.wireless.share.tpwd.create
'''
from top.api.base import RestApi


class WirelessShareTpwdCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.tpwd_param = None

    def getapiname(self):
        return 'taobao.wireless.share.tpwd.create'
