import requests, psycopg2, config
import re
from time import sleep
from bs4 import BeautifulSoup

conn = psycopg2.connect(database="bdd_ecoquelet",
user=config.user,
password=config.password,
host='127.0.0.1') 

cur = conn.cursor()

def useInfo(id, joke, rate, votes):
    print("%4d : %4d %.2f %s" % (id, votes, rate, joke))
    cur.execute("""INSERT INTO public."Jokes" VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;""",
        (id, joke)) 
    cur.execute("""INSERT INTO public."Vote" VALUES (NOW()::Date, %s, %s, %s) ON CONFLICT DO NOTHING;""", 
    (id, rate, votes)) 
    
def recupPage (page):
    url = f"https://chucknorrisfacts.net/facts.php?page={page}"
    print("Recupération de", url)

    r = requests.get(url, headers={"User-Agent": "RussianSpy"})
    soup = BeautifulSoup(r.content, 'lxml')
    
    blocks = soup.select("#content > div:nth-of-type(n+2)")
        
    for block in blocks:
        fact = block.select_one("p")
        if fact is not None:
            idb = block.select_one("ul")
            id = idb['id'][6:]         
            rate = block.select_one("span.out5Class")
            vote = block.select_one("span.votesClass")
            useInfo(int(id), fact.text, float(rate.text), int(vote.text[:-6]))

url = f"https://chucknorrisfacts.net/facts"
print("Recupération de", url)
r = requests.get(url, headers={"User-Agent": "RussianSpy"})
soup = BeautifulSoup(r.content, 'lxml')
lastPage=soup.select_one("#content > div:last-child > a:last-child")['href']
lastPageNumber = int(re.search("\d+",lastPage).group())

for p in range (1,lastPageNumber+1):
    sleep = 0.25
    recupPage(p)
           
conn.commit()
conn.close()

