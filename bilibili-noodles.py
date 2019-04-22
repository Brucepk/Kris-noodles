# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
import requests

'''
原创作者：pk哥
Date：2019/4/20
原创首发于公众号：Python知识圈，欢迎关注查看更多精彩实战项目

'''

url = 'http://comment.bilibili.com/87150521.xml'
html = requests.get(url).content
html_data = str(html, 'utf-8')
soup = BeautifulSoup(html_data, 'lxml')
results = soup.find_all('d')

comments = [comment.text for comment in results]
comments_dict = {'comments': comments}

df = pd.DataFrame(comments_dict)
df.to_csv('noodles.csv', encoding='utf-8')