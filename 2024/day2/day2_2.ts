import { sample, trouble } from "./sample";
import { input } from "./input";

const getIncreasing = (arr: Number[]): boolean => {
    let inc = 0
    let dec = 0
    for ( let i = 0; i < arr.length; i++){
        if (i != 0){
            if (arr[i-1] < arr[i]){
                inc += 1
            } else if (arr[i-1] > arr[i]) {
                dec += 1
            }
        }
    }


    return inc >= dec
}


const getErrorIndex = (line:number[]): number[] => {
    const errorArr: number[] = [];
    const maxDiff = 3;
    const minDiff = 1;

    const increasing = getIncreasing(line)

    for ( let i = 0; i < line.length; i++){

        if (i != 0) {
  
            const diff = Math.abs(line[i] - line[i-1])
            if (diff < minDiff || diff > maxDiff){
                errorArr.push(i)
                continue
                
            }   
            if (increasing !== line[i-1] < line[i] ){

                errorArr.push(i-1)
                continue
                    
            }
        } else {
            const diff = Math.abs(line[i] - line[i+1])
            if (diff < minDiff || diff > maxDiff){
                errorArr.push(i)
            }   
            if (increasing !== line[i] < line[i+1] ){
                errorArr.push(i)
            }
        }
    }
    return errorArr
}



var lines = input.split("\n");
var inputData = lines.map(( line => {
    return line.split(" ").map(Number);
}))


let safeLines = 0
inputData.forEach(line => {

    const errorIndex = getErrorIndex(line)

    if (errorIndex.length <= 0 ){
        safeLines += 1

    } else {

        for (let i = 0; i < line.length; i++){

            const newArr = line.filter((_, index) => index !== i)
            const errors = getErrorIndex(newArr);
            if (errors.length <= 0){
                safeLines += 1
            
                break
            }
        }
    }
});
console.log(safeLines)
