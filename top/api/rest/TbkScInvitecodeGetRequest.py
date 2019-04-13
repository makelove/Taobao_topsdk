# -*- coding: utf-8 -*-
# @Time    : 2019-04-13 20:11
# @Author  : play4fun
# @File    : TbkScInvitecodeGetRequest.py
# @Software: PyCharm

"""
TbkScInvitecodeGetRequest.py:
taobao.tbk.sc.invitecode.get( 淘宝客邀请码生成-社交 )
https://open.taobao.com/api.htm?docId=38046&docType=2
必须用户授权

"""

from top.api.base import RestApi


class TbkScInvitecodeGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.session = None  # 用户登录授权成功后，TOP颁发给应用的授权信息，详细介绍请点击https://open.taobao.com/doc.htm?docId=102635&docType=1。
        # 当此API的标签上注明：
        # “需要授权”，则此参数必传；
        # “不需要授权”，则此参数不需要传；
        # “可选授权”，则此参数为可选
        # SessionKey获取辅助工具 https://open.taobao.com/apitools/sessionPage.htm?spm=a219a.7386653.0.0.3617669adAoBjn

        self.relation_id = None  # 渠道关系ID
        self.relation_app = None  # 渠道推广的物料类型
        self.code_type = None  # 邀请码类型，1 - 渠道邀请，2 - 渠道裂变，3 -会员邀请

    def getapiname(self):
        return 'taobao.tbk.sc.invitecode.get'
