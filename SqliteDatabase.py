import sqlite3
conn = sqlite3.connect('astronautsTimeline.db')

def createTables():
    c = createCursor()

    # Creating tables
    c.execute('''
    CREATE TABLE Astronauts
    (
    ID integer not null constraint Astronauts_pk primary key autoincrement,
    Name text
    );
    create unique index Astronauts_ID_uindex on Astronauts (ID);
    ''')

    c.execute('''
    CREATE TABLE Images 
    (
    ID integer not null constraint Images_pk primary key autoincrement,
    DateTaken text,
    FlickrID blob
    )
    ''')

    c.execute('''
    CREATE TABLE AstronautAppearances 
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
    c.execute("INSERT INTO Astronauts (Name) VALUES (astronautName)")
    commitAndClose()

def createCursor():
    return conn.cursor()
