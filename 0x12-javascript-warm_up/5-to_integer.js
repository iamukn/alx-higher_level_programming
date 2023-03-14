#!/usr/bin/node
//  Declares a variable and assigns the first command line argument
const arg = process.argv[2];
//  parse the arg to an integer
const a = parseInt(arg, 10);

//  confirm if it is an integer
if (!(a > 0 || a <= 0)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${a}`);
}
