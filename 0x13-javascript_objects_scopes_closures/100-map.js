#!/usr/bin/node
// Import the 'list' array from the '100-data.js' file
const list = require('./100-data.js').list;
// Use the map method to create a new array
console.log(list);
console.log(list.map((item, index) => item * index));

// Print the new list
console.log(newList);
