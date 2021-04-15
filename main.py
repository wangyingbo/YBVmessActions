import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import feedparser
import utils
import wxpusher
import pytz
# import base64

from lxml.html import fromstring
import urllib.parse
import urllib3
urllib3.disable_warnings()


def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    config = utils.readJsonFile('config.json')
    # artUrl = getArticle()
    # getSubscribeUrl(artUrl)
    getSubscribeUrl()
    # a = dy
    # content = utils.getLogContent()
    # wxpusher.sendTopicMessage(
    #     config["token"],
    #     '最新VMESS节点',
    #     content,
    #     [1832],
    #     'https://fund.lsj8.ltd'
    # )


def getFeeds():
    rss = feedparser.parse('http://feeds.feedburner.com/mattkaydiary/pZjG')
    current = rss["entries"][0]
    result = re.findall(r"vmess://(.+?)</div>", rss["entries"][0]["summary"])
    i = 0
    dy = ''
    for point in result:
        i = i + 1
        dy += 'vmess://'+point+'\n'
        logging.info('【'+('%02d' % i) + '】 vmess://' + point)
    return base64.b64encode(dy.encode('utf-8'))

# 获取文章地址


def getSubscribeUrl():
    rss = feedparser.parse('http://feeds.feedburner.com/mattkaydiary/pZjG')
    current = rss["entries"][0]
    v2rayList = re.findall(
        r"v2ray\(若无法更新请开启代理后再拉取\)：(.+?)</div>", rss["entries"][0]["summary"])
    clashList = re.findall(
        r"clash\(若无法更新请开启代理后再拉取\)：(.+?)</div>", rss["entries"][0]["summary"])
    v2rayTxt = requests.request(
        "GET", v2rayList[len(v2rayList)-1], verify=False)
    clashTxt = requests.request(
        "GET", clashList[len(clashList)-1], verify=False)
    
    print(v2rayList)
    print(clashList)
    with open('./v2ray.txt', 'a+') as f:
    f.write(v2rayTxt)
    
    with open('./clash.yml', 'a+') as f:
    f.write(clashTxt)


# 主函数入口
if __name__ == '__main__':
    main("", "")
