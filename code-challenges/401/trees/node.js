'use strict';

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left; // think of these (left/right) as objects because they are also nodes
    this.right = right;
  }
}

module.exports = Node;