#!/usr/bin/env python

import MySQLdb

def main():
  db = MySQLdb.connect("172.17.0.2", "root", "abc123", "test", charset='utf8')
  cursor = db.cursor()
  #cursor.execute("SELECT VERSION()")
  #data = cursor.fetchone()
  #print "Database version : %s " % data
  sql = "SELECT * FROM MyClass;"
  try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
      idx = row[0]
      name = row[1]
      sex = row[2]
      degree = row[3]
      print "id=%s,name=%s,sex=%s,degree=%s" % \
        (idx, name, sex, degree )
  except:
    print "Error: unable to fecth data"

  db.close()

if __name__ == "__main__":
  main()
