#!/usr/bin/node
function factorial (a) {
  if (a > 1) {
    return (a * factorial(a - 1));
  } else if (a <= 0) {
    return 0;
  } else {
    return 1;
  }
}

const { argv } = require('node:process');
if (argv[2]) {
  const x = factorial(Number(argv[2]));
  console.log(x);
} else {
  console.log('1');
}
