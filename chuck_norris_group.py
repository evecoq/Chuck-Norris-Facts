#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psycopg2, config 
import cgi, cgitb
cgitb.enable()

print("""Content-type: text/html; charset=utf-8

<html>
  <head>
    <title>Exemple CGI</title>
    <link rel="stylesheet" href="evenorris.css"/>
  </head>
  <body>""")

print("<h2>Facts. Certainly</h2>")

form = cgi.FieldStorage() # récupération des info de paramètres

groups = form["groups"].value
print("//groups=", groups)

#Connection to the DB with config.py file
conn = psycopg2.connect(database=config.database, user=config.user, password=config.password, host='localhost') # connexion
cur = conn.cursor() # session

#Sending query depending on the option choise
if groups == 'god':
	sql = f"""SELECT * FROM "chuckgod";"""
elif groups == 'food':
	sql = f"""SELECT * FROM "foodview";"""
elif groups == 'chuck':
	sql = f"""SELECT * FROM "justchuckview";"""
elif groups == 'love':
	sql = f"""SELECT * FROM "love";"""
elif groups == 'pets':
	sql = f"""SELECT * FROM "petsview";"""
elif groups == 'sleep':
	sql = f"""SELECT * FROM "sleepview";"""
elif groups == 'viril':
	sql = f"""SELECT * FROM "virilview";"""
elif groups == 'virus':
	sql = f"""SELECT * FROM "virusview";"""
elif groups == 'woman':
	sql = f"""SELECT * FROM "woman";"""

#Getting the result
cur.execute(sql) 
for data in cur.fetchall() :
	print("<li>%s" % (data[0]))
