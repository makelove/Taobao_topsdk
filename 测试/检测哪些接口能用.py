# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 16:47
# @Author  : play4fun
# @File    : 检测哪些接口能用.py
# @Software: PyCharm

"""
检测哪些接口能用.py:
TODO
工作量大?

"""
import traceback
from datetime import datetime


def main():
    pass


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')