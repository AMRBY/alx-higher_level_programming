#!/usr/bin/node
// read a file

const file = require('fs');
const { argv } = require('node:process');
file.readFile(argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      return console.log(err);
    }
    console.log(data.toString());
  });
