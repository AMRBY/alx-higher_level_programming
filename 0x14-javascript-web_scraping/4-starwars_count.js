#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
request(argv[2],
  function (error, response, body) {
    if (!error) {
      let nb = 0;
      for (let j = 0; j < JSON.parse(body).results.length; j++) {
        for (let i = 0; i < JSON.parse(body).results[j].characters.length; i++) {
          if (JSON.parse(body).results[j].characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
            nb++;
          }
        }
      }
      console.log(nb);
    }
  }
);
