#!/usr/bin/python3
# -*-coding:utf-8-*-

'''
爬取“新时代中国特色社会主义”文本内容
制作成词云后，保存为png格式
'''


import requests
import jieba
import os
import wordcloud



def get_response(url):
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    res = requests.get(url, headers=headers).content.decode()
    name = '新时代中国特色社会主义'
    return res, name


def save_file(response, name):
    os.makedirs(name, exist_ok=True)
    with open(os.path.join(name, 'content.txt'), 'w', encoding='utf-8') as f:
        f.write(response)


def read_txt(response, name):
    with open(os.path.join(name, 'content.txt'), 'r', encoding='utf-8') as f:
        content = f.read()
    ls = jieba.lcut(content)
    txt = ''.join(ls)
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700, background_color="white")
    w.generate(txt)
    w.to_file("grwordcloud.png")



if __name__ == '__main__':
    url = 'https://python123.io/resources/pye/新时代中国特色社会主义.txt'
    response, name = get_response(url)
    save_file(response, name)
    read_txt(response, name)
