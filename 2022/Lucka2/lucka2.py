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
    youScore = scoreDict[you]

    if oppoScore == youScore:
        youScore += 3 
    elif oppoScore == 1 and youScore == 2 or oppoScore == 2 and youScore == 3 or oppoScore == 3 and youScore == 1:
        youScore += 6 

    return youScore


totalScore = 0

f = open("input.txt", "r")
for line in f:
    totalScore = totalScore + calcScore(line[0], line[2])

print(totalScore)


