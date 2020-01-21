#import wikipedia
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import re


website_url = requests.get('https://en.wikipedia.org/wiki/Mark_Kelly').text
#website_url = requests.get('https://en.wikipedia.org/wiki/Pedro_Duque').text
#website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text
soup = BeautifulSoup(website_url,'xml')
#print(soup.prettify())
My_table = soup.find('table',{'class':'infobox vcard'})
My_table

Info = []
Info2 = []


links = My_table.findAll('a')
links
for link in links:
    counter=+1
    Info.append(link.get('title'))


#print(Info)

links2 = My_table.findAll('th', scope = "row")
text = My_table.get_text()
print(text)



for link in links2:
    counter2=+1
    Info2.append(link.get_text())

#print(Info2)
#print(len(Info))
#print(len(Info2))




#Countries = []
#links = My_table.findAll('a')
#links
#for link in links:
#    Countries.append(link.get('title'))

#print(Countries)

#print(wikipedia.search("Barack Obama", results = 1))
#print(wikipedia.summary("Barack Obama"))

#df = pd.DataFrame()
#df['Country'] = Countries

#df
