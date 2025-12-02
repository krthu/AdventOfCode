def addScore(letter):
    pointsDict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    points = pointsDict[letter.lower()]
    if letter.lower() != letter: points = points + 26
    return points

def checkBadge(arr):
    rightArr = []
    for l in arr[0]:
        for i in arr[1]:
            if l == i: rightArr.append(i)
    for x in rightArr:
        for i in arr[2]:
            if i == x: 
                return x



score = 0
arr = []
f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka3/input.txt", "r")
for line in f:
    arr.append(line)
  
    if len(arr) == 3:
        l = checkBadge(arr)
        score = score + addScore(l)
        arr = []



    # score = score + addScore(l)
 
print(score)        