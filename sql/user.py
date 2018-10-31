#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mySQL_config import func

# 定义用户表类
class UserTB:
    ''' 用户增加、查询 '''
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
    
    # 查询用户名
    def selectUser(self):
        sql = "select * from user where USERNAME = '%s'"%self.user
        result = func(sql)
        return result
    
    # 查询用户名密码
    def selectUserPwd(self):
        sql = "select * from user where USERNAME = '%s' and PASSWORD = '%s' limit 1"%(self.user,self.pwd)
        result = func(sql)
        return result
    # 插入
    def insetinto(self):
        sql = "INSERT INTO user (USERNAME,PASSWORD) VALUES ('%s','%s')"%(self.user,self.pwd)
        result = func(sql)
        return result

     