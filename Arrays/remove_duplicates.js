// incresing sorted array means that the array has no duplicates [1,2,5,8,9,10] a[i+1] > a[i]
// decreasing sorted array means that the array has no duplicates [10,9,8,5,2,1] a[i+1] < a[i]
//non-decressing order means that the array has duplicates [1,2,2,5,8,9,10] a[i+1] >= a[i]
//so remove duplicates in-place such that each unique element appears only once. the relative order of the elements should be same.
//IN-PLACE means we don't need to create new array, we can use the same array to store the unique elements.
//use two pointers technique to remove duplicates in-place
//Time Complexity: O(n) - we are iterating through the array once

function removeDuplicates(arr) {
  let x = 0; // Pointer for next unique element
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[x]) {
      // Check if the current element is greater than the last unique element
      x = x + 1; // Move the pointer to the next position
      arr[x] = arr[i]; // Store unique element at the next position
    }
  }
      return x + 1; // Return the length of the unique elements

}
let arr = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10];
console.log(removeDuplicates(arr)); // Output: 10
console.log(arr.slice(0, removeDuplicates(arr))); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
