#!/usr/bin/node
// Define a function named nbOccurences that takes a list n a search element
exports.nbOccurences = function (list, searchElement) {
    // Initialize a variable to count the occurrences
    let nOccurrences = 0;
  
    // Iterate through the elements of the list
    for (let i = 0; i < list.length; i++) {
      // Check if the current element is equal to the search element
      if (searchElement === list[i]) {
        // Increment the occurrence count if there is a match
        nOccurrences++;
      }
    }
  
    // Return the final count of occurrences
    return nOccurrences;
  };
