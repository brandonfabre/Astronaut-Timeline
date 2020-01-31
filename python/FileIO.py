def appendToFile(fileName, contents):
    file = open(fileName, "a")
    file.write(contents + '\n')
    file.close()

def writeToFile(filename, contents):
    file = open(filename, "w")
    file.write(contents)
    file.close()

def fileContains(fileName, key):
    try:
        with open(fileName) as f:
            if key in f.read():
                return True
        return False
    except IOError:
        print("File " + fileName + " not found")

def readFromFile(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    return lines
