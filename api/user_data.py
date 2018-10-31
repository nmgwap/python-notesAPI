#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 导入flask模块
from flask import Blueprint,Flask,request
# 导入json模块
import json
# 导入自定义模块
from Utils.utils import *
# 导入mySQL_config
from sql.user_data import User_DataTB
# 创建类的实例
userData = Blueprint("userData",__name__)

# 获取用户下的数据
# @param {string}   user    用户名
# @param