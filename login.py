# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 06:00
# @Author  : srcrs
# @Email   : srcrs@foxmail.com

import base64
import json
import rsa
import time
import requests
import logging
import traceback
import os
import json

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
ch.setFormatter(logging.Formatter("[%(asctime)s]:%(levelname)s:%(message)s"))
logger.addHandler(ch)

# 自动保存会话
session = None

# 进行登录
# 手机号和密码加密代码，参考自这篇文章 http://www.bubuko.com/infodetail-2349299.html?&_=1524316738826


def login(username, password):
    global session
    session = requests.Session()
    # 这里对手机号和密码加密，传入参数需是 byte 类型
    username = username
    password = password
    # appId 联通后端会验证这个值,如不是常登录设备会触发验证码登录
    #appId = os.environ.get('APPID_COVER')
    # 设置一个标志，用户是否登录成功
    flag = False

    # cookies = {
    #     'c_sfbm': '234g_00',
    #     'logHostIP': 'null',
    #     'route': 'cc3839c658dd60cb7c25f6c2fe6eb964',
    #     'channel': 'GGPD',
    #     'city': '076|776',
    #     'devicedId': 'B97CDE2A-D435-437D-9FEC-5D821A012972',
    #     'mobileService1': 'ProEsSI6SM4DbWhaeVsPtve9pu7VWz0m94giTHkPBl40Gx8nebgV!-1027473388',
    #     'mobileServiceAll': 'a92d76b26705a45a087027f893c70618',
    # }

    headers = {
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }

    payload = "{\"email\":\""+username+"\",\"passwd\":\""+password+"\"}"

    response = session.post('http://j01.space/signin',
                            headers=headers, data=payload)
    response.encoding = 'utf-8'
    try:
        result = json.loads(response.text) 
        # response.json()
        if result['code'] == 200:
            logger.info('【登录成功】: ' + result['msg'])
            # session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1901 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36; unicom{version:android@8.0100,desmobile:' + str(username) + '};devicetype{deviceBrand:Realme,deviceModel:RMX1901};{yw_code:}'})
            flag = True
        else:
            logger.info('【登录失败】: ' +  result['msg'])
    except Exception as e:
        print(traceback.format_exc())
        logger.error('【登录异常】: ' + str(e))
    if flag:
        return session
    else:
        return False
