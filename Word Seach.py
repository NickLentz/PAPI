txtfile= open("Text.txt","r")
word =txtfile.read()
word =world.split()

LongWords = []
vowels = ["a" , "e" ,"i","o","y" ,"u"]

for i in range(0,5):
    LongWord=""
    counter = 0

    for testWord in words:

        if len(testWord) > len(LongWord):
            LongWord = testWord
            postion = counter
        counter += 1
    else:
        LongWord.append(LongWord)
        words.pop(position)
print("The Longest words are:", LongWords)

print("\n The Words in reverse and without vowels are:")

for testWord in LongWord:
    emptystring =""
    for leter in testWord:
        if letter not in vowels:
            emptystring += letter
print(emptystring[::-1]

