#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入flask模块
from flask import Flask
# 导入json模块
import json
# 导入自定义模块
from Utils.utils import *
# 导入user
from api.user import user
# 创建类的实例
app = Flask(__name__)

# 导入user接口
app.register_blueprint(user, url_prefix='/user')

# 定义首页路由
# 提示作用 
@app.route('/')
def hello_world():
    content = json.dumps(formatres(False,{},"地址只支持post"),ensure_ascii=False)
    return content

# 重定向错误400
@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"400"))
    resp = Response_headers(content)
    return resp

# 重定向错误403
@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"403"))
    resp = Response_headers(content)
    return resp

# 重定向错误404
@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"404"))
    resp = Response_headers(content)
    return resp

# 重定向错误405
@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"405"))
    resp = Response_headers(content)
    return resp

# 重定向错误410
@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"410"))
    resp = Response_headers(content)
    return resp

# 重定向错误500
@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps(formatres(False,{},"500"))
    resp = Response_headers(content)
    return resp

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')
