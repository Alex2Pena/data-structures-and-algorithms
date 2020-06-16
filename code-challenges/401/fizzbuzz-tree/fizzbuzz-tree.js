'use strict';
let tree = require('../trees/binary-tree');
// Code Challenge
// Conduct “FizzBuzz” on a tree while traversing through it. Change the values of each of the nodes dependent on the current node’s value
// JavaScript: a folder named fizzBuzzTree which contains a file called fizz-buzz-tree.js



// Write a function called FizzBuzzTree which takes a tree as an argument.
// Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
const FizzBuzzTree = (root) => {
  let newVal = '';
// If the value is divisible by 3, replace the value with “Fizz”
  if ( root.val % 3 === 0 ) newVal += 'Fizz';
// If the value is divisible by 5, replace the value with “Buzz”
  if ( root.val % 5 === 0 ) newVal += 'Buzz'; 

  let newTreeRoot = new tree.Node( newVal ? newVal : `${root.val}` );

  if ( root.left ) {
    newTreeRoot.left = FizzBuzzTree(root.left);
  }
  if ( root.right ) {
    newTreeRoot.right = FizzBuzzTree(root.right);
  }
// Return the new tree.
  return newTreeRoot;
}

module.exports = FizzBuzzTree;
