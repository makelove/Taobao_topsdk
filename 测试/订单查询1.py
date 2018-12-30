# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 11:29
# @Author  : play4fun
# @File    : 订单查询1.py
# @Software: PyCharm

"""
订单查询1.py:
http://open.taobao.com/api.htm?docId=24527&docType=2


没有权限
"""

from top.api import TbkOrderGetRequest
from top import appinfo

from config import appkey, secret

req = TbkOrderGetRequest()
req.set_app_info(appinfo(appkey, secret))

req.fields = "tb_trade_parent_id,tb_trade_id,num_iid,item_title,item_num,price,pay_price,seller_nick,seller_shop_title,commission,commission_rate,unid,create_time,earning_time,tk3rd_pub_id,tk3rd_site_id,tk3rd_adzone_id,relation_id"
req.start_time = "2018-08-23 12:18:22"
req.span = 600
req.page_no = 1
req.page_size = 20
req.tk_status = 1
req.order_query_type = "settle_time"
try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
    # http://open.taobao.com/doc.htm?spm=a219a.7386653.0.0.CudPbJ&docId=1&docType=18
    '''
    错误原因：应用没有权限访问当当前API
    解决方案：申请相应的API权限
    
    {"error_response":{"code":11,"msg":"Insufficient isv permissions","sub_code":"isv.permission-api-package-limit","sub_msg":"scope ids is 381 11655 13168 11998 12486 11653","request_id":"10enths0uz5vu"}}
    
    '''
