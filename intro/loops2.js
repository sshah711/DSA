// write a function that searches for an element in an array and returns its index, if the element is not found return -1

let arr = [111, 23, 33, 40, 5, -1, -4, 44, -35];

function searchElement(arr, element) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == element) {
      return i; // return the index of the found element
    }
  }
  return -1; // return -1 if the element is not found
}
console.log("search element index",searchElement(arr, 0));
console.log("search element index",searchElement(arr, 40));

// function that returns the count of negative numbers in an array

function countNegNum(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      count++;
    }
  }
  return count;
}

console.log("Negative numbers",countNegNum(arr));

// function that returns the largest number in an array

function largestNum(arr) {
  let large = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (large < arr[i]) {
      large = arr[i];
    }
  }
  return large;
}

console.log("largest number",largestNum(arr));


//hw
// function that returns the smallest number in an array

function smallestNum(arr) {
  let smallest = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (smallest > arr[i]) {
      smallest = arr[i];
    }
  }
  return smallest;
}

console.log("Smallest number",smallestNum(arr));