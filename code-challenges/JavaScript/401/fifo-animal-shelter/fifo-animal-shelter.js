'use strict';
// Feature Tasks
// Stretch Goal
// If a cat or dog isn’t preferred, return whichever animal has been waiting in the shelter the longest.



class Node {
  constructor(val){
    this.animal = val;
    this.next = null;
  }
}
// Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
class AnimalShelter {
  constructor(){
    this.front = null;
    this.rear = null;
  }
// enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
  enqueue(animal){
    let newAnimal = new Node(animal);

    if (!this.front && !this.rear) {
      this.front = newAnimal;
      this.rear = newAnimal;
      return;
    }

    this.rear.next = newAnimal;
    this.rear = newAnimal;
  }
// dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
  dequeue(pref){
    if(!pref) return null;
    
    if (!this.front && !this.rear) return console.log('ERROR: List is Empty!');

    if (this.front.animal === pref){
      let dequeuedNode = this.front;
      this.front = this.front.next;
      dequeuedNode.next = null;
      return dequeuedNode;
    }

    let currentNode = this.front;
    let nextNode = this.front.next;
    let prevNode = null;

    while(currentNode.next !== null && currentNode.animal !== pref){
      prevNode = currentNode;
      currentNode = currentNode.next;
      nextNode = currentNode.next;
    }
    
    if(currentNode.animal === pref){
      prevNode.next = nextNode;
      currentNode.next = null;
      return currentNode;
    }

    console.log('ERROR: that preference does not exist!');
    return null;
  }
}

module.exports = AnimalShelter;
