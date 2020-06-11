#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import lxml.html
import redis


def get_url_list(url, headers):
    response = requests.Session().get(url, headers=headers).content.decode()

    selector = lxml.html.fromstring(response)

    url_ls = selector.xpath('//ul[@class="newlist"]')
    for u_l in url_ls:
        url_list = u_l.xpath('li/span[@class="sub"]/a[2]/@href')

    for url in url_list:
        client.sadd('url_queue', url)


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    url = 'https://guba.eastmoney.com'

    client = redis.StrictRedis()
    get_url_list(url, headers)