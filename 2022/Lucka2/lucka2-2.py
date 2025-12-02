def calcScore(oppo, you):
    scoreDict = {
        "A": 1,
        "B": 2, 
        "C": 3, 
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    oppoScore = scoreDict[oppo]
    youScore = 0

    if you == "Y":
        youScore += 3
        youScore += oppoScore

    elif you == "Z":
        youScore += 6
        if oppoScore == 1:
            youScore += 2
        elif oppoScore == 2:
            youScore += 3
        elif oppoScore == 3:
            youScore += 1
    elif you == "X":
        if oppoScore == 1:
            youScore += 3
        elif oppoScore == 2:
            youScore += 1
        elif oppoScore == 3:
            youScore += 2


    return youScore


totalScore = 0

f = open("input.txt", "r")
for line in f:
    totalScore = totalScore + calcScore(line[0], line[2])
    print(totalScore)
print(totalScore)


