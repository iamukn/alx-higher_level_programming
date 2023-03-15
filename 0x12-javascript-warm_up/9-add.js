#!/usr/bin/node

const arg1 = Math.floor(process.argv[2]);
const arg2 = Math.floor(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

if (!(arg1 && arg2)) {
  console.log('NaN');
} else {
  add(arg1, arg2);
}
