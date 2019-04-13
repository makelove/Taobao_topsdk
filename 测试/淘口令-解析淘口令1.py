# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 15:26
# @Author  : play4fun
# @File    : 解析淘口令1.py
# @Software: PyCharm

"""
解析淘口令1.py:

常用
从淘口令中提取出商品ID
url

"""

from top.api import WirelessShareTpwdQueryRequest
from top import appinfo
from config import appkey, secret


def parseTKL(msg):
    req=WirelessShareTpwdQueryRequest()
    req.set_app_info(appinfo(appkey,secret))
    req.password_content=msg

    rt=req.getResponse()
    return rt

def test1():#复制框内整段文字，打开「手淘」即可「领取优惠券」并购买￥MDGGba1MLQh￥
    # msg='【杭州真丝上衣女2018新款短袖t恤夏桑蚕丝处理清仓 重磅铜氨丝女装,这款真丝t恤，宽松的版型设计，上身非常显瘦】，復·制这段描述€08skb3DzfQC€后咑閞👉淘♂寳♀👈'#商品口令
    # msg='【轻薄羽绒服女短款立领连帽时尚韩版修身秋冬大码女装外套反季促销】https://m.tb.cn/h.3n52vLA 点击链接，再选择浏览器咑閞；或復·制这段描述￥E1UAbOaNcwP￥后到👉淘♂寳♀👈'#领券
    # msg='复制整段信息，打开👉手机天猫👈，即可查看此商品:【纤麦加肥加大码女装胖mm秋装宽松显瘦时尚长袖打底外穿T恤上衣】(未安装App点这里：http://yukhj.com/s/HKvLP?tm=2d6aaf )🔑喵口令🔑'#不能解析喵口令
    msg='【堆堆领秋衣大码女装韩版修身打底衫,这是一件非常显气质的莫代尔t恤，面料柔软舒适，吸湿透气】，https://m.tb.cn/h.3EK37eh 点击链接，再选择浏览器咑閞；或復·制这段描述￥anzcbFYCKxj￥后咑閞👉淘♂寳♀👈'
    # msg='￥mEWabqcRExj￥'#过期的淘口令
    msg='￥AEpabxiRg0u￥'
    msg='描述￥i9CMbz0hLPo￥后'

    rt=parseTKL(msg)
    print(rt)

if __name__ == '__main__':
    test1()
    '''
    {'wireless_share_tpwd_query_response': {'content': '杭州真丝上衣女2018新款短袖t恤夏桑蚕丝处理清仓 重磅铜氨丝女装',
  'native_url': 'tbopen://m.taobao.com/tbopen/index.html?action=ali.open.nav&module=h5&h5Url=https%3A%2F%2Fa.m.taobao.com%2Fi572456021063.htm%3Fprice%3D198%26original_price%3D688%26sourceType%3Ditem%26sourceType%3Ditem%26suid%3Dd2109373-8046-4f3f-8b1d-172c4741dc5d%26ut_sk%3D1.Wthts%252FH5I4QDANNejADzdUSC_21646297_1536555233541.TaoPassword-WeiXin.1%26un%3D817be46c5b6cc1dfb463cb48fb1832e7%26share_crt_v%3D1%26mit_nlg_ver%3Dv1%26sp_tk%3D4oKsMDhza2IzRHpmUUPigqw%3D%26spm%3Da211b4.24728341%26visa%3D13a09278fde22a2e%26disablePopup%3Dtrue%26disableSJ%3D1&appkey=24728341&visa=13a09278fde22a2e',
  'pic_url': 'http://gw.alicdn.com/bao/uploaded/i1/2198430295/TB16g0zlcUrBKNjSZPxXXX00pXa_!!0-item_pic.jpg',
  'price': '198.00',
  'request_id': '10qsc7l1tri39',
  'suc': True,
  'thumb_pic_url': 'http://gw.alicdn.com/bao/uploaded/i1/2198430295/TB16g0zlcUrBKNjSZPxXXX00pXa_!!0-item_pic.jpg_170x170.jpg',
  'title': '淘口令-宝贝',
  
  'url': 'https://a.m.taobao.com/i572456021063.htm?price=198&original_price=688&sourceType=item&sourceType=item&suid=d2109373-8046-4f3f-8b1d-172c4741dc5d&ut_sk=1.Wthts%2FH5I4QDANNejADzdUSC_21646297_1536555233541.TaoPassword-WeiXin.1&un=817be46c5b6cc1dfb463cb48fb1832e7&share_crt_v=1&mit_nlg_ver=v1&sp_tk=4oKsMDhza2IzRHpmUUPigqw=&spm=a211b4.24728341&visa=13a09278fde22a2e&disablePopup=true&disableSJ=1'
  }}
    '''

    '''
    {'wireless_share_tpwd_query_response': 
    {'content': '半身裙套装女2018新款时尚潮 港风省心搭配女装上衣短裙两件套夏',
  'native_url': 'tbopen://m.taobao.com/tbopen/index.html?action=ali.open.nav&module=h5&h5Url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D567873872517%26ut_sk%3D1.utdid_24728341_1536566411927.TaoPassword-Outside.isv%26sp_tk%3D4oKsQVJxMGIzeFZvT3figqw%3D%26spm%3Da211b4.24728341%26visa%3D13a09278fde22a2e%26disablePopup%3Dtrue%26disableSJ%3D1&appkey=24728341&visa=13a09278fde22a2e',
  'pic_url': 'http://img.alicdn.com/bao/uploaded/i4/595412874/TB2SOfPm7KWBuNjy1zjXXcOypXa_!!595412874.jpg',
  'request_id': 'u259wsbbqld2',
  'suc': True,
  'thumb_pic_url': 'http://img.alicdn.com/bao/uploaded/i4/595412874/TB2SOfPm7KWBuNjy1zjXXcOypXa_!!595412874.jpg_170x170.jpg',
  'title': '淘口令-页面',
  
  'url': 'https://item.taobao.com/item.htm?id=567873872517&ut_sk=1.utdid_24728341_1536566411927.TaoPassword-Outside.isv&sp_tk=4oKsQVJxMGIzeFZvT3figqw=&spm=a211b4.24728341&visa=13a09278fde22a2e&disablePopup=true&disableSJ=1'}}
    '''