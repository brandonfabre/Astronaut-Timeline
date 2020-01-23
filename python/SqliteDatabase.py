import sqlite3
from FlickrImagesInfo import grabPhotoDate

conn = sqlite3.connect('astronautsTimeline.db')

def createTables():
    c = createCursor()

    # Creating tables
    # Creating Astronauts table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Astronauts
    (
    ID integer not null constraint Astronauts_pk primary key autoincrement,
    Name text
    );
    create unique index Astronauts_ID_uindex on Astronauts (ID);
    ''')

    # Creating Images table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Images
    (
    ID integer not null constraint Images_pk primary key autoincrement,
    FlickrID blob,
    DateTaken text
    )
    ''')

    # Creating AstronautAppearances table
    c.execute('''
    CREATE TABLE IF NOT EXISTS AstronautAppearances
    (
    ImageID integer,
    AstronautID integer
    )
    ''')

    # Commit tables and save
    commitAndClose()

def commitAndClose():
    conn.commit()
    conn.close()

def addAstronaut(astronautName):
    c = createCursor()
    c.execute(
    '''
    INSERT INTO Astronauts (Name)
    VALUES (astronautName)
    WHERE NOT EXISTS (SELECT Name FROM Astronauts WHERE Name=astronautName);
    ''')
    commitAndClose()

def addImage(imageID):
    c = createCursor()
    dateTaken = grabPhotoDate(imageID)
    c.execute(
    '''
    INSERT INTO Images (FlickrID, DateTaken)
    VALUES (imageID, dateTaken)
    WHERE NOT EXISTS (SELECT FlickrID FROM Images WHERE FlickrID=imageID);
    '''
    )

# def addAstronautToImage(astronautName, imageName):
#     c = createCursor()
#     c.execute(
#     '''
#     INSERT INTO AstronautAppearances (ImageID, AstronautID)
#     VALUES ()
#     '''
#     )

def createCursor():
    return conn.cursor()
