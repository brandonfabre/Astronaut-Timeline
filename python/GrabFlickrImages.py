import requests
import re
from FileIO import readFromFile

def grabPhotoDate(imageID):
    photoURLPrefix = "https://www.flickr.com/photos/nasacommons/"
    albumID = "72157648186433655"

    photoURL = photoURLPrefix + str(imageID) + '/in/album-' + albumID

    urlContents = requests.get(photoURL).text

    regexPattern = "class=\"date-taken-label\" title=\"Uploaded on (.*)\""
    photoDate = re.findall(regexPattern, urlContents)[0]
    return convertToNumericDate(photoDate)

def convertToNumericDate(strDate):
    strDate = strDate.replace(',', '')
    dateArray = strDate.split(' ')

    month = dateArray[0]
    date = dateArray[1]
    year = dateArray[2]

    numericDate = year + "-" + monthSwitcher(month).zfill(2) + "-" + date.zfill(2)

    return numericDate

def monthSwitcher(stringMonth):
    switcher = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return str(switcher.get(stringMonth, "Invalid month"))

grabPhotoDate()
