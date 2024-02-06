#! /usr/bin/env python3

import os, stat
from sys import stderr, argv

infile=argv[1]
word_count = {}

def populateWordDic():
    fd = os.open(infile, os.O_RDONLY, stat.S_IRWXU);
    assert fd >= 0
    word = ""
    char = fd.read(1).decode()
    while len(char) >0:
        if char.isspace():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            word = ""
        if char.isalpha():
            word.append(char)
        fd.read(1).decode()
    fd.close()

def countWords():
    populateWordDic()
    
    if len(word_dic)== 0:
        os.write(2,"No words found\n".encode())
        return
    
    for key in word_dic:
        os.write(2, f"{key} : {word_dic[key]} occurences".encode())

countWords()
