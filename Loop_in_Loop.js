// loop inside a loop

for (let i = 0; i < 2; i++) {
    for (let j = 0; j < 2; j++) {
        // console.log("*");
        console.log("i:", i, "j:", j);
    }
}


for (let i = 0; i < 4; i++) {
    for (let j = 0; j < i; j++) {
        console.log("x:", i, "y:", j);
    }
}


for (let i = 0; i < 3; i++) {
    for (let j = i; j > 0; j--) {
        console.log("c:", i, "d:", j);
    }
}


for (let i = 4; i > 0; i--) {
    for (let j = 0; j < i; j++) {
        console.log("e:", i, "f:", j);
    }
}