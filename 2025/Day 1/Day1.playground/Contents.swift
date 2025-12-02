import Cocoa

var testData = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


let lines = data.split(separator: "\n");

var number = 50;
var times0 = 0;
var rotation0 = 0;

for line in lines {
    print("Line: \(line)")
    var shouldAdd = (line.first == "R")
    var toAdd = String(line.dropFirst())
    var numToAdd = Int(toAdd)!
//    let result = change(atNumber: number, amount: shouldAdd ?  numToAdd: -numToAdd)
    let result = newChange(atNumber: number, amount: shouldAdd ?  numToAdd: -numToAdd)
    number = result.newNumber
    rotation0 += result.timesZero
    
//    if number == 0 {
//        times0 += 1
//    }
}
print(times0 + rotation0);



func change(atNumber: Int, amount: Int) -> (newNumber: Int, rotations: Int){
   // var shortendAmount = amount % 99
   // print("SHortend \(shortendAmount)")
    var rotations = Int((atNumber + amount)/100)
   

    var newNumber = (atNumber + amount) % 100
    

    if newNumber < 0 {
        newNumber += 100
        rotations += 1
    } else if newNumber > 99 {
        newNumber -= 100
        rotations += 1
    }
//    else if newNumber == 0 {
//        rotations += 1
//    }


    

    return (newNumber, rotations)
}

func newChange(atNumber: Int, amount: Int) -> (newNumber: Int, timesZero: Int) {
    let absAmount = abs(amount)
    var timesZero = 0
    
    if amount > 0 {
        let clicksToFirstZero = (atNumber == 0) ? 100 : (100 - atNumber)
        
        if absAmount >= clicksToFirstZero {
        
            timesZero += 1
            
   
            let remainingClicks = absAmount - clicksToFirstZero
            timesZero += remainingClicks / 100
        }
    } else if amount < 0 { // Rotation åt Vänster (L)

        let clicksToFirstZero = (atNumber == 0) ? 100 : atNumber
        
        if absAmount >= clicksToFirstZero {

            timesZero += 1

            let remainingClicks = absAmount - clicksToFirstZero
            timesZero += remainingClicks / 100
        }
    }
    
    let newNumber = ((atNumber + amount) % 100 + 100) % 100
    
    return (newNumber, timesZero)
}

