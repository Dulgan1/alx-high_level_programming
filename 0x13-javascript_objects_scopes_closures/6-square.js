#!/usr/bin/node

const SSquare = require('./5-square');

module.exports = class Square extends SSquare {
  charPrint (c) {
    if (c == null) {
      this.print();
    } else {
      for (let y = 1; y <= this.height; y++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
