#!/usr/bin/node
// Initialize a counter to keep track of the number of arguments printed
let count = 0;

exports.logMe = function (item) {
  // Print the current count and the argument value
  console.log(count + ': ' + item);

  // Increment the count for the next call
  count++;
};
