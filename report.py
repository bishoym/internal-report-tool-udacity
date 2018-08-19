import psycopg2
from datetime import datetime
from datetime import time
from datetime import date


DBNAME = "news"

#TASK 1
db = psycopg2.connect(dbname=DBNAME)
c = db.cursor()
query = "SELECT title, count(*) AS views FROM (SELECT REPLACE(path, '/article/', '') AS newpath, * FROM log) AS newlog JOIN articles ON articles.slug = newlog.newpath  GROUP BY title ORDER BY views DESC LIMIT 3;"
c.execute(query)
topthree = c.fetchall()
print("Task 1- What are the top three most viewed articles?")
print
for row in topthree:
    print " ", row[0], "-", row[1], "views"
db.close()

print

#TASK 2
db = psycopg2.connect(dbname=DBNAME)
c = db.cursor()
query = "SELECT name, count(*) AS views FROM (SELECT REPLACE(path, '/article/', '') AS newpath, * FROM log) AS newlog JOIN articles ON articles.slug = newlog.newpath JOIN authors ON authors.ID = articles.author  GROUP BY name ORDER BY views DESC;"
c.execute(query)
popular_authors = c.fetchall()
print("Task 2- Who are our celebrity authors?")
print
print "Introducing:"
print
for row in popular_authors:
  print " ", row[0], "-", row[1], "views"
db.close()

print

#TASK 3
db = psycopg2.connect(dbname=DBNAME)
c = db.cursor()
query = "SELECT date, errper FROM  (SELECT  time::timestamp::date AS date, ROUND((err * 100.0) / req, 3) AS errper FROM (SELECT a.time::timestamp::date, count(*) AS req, count(*) FILTER (WHERE a.status != '200 OK') AS err FROM log AS a, log AS b WHERE a.id = b.id GROUP BY a.time::timestamp::date ORDER BY a.time::timestamp::date) AS reduced) AS postproc WHERE errper > 1.0;"
c.execute(query)
badday = c.fetchall()
print("Task 3- On which days did more than 1% of requests lead to errors?")
print
for row in badday:
    print " ", row[0].strftime("%B %d, %Y"), " - ", row[1], "%"
db.close()
