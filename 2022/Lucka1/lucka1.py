print ("Hello world")
f = open("input.txt", "r")

biggestNr = 0
elf1 = 0
elf2 = 0
elf3 = 0
indexElf = 0
tempnr = 0
i = 0

for n in f:
    if (len(n.strip())==0):
        print (tempnr)
        if tempnr > elf1:
            elf3 = elf2
            elf2 = elf1
            elf1 = tempnr
            
        elif tempnr > elf2:
            elf3 = elf2
            elf2 = tempnr
            
        elif tempnr > elf3:
            elf3 = tempnr

            
        print(tempnr)    
        print("big",biggestNr)
        tempnr = 0

    else:

        num = int(n)
        tempnr += num
    
    
    i+=1

print(elf1 + elf2 + elf3 )


