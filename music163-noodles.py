# -*- coding:utf-8 -*-
import requests
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
import PIL.Image as Image
from os import path
import time
import random

'''
原创作者：pk哥
Date：2019/4/20
原创首发于公众号：Python知识圈，欢迎关注查看更多精彩实战项目

'''


def get_html(url):  # 获取网页json格式信息
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    html = requests.get(url, headers=headers).json()
    return html


hot_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_1359595520?limit=20&offset=0'
html = get_html(hot_url)
hotComments = html['hotComments']
contentlist = []
for i in hotComments:  # 绘制热评词云图
    content = i['content']
    contentlist.append(content)
text = "".join(contentlist)
cut = jieba.cut(text, cut_all=True)  # 分词
word = ",".join(cut)
coloring = np.array(Image.open("1.jpg"))  # 电脑中自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=3000, max_font_size=200,
                         mask=coloring, random_state=100, font_path='./font/STXINGKA.TTF',
                         scale=2).generate(word)  # 定义词云背景图颜色、尺寸、字体大小、电脑中字体选择,random_state 为每个单词返回一个PIL颜色
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))  # 绘图颜色
plt.imshow(my_wordcloud)  # 绘图内容
plt.axis("off")
# plt.show()  # 显示图
d = path.dirname(__file__)  # project 当前目录
my_wordcloud.to_file(path.join(d, '热门评论图.png'))
print('热门评论词云图完成，在项目代码目录下查看')

allcomments = []  # 提取前 100 页评论信息
for j in range(0, 2001, 20):
    all_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_1359595520?limit=20&offset={}'.format(j)
    for k in range(0, 20):
        html = get_html(all_url)
        comment = html['comments'][k]['content']  # 绘制热评词云图
        allcomments.append(comment)
    print('正在收集全部评论，请稍等。。。')
    time.sleep(int(format(random.randint(3, 8))))
text = "".join(allcomments)
cut = jieba.cut(text, cut_all=True)  # 分词
word = ",".join(cut)
coloring = np.array(Image.open("2.jpg"))  # 电脑中自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=3000, max_font_size=200,
                         mask=coloring, random_state=100, font_path='./font/STXINGKA.TTF',
                         scale=2).generate(word)  # 定义词云背景图颜色、尺寸、字体大小、电脑中字体选择,random_state 为每个单词返回一个PIL颜色
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))  # 绘图颜色
plt.imshow(my_wordcloud)  # 绘图内容
plt.axis("off")
# plt.show()  # 显示图
d = path.dirname(__file__)  # project 当前目录
my_wordcloud.to_file(path.join(d, '全部评论.png'))
print('全部评论词云图完成，在项目代码目录下查看')