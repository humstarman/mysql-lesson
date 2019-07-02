#!/usr/bin/env python

import MySQLdb

def main():
  db = MySQLdb.connect("172.17.0.2", "root", "abc123", "test", charset='utf8')
  cursor = db.cursor()
  
  sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
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
