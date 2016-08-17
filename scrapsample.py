import urllib
from urllib2 import urlopen 
import os
from bs4 import BeautifulSoup

def make_soup(url):
	thepage =urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

playerdatasaved =""
#india team
m = 1
for m in range(1,9):
	i =1
	for i in range(1,16): 
		soup = make_soup('http://stats.espncricinfo.com/ci/engine/stats/index.html?class=11;page='+str(i)+';team='+str(m)+';template=results;type=batting')
		for record in soup.findAll("tr", attrs={"class": "data1"}):
			playerdata = ""
			for data in record.findAll('td'):
				playerdata = playerdata + ',' + data.text
			#if playerdata == "No records available to match this quer":
			#	playerdata = ""
			if playerdata[1:-1] == "No records available to match this quer":
				playerdatasaved =playerdatasaved + ""
			else:
				playerdatasaved = playerdatasaved + "\n" + playerdata[1:-1]
			print playerdata

header = "Player,Span,Mat,Inns,NO,Runs,HS,Ave,100,50,0"+"\n"
#print(playerdatasaved)
file = open(os.path.expanduser("cricket.csv"),"wb")
file.write(bytes(header).encode('utf-8'))
file.write(bytes(playerdatasaved).encode('utf-8'))
