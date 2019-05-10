#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by hubiao on 2017/12/26
import sys
import time,datetime
import json
import requests
from util.Config import ManageConfig


class WeiXinMessage:
    '''
    发送微信消息提醒功能
    '''
    __weixin = ManageConfig().getConfig('weixin')
    __CorpID = __weixin['CorpID']
    __Secret = __weixin['Secret']
    # 企业应用的id
    __AgentId = __weixin['AgentId']
    def __init__(self):
        self.expire_time = sys.maxsize
        self.access_token = self.get_token()
        self.url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.access_token}"


    def get_token(self):
        '''
        获取access_token
        '''
        if self.expire_time >time.time():
            response = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.__CorpID}&corpsecret={self.__Secret}')
            response_json = json.loads(response.content)
            self.expire_time = time.time() + response_json['expires_in']
            self.access_token = response_json['access_token']
        return self.access_token

    def send_message_text(self,title,content):
        '''
        发送文本消息
        :param title:消息的标题
        :param content:消息的内容
        :return:
        '''
        wechat_json = {
            "toparty":"3",
            "msgtype":"text",
            "agentid":self.__AgentId,
            "text": {
               "content" : f"消息主题：{title}\n消息内容：{content}"
           },
            "safe":0
        }
        response = requests.post(self.url,data=json.dumps(wechat_json)).json()
        if response["errcode"] == 0 and response["errmsg"] == "ok":
            print("发送成功")
        else:
            print("发送失败")

    def send_message_textcard(self,title,content,satr,toparty,msg_url="#"):
        '''
        发送卡片消息
        :param title:消息的标题
        :param content:消息的内容
        :param satr:消息状态
        :param toparty:通知的部门
        :param msg_url:点击卡片后跳转的连接
        :return:
        '''
        wechat_json = {
            "toparty":f"{toparty}",
            "msgtype":"textcard",
            "agentid":self.__AgentId,
            "textcard": {
                "title":f"{title}({satr})",
                "description" : content,
                "url":msg_url,
                "btntxt":"查看更多"
           },
            "safe":0
        }
        response = requests.post(self.url,data=json.dumps(wechat_json)).json()
        if response["errcode"] == 0 and response["errmsg"] == "ok":
            print("发送成功")
        else:
            print("发送失败")


    def send_message_markdown(self,title,content,satr,toparty):
        '''
        发送markdown消息
        :param title:消息的标题
        :param content:消息的内容
        :param satr:消息状态
        :param msg_url:点击卡片后跳转的连接
        :return:
        '''
        wechat_json = {
            "toparty":f"{toparty}",
            "msgtype" : "markdown",
            "agentid" : self.__AgentId,
            "markdown" : {
                "content" : f"""您的会议室已经预定，稍后会同步到`邮箱`
                    >**事项详情**
                    >事　项：<font color=\"info\">开会</font>
                    >组织者：@miglioguan
                    >参与者：@miglioguan、@kunliu、@jamdeezhou、@kanexiong、@kisonwang
                    >
                    >会议室：<font color=\"info\">广州TIT 1楼 301</font>
                    >日　期：<font color=\"warning\">2018年5月18日</font>
                    >时　间：<font color=\"comment\">上午9:00-11:00</font>
                    > 
                    >请准时参加会议。
                    >
                    >如需修改会议信息，请点击：[修改会议信息](https://work.weixin.qq.com)"""
                }
            }
        response = requests.post(self.url,data=json.dumps(wechat_json)).json()
        print(response)
        if response["errcode"] == 0 and response["errmsg"] == "ok":
            print("发送成功")
        else:
            print("发送失败")


if __name__ == '__main__':
    send = WeiXinMessage()
    send.send_message_textcard('今日演示企业巡检结果','通过全部测试','PASS','3')
    # send.send_message_markdown()
    # send.send_message_text('快递已到','你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。')