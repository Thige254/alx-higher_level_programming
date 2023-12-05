#!/usr/bin/node
// Use the fs (File System) module to perform file operations
const fs = require('fs');

// Read the content of the first source file (process.argv[2])
const fArg = fs.readFileSync(process.argv[2]).toString();

// Read the content of the second source file (process.argv[3])
const sArg = fs.readFileSync(process.argv[3]).toString();

// Concatenate the content of the two files
const concatenatedContent = fArg + sArg;

// Write the concatenated content to the destination file (process.argv[4])
fs.writeFileSync(process.argv[4], concatenatedContent);
#!/usr/bin/node
// Use the fs (File System) module to perform file operations
const fs = require('fs');

// Read the content of the first source file (process.argv[2])
const fArg = fs.readFileSync(process.argv[2]).toString();
// Read the content of the second source file (process.argv[3])
const sArg = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], fArg + sArg);
