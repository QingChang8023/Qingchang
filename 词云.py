# encoding: utf-8
import os
from pyecharts import WordCloud


# 词云
def wordcloud(x, y, label):
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", x, y, word_size_range=[20, 100], shape="triangle-forward")
    wordcloud.render()
    os.system(r"render.html")


x = [
    '人生苦短我用Python', 'Web', '人工智能', '大数据', 'Django',
    'Flask', '机器学习', '数据分析', '深度学习', '运维测试', '爬虫',
    '面试啊', '找工作啊', '黑马成就你的未来', '一睡一上午', "数据处理",
    '小姐姐呢', '天天懵逼', '毕业', '简历咋编啊', '庆长']

# 你们懂的
y = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265, 5000]
label = "词云"
wordcloud(x, y, label)
