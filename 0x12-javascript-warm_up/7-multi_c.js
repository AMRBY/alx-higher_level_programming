#!/usr/bin/node
const { argv } = require('node:process');
for (let i = 0; i < Number(argv[2]); i++) {
  console.log('C is fun');
}
