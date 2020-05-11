'use strict';

//Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    };
};

class LinkedList {
    constructor(value) {
        this.head = null;
        this.tail = null;
        this.size = 0;
    };

    // Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    add(value) {
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode;
        };
        if (this.tail === null) {
            this.tail = newNode
            this.size++
        };
        if (this.tail !== null) {
            this.tail.next = newNode;
            this.tail = newNode;
        };

        console.log('I am the head', this.head);
        console.log('I am the tail', this.tail);
        // need to tell a new node what to do or where to go once there is already a head in place.
    };

    // Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    includes(value) {
        let ImHereNow = this.head;

        while (ImHereNow !== null) {
            console.log('imHere', ImHereNow.value, 'Value', value);
            if (ImHereNow.value === value) {
                console.log(true);
                return true;
            };
            ImHereNow = ImHereNow.next;
        };
        console.log(false);
        return false;
    };

    // Define a method called toString which takes in no arguments and returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
    toString() {
        if (!this.head) {
            console.log('NULL')
            return 'NULL';
        }
        let ImHereNow = this.head;
        let string = '';
        while (ImHereNow.next !== null) {
            string += `{${ImHereNow.value}} -> `;
            ImHereNow = ImHereNow.next;
        }
        string += `{${ImHereNow.value}} -> NULL `;
        console.log('I am a string', string);
        return string;
    };
    // .append(value) which adds a new node with the given value to the end of the list
    append(value) {
        let node = new Node(value);

        if (!this.head) {
            this.head = node;
        } else {
            let IamHere = this.head;
            while (IamHere.next) {
                IamHere = IamHere.next;
            };
            IamHere.next = node;
        };
        console.log(node.value, 'Just got added to the list');
        return this;
    };

    // .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    insertBefore(value, newVal) {
        if (this.includes(value)) {
            let newNode = new Node(newVal);
            let IamHere = this.head;
            while (IamHere.next.value !== value) {
                IamHere = IamHere.next;
            }
        }
    };
    // add ot the begining of the linked list
    addToHead(value) {
        const newNode = {
            value
        }; 
        newNode.next = this.head; // 2
        this.head = newNode; // 3
        this.length++;
        return this;

    }

    // It inserts an element at the given index in a list. Insert element at the position index 
    insertAt(element, index) {
        let newNode = new Node(element);
        let IamHere = this.head;
        let llIndex = 0;

        while(llindex !== index) {
            IamHere = IamHere.next;
            llindex++;
        }
        


        return this;
    }





    // .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    //     insertAfter(value, newValue){

    //     }
    // };




    printList() {
        const array = [];
        let currentNode = this.head;
        console.log('i am the current node', currentNode);
        while (currentNode !== null) {
            array.push(currentNode.value)
            currentNode = currentNode.next
        }
        console.log('I am an array', array);
        return array;
    }
}
// Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
const list = new LinkedList();
list.add(40);
list.add(41);
list.add(39);
list.add(69);
list.includes(77);
list.includes(39);
list.toString();
list.append(102);
list.addToHead(22);

list.printList();





// Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

// Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

// Structure and Testing
// Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

// Write tests to prove the following functionality:

// Can successfully instantiate an empty linked list
// Can properly insert into the linked list
// The head property will properly point to the first node in the linked list
// Can properly insert multiple nodes into the linked list
// Will return true when finding a value within the linked list that exists
// Will return false when searching for a value in the linked list that does not exist
// Can properly return a collection of all the values that exist in the linked list
// Ensure your tests are passing before you submit your solution.






// Code challenge 6

// Feature Tasks
// Write the following methods for the Linked List class:

// .append(value) which adds a new node with the given value to the end of the list
// .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
// .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
// Examples
// .append(value)
// Input	Args	Output
// head -> [1] -> [3] -> [2] -> X	5	head -> [1] -> [3] -> [2] -> [5] -> X
// head -> X	1	head -> [1] -> X
// .insertBefore(value, newVal)
// Input	Args	Output
// head -> [1] -> [3] -> [2] -> X	3, 5	head -> [1] -> [5] -> [3] -> [2] -> X
// head -> [1] -> [3] -> [2] -> X	1, 5	head -> [5] -> [1] -> [3] -> [2] -> X
// head -> [1] -> [2] -> [2] -> X	2, 5	head -> [1] -> [5] -> [2] -> [2] -> X
// head -> [1] -> [3] -> [2] -> X	4, 5	Exception
// .insertAfter(value, newVal)
// Input	Args	Output
// head -> [1] -> [3] -> [2] -> X	3, 5	head -> [1] -> [3] -> [5] -> [2] -> X
// head -> [1] -> [3] -> [2] -> X	2, 5	head -> [1] -> [3] -> [2] -> [5] -> X
// head -> [1] -> [2] -> [2] -> X	2, 5	head -> [1] -> [2] -> [5] -> [2] -> X
// head -> [1] -> [3] -> [2] -> X	4, 5	Exception
// Unit Tests
// Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

// You have access to the Node class and all the properties on the Linked List class.

// Write tests to prove the following functionality:

// Can successfully add a node to the end of the linked list
// Can successfully add multiple nodes to the end of a linked list
// Can successfully insert a node before a node located i the middle of a linked list
// Can successfully insert a node before the first node of a linked list
// Can successfully insert after a node in the middle of the linked list
// Can successfully insert a node after the last node of the linked list
// Unit tests must be passing before you submit your final solution code.

// Stretch Goal
// Once you’ve achieved a working solution, write an additional method to delete a node with the given value from the linked list.