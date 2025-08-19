//given an integer array and a value, remove all instances of that value in the array
//the relative order of the elements should be same.
//IN-PLACE means we don't need to create new array, we can use the same array to store the unique elements.
//use two pointers technique to remove elements in-place
function removeElement(arr, val) {
  let x = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == val) {
      continue; // Skip the element if it matches the value to be removed
    } else {
      arr[x] = arr[i]; // Store the current element at the next position
      x++; // Move the pointer to the next position
    }
  }
  return x; // Return the length of the modified array
}

let arr = [1,1, 1, 7, 8, 4, 5, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10];
let val = 5;
console.log(removeElement(arr, val)); 
console.log(arr.slice(0, removeElement(arr, val)));
