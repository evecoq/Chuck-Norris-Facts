This project is let's you to get all the facts about Chuck Norris from the ChuckNorrisFacts website (https://chucknorrisfacts.net/), stock it in PostgreSQL database and do your search in it via a simple interface.
You can search the facts by parameters as a rate, votes number or a key word. You have also some already defined categories of facts that are about a common subject. 
The facts are inserted into two tables: the first one with the facts and its' id and the second one is with the id, rate, votes and the date.
</br>There are five files :
- scrapping.py for getting the data from the website andinsert it into the database.
- the chuck_norris.html file for creating the interface.
- the chuck_norris.css file that gives a little fancy touch to the interface.
- the chuck_norris.py file with which we send the queries to the database depending on choosen parameters (rate, vote, number of facts that we want to see)
- the chuck_norris_groups.py file with the queries to the database depending on the choosen subjest of the jokes.
