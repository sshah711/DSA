//loops while, for, do while - whenever you want to repeat a task you want loops
//for loop - initialization, condition, increment/decrement
for (let i = 2; i < 15; i=i+3) {
    console.log("hello",i);
}

for (let i = 10; i >= -10; i=i-2) {
    console.log("hii",i);
}

//nothing will be printed because the condition is false
for (let i = 5; i < 4; i++) {
    console.log("hello",i);
}

//infinite loop
// for (let i = 1; i >0; i++) {
//     console.log("i",i);
// }
    
//function inside a loop
function printHello() {
    console.log("hello");
}
for (let i = 0; i < 5; i++) {
    printHello();
}

//array inside a loop
let arr = [11, 20, 1, 14, 95,-3,-2];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

//from the array print only odd numbers
for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 != 0) {
        console.log(arr[i]);
    }
}

//while loop - condition, body
let j = 0;
while (j < 5) { 
    console.log("hello", j);
    j++;
}