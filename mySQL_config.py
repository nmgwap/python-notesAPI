#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入数据库连接池模块
from DBUtils.PersistentDB import PersistentDB
# 导入数据库模块
import pymysql
# 创建数据库连接池
POOL = PersistentDB(
    creator=pymysql,    # 使用链接数据库的模块
    maxusage=None,      # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],      # 开始会话前执行的命令列表。
    ping=0,             # ping MySQL服务端，检查是否服务可用。
    closeable=False,    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,   # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Admin@123456',
    database='test',
    charset='utf8'
)

def func(sql):
    conn = POOL.connection(shareable=False)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

if __name__ == '__main__':
    sql = "select * from user"
    func(sql)