# -*- coding: utf-8 -*-
# @Time    : 2019-05-05 15:46
# @Author  : play4fun
# @File    : random_emoji.py
# @Software: PyCharm

"""
random_emoji.py:
"""
import traceback
from datetime import datetime

import re
from random import choice
from itertools import product


def emoji_list():  # 淘口令前后缀字符串
    # tkl_valid_char = ['$', '¥', '€', '💰', '🔑', '🎵', '✔️', '💲', '🔐', '📲']  # $￥¥€💰🔑🎵✔️💲🔐📲
    dollor = [('$', '$'),
              ('￥', '￥'),
              ('€', '€'), ]
    emojis1 = ['💰', '🔑', '🎵', '💲', '🔐', '📲']  # '✔️'不能作为第一个字符
    emojis2 = ['💰', '🔑', '🎵', '✔️', '💲', '🔐', '📲']
    emoji_list = dollor + list(product(emojis1, emojis2))

    return emoji_list


def random_emoji(tkl: str):
    pattern = "([$￥¥€💰🔑🎵✔️💲🔐📲])([0-9a-zA-Z]{11})([$￥¥€💰🔑🎵✔️💲🔐📲])"
    rs = re.findall(pattern, tkl)
    if len(rs) > 0:
        for t1 in rs:
            t1s = ''.join(t1)#旧的淘口令

            co = choice(emoji_list())
            nstr = f"{co[0]}{t1[1]}{co[1]}"#生成新淘口令
            tkl = tkl.replace(t1s, nstr)

    return tkl


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        tkl = f'''笨笨狗膨化食品粗粮夹心米果 能量棒糙米卷 早餐饼干休闲零食54支
【在售价】22.80元
【券后价】12.80元
【下单链接】https://m.tb.cn/h.ecHATMZ
-----------------
复制这条信息，￥8S7JY1cryHh￥，到【手机淘宝】即可查看'''
        print(random_emoji(tkl))
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
