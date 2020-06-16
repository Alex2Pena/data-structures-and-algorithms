// Feature Tasks
// JavaScript: a function called multiBracketValidation(input)

// Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

// Round Brackets : ()
// Square Brackets : []
// Curly Brackets : {}
// Example
// Input	Output
// {}	TRUE
// {}(){}	TRUE
// ()[[Extra Characters]]	TRUE
// (){}[[]]	TRUE
'use strict';
// {}{Code}[Fellows](())	TRUE
// [({}]	FALSE
// (](	FALSE
// {(})	FALSE
// Consider these small examples and why they fail.

// Input	Output	Why
// {	FALSE	error unmatched opening { remaining.
// )	FALSE	error closing ) arrived without corresponding opening.
// [}	FALSE	error closing }. Doesn’t match opening (.

const multiBracketValidation = (str) => {
  let strArray = str.split('');
  
  let finalCount = strArray.reduce((acc, currentVal) => {
    if(currentVal === '(' || currentVal === '{' || currentVal === '['){
      return ++acc;
    } else if(currentVal === ')' || currentVal === '}' || currentVal === ']') {
      return --acc;
    }
    return acc;
  }, 0);

  return finalCount === 0;
}

module.exports = multiBracketValidation;
