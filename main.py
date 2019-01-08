#! /usr/local/bin/python3
import eyed3
import re
import os
import sys

def totalFiles(path):
    filesPath = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filesPath.append(os.path.join(root, file))
    return filesPath

def searchPath(files):
    m = re.compile('(.*/)?(.+)\.(mp3|wma)$', flags=re.I)
    for name in files:
        res = m.search(name)
        if res != None:
            manageMusicFile(name, res.group(2))

def manageMusicFile(name, new):
    file = eyed3.load(name)
    file.initTag()
    file.tag.title = new
    file.tag.save()

try:
    path = sys.argv[1]
except Exception as e:
    path = os.curdir

files = totalFiles(path)
searchPath(files)
