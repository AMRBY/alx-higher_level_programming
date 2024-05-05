#!/usr/bin/node
// empty object if w or h <= 0
const Square = require('./5-square');
module.exports = class SSquare extends Square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
};
