- 视频: https://www.bilibili.com/video/av51745248/

- 参考
    - 自然语言处理（五 文本相似度）https://blog.csdn.net/hustchenze/article/details/78815948
    - Python 字符串相似性的几种度量方法 https://blog.csdn.net/dcrmg/article/details/79228589
    - 比较两个字符串的相似度 https://blog.csdn.net/gt11799/article/details/40146343

- 原理
    - 评价字符串相似度最常见的办法就是：把一个字符串通过插入、删除或替换这样的编辑操作，变成另外一个字符串，所需要的最少编辑次数，这种就是编辑距离（edit distance）度量方法，也称为Levenshtein距离。
    - 海明距离是编辑距离的一种特殊情况，只计算等长情况下替换操作的编辑次数，只能应用于两个等长字符串间的距离度量。
