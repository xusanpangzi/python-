#在网上搜了一个爬虫的程序，改了改。很奇怪，我用原程序中的网址可以爬取图片，但是我自己找的网址就是不行，同样是贴吧里的。
# 这个问题不知道什么时候才能解决

import requests
import re
import os
import urllib
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def pagelist(html):
    imgre = re.compile(r'src="(.+?\.jpg)" size')
    imglist=imgre.findall(html)
    x = 0
    path = 'C:\\Users\\qqq\\PycharmProjects\\untitled\\python小项目\\thirteen'
    # 将图片保存到thirteen文件夹中，如果没有 则创建
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'  # 保存在test路径下
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))  # 打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
        x = x + 1
    return imglist

def main():
    url='https://tieba.baidu.com/p/5287936288'
    html=getHTMLText(url)
    print(pagelist(html))
main()

