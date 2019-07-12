# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 18:41
# @Author  : play4fun
# @File    : compare_2string_similarity.py
# @Software: PyCharm

"""
compare_2string_similarity.py:
"""
import traceback
from datetime import datetime
from pprint import pprint

def main():
    from difflib import SequenceMatcher

    str1 = '赫本风气质长裙小清新女2019春夏新款中长款波点雪纺连衣裙'
    str2 = '2019法式复古山本赫本风气质长裙小清新女夏裙子中长款连衣裙子'
    ratio = SequenceMatcher(None, str1, str2).ratio()
    print('相似度为', ratio)
    print('-'*40)

    #
    title = "2019春夏新款复古民族风"
    titles = ['棉麻唐装两件套女春夏新款2019民族风女装复古刺绣盘扣喇叭袖套装', '2019春夏新款宽松显瘦大码棉麻女装 民族风复古绣花 刺绣连衣裙', '2019两件套雪纺连衣裙女春夏新款民族风绣花复古显瘦套装中长裙子', '春夏新款两件套女2019民族风女装文艺复古绣花雪纺披肩加无袖裙子', '2019春夏新款复古民族风女装V领宽松七分袖碎花棉麻连衣裙长裙子', '童装春夏装2019新款女童连衣裙子长袖复古中国民族风汉服儿童旗袍', '2019民族风春夏新款女装棉麻连衣裙两件套装复古印花中长裙套装裙', '2019春夏新款民族风印花高腰复古a字半身裙防走光短裙显瘦包臀裙', '2019春夏新款民族风文艺复古百搭大码棉麻绣花短袖宽松t恤上衣女', '2019春夏新款民族风大码女装棉麻连衣裙复古印花旅游度假时尚套装']
    scores = [(t,SequenceMatcher(None, title, t).ratio()) for t in titles]
    # print('相似度为', scores)
    print(title)
    pprint(scores)
    pass


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
