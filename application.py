import os
from pathlib import Path

currentDir = str(Path.cwd())

totalFiles = []
with os.scandir(currentDir) as ficheros:
    ficherosMP3 = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
    totalFiles = ficherosMP3


x = currentDir.split("\\")
nameFile = str(x[len(x)-1]) + "_MP3.txt"

if (len(totalFiles) > 0) :
    file = open(nameFile, "w")
    for name in totalFiles:
        file.write(name + "\n") # file.write(os.linesep)
        
    file.close()
else:
    file = open("NotFoundMP3.txt", "w")
