/*
 * * * *
 * * * *
 * * * *
 * * * *
 */
for (let i = 0; i < 4; i++) {
  let row = " ";
  for (let j = 0; j < 4; j++) {
    row += "* ";
  }
  console.log(row);
}

/*
 *
 * *
 * * *
 * * * *
 */
for (let i = 0; i < 5; i++) {
  let row = " ";
  for (let j = 0; j <= i; j++) {
    // for (let j = 0; j <i+1; j++)  same as above

    row += "* ";
  }
  console.log(row);
}

/*
    1
    1 2
    1 2 3   
    1 2 3 4
    1 2 3 4 5
*/
for (let i = 0; i < 5; i++) {
  let row = " ";
  for (let j = 0; j <= i; j++) {
    row += j + 1 + " ";
  }
  console.log(row);
}

/*
    1
    2 2
    3 3 3   
    4 4 4 4
    5 5 5 5 5
*/
for (let i = 0; i < 5; i++) {
  let row = " ";
  for (let j = 0; j <= i; j++) {

    row += i + 1 + " ";
  }
  console.log(row);
}

/*
    1 2 3 4 5
    1 2 3 4
    1 2 3   
    1 2
    1
*/

for (let i = 5; i > 0; i--) {
  let row = " ";
  for (let j = 0; j < i; j++) {
    row += j + 1 + " ";
  }
  console.log(row);
}

/*
    5 5 5 5 5
    4 4 4 4 
    3 3 3
    2 2
    1
*/

for (let i = 5; i > 0; i--) {
  let row = " ";
  for (let j = 0; j < i; j++) {
    row += i + " ";
  }
  console.log(row);
}

/*
 * * * *
 * * *
 * *
 *
 */

for (let i = 4; i > 0; i--) {
  let row = " ";
  for (let j = 0; j < i; j++) {
    row += "* ";
  }
  console.log(row);
}

/*
  _  _  _  _  *
  _  _  _  *  *
  _  _  *  *  *
  _  *  *  *  *
  *  *  *  *  *
 */

for (let i = 0; i < 5; i++) {
  let row = " ";
  for (let j = 0; j < 5 - (i + 1); j++) {
    row += " _ ";
  }
  for (let k = 0; k < i + 1; k++) {
    row += " * ";
  }
  console.log(row);
}

/*    
  _  _  _  _  *
  _  _  _  *  *  *
  _  _  *  *  *  *  *
  _  *  *  *  *  *  *  *
  *  *  *  *  *  *  *  *  *
 */
for (let i = 0; i < 5; i++) {
  let row = " ";
  for (let j = 0; j < 5 - (i + 1); j++) {
    row += " _ ";
  }
  for (let k = 0; k < (i + 1) * 2 - 1; k++) {  // (2+1)*2 -1=5
    row += " * ";
  }
  console.log(row);
}


/*
    1
    1 0
    1 0 1   
    1 0 1 0
    1 0 1 0 1
*/
for (let i = 0; i < 5; i++) {
  let row = " ";
  let switchValue = 1; 
  for (let j = 0; j <= i; j++) {
    row += switchValue + " ";
    if (switchValue == 1) {
      switchValue = 0;
    }
    else {
      switchValue = 1;
    }
  }
  console.log(row);
}

/*
 1
 0 1
 0 1 0
 1 0 1 0
 1 0 1 0 1
 0 1 0 1 0 1
 0 1 0 1 0 1 0
 1 0 1 0 1 0 1 0
 1 0 1 0 1 0 1 0 1
 0 1 0 1 0 1 0 1 0 1
*/

let switchValue = 1; 
for (let i = 0; i < 10; i++) {
  let row = " ";
  for (let j = 0; j <= i; j++) {
    row += switchValue + " ";
    if (switchValue == 1) {
      switchValue = 0;
    }
    else {
      switchValue = 1;
    }
  }
  console.log(row);
}