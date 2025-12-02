def checkString(lineToCheck, uniqueChars):
    charArr=[]
    foundMatch = False
    print(uniqueChars)
    while foundMatch == False:
        for index in range(0, len(lineToCheck),1):

            charArr.insert(0,lineToCheck[index])
            
            if len(charArr) < uniqueChars:
                next
            elif len(charArr) > uniqueChars:
                # print(charArr)

                charArr.pop()
              
                # print(charArr)
            foundmatch = newCheck(charArr,uniqueChars)
            # if foundMatch == True:
                # return True

def newCheck(charArr, uniqueChars):
    print(charArr)
    for n in range(1,uniqueChars, 1):
        charToCheck = charArr.pop()
        # print(charToCheck)
        if charToCheck in charArr:

            return False
            
        else:
            charArr.insert(0, charToCheck)
    return True

def checkIt(charArr, uniqueChars):
   
  
    for charIndex in range(0,uniqueChars-1,1):
        print(charArr[charIndex])
        for checkIndex in range(charIndex, uniqueChars-1,1):
            print(charArr[checkIndex])
            # print(charArr[charIndex], charArr[checkIndex])
            if charArr[charIndex] == charArr[checkIndex]:
                 
                 return False
           
  
    return True


howManyUniqueChars = 4




f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka6/sample.txt", "r")
for line in f:
    
    checkString(line, howManyUniqueChars)