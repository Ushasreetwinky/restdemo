import urllib
from urllib2 import urlopen
import os
from bs4 import BeautifulSoup

def make_soup(url):
    thepage =urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

officerdatasaved =""
#india team

i =133
for i in range(133,200):

    soup = make_soup('https://supremo.nic.in/ERSheetHtml.aspx?OffIDErhtml='+str(i)+'&PageId=')
    # print soup
    
    for row in soup.findAll('table')[3].tbody.findAll('tr'):
        officerdata=""
        for data in row.findAll("td")[1:]:
            officerdata=officerdata+","+data.text
        officerdatasaved=officerdatasaved + "\n" +officerdata[1:]

#if playerdata == "No records available to match this quer":
# playerdata = ""
    # if officerdata[1:-1] == "No records available to match this quer":
    #     officerdatasaved =officerdatasaved + ""
    # else:
    #     officerdatasaved = officerdatasaved + "\n" + officerdata[1:-1]

print officerdatasaved
header="Designation,Department/Office,Organisation,Experience,Period"+""

# header = "Player,Span,Mat,Inns,NO,Runs,HS,Ave,100,50,0"+"\n"
#print(playerdatasaved)
file = open(os.path.expanduser("ss.csv"),"wb")
file.write(bytes(header).encode('utf-8'))
file.write(bytes(officerdatasaved).encode('utf-8'))