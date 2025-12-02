def checkString(lineToCheck, uniqueChars):
    charArr=[]
    for stringIndex in range(0, len(lineToCheck),1):
        # print(lineToCheck[stringIndex])
        charArr.insert(0,lineToCheck[stringIndex])
        if len(charArr) == uniqueChars:
            newArr = charArr.copy()
            if newCheck(newArr):
                print(stringIndex+1)
                break
            else:
                print(charArr)    
                discard = charArr.pop()
                print(discard)         


def newCheck(charArr):
    print(charArr, "from new")
    for n in range(0, len(charArr),1):
        charToCheck = charArr.pop()
        for char in charArr:
            if charToCheck == char:
                return False
        charArr.insert(0, charToCheck)
    return True


howManyUniqueChars = 14




f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka6/input.txt", "r")
lineArr = f.readlines()
line = lineArr[0]

checkString(line, howManyUniqueChars)