#!/usr/bin/python3
# -*-coding:utf-8-*-


'''
爬取网页为:
http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html

获取2020年全国大学排名
'''


import requests
import os
import csv
from bs4 import BeautifulSoup


def get_response(url):
    '''
    获取网页链接，返回网页内容
    @param url: 获取网页链接
    @return: 返回网页内容
    '''
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    r = requests.get(url, headers=headers).content.decode()
    return r


def get_content_list(response) -> list:
    '''
    获取网页内容，返回<tr>标签的列表形式
    @param response: 获取网页内容
    @return: 返回<tr>标签的列表形式
    '''
    soup = BeautifulSoup(response, 'lxml')
    content = soup.find_all('tr', class_='alt')
    return content


def get_content(con):
    '''
    获取网页<tr>标签内容，返回<td>标签中的内容
    @param con:获取网页<tr>标签内容
    @return:返回<td>标签中的内容
    '''
    rank = con.find_all('td')[0].string
    name = con.find_all('td')[1].string
    score = con.find_all('td')[4].string
    return rank, name, score


def save_file(data:list):
    '''
    获取数据列表，以CSV格式保存文件
    @param data: 获取数据列表
    @return:
    '''
    txt_name = '大学排名'
    os.makedirs(txt_name, exist_ok=True)
    with open(os.path.join(txt_name, 'result.csv'), 'w', encoding='gbk', newline='')as f:
        write = csv.DictWriter(f, fieldnames=['排名', '大学名称', '综合得分'])
        write.writeheader()
        write.writerows(data)


if __name__ == '__main__':
    data = {}
    big_data = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    response = get_response(url)
    content_list = get_content_list(response)
    for con in content_list:
        rank, name, score = get_content(con)
        data = {'排名': rank, '大学名称': name, '综合得分': score}
        big_data.append(data)
    save_file(big_data)
