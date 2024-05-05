#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
const dict = {};
request(argv[2],
  function (error, response, body) {
    if (!error) {
      for (let i = 0; i < JSON.parse(body).length; i++) {
        const user = JSON.parse(body)[i].userId;
        if (!dict[user]) {
          dict[user] = 0;
        }
        if (JSON.parse(body)[i].completed) {
          dict[user]++;
        }
      }
      console.log(dict);
    }
  }
);
