#!/usr/bin/env python

import MySQLdb

def main():
  db = MySQLdb.connect("172.17.0.2", "root", "abc123", "test", charset='utf8')
  cursor = db.cursor()
  insert_stmt = (
    "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)" 
    "VALUES (%s, %s, %s, %s, %s)"
  )
  data = ('L','Lee',22,'L',3000)
  try:
    cursor.execute(insert_stmt,data)
    db.commit()
  except:
    print "insert error"
    db.rollback()

  db.close()

if __name__ == "__main__":
  main()
