#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        // If w or h is not a positive integer, create an empty object
        Object.assign(this, {});
      }
    }
  
    print () {
      // Print the rectangle using the character X
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
  
  module.exports = Rectangle;
  
  // Test the class
  const r1 = new Rectangle(2, 3);
  r1.print();
  
  const r2 = new Rectangle(10, 5);
  r2.print();
