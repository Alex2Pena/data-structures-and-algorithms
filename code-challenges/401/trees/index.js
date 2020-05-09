const BinaryTree = require('./binary-tree.js');
const Node = require('./node.js');

let one = new Node(1);
let two = new Node(2);
let three = new Node(3);
let four = new Node(4);
let five = new Node(5);

one.left = two;
one.right = three;
three.left = four;
three.right = five;

let tree = new BinaryTree(one);

console.log('binary tree', tree);

console.log('pre order (data, l, r)', tree.preOrder());
console.log('in order (l, data, r)', tree.inOrder());
console.log('post order (l, r, data)', tree.postOrder());
console.log('add', tree.add());
// console.log('contains', tree.contains());