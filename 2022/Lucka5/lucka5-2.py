def extractStorage(stringArr):
    storage = []
    num = stringArr.pop()
    numbersOfRow = num.split()
    indexToExtract = [1]
    for n in numbersOfRow:
        storage.append([])
        if n != "1":
            indexToExtract.append(indexToExtract[-1]+4)
    # print(storage)
    # print(indexToExtract)
    for line in stringArr:
        counter = 0
        for charNr in indexToExtract:
            if line[charNr] != " ":
                storage[counter].append(line[charNr])
            counter +=1
    # reverseStorage=[]
    # for reversed in storage:
    #     reverseStorage.append(reversed.reverse())
    # print(storage)
    return storage

def getInstructions(storage, f):
    instructions = []
    for line in f:
        splitLine = line.split()

        instructions.append([splitLine[1], splitLine[3], splitLine[5]])


    return instructions

def makeInstructions(storage, instructions):
    for instruction in instructions:
        temp = []
        for i in range(0,int(instruction[0])):
            temp.append(storage[int(instruction[1])-1].pop(0))
        print(len(temp))
        print(storage)
        for t in range(len(temp), 0, -1):
            print(t)
            storage[int(instruction[2])-1].insert(0, temp[t-1])
        print(storage)
    finalString = ""
    for i in storage:
        finalString = finalString + i[0]
    print(finalString)

f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka5/input.txt", "r")

arr = []

for line in f:
    if line != "\n":    
        arr.append(line)
    else:
        break
storage = extractStorage(arr)


instructions = getInstructions(storage, f)

getFinalString = makeInstructions(storage, instructions)