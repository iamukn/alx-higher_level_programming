#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);

function fact (x) {
  if (x === 1 || x === undefined || x === 0 || isNaN(x)) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}

console.log(fact(arg));
