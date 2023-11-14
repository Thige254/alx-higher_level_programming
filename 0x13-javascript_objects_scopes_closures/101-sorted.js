#!/usr/bin/node
// Import the dictionary of occurrences by user id from 101-data.js
const dict = require('./101-data').dict;

// Convert the dictionary to an array of key-value pairs
const totalList = Object.entries(dict);

// Extract unique values from the dictionary
const uniqueValues = [...new Set(Object.values(dict))];

// Create a new dictionary to store user ids by occurrence
const newDict = {};

// Loop through unique values to populate the new dictionary
for (const j in uniqueValues) {
  // Initialize an empty list for user ids
  const list = [];
  // Loop through the total list to find user ids with the current occurrence
  for (const k in totalList) {
    // Check if the occurrence matches the current unique value
    if (totalList[k][1] === uniqueValues[j]) {
      // Add the user id to the list
      list.unshift(totalList[k][0]);
    }
  }
  newDict[uniqueValues[j]] = list;
}

// Print the new dictionary
console.log(newDict);
