#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 导入flask模块
from flask import Blueprint,Flask,request
# 导入json模块
import json
# 导入自定义模块
from Utils.utils import *
# 导入mySQL_config
from sql.user import UserTB
# 创建类的实例
user = Blueprint('user',__name__)
 
# 登录
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # POST、GET:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        param = request.form.to_dict()
        if param.get("user") != None and param.get("pwd") != None:
            if param.get("user") != "" and len(param.get("user")) < 8 and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                user = UserTB(param.get("user"),param.get("pwd"))
                user = user.selectUser()
                if user == ():
                    content = json.dumps(formatres(False,{},"用户名不存在"),ensure_ascii=False)
                else:
                    userPwd = UserTB(param.get("user"),param.get("pwd"))
                    userPwd = userPwd.selectUserPwd()
                    if userPwd == ():
                        content = json.dumps(formatres(False,{},"用户名密码不正确"),ensure_ascii=False)
                    else:
                        content = json.dumps(formatres(True,{},"登录成功"),ensure_ascii=False)
            else:
                content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return content

# 注册
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/reg',methods=['post'])
def reg():
    if request.method == 'POST':
        param = request.form.to_dict()
        if param.get("user") != None and param.get("pwd") != None:
            if param.get("user") != "" and len(param.get("user")) < 8 and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                user = UserTB(param.get("user"),param.get("pwd"))
                user = user.selectUser()
                if user != ():
                    content = json.dumps(formatres(False,{},"用户名已存在"),ensure_ascii=False)
                else:
                    try:
                        insetintouser = UserTB(param.get("user"),param.get("pwd"))
                        insetintouser = insetintouser.insetinto()
                        if insetintouser == ():
                            content = json.dumps(formatres(True,{},"用户创建成功"),ensure_ascii=False)
                        else:
                            content = json.dumps(formatres(False,{},"用户创建失败"),ensure_ascii=False)
                    except:
                        content = json.dumps(formatres(False,{},"用户创建失败，可能用户名过长"),ensure_ascii=False)
            else:
                content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return content


