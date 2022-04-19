import os
from pathlib import Path

currentDir = str(Path.cwd())

totalFiles = []
with os.scandir(currentDir) as ficheros:
    ficherosMP3 = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.mp3')]
    totalFiles = ficherosMP3
    # print(ficherosMP3)


x = currentDir.split("\\")
nameFile = str(x[len(x)-1]) + "_MP3.txt"

if (len(ficherosMP3) > 0) :
    file = open(nameFile, "w", encoding="utf-8")
    for name in ficherosMP3:
        file.write(str(name) + "\n")
        # file.write(os.linesep)

    file.close()
else:
    file = open("NotFoundMP3.txt", "w")
