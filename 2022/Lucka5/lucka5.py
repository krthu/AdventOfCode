

f = open("/Users/kristianthun/Documents/Code/AdventOfCode2022/Lucka5/sample.txt", "r")
arr = []

for line in f:
   
    if line != "\n":
        
        arr.append(line)
        
        # n=4
        # line2 = [line[i:i+n] for i in range(0, len(line), n)]
        # print(line[5])
    else:
        break
num = arr.pop()
print(num)
numbersOfRow = num.split()
storage = []
for n in arr:
    if n == " ":
        next
    storage.append(n[1])    
print(storage)



print(arr)
