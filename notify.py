
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 06:30
# @Author  : srcrs
# @Email   : srcrs@foxmail.com

import smtplib
import traceback
import os
import requests
import urllib
import json
# from email.mime.text import MIMEText

# 发送push+通知


def sendPushplus(token):
    try:
        # 发送内容
        data = {
            "token": token,
            "title": "VMESS每日节点",
            "content": readFile_html('./log.txt')
        }
        url = 'http://www.pushplus.plus/send'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('push+通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())


def sendWxPusherByTopic(appToken, topicId):
    try:
        content = readFile_html('./log.txt')
        # 发送内容  1832
        data = {
            "appToken": appToken,
            "content": content,
            "summary": "最新VMESS节点",
            "contentType": 1,
            "topicIds":  [topicId],
            "url": "https://fund.lsj8.ltd"
        }
        # body = '{"appToken":"'+appToken + \
            # '","content":"' + \
            # content + \
            # '","summary":"最新VMESS节点","contentType":1,"topicIds":[' + \
            # topicId+'],"url":"https://fund.lsj8.ltd"}'
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        headers = {'Content-Type': 'application/json'}
        body = json.dump(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('wxpusher通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())


# 返回要推送的通知内容
# 对html的适配要更好
# 增加文件关闭操作
def readFile_html(filepath):
    content = ''
    with open(filepath, "r", encoding='utf-8') as f:
        for line in f.readlines():
            content += line + '<br>'
    return content
