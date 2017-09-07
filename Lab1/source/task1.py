import re

fileName1 = "file1.txt"
fileName2 = "file2.txt"

infile = open(fileName1,'r')
file = open(fileName2,'r+')

def deletec(xStr):
    format = 'abcdefghijklmnopqrstuvwxyz'
    str = xStr
    for s in str:
        if not s in format:
            xStr = xStr.replace(s,'')
    return xStr

def find(xStr):
    newfile = open(fileName2,'r+')
    newlines = newfile.readlines()
    temp = 0
    for newline in newlines:
        words = newline.split(" ")
        #find if the word is already added to the file
        if xStr in words:
            value = eval(words[-1])
            newvalue = value +1
            updateline= newline.replace(str(value),str(newvalue))
            update(newline,updateline)
            temp = 1
            break
    #new word
    if temp == 0:
        newfile.write(xStr+" 1\n")
    newfile.close()

#replace the old value to the new value
def update(line,newline):
    readfile = open(fileName2,'r')
    readlines = readfile.readlines()
    writefile = open(fileName2,'w+')
    for readline in readlines:
        if line in readline:
            readline = newline
        writefile.write(readline)
    readfile.close()
    writefile.close()

line = infile.readline()
while line!="":

    for xStr in line.split(" "):
        xStr = xStr.lower()
        # make sure xStr are all words
        if xStr.isalpha()!= True:
            xStr = deletec(xStr)
        find(xStr)
    line = infile.readline()