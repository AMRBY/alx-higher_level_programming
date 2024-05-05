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
      this.print(c);
    } else {
      this.print('X');
    }
  }
};
