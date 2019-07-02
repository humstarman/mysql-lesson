#!/usr/bin/env python

import MySQLdb

def main():
  db = MySQLdb.connect("172.17.0.2", "root", "abc123", "test", charset='utf8')
  cursor = db.cursor()
  
  sql = "INSERT INTO MyClass(id,name,sex,degree) \
       VALUES (%s, %s, %s, %s)" % \
       (41,'Mac',0 , 20.0)
  print sql
  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "insert error"
    db.rollback()

  db.close()

if __name__ == "__main__":
  main()
