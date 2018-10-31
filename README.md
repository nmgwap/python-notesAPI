#### 项目介绍
基于python+Flask编写的api

#### 技术栈
python+Flask+pymysql
#### 目录结构
------------------------

```bash

├── /api/               # 接口文件
├──────/user            # 用户
├── /doc/               # 说明文档
├── /sql/               # SQL类
├──────/user            # 用户
├── /sqlTableFiles/     # sql表文件     不是专业后端，数据库表可能设计有问题
├──────/user_data.sql   # 用户数据表        
├──────/user.sql        # 用户表            
├── /Utils/             # 公共方法
├──────/utils           # 公用方法
├── .editorconfig       # 定义代码格式
├── mySQL_config.py     # 数据库连接文件
├── requirements.txt    # 项目依赖文件
├── run.py              # 入口文件（执行文件）
└── README.md           # 项目文档

```

#### 前期准备

> 1. 本地安装mysql

> 2. 新建test库

> 3. 导入sql文件下的两个sql文件

> 4. 修改连接配置(mySQL_config.py)

```bash

import pymysql
# 创建数据库连接池
POOL = PersistentDB(
    creator=pymysql,    # 使用链接数据库的模块
    maxusage=None,      # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],      # 开始会话前执行的命令列表。
    ping=0,             # ping MySQL服务端，检查是否服务可用。
    closeable=False,    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,   # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',   # 数据库地址
    port=3306,          # 数据库端口号
    user='root',        # 用户名
    password='123456',  # 密码
    database='test',    # 数据库库名
    charset='utf8'      # 编码
)


```

#### 添加接口

> 在api文件夹下新建文件夹，和user同级，创建__init__.py(内容为空也可以)和接口文件
> 修改run.py,

```bash

# -*- coding: utf-8 -*-

# 导入flask模块
from flask import Flask
# 导入json模块
import json
# 导入sys
import sys
# 找到Utils
sys.path.append("Utils")
# 导入自定义模块
from utils import formatres,Response_headers
# 找到api
sys.path.append("api")
# 导入user
from user.user import user 
# >>>>>>>>>>>>>>>>>>>>
# 导入你的文件夹
# >>>>>>>>>>>>>>>>>>>>

# 创建类的实例
app = Flask(__name__)

# 导入user接口
app.register_blueprint(user, url_prefix='/user')
# >>>>>>>>>>>>>>>>>>>>
# 导入接口并设置路径
# >>>>>>>>>>>>>>>>>>>>


```


#### 运行项目


``` bash


# 安装依赖文件
pip install -r requirements.txt

# 启动程序
python run.py

# 配置站点
在浏览器中输入http://127.0.0.1:5000



```

#### 接口预览


``` bash

# 登录接口（post）
# @url:   http://127.0.0.1:5000/user/login
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}



# 注册接口（post）
# @url:   http://127.0.0.1:5000/user/reg
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}

```



#### 说明

>  本项目主要用于熟悉如何用 python 架构一个后端管理平台项目

>  如果对您有帮助，您可以点右上角 "Star" 支持一下 谢谢！ ^_^

>  或者您可以 "follow" 一下，我会不断开源更多的有趣的项目

>  开发环境 w7  Chrome 61 vscode

>  如有问题请直接在 Issues 中提，或者您发现问题并有非常好的解决方案，欢迎 PR 👍