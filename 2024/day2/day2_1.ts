import { sample } from "./sample";
import { input } from "./input";

const checkoutLine = (line: number[]): boolean => {
    const maxDiff = 3;
    const minDiff = 1;
    var increasing = line[0] < line[1];

    for ( let i = 0; i < line.length; i++){
        if (i != 0) {
            if (increasing !== line[i-1] < line[i] ){
                return false
            }
            const diff = Math.abs(line[i] - line[i-1])
            if (diff < minDiff || diff > maxDiff){
                return false
            }

        }
    }

    return true
}

var lines = input.split("\n");
var inputData = lines.map(( line => {
    return line.split(" ").map(Number);
}))

console.log(inputData);
let safeLines = 0
inputData.forEach(line => {
    let safe = checkoutLine(line);
    if (safe){safeLines += 1}
});
console.log(safeLines)




