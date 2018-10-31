#!/usr/bin/python3
# -*- coding:utf-8 -*-

from mySQL_config import func

# 定义用户数据表类
class User_DataTB:
    ''' 用户数据增加、查询、修改'''
    def __init__(self,user,pwd,title,content):
        self.user = user
        self.pwd = pwd
        self.title = title
        self.content = content
    
    # 查询用户数据
    def selectUserData(self):
        sql = ""
        result = func(sql)
        return result

    # 添加用户数据
    def addUserFata(self):
        sql = ""
        result = func(sql)
        return result

    # 修改用户数据
    def updateUserFata(self):
        sql = ""
        result = func(sql)
        return result
    
    # 删除用户数据
    def deleteUserData(self):
        sql = ""
        result = func(sql)
        return result