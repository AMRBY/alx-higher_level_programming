#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const { argv } = require('node:process');
add(Number(argv[2]), Number(argv[3]));
