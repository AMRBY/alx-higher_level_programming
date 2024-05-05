#!/usr/bin/node
// empty object if w or h <= 0
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    if (size > 0) {
      super(size, size);
    } else {
      super(0, 0);
    }
  }
};
