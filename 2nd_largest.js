// function that returns the 2nd largest number in an array
//corner cases: array has less than 2 elements
//array has duplicate elements
//array has empty
//array has negative numbers
//array has infinite numbers


let arr2 = [22];
let arr = [53, 63, 63, 3, 20, 5, -11, -94, 44, -5];
function secLargestNum(arr) {
    if (arr.length < 2) {
        return "Array must contain at least two elements";
    }
  let large = arr[0];
  let secLarge = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (large < arr[i]) {
      secLarge = large; // update second largest before changing 1st largest
      large = arr[i];} // update 1st largest to new largest
      else if (secLarge < arr[i] && arr[i] !== large) { //remove duplicates and ensure secLarge is not equal to large
        secLarge = arr[i];
      }
    }
  return secLarge;
}

console.log("2nd largest number: ", secLargestNum(arr));
