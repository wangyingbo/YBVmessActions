import requests
import json
import time
import re
import logging
# import login
import traceback
import os
import random
import notify
import datetime
import feedparser
from lxml.html import fromstring
import pytz


def main(event, context):
    # user = readJson()
    getFeeds()
    # for user in users:
    #     # 清空上一个用户的日志记录
    #     open('./log.txt', mode='w', encoding='utf-8')
    # global client
    # client = login.login(user["username"], user["password"])
    # print(client != False)
    # if client != False:
    #     getUserInfo()
    #     checkIn()
    #     notify.sendPushplus(user["appId"])


def getFeeds():
    logging.info('【发布时间】: ')
    # print("TODO 获取用户信息")
    rss = feedparser.parse('http://feeds.feedburner.com/mattkaydiary/pZjG')
    current = rss["entries"][0]
    # print(rss["entries"][0]["summary"])
    # logging.info('【发布时间】: ' + current["published"])
    result = re.findall(r"vmess://(.+?)</div>", rss["entries"][0]["summary"])
    # print(result)
    i = 0
    for point in result:
        i = i + 1
        logging.error('【'+('%02d' % i) + '】 vmess://' + point)
        # print('【'+('%02d' % i) + '】 vmess://' + point)


# 读取用户配置信息
# 错误原因有两种：格式错误、未读取到错误


def readJson():
    try:
        # 用户配置信息
        with open('./config.json', 'r') as fp:
            users = json.load(fp)
            return users
    except Exception as e:
        print(traceback.format_exc())
        logging.error('账号信息获取失败错误，原因为: ' + str(e))
        logging.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
        logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')


# 主函数入口
if __name__ == '__main__':
    main("", "")
