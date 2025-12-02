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
        for i in range(0,int(instruction[0])):
            temp = storage[int(instruction[1])-1].pop(0)
            storage[int(instruction[2])-1].insert(0, temp)
    
    finalString = ""
    for i in storage:
        finalString = finalString + i[0]
    print(finalString)

f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka5/sample.txt", "r")

arr = []

for line in f:
    if line != "\n":    
        arr.append(line)
    else:
        break
storage = extractStorage(arr)


instructions = getInstructions(storage, f)

getFinalString = makeInstructions(storage, instructions)