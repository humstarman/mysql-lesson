#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
import re

def main():
  db = pymysql.connect("172.17.0.2", "root", "abc123", "news", charset='utf8')
  cursor = db.cursor()
  sql = "SELECT * FROM mynews LIMIT 100" 
  pattern = re.compile('[\u4e00-\u9fa5]+')
  try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    rets = cursor.fetchall()
    for (url,title) in rets:
      if pattern.search(title) != None:
        print(title)
       
  except:
    print ("Error: unable to fetch data")


if __name__ == "__main__":
  main()
