#!/usr/bin/node
// read a file

const request = require('request');
const { argv } = require('node:process');
request(argv[2],
  function (error, response, body) {
    if (!error) {
      for (let j = 1; j < 11; j++) {
        let nb = 0;
        for (let i = 0; i < JSON.parse(body).length; i++) {
          if (JSON.parse(body).userId == j) {
	    if (JSON.parse(body).completed === "true") {
            	nb++;
	    }
          }
        }
        console.log("'%d': %d", j, nb):
      }
    }
  }
);
