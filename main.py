import requests
import json
import time
import re
import logging
import traceback
import os
import random
# import notify
import datetime
import feedparser
import utils
import wxpusher
from lxml.html import fromstring
import pytz


def main(event, context):
    config = utils.readJsonFile('config.json')
    getFeeds()
    content = utils.getLogContent()
    wxpusher.sendTopicMessage(
        config["token"],
        '测试推送',
        content,
        '1832',
        'https://fund.lsj8.ltd'
    )

    utils.clearLog()
    # # 清空日志记录
    # open('./log.txt', mode='w', encoding='utf-8')


def getFeeds():
    rss = feedparser.parse('http://feeds.feedburner.com/mattkaydiary/pZjG')
    current = rss["entries"][0]
    result = re.findall(r"vmess://(.+?)</div>", rss["entries"][0]["summary"])
    i = 0
    for point in result:
        i = i + 1
        logging.info('【'+('%02d' % i) + '】 vmess://' + point)


# 主函数入口
if __name__ == '__main__':
    # 初始化日志文件
    utils.initLog('log.txt')
    main("", "")
