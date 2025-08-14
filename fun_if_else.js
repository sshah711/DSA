//function

function f1(name) {
  console.log("hello " + name);
}

f1("sakshi");

function sum(a, b) {
  let add = a + b;
  console.log("addition", add);
}
sum(2, 3);

function mul(a, b) {
  let mul = a * b;
  console.log("multiplication", mul);
}
mul(2, 3);

function square(a) {
  let sq = a * a;
  // console.log("square", sq);
  return sq
}
let result = square(-55);
console.log("square", result);


//create a function which acdept the age and check if a person is eligible for voting or not
function isVote(num) {
  if (num < 0) {
    console.log("invalid age");
  }
  else if (num >= 18) {
    console.log("eligible for vote");
  } else {
    console.log("not eligible for vote");
  }
}
isVote(20);
isVote(6);
isVote(-5);

// create a function which accept a number and check if it is even or odd
function isEven(num) {
  if (num < 0) {
    console.log("invalid number");
  } else if (num % 2 === 0) {
    console.log("even number");
  } else {
    console.log("odd number");
  }
}
isEven(110);
isEven(125); 
isEven(-3);