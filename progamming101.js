const a = 1;
// we can not change the value later . if i changed so it will give me an error
// a=10

let b = 2;
// console.log(b);
//2
// we can change the value later . if i changed so it will not give me an error

b = 20;
// console.log(b);
//20

var c = 3;
// we can change the value later . if i changed so it will not give me an error

let fname = 2;
let lname = 3;

let fullname = fname + " " + lname;  //concatenation
let fullname1 = fname  + lname;  //addition
console.log(fullname);
console.log(fullname1);



// array is a collection of items

let arr=[1,2,33,44,55]
console.log(arr[2])


let arr1 = ["a", "b", "c", "d"];
console.log(arr1[0]);

let arr2 = [1, true, "hello", null, undefined, { key: "value" }, [1, 2,[55,66,77], 3]];
console.log(arr2[6]);
console.log(arr2[6][1]);
console.log(arr2[6][2][1]);

//objects are used to store key-value pairs
let obj = {          // object is key value pair
    name: "shah",
    fname: "sakshi",
    num: 123,
    arr: [1, 2, 3],
    nestedObj: {
        key1: "aaa",
        key2: 1
    }
};
console.log(obj.name + " " + obj.fname); 
console.log(obj.arr[1]); 
console.log(obj.nestedObj.key1);