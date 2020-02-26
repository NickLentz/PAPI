txtfile  =  open("Text2.txt", "r")
word     =  txtfile.read()
word     =  word.split()
BadLet   =  ["c", "f", "k", "r"]
notCons  =  ["a", "e", "i", "o", "u", "y", ";", "."]


for word in words:
    badCount = 0
    normalCount = 0
    for letter in word:
        if letter in badLet:
            badCount +=1
        elif leter not in notCons:
            normalCount +=1
