#!/usr/bin/node

// Import the 'dict' object from the '101-data.js' file
const occurrencesDict = require('./101-data').dict;

// Convert the dictionary to an array of key-value pairs
const entries = Object.entries(occurrencesDict);

// Extract the unique values (occurrences) from the dictionary
const uniqueOccurrences = [...new Set(Object.values(occurrencesDict))];

// Create a new dictionary to store user ids by occurrences
const userIdsByOccurrences = {};

// Iterate over unique occurrences and build the new dictionary
for (const occurrence of uniqueOccurrences) {
  // Use filter to get user ids with the current occurrence
  const userIds = entries
    .filter(([userId, count]) => count === occurrence)
    .map(([userId]) => userId);
  
  // Add the user ids to the new dictionary
  userIdsByOccurrences[occurrence] = userIds;
}

// Print the new dictionary
console.log(userIdsByOccurrences);
