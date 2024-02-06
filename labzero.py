#! /usr/bin/env python3

import os, stat
from sys import stderr, argv

infile=argv[1]
word_count = {}

def populateWordDic():
    fd = os.open(infile, os.O_RDONLY, stat.S_IRWXU);
    assert fd >= 0
    print("Opened Successfully")
    word = ""
    char = os.read(fd,1).decode()
    #x = 0
    while len(char) >0:
        print(char)
        #if x%200==0:
        #    print(x)
        #x=x+1
        if char.isspace():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            word = ""
        if char.isalpha():
            word = word + char
        char = os.read(fd,1).decode()
    os.close(fd)

def countWords():
    populateWordDic()
    
    if len(word_count)== 0:
        os.write(2,"No words found\n".encode())
        return
    
    for key in word_count:
        os.write(2, f"{key} : {word_count[key]} occurences\n".encode())

countWords()
