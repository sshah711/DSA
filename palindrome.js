var isPalindrome = function (number) {
  let n = number;
  let reverse = 0;
  reminder = 0;
    if (number == 0) { // Handle the case where the number is 0
    return true;
  }
  if (number < 0) { // Handle negative numbers
    return false;
  }
  while (number > 0) {
    reminder = number % 10; // Get the last digit
    reverse = reverse * 10 + reminder; //reversed the number
    number = Math.floor(number / 10); // Remove the last digit
  }
  return n === reverse; // Check if the original number is equal to the reversed number
};

let num = 0;
let num1 = -252;
let num2 = 505;

console.log(isPalindrome(num));
console.log(isPalindrome(num2));
console.log(isPalindrome(num1));
