def checkRange(data):
    highestTree = []
    points = 0
    for arr in data:
        index = 0
        # print(index)
        for tree in arr:
            print("tree",tree)
            if len(highestTree) != len(arr):
                highestTree.append(tree)
                points += 1
            
            elif highestTree[index] < tree:
                print("Index", index)
                highestTree[index] = tree
                points +=1
            index += 1
        print("highest", highestTree)
        
    print(highestTree)
    print(points)
    return points


def checkLeft(data):
    highestTree = []
    points = 0
    for n in range(0, len(data[0])):
        for row in range(0, len(data)):
            if len(highestTree) != len(data):
                highestTree.append(data[row][n])
                points += 1
            
            elif highestTree[row] < data[row][n]:
                highestTree[row] = data[row][n]
                points +=1
            row += 1
        n += 1
        print("highest", highestTree)
    return(points)





with open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka8/sample.txt", mode="rt") as f:
    data = f.read().splitlines()
    score = 0
    print(data)
    treeInts = []
    i=0
    for line in data:
        data[i] = list(map(int, line))
        i += 1
    for line in data:
        print(line)
    print(len(data[0]))
    for row in range(0, len(data)):
        for index in range(0, len(data[0])):
            # print("row", row, "index", index)
            # print(data[row][index])
            if row == 0 or index == 0 or row == len(data) or index == len(data[0]):
                (print("AddPoint", row, index))
            else:
                for left in range(index - 1, 0, -1):
                    if data[row][index] > data[row][left]:
                        next
                        # print("bigger", data[row][index], data[row][left])
                    else:
                        break
                    print("bigger", data[row][index])



    




