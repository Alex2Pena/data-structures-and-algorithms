// Feature Tasks
// Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

// Example
// Input	           Output
// [2,4,6,8], 5	       [2,4,5,6,8]
// [4,8,15,23,42], 16  [4,8,15,16,23,42]
// [1, 2, 3, 4, 5, 6, 7, 8], 

// Stretch Goal
// Once you’ve achieved a working solution, write a second function that removes an element from the middle index and shifts other elements in the array to fill the new gap.


function insertShiftArray(arr, value){
    // create empty array
    let newArr = [];

    // find middle index of input array
    let middleIndex = Math.ceil(arr.length/2);

    // loop through first half of input array
    // for each iteration, 
    // set new array's index equal to same index in input array
    for (let i = 0; i < middleIndex; i++) {
    // insert value from the input array into the new array
    newArr[i] = arr[i]
    console.log('newArr after', newArr)
}

// insert new value to middle of new array
newArr[middleIndex] = value

// fill in second half of newArray with original array
for (let i = middleIndex; i < arr.length; i++) {
    console.log(`i: ${i}
    newArr: ${newArr}
    newArr[${i}]: ${newArr[i]}
    arr: ${arr}
    arr[${i}]: ${arr[i]}`)
    newArr[i+1] = arr[i];
    }

    return newArr;

};
let result = insertShiftArray([1, 2, 3, 4, 5], 'value')
console.log(result) // should be [1, 2, 3, 'value', 4, 5]

// [emty item, 4]

module.exports = insertShiftArray;
``