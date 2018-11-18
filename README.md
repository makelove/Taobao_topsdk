# Taobao_topsdk
淘宝客-淘宝联盟-阿里妈妈 topsdk

- 从淘宝下载的top，python是2.7的，满是bug
    - 现在已经修改为python 3.6
- Enjoy！
    - 有一些api没有加入，因为下载sdk时，淘宝是根据你的权限自动生成的。很讨厌！
    - 有时候新增加了一些api，也不知道
- 安装
    - python setup.py clean 
    - python setup.py install 
    
- 更新update
    - 2018.11.1
        - 在【阿里开放平台－控制台】下载Java sdk 发现更新了。需要【点击生成】，无语！
        - 新增了 TbkShopConvertRequest TbkScOptimusMaterialRequest
        - 很有用的api是TbkTpwdConvertRequest
            - 支持通过淘口令解析商品id，并提供对应的淘客转链接
            - 反向解析：淘口令-->s.click.taobao.com链接
            - 把别人的淘口令转成自己的淘口令
            -  跟 TbkTpwdCreateRequest 相反
            
