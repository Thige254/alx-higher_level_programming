#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error(writeError);
      return;
    }

    console.log(`Body response written to ${filePath}`);
  });
});
