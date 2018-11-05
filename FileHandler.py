# handles the files the language is creating the code for
import os

import interpreter as i
start = "output/{}/".format(i.projectName)


files = {}
curFile = ""


def createFile(name="file"+str(len(files))+".java"):
    if not os.path.exists(start):
        os.mkdir(start)

    with open(start+name,"w+") as f:
        pass
    global curFile
    curFile = start+name
    return curFile


def addToFile(file="", text=""):
    if curFile == "":
        file = createFile()
    file = curFile
    if not text.endswith("\n"):
        text += "\n"

    with open(file, "a+") as f:
        f.write(text)