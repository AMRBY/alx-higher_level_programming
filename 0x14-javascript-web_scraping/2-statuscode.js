#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
request(argv[2],
  function (error, response) {
    if (!error) {
      console.log('code:', response.statusCode);
    }
  }
);
