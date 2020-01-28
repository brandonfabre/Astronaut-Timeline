import wikipedia

def printAstronautSummary(astronautName):
    print("Astronaut: " + astronautName)
    print(wikipedia.summary(astronautName) + "\n")

printAstronautSummary("Peggy Whitson")
printAstronautSummary("Michael Lopez Alegria")
printAstronautSummary("Scott Altman")
