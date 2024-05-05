
#!/usr/bin/node
// read a file

const file = require('fs');
const { argv } = require('node:process');
file.writeFile(argv[2], argv[3],
  function (err) {
    if (err) {
      return console.log(err);
    }
  });
