#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '906514731@qq.com'

# 每天定时发送天气消息到微信
import requests
from lightpush import lightpush


# 获取数据
def getUrlData(address):
    response = requests.get(
        "https://free-api.heweather.com/s6/weather/now?location=" + address + "&key=e19043a44b874b7fa5f4b7a9e5ece02b")
    data = response.json()
    return data


# 发送信息到wechat
def sendDataToWechat(tite, data):
    lgp.set_group_push("6616-d0281c7704557cd46cff880b6da76a5a")
    lgp.group_push(tite, data)

# 解析数据
def parseData(city):
    JsonData = getUrlData(city)
    li = JsonData.get("HeWeather6")
    for l in li:
        basic = l.get("basic")
        admin_area = basic.get("admin_area")
        location = basic.get("location")
        now = l.get("now")
        fl = now.get("fl")
        tmp = now.get("tmp")
        cond_txt = now.get("cond_txt")
        wind_sc = now.get("wind_sc")
        update = l.get("update")
        loc = update.get("loc")
        sendDataToWechat(admin_area + location + "天气消息",
                         "体感温度" + fl + "度,实际温度" + tmp + "度,天气" + cond_txt + ",风力" + wind_sc + "级,更新时间：" + loc)


if __name__ == '__main__':
    lgp = lightpush()
    # parseData("海淀,北京")
    parseData("昌平,北京")