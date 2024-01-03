#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

const fileStream = fs.createWriteStream(filePath);

request(url)
  .on('error', (error) => {
    console.error(`Error requesting ${url}: ${error.message}`);
  })
  .on('response', (response) => {
    if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
      fileStream.close(); // Close the file stream on error
    }
  })
  .pipe(fileStream);

fileStream.on('finish', () => {
  console.log(`Body response written to ${filePath}`);
});

fileStream.on('error', (error) => {
  console.error(`Error writing to ${filePath}: ${error.message}`);
});
