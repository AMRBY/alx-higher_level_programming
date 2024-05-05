#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(url,
  function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).title);
    }
  }
);
