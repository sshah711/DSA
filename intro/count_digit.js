
//finding last digit = n % 10
//remove last digit = Math.floor(n/10)

//function that returns the count of a specific digit in a number
function countDigit(number) {
  let count = 0;
  if (number == 0) {   // Handle the case where the number is 0
    return 1;
  }
  number = Math.abs(number); // Convert to absolute value to handle negative numbers

  while (number > 0) {
    number = Math.floor(number / 10);
    count++;
  }
  return count;
}

let num = 0;
let num1 = -235065;
let num2 = 5065;

console.log(countDigit(num));
console.log(countDigit(num1));
console.log(countDigit(num2));
