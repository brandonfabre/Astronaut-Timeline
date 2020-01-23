import requests
from bs4 import BeautifulSoup
from FileIO import readFromFile
import re

def getPersonInfo():
    names = readFromFile("astronautsNames.txt")

    for name in names:
        print(name.strip('\n'))

        url = 'https://en.wikipedia.org/wiki/' + name.replace(' ', '_').title().strip('\n')
        print(url)
        urlContents = requests.get(url).text
        soup = BeautifulSoup(urlContents, 'xml')
        infoBoxContents = soup.find('table', {'class': 'infobox biography vcard'})

        birthDateSpan = soup.find('span', {'class': 'bday'})
        birthDatePattern = "([0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9])"
        regexFindBirthDate = re.findall(birthDatePattern, str(birthDateSpan))
        if regexFindBirthDate:
               print('Birth: ', regexFindBirthDate)
        else:
               print('Birth date not found')

        print()

getPersonInfo()
