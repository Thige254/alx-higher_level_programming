#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  // Function to fetch character data and print the name
  const fetchAndPrintCharacter = (characterUrl) => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
        return;
      }

      if (characterResponse.statusCode !== 200) {
        console.error(`Failed to retrieve character data. Status code: ${characterResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);
    });
  };

  // Iterate through charactersUrls and print names
  charactersUrls.forEach(fetchAndPrintCharacter);
});
