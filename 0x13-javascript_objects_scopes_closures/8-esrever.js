#!/usr/bin/node

exports.esrever = function (list) {
    // Initialize variables to keep track of the indices
    let len = list.length - 1; // Index of the last element
    let i = 0; // Index of the first element
  
    // Iterate through the list until the middle is reached
    while ((len - i) > 0) {
      // Swap the elements at positions len and i
      const aux = list[len];
      list[len] = list[i];
      list[i] = aux;
  
      // Move towards the center of the list
      i++;
      len--;
    }
  
    // Return the reversed list
    return list;
  };
