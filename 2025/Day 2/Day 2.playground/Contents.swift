import Cocoa

var testData = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

var input = """
    269194394-269335492,62371645-62509655,958929250-958994165,1336-3155,723925-849457,4416182-4470506,1775759815-1775887457,44422705-44477011,7612653647-7612728309,235784-396818,751-1236,20-36,4-14,9971242-10046246,8796089-8943190,34266-99164,2931385381-2931511480,277-640,894249-1083306,648255-713763,19167863-19202443,62-92,534463-598755,93-196,2276873-2559254,123712-212673,31261442-31408224,421375-503954,8383763979-8383947043,17194-32288,941928989-941964298,3416-9716
    """

let ranges = input.split(separator: ",")
var invalidNums:[Int] = [];

for range in ranges {
    let nums = range.split(separator: "-")
    invalidNums = invalidNums + check(low: Int(nums[0]) ?? 0, high: Int(nums[1]) ?? 0)
}

print(invalidNums.count)
var count = 0;

for num in invalidNums {
    count = num + count
}
print(count);

func check(low: Int, high: Int) -> [Int]{
    var invalidNums:[Int] = [];
    for low in low...high {
        let num = String(low)
        let mid = num.count / 2
        let midIndex = num.index(num.startIndex, offsetBy: mid)
        let firstHalf = String(num[..<midIndex])
        let secoundHalf = String(num[midIndex...])
        if firstHalf == secoundHalf {
            invalidNums.append(low)
        }

    }
    return invalidNums
}
