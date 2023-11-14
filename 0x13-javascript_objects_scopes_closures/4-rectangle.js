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
      for (let row = 0; row < this.height; row++) {
        let s = '';
        // Loop through each column (width)
        for (let col = 0; col < this.width; col++) {
          // Append 'X' to the string for each column
          s += 'X';
        }
        // Print the string representing a row of the rectangle
        console.log(s);
      }
    }
  
    // Method to exchange width and height of the rectangle
    rotate() {
      const aux = this.width;
      this.width = this.height;
      this.height = aux;
    }
  
    // Method to double the width and height of the rectangle
    double() {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
  // Export the Rectangle class for external use
  module.exports = Rectangle;
