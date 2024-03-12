#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log('0');
} else {
  let c = Number(argv[2]);
  let a = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    const b = Number(argv[i]);
    if (a < b) {
      c = a;
      a = b;
    } else if (c < b && b !== a) {
      c = b;
    }
  }
  console.log(c);
}
