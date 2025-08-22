//merge sorted arrays
// given two sorted(in non-decreasing order) arrays and 2 integers- represent the no. of elements in arrays.
// merge them into a single sorted(in non-decreasing order) array
// the final sorted array should not be returnd by the function, instead the merged elements should be stored in the first array.
// the first array should have enough space to hold the elements of both arrays.

function mergeSortedArrays(arr1, arr2, m, n) {
//approach 1: 

//   let a1=arr1.slice(0, m).sort((a, b) => a - b); // Get the first m elements of arr1
//   let a2=arr2.sort((a, b) => a - b);
//   let p1=0; // Pointer for arr1
//   let p2=0; // Pointer for arr2

//     for (let i = 0; i < m + n; i++) {
//     if (p1 < m && (p2 >= n || a1[p1] <= a2[p2])) {
//       arr1[i] = a1[p1]; // If arr1 has elements left and is less than or equal to arr2, take from arr1
//       p1++;
//     } else {
//       arr1[i] = a2[p2]; // Otherwise, take from arr2
//       p2++;
//     }

// }
//     return arr1; // Return the merged array


//approach 2:

  let p1 = m - 1; // Pointer for the last element of arr1
  let p2 = n - 1; // Pointer for the last element of arr2
  let i = m + n - 1; // Pointer for the last position in arr1
let a1=arr1.slice(0, m).sort((a, b) => a - b);
let a2=arr2.sort((a, b) => a - b);
  // Merge the arrays from the end to the beginning
  while (p1 >= 0 && p2 >= 0) {
    if(p2 < 0) {
      break; // If arr2 is exhausted, break the loop
    }
    if (p1>=0 && a1[p1] > a2[p2]) {
      a1[i] = a1[p1]; // Place larger element at the end of arr1
      p1--;
    } else {
      a1[i] = a2[p2]; // Place larger element from arr2 at the end of arr1
      p2--;
    }
    i--; // Move to the next position
  }

  return a1; // Return the merged array
}

let arr1 = [1, 7, 3, 0, 0]; // Array with enough space for arr2
let arr2 = [2, 6]; // Second sorted array
let m = 3; // Number of elements in arr1 (excluding the zeros)
let n = 2; // Number of elements in arr2
console.log(mergeSortedArrays(arr1, arr2, m, n)); // Output: [1, 2, 3, 6, 7]

let arr3 = [11, 2, 13, 0, 0, 0]; // Array with enough space for arr4
let arr4 = [4, 15, 6]; // Second sorted array
let m2 = 3; // Number of elements in arr3 (excluding the zeros)
let n2 = 3; // Number of elements in arr4   
console.log(mergeSortedArrays(arr3, arr4, m2, n2)); // Output: [1, 2, 3, 4, 5, 6]