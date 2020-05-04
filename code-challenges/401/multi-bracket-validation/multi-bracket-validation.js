// Feature Tasks
// On your main file, create…
// C#: a method called public static bool MultiBracketValidation(string input)
// JavaScript: a function called multiBracketValidation(input)
// Python: a function called multi_bracket_validation(input)
// Java: a method public static boolean multiBracketValidation(String input)
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
// {}{Code}[Fellows](())	TRUE
// [({}]	FALSE
// (](	FALSE
// {(})	FALSE
// Consider these small examples and why they fail.

// Input	Output	Why
// {	FALSE	error unmatched opening { remaining.
// )	FALSE	error closing ) arrived without corresponding opening.
// [}	FALSE	error closing }. Doesn’t match opening (.