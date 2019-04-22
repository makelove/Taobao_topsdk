# Taobao_topsdk
淘宝客-淘宝联盟-阿里妈妈 topsdk

- 文档
    - 官方-淘宝客API https://open.taobao.com/api.htm?docId=24515&docType=2
    - [阿里开放平台－控制台](http://console.open.taobao.com/app/appList.htm#/app/manager)

- 最新消息
    - 2019-04-01
        - [淘宝客新等级体系正式上线&FAQ专场](https://tbk.bbs.taobao.com/detail.html?spm=a219t.7900221/1.1998910419.de4e1af6f0.6edb75a58McTjx&postId=9119458)
    - 2019-02-20
        - [推广位创建总数不超过200个](https://tbk.bbs.taobao.com/detail.html?spm=a219t.7900221/1.1998910419.39.6edb75a58McTjx&appId=45301&postId=9102740)
    - 2019-01-16
        - [《淘宝客私域用户管理》-新手指南](https://mo.m.taobao.com/pdum)
    - 2018-05-28
        - [史上最详细淘宝联盟API使用教程](https://tbk.bbs.taobao.com/detail.html?postId=8576944)
        - [官方推荐商品库大全（提供最新API获取方式）](https://tbk.bbs.taobao.com/detail.html?appId=45301&postId=8576096)

| key | 含义 |
| ------ | ------ |
| pict_url | 商品主图 |
| reserve_price | 商品一口价格 |
| zk_final_price | 商品折扣价格 |
| volume | 30天销量 |
| provcity | 宝贝所在地  发货地 |
| user_type | 卖家类型，0表示淘宝集市，1表示天猫商城 |


- 从淘宝下载的top，python是2.7的，满是bug
    - 现在已经修改为python 3.6
- Enjoy！
    - 有一些api没有加入，因为下载sdk时，淘宝是根据你的权限自动生成的。
    - 有时候新增加了一些api，也不知道

- 更新update
    - 2018.11.1
        - 在【阿里开放平台－控制台】下载Java sdk 发现更新了。需要【点击生成】，无语！
        - 新增了 TbkShopConvertRequest TbkScOptimusMaterialRequest
        - 很有用的api是TbkTpwdConvertRequest
            - 支持通过淘口令解析商品id，并提供对应的淘客转链接
            - 反向解析：淘口令-->s.click.taobao.com链接
            - 把别人的淘口令转成自己的淘口令
            -  跟 TbkTpwdCreateRequest 相反

- 安装
    - python setup.py clean
    - python setup.py install
    - 更方便
        - https://pypi.org/project/topsdk/
        - pip install topsdk
        - 更新
            - pip install topsdk --upgrade
        - 卸载
            - pip uninstall topsdk

- 上传到pypi
    - rm -rf build dist
    - 打包
        - python3 setup.py sdist bdist_wheel
    - ls dist/
    - 上传
        - twine upload dist/*
    - 不能安装问题
        - UnicodeEncodeError: 'ascii' codec can't encode characters in position 38-42: ordinal not in range(128)
        - 在py文件头添加
        ```python
        # -*- coding: utf-8 -*-
        ```
        - 1

- 应用
    - 利用【大淘客】建站
        - 演示DEMO http://youhui.dark.net.cn/
        - 帮助文档 http://help.dataoke.com/hc/kb/category/1012170/
        - [大淘客CMS系统如何使用](http://help.dataoke.com/hc/kb/article/1128855/)
            - 大淘客CMS系统使用首先需要拥有自己的网站，最基础就是有空间和域名，建议空间最好是支持PHP5.4及以上的，同时购买域名时请确认备案域名和注册域名一致，如出现差异是无法使用大淘客CMS系统的。
        - 缺点:
            - 不支持HTTPS,会被劫持流量
            - 可能会偷单
    - App
    - 公众号-订阅号
    - 微信小程序

- 交流
    - 公众号:真AI人工智能
    <img src="http://images7n.dark.net.cn/true_ai_wxpa.jpg" width = "300" height = "300" alt="wechat_public_account"  />

    - 加我微信:sexy8dream
    <img src="http://images7n.dark.net.cn/sexy8dream.jpg" width = "300" height = "300" alt="wechat_account"  />

    - 扫码进群
    <img src="http://images7n.dark.net.cn/cps-union-tb-jd-pdd8.jpg" width = "300" height = "473" alt="wechat_group"  />