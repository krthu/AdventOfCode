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


score = 0
f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka3/input.txt", "r")
for line in f:
    arr = {}
    l = ""
    for i in range(int(len(line)/2),int(len(line))):
        # print(line[i])
        for x in range(0, int(len(line)/2)):
            if line[i] == line[x]: 
                l = line[x]

                break
    score = score + addScore(l)
 
print(score)        