import requests
from bs4 import BeautifulSoup
import argparse
import re
import math

"""
Pulling search results from google, adding a little voodo, a little sourcery and a chunk of chem trails chem to turn it
into realistic soccer results for world championship tip game. If I win the office contest, the alorythm will be 
patented in NO time. Up to now its free as in free.
"""


def returnCount(searchTerm):
	numString = ""

	"""parser = argparse.ArgumentParser(description='Get Google Count.')
	parser.add_argument('word', help='word to count')
	args = parser.parse_args()"""

	r = requests.get('http://www.google.com/search',
	                 params={'q':'"'+searchTerm+'"',
	                         "tbs":"li:1"}
	                )

	soup = BeautifulSoup(r.text, 'html.parser')
	textReturn = soup.find('div',{'id':'resultStats'}).text
	#print(textReturn)
	numTemp = re.findall("[0-9]+",textReturn)
	for i in numTemp:
	        numString+=i

	return(int(numString))


while not():
    
	team1 = input("Name des ersten Teams: ")
	team2 = input("Name des zweiten Teams: ")


	team1_hits = returnCount(team1+" Fussball")
	team2_hits = returnCount(team2+" Fussball")

	#Je größer die Differenz, desto höher die zu verteilenden Pkte
	score = int(math.pow(math.fabs(team1_hits - team2_hits), 1./4)/3)

	team1_ergebn = int(score / ((team1_hits + team2_hits)/team1_hits))
	team2_ergebn = int(score / ((team1_hits + team2_hits)/team2_hits))

	print("Score: {0}".format(score))
	print("Team1: {0} : Team 2: {1}, Ergebnis: {2}:{3}".format(team1, team2, team1_ergebn, team2_ergebn))


