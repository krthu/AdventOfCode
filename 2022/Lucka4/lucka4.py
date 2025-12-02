def score(elf1, elf2):
    points = 0
    elf1Start = int(elf1[0])
    elf1End = int(elf1[1])
    elf2Start = int(elf2[0])
    elf2End = int(elf2[1])
    if elf1Start <= elf2Start and elf1End >= elf2End or elf2Start <= elf1Start and elf2End >= elf1End:
        points += 1
    print(points)
    return points




def splitLine(line):
    elves = line.split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    
    # print(int(elf1[0]), int(elf1[1]))
    # print(int(elf2[0]), int(elf2[1]))
    points = score(elf1, elf2,)
    return points



f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka4/input.txt", "r")
points = 0
for line in f:
    roundScore = splitLine(line)
    points = points + roundScore

print(points)