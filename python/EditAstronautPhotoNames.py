import os

for file in os.listdir("./astronautFaces/"):
    filename = os.fsdecode(file)
    print(filename)
    os.rename(r'./astronautFaces/'+filename, r'./astronautFaces/'+filename+'.jpg')