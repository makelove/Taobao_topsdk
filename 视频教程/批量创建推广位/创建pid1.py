# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 14:31
# @Author  : play4fun
# @File    : 创建pid1.py
# @Software: PyCharm

"""
创建pid1.py:

淘宝




"""
import string
import random
import requests
from time import sleep

s = requests.Session()
url = 'https://pub.alimama.com/common/adzone/selfAdzoneCreate.json'
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "authority": "pub.alimama.com",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://pub.alimama.com",
    "referer": "https://pub.alimama.com/promo/search/index.htm",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# TODO 更换为你的cookies
cookies = {

}


# def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
def random_string_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    for i in range(6):  # TODO
        # 生成随机字符串
        pidn = 'AI_' + random_string_generator(8)  # TODO 修改前缀
        print('PID:', pidn)
        params = {
            'tag': 29,
            'gcid': 0,
            'siteid': 123123,  # TODO 更换为你的siteid
            'selectact': 'add',
            'newadzonename': pidn,
            '_tb_token_': cookies['_tb_token_']
        }

        # 请求 selfAdzoneCreate.json
        response = s.post(url, params=params, headers=headers, cookies=cookies)
        js = response.json()
        print(js)
        if 'data' in js:
            print('创建成功', js['data'])

        # 打印 dict
        print('-' * 30)
        sleep(6)

    pass


if __name__ == '__main__':
    main()
    # TODO 上传到数据库
