#!/usr/bin/node
// read a file

const file = require('fs');
const request = require('request');
const { argv } = require('node:process');
request(argv[2],
  function (error, response, body) {
    if (!error) {
      file.writeFile(argv[3], body, function () {});
    }
  });
