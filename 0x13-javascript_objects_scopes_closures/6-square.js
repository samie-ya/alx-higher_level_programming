#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
