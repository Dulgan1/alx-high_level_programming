#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print () {
    for (let y = 0; y <= this.height; y++) {
      for (let x = 0; x <= this.width; x++) {
        console.log('X');
      }
    }
  }
};
