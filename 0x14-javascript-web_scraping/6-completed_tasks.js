#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
const dict = {};
request(argv[2],
  function (error, response, body) {
    if (!error) {
      for (let j = 1; j < 11; j++) {
        let nb = 0;
        for (let i = 0; i < JSON.parse(body).length; i++) {
          if (JSON.parse(body)[i].userId === j) {
            if (JSON.parse(body)[i].completed) {
              nb++;
            }
          }
        }
        dict[j - 1] = nb;
      }
      console.log(dict);
    }
  }
);
