#!/usr/bin/env python

import MySQLdb
import random

def main():
  n = 10000
  db = MySQLdb.connect("172.17.0.2", "root", "abc123", "test", charset='utf8')
  cursor = db.cursor()
  insert_stmt = (
    "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)" 
    "VALUES (%s, %s, %s, %s, %s)"
  )
  mf = ['M','F']
  for i in range(n):
    first_name = chr(random.randint(65,90))
    len_ln = random.randint(2,10)
    last_name = ""
    for i in range(len_ln):
      if i == 0 :
        last_name += chr(random.randint(65,90))
      else:
        last_name += chr(random.randint(97,122))
    age = random.randint(18,60)
    sex = random.choice(mf) 
    income = random.randint(1000,6000)
 
    data = (first_name,last_name,age,sex,income)
    try:
      cursor.execute(insert_stmt,data)
      db.commit()
    except:
      print "insert error"
      db.rollback()

  db.close()

if __name__ == "__main__":
  main()
