//reverse a string, the input string is given as an array of characters
//IN-PLACE means we don't need to create new array, we can use the same array to store the unique elements.

function reverseString(arr) {
  let l = 0; // Pointer for the start of the array
  let r = arr.length - 1; // Pointer for the end of the array

  // for (let i = 0; i < Math.floor(arr.length / 2); i++) {
  //     let temp = arr[i]; // Store the current left element
  //     arr[i] = arr[arr.length - 1 - i]; // Swap the left element with the right element
  //     arr[arr.length - 1 - i] = temp; // Assign the stored left element to the right position

  // }
  while (l < r) {
    let temp = arr[l];
    arr[l] = arr[r];
    arr[r] = temp;
    l++; // Move the left pointer to the right
    r--; // Move the right pointer to the left
  }
  return arr; // Return the reversed array
}

let arr = ["s", "a", "k", "s", "h", "i"];
console.log(reverseString(arr)); // Output: ['i','h','s','k','a','s']

let arr2 = ["h", "e", "l", "l", "o"];
console.log(reverseString(arr2)); // Output: ['o','l','l','e','h']
