#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psycopg2, config 
import cgi, cgitb

cgitb.enable()

print("""Content-type: text/html; charset=utf-8

<html>
  <head>
    <title>Exemple CGI</title>
    <link rel="stylesheet" href="chuck_norris.css"/>
  </head>
  <body>""")

print("<h2>Facts. Certainly</h2>")

#Getting the search parameters form
form = cgi.FieldStorage()

motcle = form["motcle"].value
number = form["number"].value
rate = form["rate"].value
votes = form["votes"].value

print("motcle= ", motcle)
print("//number= ", number)
print("//rate=", rate)
print("//votes=", votes)

#Database connection with a config.py file
conn = psycopg2.connect(database=config.database, user=config.user, password=config.password, host='localhost')
cur = conn.cursor()

#Queries that gets the facts from database depending on the choosen parameters. Chuckview is the view that unies the both of tables in one.
if rate == 'bas' and votes == 'min':    
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 1 AND rate <=2 AND votes >= 0 AND votes <= 100 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'bas' and votes == 'med':    
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 1 AND rate <=2 AND votes >= 100 AND votes <= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'bas' and votes == 'more':    
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 1 AND rate <=2 AND votes >= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'bas' and votes == 'all':    
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 1 AND rate <=2 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'medium' and votes == 'min':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 2 AND rate <=4 AND votes >= 0 AND votes <= 100 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'medium' and votes == 'med':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 2 AND rate <=4 AND votes >= 100 AND votes <= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'medium' and votes == 'more':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 2 AND rate <=4 AND votes >= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'medium' and votes == 'all':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 2 AND rate <=4 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'haut' and votes == 'min':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 4 AND rate <=5 AND votes >= 0 AND votes <= 100 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'haut' and votes == 'med':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 4 AND votes >= 100 AND votes <= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'haut' and votes == 'more':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 4 AND votes >= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'haut' and votes == 'all':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND rate >= 4 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'tout' and votes == 'min':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND votes >= 0 AND votes <= 100 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'tout' and votes == 'med':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND votes >= 100 AND votes <= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'tout' and votes == 'more':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' AND votes >= 1000 LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")
elif rate == 'tout' and votes == 'all':
	sql = f"""SELECT * FROM "chuckview" WHERE joke LIKE '%{motcle}%' LIMIT {number};"""
	#print(f"<p>Requete SQL: <inline class='sql'>{sql}</inline></p>")

#getting the asked data
cur.execute(sql) # requête SELECT
for data in cur.fetchall() : 
 	print("<li>%s :%s</li>" % (data[0], data[1]))




