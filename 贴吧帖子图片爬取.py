# -*- coding: utf-8 -*-


# url:https://tieba.baidu.com/f?kw=%E5%A6%B9%E5%AD%90&ie=utf-8&pn=150
# "//li[@class="j_thread_list clearfix"]"
import requests
from pprint import pprint
from lxml import etree
import os


class Tieba(object):
    """贴吧帖子爬取"""

    def __init__(self):
        self.base_url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.kw = input("请输入贴吧名：")
        # self.kw = "妹子"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }

    def url_list(self):
        """构建url"""
        return [self.base_url.format(self.kw, pn) for pn in range(0, 100, 50)]

    def run(self, ):
        """读取"""
        images_list = []
        # 获取url的html内容
        for url in self.url_list():
            response = requests.get(url, headers=self.headers)
            html = response.content.decode('utf-8')
            # 提取数据
            # 构建节点对象
            rootElement = etree.HTML(html)
            # 初步提取（行数据）
            rows = rootElement.xpath('//li[@class="tl_shadow tl_shadow_new"]')
            for row in rows:
                # 精确提取内容
                title = row.xpath('.//div[@class="ti_title"]/span/text()')
                if title is not None and len(title) > 0:
                    # 提取的内容为列表形式，以下标取出来
                    title = title[0]
                    # print(title)
                # 提取图片
                images = row.xpath('.//img[@class="j_media_thumb_holder medias_img medias_thumb_holder"]/@data-url')
                if images is not None and len(images) > 0:
                    for image in images:
                        images_list.append(image)
        return images_list

    def write(self):
        """写入"""
        # 路径
        cur_path = os.path.abspath(os.curdir) +'/{}'.format(self.kw)
        # 新建文件夹
        os.mkdir(cur_path)
        n = 1
        images = self.run()
        for image in images:
            # 下载图片
            try:
                print('开始下载第{}张'.format(n))
                with open(cur_path+'/{}.jpg'.format(n), 'wb+') as f:
                    f.write(requests.get(image).content)
                n += 1
            except:
                print('第{}张下载失败'.format(n))
                pass


if __name__ == '__main__':
    tieba = Tieba()
    tieba.write()
