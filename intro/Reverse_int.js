function reverseInt(number) {
  let reverse = 0;
  let n = number;
  if (number == 0) {
    return 0;
  }
  number = Math.abs(number);
  //   if (number < 0) {
  //     return -reverseInt(-number); // Call the function recursively with positive number
  //   }
  while (number > 0) {
    let last = number % 10; // Get the last digit
    reverse = reverse * 10 + last; //reversed the number
    number = Math.floor(number / 10); // Remove the last digit
  }

  return n < 0 ? -reverse : reverse; // Return negative if original number was negative
}

let num = 0;
// let num1 = 2**31;
let num1 = 214;
let num2 = 761523;

console.log(reverseInt(num));
console.log(reverseInt(num2));
console.log(reverseInt(num1));
