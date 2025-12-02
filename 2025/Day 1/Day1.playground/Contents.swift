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

for line in lines {
    var shouldAdd = (line.first == "R")
    var toAdd = String(line.dropFirst())
    var numToAdd = Int(toAdd)!
    number = change(atNumber: number, amount: shouldAdd ?  numToAdd: -numToAdd)
    if number == 0 {
        times0 += 1
    }
}
print(times0);



func change(atNumber: Int, amount: Int) -> Int {
   // var shortendAmount = amount % 99
   // print("SHortend \(shortendAmount)")
    var newNumber = (atNumber + amount) % 100
    
    //print("newNumber \(newNumber)")
    if newNumber < 0 {
        newNumber += 100
    } else if newNumber > 99 {
        newNumber -= 100
    }
    return newNumber
}

