#!/usr/bin/python3

def getconfig(start, end):
    first=int(start)
    last=int(end)+1
    counter=1
    if (first>last):
        return
    for number in range(first, last, 1):
        print (str(counter) + ":   ip address 192." + str(number//256) + "." + str(number%256) + ".0")
        counter+=1


