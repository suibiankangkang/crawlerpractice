#!/usr/bin/python3
# ! -*-coding:utf-8-*-

import requests
import os
import time
import re
from bs4 import BeautifulSoup

'''
练习的网站是糗事百科
https://www.qiushibaike.com/text/page/1
到
https://www.qiushibaike.com/text/page/13
'''


def get_html(url):
    '''
    输入url链接，返回网页内容
    :param url: 网页链接
    :return: 返回网页内容
    '''
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers).content.decode()
    return response


def get_tag_list(response):
    '''
    输入网页内容，返回标签对象列表
    :param response: 网页内容
    :return: 返回标签对象列表
    '''
    soup = BeautifulSoup(response, 'html.parser')
    tag = soup.find('div', class_="col1 old-style-col1")
    tag_list = tag.find_all('div', class_=re.compile("article .*?"))
    return tag_list


def get_content(tag):
    '''
    获取标签对象，返回标签的文本内容
    :param tag:标签对象
    :return:返回标签的文本内容
    '''
    content = tag.find('div', class_='content').find('span').get_text()
    return content

def get_author(tag):
    '''
    获取标签对象，返回作者昵称
    :param tag: 标签对象
    :return: 返回作者昵称
    '''
    author = tag.find('h2').string
    return '作者:'+author

def get_vote(tag):
    '''
    获取标签对象，返回点赞数
    :param tag: 标签对象
    :return: 返回点赞数
    '''
    vote = tag.find('span', class_="stats-vote").find('i', class_="number").get_text()
    return '点赞数'+vote

def save_txt(content, author, vote):
    '''
    获取
    :param content:
    :return:
    '''
    os.makedirs('糗事百科', exist_ok=True)
    with open(os.path.join('糗事百科', 'qiubai' + '.txt'), 'a', encoding='utf-8') as f:
        f.write(author+content+vote+'\n------------------------------------\n')

if __name__ == '__main__':
    for i in range(1, 13):
        time.sleep(1)
        url = 'https://www.qiushibaike.com/text/page/'+str(i)
        html = get_html(url)
        tag_list = get_tag_list(html)
        for tag in tag_list:
            content = get_content(tag)
            author = get_author(tag)
            vote = get_vote(tag)
            save_txt(content, author, vote)
