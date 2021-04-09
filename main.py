import requests
import json
import time
import re
import logging
import traceback
import os
import random
import notify
import datetime
import feedparser
from lxml.html import fromstring
import pytz


def main(event, context):
    token = readJson()
    # getFeeds()
    logging.info('这是一条测试信息')
    notify.sendWxPusherByTopic(token, "1832")
    # for user in users:
    #     notify.sendPushplus(user["appId"])

    # 清空日志记录
    open('./log.txt', mode='w', encoding='utf-8')


def getFeeds():
    rss = feedparser.parse('http://feeds.feedburner.com/mattkaydiary/pZjG')
    current = rss["entries"][0]
    # print(rss["entries"][0]["summary"])
    # logging.info('【发布时间】: ' + current["published"])
    result = re.findall(r"vmess://(.+?)</div>", rss["entries"][0]["summary"])
    i = 0
    for point in result:
        i = i + 1
        logging.info('【'+('%02d' % i) + '】 vmess://' + point)


# 读取用户配置信息
# 错误原因有两种：格式错误、未读取到错误
def readJson():
    try:
        # 用户配置信息
        with open('./token.txt', 'r') as fp:
            return fp
        # with open('./config.json', 'r') as fp:
        #     users = json.load(fp)
        #     return users
    except Exception as e:
        print(traceback.format_exc())
        logging.error('账号信息获取失败错误，原因为: ' + str(e))
        logging.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
        logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')


# 主函数入口
if __name__ == '__main__':
    # 日志基础配置
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建一个handler，用于写入日志文件
    # w 模式会记住上次日志记录的位置
    fh = logging.FileHandler('./log.txt', mode='a', encoding='utf-8')
    fh.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(fh)
    # 创建一个handler，输出到控制台
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(
        "[%(asctime)s]:%(levelname)s:%(message)s"))
    logger.addHandler(ch)

    main("", "")
