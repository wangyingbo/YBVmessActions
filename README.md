# VmessActions
通过GitHub的actions 自动采集节点 并推送到微信


1、在 http://www.pushplus.plus/push1.html 获取推送token 

2、在SECRETS中添加

Name：USERS_COVER

Value：
[
    {
        "appId": "第一步中获取的token"
    }
]
