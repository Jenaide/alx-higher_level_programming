#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Retangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
