# encoding: utf-8
import os
from pyecharts import Bar,Pie,Line,WordCloud
def get_charts(x,y,label,type):
    if type==1:
        c = Pie("饼状图")
    elif type==2:
        c = Bar("条形图")
    elif type==3:
        c = Line("折线图")
    c.add(label, x,y,is_more_utils=True)
    c.show_config()
    c.render()
    os.system(r"render.html")

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y = [5, 20, 36, 10, 75, 90]
label = "服装"
type=3
# 图表绘制
get_charts(x,y,label,type)

# 词云
def wordcloud(x,y,label):
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", x, y, word_size_range=[20, 100])
    wordcloud.render()
    os.system(r"render.html")
x = [
 'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
y = [
 10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]

