## HTTP Requests in JavaScript

### Introduction
HTTP (HyperText Transfer Protocol) requests are essential for interacting with web servers, APIs, and other services over the internet. In JavaScript, especially in Node.js, you can make HTTP requests using various modules like `request` (which is deprecated) or modern alternatives like `fetch`.

### Making HTTP Requests with `fetch`

The `fetch` function is a modern and widely-used method for making HTTP requests in JavaScript. It is available in both the browser and Node.js (with additional packages).

#### Basic Usage
Here's a simple example of using `fetch` to make a GET request to a public API:

```javascript
// Fetching data from a public API
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json()) // Parsing the JSON response
  .then(data => {
    console.log(data); // Output the data to the console
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

### Making HTTP Requests with `axios`

`axios` is a popular alternative to `fetch` that simplifies HTTP requests and provides additional features.

#### Installation
To use `axios`, you need to install it using npm:

```bash
npm install axios
```

#### Basic Usage
Here's an example of using `axios` to make a GET request:

```javascript
const axios = require('axios');

// Fetching data from a public API
axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    console.log(response.data); // Output the data to the console
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

### Making POST Requests

POST requests are used to send data to a server to create or update a resource. Both `fetch` and `axios` can be used to make POST requests.

#### Using `fetch` for POST Requests

```javascript
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1
  })
})
  .then(response => response.json())
  .then(data => {
    console.log(data); // Output the data to the console
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

#### Using `axios` for POST Requests

```javascript
axios.post('https://jsonplaceholder.typicode.com/posts', {
  title: 'foo',
  body: 'bar',
  userId: 1
})
  .then(response => {
    console.log(response.data); // Output the data to the console
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

### Real-World Application

HTTP requests are used in various real-world applications, such as:
1. **Fetching Weather Data**: Retrieve current weather information from an API to display on a website or app.
2. **Submitting Forms**: Send user input from a form to a server for processing.
3. **Interacting with Databases**: Communicate with backend services to store, update, or retrieve data from a database.

### Technical End of Chapter MCQ

1. What does HTTP stand for?
    a. HyperText Transfer Protocol  
    b. HyperText Transmission Protocol  
    c. HighText Transfer Protocol  
    d. HighText Transmission Protocol  

2. Which module is commonly used in Node.js for making HTTP requests?
    a. `http-request`  
    b. `fetch`  
    c. `axios`  
    d. `request`  

3. How do you install `axios` using npm?
    a. `npm install fetch`  
    b. `npm install request`  
    c. `npm install axios`  
    d. `npm install http-request`  

4. What is the HTTP method used to send data to a server to create or update a resource?
    a. GET  
    b. POST  
    c. PUT  
    d. DELETE  

5. In the `fetch` function, which method is used to parse the response as JSON?
    a. `response.text()`  
    b. `response.json()`  
    c. `response.parse()`  
    d. `response.data()`  

6. How do you handle errors in a `fetch` request?
    a. Using `.then()`  
    b. Using `.catch()`  
    c. Using `try...catch`  
    d. Using `.finally()`  

7. Which of the following is a correct way to send JSON data in a `fetch` POST request?
    a. `body: JSON.stringify(data)`  
    b. `data: JSON.stringify(data)`  
    c. `body: data`  
    d. `data: data`  

8. What does the `Content-Type` header specify in a POST request?
    a. The type of the response  
    b. The length of the content  
    c. The format of the request body  
    d. The URL of the server  

9. Which HTTP method is used to retrieve data from a server?
    a. GET  
    b. POST  
    c. PUT  
    d. DELETE  

10. What is the purpose of the `.then()` method in a `fetch` request?
    a. To handle errors  
    b. To parse the response  
    c. To execute code after the request completes  
    d. To set request headers  

### Answers

1. a. HyperText Transfer Protocol
2. c. `axios`
3. c. `npm install axios`
4. b. POST
5. b. `response.json()`
6. b. Using `.catch()`
7. a. `body: JSON.stringify(data)`
8. c. The format of the request body
9. a. GET
10. c. To execute code after the request completes

## Working with APIs

### Introduction
APIs (Application Programming Interfaces) allow different software applications to communicate with each other. RESTful APIs (Representational State Transfer) are a common type of API that uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

### Understanding RESTful APIs

RESTful APIs follow a set of principles that make web services easy to use and scalable. These principles include:

1. **Statelessness**: Each request from a client to a server must contain all the information needed to understand and process the request.
2. **Client-Server Architecture**: The client and server are separate entities that interact through requests and responses.
3. **Uniform Interface**: Resources are identified in requests (e.g., through URLs), and operations on these resources are performed using standard HTTP methods.

#### HTTP Methods
- **GET**: Retrieve data from the server.
- **POST**: Send data to the server to create a new resource.
- **PUT**: Update an existing resource on the server.
- **DELETE**: Remove a resource from the server.

### Interacting with RESTful APIs

To interact with a RESTful API, you make HTTP requests to specific endpoints and handle the responses.

#### Making a GET Request

Here’s an example of making a GET request to fetch data from an API:

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    console.log(data); // Output the data to the console
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

### Parsing JSON Data

Most APIs return data in JSON (JavaScript Object Notation) format, which is easy to parse and work with in JavaScript.

#### Example

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    console.log(`Title: ${data.title}`); // Output specific data to the console
    console.log(`Body: ${data.body}`);
  })
  .catch(error => {
    console.error('Error:', error); // Handle any errors
  });
```

### Real-World Application

APIs are used in various real-world applications, such as:
1. **Weather Applications**: Fetch weather data from an API to display current conditions and forecasts.
2. **Social Media Integration**: Post updates or retrieve user data from social media platforms.
3. **E-commerce**: Interact with payment gateways or inventory management systems.

### Technical End of Chapter MCQ

1. What does API stand for?
    a. Application Programming Interface  
    b. Application Processing Interface  
    c. Automated Programming Interface  
    d. Application Protocol Interface  

2. Which principle states that each request must contain all the information needed to process it?
    a. Client-Server Architecture  
    b. Statelessness  
    c. Uniform Interface  
    d. Layered System  

3. Which HTTP method is used to retrieve data from a server?
    a. GET  
    b. POST  
    c. PUT  
    d. DELETE  

4. Which HTTP method is used to create a new resource on a server?
    a. GET  
    b. POST  
    c. PUT  
    d. DELETE  

5. What format do most APIs return data in?
    a. XML  
    b. HTML  
    c. JSON  
    d. CSV  

6. How do you parse a JSON response in JavaScript?
    a. `response.text()`  
    b. `response.parse()`  
    c. `response.json()`  
    d. `response.data()`  

7. What does the `fetch` function return?
    a. A Promise  
    b. An Array  
    c. An Object  
    d. A String  

8. Which method is used to handle errors in a `fetch` request?
    a. `.then()`  
    b. `.catch()`  
    c. `.finally()`  
    d. `.error()`  

9. What does REST stand for?
    a. Representational State Transfer  
    b. Representational Service Transfer  
    c. Resource State Transfer  
    d. Resource Service Transfer  

10. What is an endpoint in the context of APIs?
    a. The server that hosts the API  
    b. The URL where an API can be accessed  
    c. The method used to access the API  
    d. The data returned by the API  

### Answers

1. a. Application Programming Interface
2. b. Statelessness
3. a. GET
4. b. POST
5. c. JSON
6. c. `response.json()`
7. a. A Promise
8. b. `.catch()`
9. a. Representational State Transfer
10. b. The URL where an API can be accessed

## Asynchronous Programming

### Introduction
Asynchronous programming allows code to run without blocking the main thread, enabling multiple operations to occur simultaneously. This is especially useful for handling tasks like network requests, file reading, or other I/O operations. There are three main ways to manage asynchronous operations in JavaScript: callbacks, promises, and async/await syntax.

### Managing Asynchronous Operations

#### Callbacks

A callback is a function passed as an argument to another function, which is then executed after some operation has been completed.

**Example with Callbacks:**

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: 'John Doe' };
    callback(data); // Invoke the callback function with the data
  }, 2000); // Simulate a 2-second delay
}

function displayData(data) {
  console.log(`ID: ${data.id}, Name: ${data.name}`);
}

fetchData(displayData); // Call fetchData with displayData as the callback
```

#### Promises

Promises provide a cleaner and more readable way to handle asynchronous operations. A promise represents an operation that will either resolve or reject in the future.

**Example with Promises:**

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { id: 1, name: 'John Doe' };
      resolve(data); // Resolve the promise with the data
    }, 2000); // Simulate a 2-second delay
  });
}

fetchData()
  .then(data => {
    console.log(`ID: ${data.id}, Name: ${data.name}`);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

#### Async/Await

Async/await syntax allows you to write asynchronous code in a more synchronous and readable manner. It is built on top of promises.

**Example with Async/Await:**

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { id: 1, name: 'John Doe' };
      resolve(data); // Resolve the promise with the data
    }, 2000); // Simulate a 2-second delay
  });
}

async function displayData() {
  try {
    const data = await fetchData(); // Wait for the promise to resolve
    console.log(`ID: ${data.id}, Name: ${data.name}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

displayData(); // Call the async function
```

### Handling API Response Data Asynchronously

Asynchronous operations are crucial when working with APIs to handle response data without blocking the main thread.

**Example with Fetch API using Async/Await:**

```javascript
async function getPost() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data = await response.json(); // Parse the JSON response
    console.log(`Title: ${data.title}`);
    console.log(`Body: ${data.body}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

getPost(); // Call the async function
```

### Real-World Application

Asynchronous programming is used in various real-world applications, such as:
1. **Web Applications**: Fetching data from a server without blocking the user interface.
2. **Mobile Apps**: Downloading files or data in the background while allowing users to interact with the app.
3. **Game Development**: Loading game assets asynchronously to ensure smooth gameplay.

### Technical End of Chapter MCQ

1. What is a callback function?
    a. A function that is executed after another function completes  
    b. A function that blocks the main thread  
    c. A function that always runs synchronously  
    d. A function that returns a promise  

2. What does a promise represent in JavaScript?
    a. An error that will occur  
    b. A value that may be available now, later, or never  
    c. A synchronous operation  
    d. A function that never resolves  

3. Which method is used to handle the resolved value of a promise?
    a. `.catch()`  
    b. `.then()`  
    c. `.finally()`  
    d. `.done()`  

4. How do you create a promise in JavaScript?
    a. `new Promise()`  
    b. `Promise.create()`  
    c. `promise()`  
    d. `Promise()`  

5. What keyword is used to pause the execution of an async function until a promise is resolved?
    a. `wait`  
    b. `halt`  
    c. `pause`  
    d. `await`  

6. Which of the following is true about async/await?
    a. It makes asynchronous code run synchronously  
    b. It is built on top of callbacks  
    c. It is built on top of promises  
    d. It is a new type of promise  

7. How do you handle errors in an async function?
    a. Using `.then()`  
    b. Using `.finally()`  
    c. Using `try...catch`  
    d. Using `.error()`  

8. What does the `fetch` function return?
    a. A callback  
    b. An object  
    c. A promise  
    d. A string  

9. In the context of asynchronous programming, what does "non-blocking" mean?
    a. The code stops executing until the operation completes  
    b. The code continues executing while the operation is performed in the background  
    c. The operation is performed synchronously  
    d. The operation never completes  

10. What is the main advantage of using async/await over promises?
    a. It makes the code run faster  
    b. It allows for synchronous-like code structure  
    c. It eliminates the need for error handling  
    d. It uses less memory  

### Answers

1. a. A function that is executed after another function completes
2. b. A value that may be available now, later, or never
3. b. `.then()`
4. a. `new Promise()`
5. d. `await`
6. c. It is built on top of promises
7. c. Using `try...catch`
8. c. A promise
9. b. The code continues executing while the operation is performed in the background
10. b. It allows for synchronous-like code structure

## Command Line Arguments in Node.js

### Introduction
Command line arguments are parameters passed to a program when it is executed. In Node.js, these arguments can be accessed using the `process.argv` array. This feature allows scripts to accept input directly from the command line, enabling dynamic behavior based on user input.

### Understanding `process.argv`

The `process.argv` property is an array containing the command line arguments passed when the Node.js process was launched. The first element is the path to the Node.js executable, the second element is the path to the JavaScript file being executed, and the subsequent elements are the command line arguments.

**Example:**

If you run the following command:
```bash
node script.js arg1 arg2 arg3
```
The `process.argv` array would look like this:
```javascript
[
  '/path/to/node',
  '/path/to/script.js',
  'arg1',
  'arg2',
  'arg3'
]
```

### Accessing Command Line Arguments

To access the command line arguments, you can simply reference the elements of the `process.argv` array.

**Example:**

```javascript
// script.js
const args = process.argv.slice(2); // Remove the first two elements
console.log(args); // Output: ['arg1', 'arg2', 'arg3']
```

### Using Command Line Arguments in Scripts

You can use command line arguments to modify the behavior of your scripts.

**Example: A Simple Calculator**

```javascript
// calculator.js
const args = process.argv.slice(2); // Remove the first two elements

if (args.length < 3) {
  console.log('Usage: node calculator.js <num1> <operation> <num2>');
  process.exit(1);
}

const num1 = parseFloat(args[0]);
const operation = args[1];
const num2 = parseFloat(args[2]);

let result;

switch (operation) {
  case '+':
    result = num1 + num2;
    break;
  case '-':
    result = num1 - num2;
    break;
  case '*':
    result = num1 * num2;
    break;
  case '/':
    result = num1 / num2;
    break;
  default:
    console.log('Invalid operation. Use +, -, *, or /.');
    process.exit(1);
}

console.log(`Result: ${result}`);
```

You can run the calculator script with command line arguments:
```bash
node calculator.js 5 + 3
```

### Real-World Application

Command line arguments are useful in various real-world applications, such as:
1. **Automation Scripts**: Pass different parameters to automate tasks like file processing or data analysis.
2. **Build Tools**: Customize build processes by passing options to scripts that compile or bundle code.
3. **Configuration Management**: Provide different configurations to a server or application without hardcoding values.

### Technical End of Chapter MCQ

1. What does the `process.argv` array contain?
    a. Environment variables  
    b. Command line arguments  
    c. Node.js settings  
    d. System properties  

2. What is the first element of the `process.argv` array?
    a. The script name  
    b. The first argument  
    c. The Node.js executable path  
    d. The operating system  

3. How do you access the command line arguments excluding the first two elements?
    a. `process.argv.slice(1)`  
    b. `process.argv.slice(2)`  
    c. `process.argv.shift()`  
    d. `process.argv.pop()`  

4. Which method converts a string to a floating-point number in JavaScript?
    a. `parseInt()`  
    b. `Number()`  
    c. `parseFloat()`  
    d. `toFloat()`  

5. What will `process.argv[2]` return when running `node script.js 10`?
    a. `node`  
    b. `script.js`  
    c. `10`  
    d. `undefined`  

6. What does `process.exit(1)` do?
    a. Terminates the script with a success code  
    b. Continues the script execution  
    c. Terminates the script with an error code  
    d. Restarts the script  

7. In a command `node app.js hello world`, what will `process.argv[3]` output?
    a. `app.js`  
    b. `hello`  
    c. `world`  
    d. `undefined`  

8. How do you check the number of command line arguments passed to a script?
    a. `process.argv.length`  
    b. `process.argv.size`  
    c. `process.argv.count`  
    d. `process.argv.number`  

9. What is the result of `parseFloat('3.14')`?
    a. `3`  
    b. `'3.14'`  
    c. `3.14`  
    d. `NaN`  

10. Which of the following is a valid use of command line arguments in a Node.js script?
    a. To change the script's filename  
    b. To modify the script's execution environment  
    c. To pass dynamic input to the script  
    d. To change the Node.js version  

### Answers

1. b. Command line arguments
2. c. The Node.js executable path
3. b. `process.argv.slice(2)`
4. c. `parseFloat()`
5. c. `10`
6. c. Terminates the script with an error code
7. c. `world`
8. a. `process.argv.length`
9. c. `3.14`
10. c. To pass dynamic input to the script

## Array Manipulation and Iteration

### Introduction
Arrays are fundamental data structures in JavaScript used to store multiple values. Understanding how to manipulate and iterate over arrays is crucial for effective programming. This section covers essential array methods and iteration techniques to format and display data, such as character names.

### Basic Array Operations

#### Creating an Array

An array can be created using square brackets `[]`.

**Example:**

```javascript
let characters = ['Alice', 'Bob', 'Charlie', 'Diana'];
console.log(characters); // Output: ['Alice', 'Bob', 'Charlie', 'Diana']
```

#### Accessing Array Elements

Array elements can be accessed using their index, starting from 0.

**Example:**

```javascript
console.log(characters[0]); // Output: 'Alice'
console.log(characters[2]); // Output: 'Charlie'
```

### Iterating Over Arrays

#### Using `for` Loop

The `for` loop is a traditional way to iterate over arrays.

**Example:**

```javascript
for (let i = 0; i < characters.length; i++) {
  console.log(characters[i]);
}
```

#### Using `forEach` Method

The `forEach` method executes a provided function once for each array element.

**Example:**

```javascript
characters.forEach(function(character) {
  console.log(character);
});
```

#### Using `map` Method

The `map` method creates a new array with the results of calling a provided function on every element.

**Example:**

```javascript
let upperCaseCharacters = characters.map(function(character) {
  return character.toUpperCase();
});
console.log(upperCaseCharacters); // Output: ['ALICE', 'BOB', 'CHARLIE', 'DIANA']
```

#### Using `filter` Method

The `filter` method creates a new array with all elements that pass the test implemented by the provided function.

**Example:**

```javascript
let filteredCharacters = characters.filter(function(character) {
  return character.startsWith('C');
});
console.log(filteredCharacters); // Output: ['Charlie']
```

### Array Manipulation

#### Adding Elements

Elements can be added to the end of an array using `push`.

**Example:**

```javascript
characters.push('Eve');
console.log(characters); // Output: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
```

#### Removing Elements

Elements can be removed from the end of an array using `pop`.

**Example:**

```javascript
characters.pop();
console.log(characters); // Output: ['Alice', 'Bob', 'Charlie', 'Diana']
```

#### Modifying Elements

Array elements can be modified directly using their index.

**Example:**

```javascript
characters[1] = 'Bobby';
console.log(characters); // Output: ['Alice', 'Bobby', 'Charlie', 'Diana']
```

### Real-World Application

Array manipulation and iteration are used in various real-world applications, such as:
1. **Data Processing**: Filtering and formatting data before displaying it in a web application.
2. **Inventory Management**: Keeping track of items in a store and updating stock levels.
3. **User Interfaces**: Displaying lists of users, products, or other items dynamically.

### Example: Formatting and Displaying Character Names

**Example:**

```javascript
let characters = ['Alice', 'Bob', 'Charlie', 'Diana'];

// Format and display character names in a sentence
let formattedCharacters = characters.map(function(character, index) {
  return `${index + 1}. ${character}`;
});

formattedCharacters.forEach(function(character) {
  console.log(character);
});

// Output:
// 1. Alice
// 2. Bob
// 3. Charlie
// 4. Diana
```

### Technical End of Chapter MCQ

1. What is the index of the first element in an array?
    a. 1  
    b. 0  
    c. -1  
    d. 2  

2. Which method is used to iterate over each element of an array and execute a function?
    a. `for`  
    b. `while`  
    c. `forEach`  
    d. `map`  

3. How do you add an element to the end of an array?
    a. `pop`  
    b. `push`  
    c. `shift`  
    d. `unshift`  

4. What does the `filter` method return?
    a. The first element that matches the condition  
    b. A new array with elements that match the condition  
    c. The length of the array  
    d. A boolean value  

5. Which method creates a new array with the results of calling a function on every element?
    a. `forEach`  
    b. `filter`  
    c. `map`  
    d. `reduce`  

6. How do you remove the last element from an array?
    a. `pop`  
    b. `push`  
    c. `shift`  
    d. `unshift`  

7. How can you modify the second element of an array `arr` to be 'New Value'?
    a. `arr[1] = 'New Value'`  
    b. `arr[2] = 'New Value'`  
    c. `arr[0] = 'New Value'`  
    d. `arr[3] = 'New Value'`  

8. What does the `map` method return?
    a. The original array  
    b. A new array with transformed elements  
    c. The length of the array  
    d. A boolean value  

9. What will `characters[characters.length - 1]` return?
    a. The first element  
    b. The middle element  
    c. The last element  
    d. Undefined  

10. Which method would you use to execute a function for each element and also create a new array based on the function's result?
    a. `forEach`  
    b. `map`  
    c. `filter`  
    d. `reduce`  

### Answers

1. b. 0
2. c. `forEach`
3. b. `push`
4. b. A new array with elements that match the condition
5. c. `map`
6. a. `pop`
7. a. `arr[1] = 'New Value'`
8. b. A new array with transformed elements
9. c. The last element
10. b. `map`

## Star Wars Characters

### Introduction
In this note, we will learn how to write a script that prints all characters of a specified Star Wars movie. The script will take the movie ID as a positional argument, fetch data from the Star Wars API, and display each character name in the order they appear in the "characters" list of the /films/ endpoint.

### Requirements
1. **Movie ID as a Positional Argument**: The first positional argument passed to the script will be the Movie ID.
2. **Display Character Names**: The script should print one character name per line.
3. **Star Wars API**: The script must use the Star Wars API.
4. **Request Module**: The script must use the `request` module to make HTTP requests.

### Setup

1. **Install the `request` module**:
    ```bash
    npm install request
    ```

2. **Star Wars API Endpoint**:
    - **Films Endpoint**: `https://swapi-api.hbtn.io/api/films/<MOVIE_ID>/`

### Script

Below is a detailed script to achieve the task:

```javascript
#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
```

### Explanation

1. **Importing the `request` module**:
    ```javascript
    const request = require('request');
    ```

2. **Getting the Movie ID from Command Line Arguments**:
    ```javascript
    const movieId = process.argv[2];
    ```

3. **Constructing the API URL for the Movie**:
    ```javascript
    const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
    ```

4. **Making the Initial Request to the Films Endpoint**:
    ```javascript
    request(apiUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      characters.forEach((characterUrl) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            console.error('Error:', error);
            return;
          }
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        });
      });
    });
    ```

    - **Parse Film Data**: Parse the response body to get the film data.
    - **Extract Characters**: Extract the list of character URLs from the film data.
    - **Fetch and Display Character Names**: For each character URL, make another request to get the character data and print the character name.

### Real-World Application

Fetching and displaying data from APIs is a common task in web development. This script demonstrates how to make sequential API requests and process the data in a real-world scenario.

### Technical End of Chapter MCQ

1. What module is used to make HTTP requests in the script?
    a. `http`
    b. `https`
    c. `request`
    d. `axios`

2. How is the Movie ID passed to the script?
    a. As an environment variable
    b. As a query parameter
    c. As a positional argument
    d. As a header

3. What is the base URL for the Star Wars API?
    a. `https://api.starwars.com`
    b. `https://swapi.dev`
    c. `https://swapi-api.hbtn.io/api/`
    d. `https://swapi.co`

4. What type of data format is returned by the Star Wars API?
    a. XML
    b. JSON
    c. CSV
    d. HTML

5. What does the `request` function's callback parameter `body` contain?
    a. The request headers
    b. The response status code
    c. The response body
    d. The request method

6. How are the character URLs accessed in the script?
    a. From the `title` field of the film data
    b. From the `characters` field of the film data
    c. From the `director` field of the film data
    d. From the `planets` field of the film data

7. What method is used to parse the JSON response body?
    a. `JSON.stringify()`
    b. `JSON.parse()`
    c. `JSON.decode()`
    d. `JSON.read()`

8. How are multiple character requests handled in the script?
    a. Using a `for` loop
    b. Using a `while` loop
    c. Using `forEach` method
    d. Using `map` method

9. What does the script do if there is an error in the HTTP request?
    a. Logs the error to the console and stops
    b. Retries the request
    c. Ignores the error and continues
    d. Returns a default value

10. What will the script output if the Movie ID is invalid?
    a. "Invalid Movie ID"
    b. "Movie not found"
    c. An error message
    d. "No characters found"

### Answers

1. c. `request`
2. c. As a positional argument
3. c. `https://swapi-api.hbtn.io/api/`
4. b. JSON
5. c. The response body
6. b. From the `characters` field of the film data
7. b. `JSON.parse()`
8. c. Using `forEach` method
9. a. Logs the error to the console and stops
10. c. An error message
