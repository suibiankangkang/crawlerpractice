#!/usr/bin/python3
# coding:utf-8

import requests
import re
import os
import time

def get_url_list(response):
    '''
    获取链接列表
    :param response: html内容
    :return: 链接列表
    '''
    url_list = []
    text = re.findall('<dt>神圣罗马帝国 小说全部目录</dt>(.*?)</dl>', response, re.S)[0]
    text_url = re.findall('href="(.*?)"', text, re.S)
    for url in text_url:
        url_list.append(url)
    return url_list

def get_article(response):
    '''
    获取正文内容
    :param response: html内容
    :return: 文章标题 & 正文内容
    '''
    name = re.search('<h1>(.*?)</h1>', response, re.S).group(1)
    for ch in '\/:*?"<>|':
        name = name.replace(ch, 'x')
    text = re.search('<div id="content">(.*?)</div>', response, re.S).group(1)
    text = text.replace('<br>', '\n')
    return name, text

def save(name, text):
    '''
    保存到本地
    :param name: 文章标题
    :param text: 正文内容
    :return:
    '''
    os.makedirs('神圣罗马帝国', exist_ok=True)
    with open(os.path.join('神圣罗马帝国', name+'.txt'), 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    url = 'http://www.kannunu8.com/book/617/'
    response = requests.get(url, headers=headers).content.decode()

    url_list = get_url_list(response)
    for url in url_list:
        time.sleep(1)
        response = requests.get('http://www.kannunu8.com'+url, headers=headers).content.decode()
        name, text = get_article(response)
        save(name, text)
