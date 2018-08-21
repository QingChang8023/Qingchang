import requests
from lxml import etree

url = "http://m.youdao.com/translate"
headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)'
           }
data = input('请输入：')
content = {"inputtext":data,"type":"AUTO"}
con = requests.post(url,content).content.decode("utf8")
html = etree.HTML(con)
res = html.xpath("//ul[@id='translateResult']/li/text()")
print(res)