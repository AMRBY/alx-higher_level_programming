#!/usr/bin/node
const { argv } = require('node:process');
if (Number(argv[2])) {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('X'.repeat(Number(argv[2])));
  }
} else {
  console.log('Missing size');
}
