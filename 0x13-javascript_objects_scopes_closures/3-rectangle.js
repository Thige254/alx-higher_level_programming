#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
    // Constructor with width and height parameters
    constructor(w, h) {
      // Check if both width and height are positive integers
      if (w > 0 && h > 0) {
        // Initialize instance attributes width and height
        this.width = w;
        this.height = h;
      }
    }
  
    // Method to print the rectangle using the character 'X'
    print() {
      // Loop through each row (height)
      for (let i = 0; i < this.height; i++) {
        let s = '';
        // Loop through each column (width)
        for (let j = 0; j < this.width; j++) {
          // Append 'X' to the string for each column
          s += 'X';
        }
        // Print the string representing a row of the rectangle
        console.log(s);
      }
    }
  }
  
  // Export the Rectangle class for external use
  module.exports = Rectangle;
