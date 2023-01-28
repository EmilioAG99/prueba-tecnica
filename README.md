# Prueba técnica

### _Luis Emilio Alcántara Guzmán_

---

## 1. Requirements

Design an API endpoint that provides autocomplete suggestions for large cities in the US and Canada.

- The endpoint is exposed at /search
- The partial (or complete) search term is passed as a query string parameter q
- The endpoint returns a JSON response with an array of scored suggested matches
- You must consider the following:

1.  The suggestions are sorted by descending score
2.  Each suggestion has a score between 0 and 1 (inclusive) indicating confidence in the suggestion (1 is most confident)
3.  Each suggestion has a name which can be used to disambiguate between similarly named locations
4.  Each suggestion has a latitude and longitude

---

## 2. How it works

- This API will provide a list of cities based on a search term, latitude and longitude given in the query parameters of the '/search' endpoint.
- Required parameters:

1.  Search term
2.  Latitude
3.  Longitude

- For an accurate response, you should provide the mentioned parameters within your request.

### 2.1 Implementation

- The API will take the parameters from the request to search through a list of JSON object, the goal is to find all the cities that contain the given search term and are close to the geographic location (latitude and longitude)
- The API has an arbitrary value to determine whether the city is close enough to the latitude and longitude that are passed in the request
- If there are no cities that match the given criteria, it will return an empty array, otherwise it will return an array of object that contain the information of the filtered cities
- If the API fails to respond, it will return an HTTP error with code 400. This will also give a message with details of the error.

---

## Endpoints

- **URL**: /search
- **HTTP Action**: Get
- **Description**: This endpoint will return a list of cities that matched the request parameters

## How to use this API

- Install Flask using pip
- run: "flask --app main run" within the main directory
- To do a request you have to access your localhost in port 5000 using "/search" and the query parameters

## 3. References

1. [Flask Installation](https://flask.palletsprojects.com/en/2.2.x/installation/)
2. [Flask Quick start](https://flask.palletsprojects.com/en/2.2.x/quickstart/)

## 4. Test
![Sucessful](https://user-images.githubusercontent.com/44034926/215229100-243ebec6-94b9-4171-8d8b-64fe573e163b.png)
![Empty](https://media.discordapp.net/attachments/929234619885289482/1068682730558193705/Screen_Shot_2023-01-27_at_6.03.32_p.m..png)
