# Taobao_topsdk
淘宝客-淘宝联盟-阿里妈妈 topsdk

- 文档
    - 官方-淘宝客API https://open.taobao.com/api.htm?docId=24515&docType=2

| key | 含义 |
| ------ | ------ |
| pict_url | 商品主图 |
| reserve_price | 商品一口价格 |
| zk_final_price | 商品折扣价格 |
| volume | 30天销量 |
| provcity | 宝贝所在地  发货地 |


- 从淘宝下载的top，python是2.7的，满是bug
    - 现在已经修改为python 3.6
- Enjoy！
    - 有一些api没有加入，因为下载sdk时，淘宝是根据你的权限自动生成的。很讨厌！
    - 有时候新增加了一些api，也不知道
- 安装
    - python setup.py clean 
    - python setup.py install 
    - 更方便
        - https://pypi.org/project/topsdk/
        - pip install topsdk
        - pip install topsdk --upgrade
        - 卸载 
            - pip uninstall topsdk
    
- 更新update
    - 2018.11.1
        - 在【阿里开放平台－控制台】下载Java sdk 发现更新了。需要【点击生成】，无语！
        - 新增了 TbkShopConvertRequest TbkScOptimusMaterialRequest
        - 很有用的api是TbkTpwdConvertRequest
            - 支持通过淘口令解析商品id，并提供对应的淘客转链接
            - 反向解析：淘口令-->s.click.taobao.com链接
            - 把别人的淘口令转成自己的淘口令
            -  跟 TbkTpwdCreateRequest 相反
            
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


- 交流
    - 加我微信:sexy8dream
    - 扫码进群
    <img src="http://images7n.dark.net.cn/cps-union-tb-jd-pdd4.jpg" width = "300" height = "473" alt="wechat_donate"  />