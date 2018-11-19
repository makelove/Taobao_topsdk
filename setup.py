#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# packages=find_packages()
# print('找到的packages:',packages)#['top', 'aliyun', 'test', 'top.api', 'top.api.rest', 'aliyun.api', 'aliyun..rest']


setup(
    name='topsdk',
    version='18.11.19',  # 按日期
    author='top',
    author_email='xuteng.xt@alibaba-inc.com',
    # packages=find_packages(),
    packages=['top'],
    install_requires=[],
    license='MIT',
    description="淘宝联盟topsdk-淘宝返现工具",
    long_description_content_type="text/markdown",
    long_description='淘宝联盟topsdk,进行导购推广,有了它，不需要去写爬虫抓取联盟商品信息'
)
