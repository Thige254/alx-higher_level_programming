#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

try {
  // Read the content of the first source file
  const fileAContent = fs.readFileSync(process.argv[2], 'utf8');

  // Read the content of the second source file
  const fileBContent = fs.readFileSync(process.argv[3], 'utf8');

  // Concatenate the content of the two files
  const concatenatedContent = fileAContent + fileBContent;

  // Write the concatenated content to the destination file
  fs.writeFileSync(process.argv[4], concatenatedContent);

  console.log('Concatenation successful!');
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
