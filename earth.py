#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '906514731@qq.com'

# 每天定时发送天气消息到微信
import requests
import redis
from lightpush import lightpush


# 获取数据
def getUrlData():
    response = requests.get(
        "https://www.earthquakeim.com/system/weixin/earthquake/data.json")
    data = response.json()
    return data


# 发送信息到wechat
def sendDataToWechat(tite, data):
    lgp.set_group_push("6616-d0281c7704557cd46cff880b6da76a5a")
    lgp.group_push(tite, data)


# 解析数据
def parseData(client):
    JsonData = getUrlData()
    li = JsonData.get("data")
    update = client.get('erath_id')
    serviseId = li[0].get("id")
    id = int(serviseId)
    if update is None:
        client.set('erath_id', id)
        sendDataToWechat(li[0].get("location"),"震级："+str(li[0].get("magnitude"))+"\r\n发生时间："+str(li[0].get("earthquake_time")))
    else:
        localId = client.get('erath_id')
        if int(localId) < id:
            client.set('erath_id', id)
            sendDataToWechat(li[0].get("location"),"震级："+str(li[0].get("magnitude"))+"\r\n发生时间："+str(li[0].get("earthquake_time")))
        else:
            print ("暂无最新地震")


    client.connection_pool.disconnect();


def connectRedis():
    pool = redis.ConnectionPool(host='127.0.0.1')
    # 建立连接
    client = redis.Redis(connection_pool=pool)
    parseData(client)


if __name__ == '__main__':
    lgp = lightpush()
    connectRedis();
