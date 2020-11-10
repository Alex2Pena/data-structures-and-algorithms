'use strict';
let node = require('./node.js')
class BinaryTree {
  constructor(root = null) {
    this.root = root;
  }

  // DFS method - depth first search - read the node, then go left, then go right
  preOrder() {
    let results = [];

    let _walk = node => {
      results.push(node.value); // this is where we "read" the node

      if (node.left) _walk(node.left);
      if (node.right) _walk(node.right);
    }

    _walk(this.root); // this is where we kick off the traversal
    return results;
  }

  inOrder() {
    let results = [];

    let _walk = node => {
      if (node.left) _walk(node.left);
      results.push(node.value); // this is where we "read" the node
      if (node.right) _walk(node.right);
    }

    _walk(this.root); // this is where we kick off the traversal
    return results;
  }

  postOrder() {
    let results = [];

    let _walk = node => {
      if (node.left) _walk(node.left);
      if (node.right) _walk(node.right);
      results.push(node.value); // this is where we "read" the node
    }

    _walk(this.root); // this is where we kick off the traversal
    return results;
  }


  // Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.\
  add(value) {
    let newNode = new Node(value);
    if(!this.root){
      this.root=newNode;
    }
    // Left
    if(this.root.value < node.value){
      _walk(node.left);
    }
    // Right
    if(this.root.value > node.value){
      _walk(node.right)
    }
    return this;
    }
}

module.exports = BinaryTree;