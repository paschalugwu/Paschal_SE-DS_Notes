## Running JavaScript Using Node.js

Node.js is a powerful tool that allows you to run JavaScript outside of a web browser. It uses the V8 JavaScript engine, which is the same engine used by Google Chrome, to execute code on the server side. Here's a step-by-step guide on how to run JavaScript using Node.js, along with some examples and practical applications.

### Installing Node.js

1. **Download and Install Node.js**:
   - Go to the [Node.js website](https://nodejs.org/) and download the installer for your operating system.
   - Run the installer and follow the instructions to install Node.js.

2. **Verify Installation**:
   - Open your terminal (Command Prompt on Windows, Terminal on macOS or Linux).
   - Type `node -v` and press Enter. You should see the version number of Node.js you installed.
   - Type `npm -v` to check the version of npm (Node Package Manager), which is installed along with Node.js.

### Running Your First JavaScript Program

1. **Create a JavaScript File**:
   - Create a new file named `app.js` in a directory of your choice.

2. **Write JavaScript Code**:
   - Open `app.js` in a text editor and write the following code:
     ```javascript
     console.log('Hello, Node.js!');
     ```

3. **Run the JavaScript File**:
   - In your terminal, navigate to the directory where `app.js` is located.
   - Run the following command:
     ```bash
     node app.js
     ```
   - You should see the output `Hello, Node.js!` in the terminal.

### Real-World Applications

#### Example 1: Simple Web Server

Node.js is often used to build web servers. Here's a simple example of a web server that responds with "Hello, World!" for every request:

1. **Create a new file named `server.js`** and write the following code:
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');
     res.end('Hello, World!\n');
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```

2. **Run the server**:
   - In your terminal, navigate to the directory where `server.js` is located.
   - Run the following command:
     ```bash
     node server.js
     ```
   - Open your web browser and go to `http://127.0.0.1:3000/`. You should see "Hello, World!".

#### Example 2: Reading a File

Node.js can also be used to read files. Here's an example that reads the content of a file and logs it to the console:

1. **Create a new file named `readFile.js`** and write the following code:
   ```javascript
   const fs = require('fs');

   fs.readFile('example.txt', 'utf8', (err, data) => {
     if (err) {
       console.error(err);
       return;
     }
     console.log(data);
   });
   ```

2. **Create a file named `example.txt`** in the same directory and add some text to it.

3. **Run the script**:
   - In your terminal, navigate to the directory where `readFile.js` is located.
   - Run the following command:
     ```bash
     node readFile.js
     ```
   - You should see the content of `example.txt` logged to the console.

### End of Chapter Quiz

1. What is Node.js?
   - a) A JavaScript library for building user interfaces
   - b) A tool for running JavaScript on the server side
   - c) A version control system
   - d) A CSS framework

2. Which command verifies the Node.js installation?
   - a) node --verify
   - b) node -check
   - c) node -v
   - d) node --version

3. What is the purpose of npm in Node.js?
   - a) To manage Node.js versions
   - b) To manage packages and dependencies
   - c) To compile JavaScript code
   - d) To run JavaScript code

4. How do you run a JavaScript file named `script.js` using Node.js?
   - a) node run script.js
   - b) node script.js
   - c) npm script.js
   - d) nodejs script.js

5. What does the `require` function do in Node.js?
   - a) It compiles JavaScript code
   - b) It imports modules or packages
   - c) It runs the Node.js server
   - d) It manages dependencies

6. Which module is used to create a web server in Node.js?
   - a) fs
   - b) http
   - c) path
   - d) os

7. What is the output of the following code?
   ```javascript
   console.log('Hello, Node.js!');
   ```
   - a) Hello, World!
   - b) Hello, Node.js!
   - c) Hello, JavaScript!
   - d) Hello, Server!

8. How do you read the content of a file in Node.js?
   - a) Using the `http` module
   - b) Using the `fs` module
   - c) Using the `read` module
   - d) Using the `file` module

9. What is the correct syntax to set the Content-Type header in a Node.js HTTP response?
   - a) `res.setHeader('Content', 'text/plain');`
   - b) `res.setContentType('text/plain');`
   - c) `res.setHeader('Content-Type', 'text/plain');`
   - d) `res.setType('Content', 'text/plain');`

10. Which of the following is true about Node.js?
    - a) It can only be used to build web servers
    - b) It is a programming language
    - c) It allows running JavaScript on the server side
    - d) It is a database management system

### Answers

1. b) A tool for running JavaScript on the server side
2. c) node -v
3. b) To manage packages and dependencies
4. b) node script.js
5. b) It imports modules or packages
6. b) http
7. b) Hello, Node.js!
8. b) Using the `fs` module
9. c) `res.setHeader('Content-Type', 'text/plain');`
10. c) It allows running JavaScript on the server side

## Using Node.js Modules

Node.js modules are a fundamental part of building applications with Node.js. They allow you to organize your code into reusable pieces and to use external libraries to add functionality to your application. Here’s a detailed guide on how to use Node.js modules, along with examples and practical applications.

### Understanding Node.js Modules

Node.js has a built-in module system. Modules are essentially JavaScript files that export code for use in other JavaScript files. There are three types of modules in Node.js:
1. **Core Modules**: These are built-in modules provided by Node.js, such as `http`, `fs`, and `path`.
2. **Local Modules**: These are custom modules created by the developer.
3. **Third-Party Modules**: These are modules installed via npm (Node Package Manager).

### Using Core Modules

Node.js comes with a set of core modules that you can use without installing anything extra. Here are some examples:

#### Example 1: Using the `fs` Module

The `fs` (file system) module allows you to interact with the file system.

1. **Create a file named `fileExample.js`** and write the following code:
   ```javascript
   const fs = require('fs');

   fs.readFile('example.txt', 'utf8', (err, data) => {
     if (err) {
       console.error(err);
       return;
     }
     console.log(data);
   });
   ```

2. **Create a file named `example.txt`** in the same directory and add some text to it.

3. **Run the script**:
   ```bash
   node fileExample.js
   ```

#### Example 2: Using the `http` Module

The `http` module allows you to create a web server.

1. **Create a file named `httpExample.js`** and write the following code:
   ```javascript
   const http = require('http');

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');
     res.end('Hello, World!\n');
   });

   server.listen(3000, '127.0.0.1', () => {
     console.log('Server running at http://127.0.0.1:3000/');
   });
   ```

2. **Run the script**:
   ```bash
   node httpExample.js
   ```

3. **Open your web browser** and go to `http://127.0.0.1:3000/`. You should see "Hello, World!".

### Creating and Using Local Modules

You can create your own modules to organize your code better.

#### Example 3: Creating a Local Module

1. **Create a file named `math.js`** and write the following code:
   ```javascript
   function add(a, b) {
     return a + b;
   }

   function subtract(a, b) {
     return a - b;
   }

   module.exports = { add, subtract };
   ```

2. **Create a file named `app.js`** and write the following code to use the `math` module:
   ```javascript
   const math = require('./math');

   console.log(`2 + 3 = ${math.add(2, 3)}`);
   console.log(`5 - 2 = ${math.subtract(5, 2)}`);
   ```

3. **Run the script**:
   ```bash
   node app.js
   ```

### Using Third-Party Modules

Third-party modules are installed using npm. You can use these modules to add various functionalities to your application.

#### Example 4: Using a Third-Party Module

1. **Initialize a new Node.js project** (if not already done):
   ```bash
   npm init -y
   ```

2. **Install the `axios` module**:
   ```bash
   npm install axios
   ```

3. **Create a file named `fetchData.js`** and write the following code:
   ```javascript
   const axios = require('axios');

   axios.get('https://jsonplaceholder.typicode.com/posts/1')
     .then(response => {
       console.log(response.data);
     })
     .catch(error => {
       console.error(error);
     });
   ```

4. **Run the script**:
   ```bash
   node fetchData.js
   ```

### End of Chapter Quiz

1. What is a module in Node.js?
   - a) A database
   - b) A reusable piece of code
   - c) A JavaScript function
   - d) A configuration file

2. Which of the following is a core module in Node.js?
   - a) lodash
   - b) axios
   - c) fs
   - d) express

3. How do you import a core module in Node.js?
   - a) import 'fs'
   - b) include 'fs'
   - c) require('fs')
   - d) using 'fs'

4. Which command is used to install a third-party module in Node.js?
   - a) node install <module>
   - b) npm install <module>
   - c) install <module>
   - d) require <module>

5. How do you export functions from a local module in Node.js?
   - a) export { functionName }
   - b) module.export = { functionName }
   - c) module.exports = { functionName }
   - d) exports.functionName

6. Which of the following modules allows you to create a web server?
   - a) http
   - b) fs
   - c) os
   - d) path

7. What is the output of the following code if `math.js` exports an `add` function?
   ```javascript
   const math = require('./math');
   console.log(math.add(1, 2));
   ```
   - a) 1
   - b) 2
   - c) 3
   - d) Error

8. What is the purpose of the `axios` module in Node.js?
   - a) To handle file operations
   - b) To make HTTP requests
   - c) To create web servers
   - d) To manage databases

9. How do you initialize a new Node.js project?
   - a) node init
   - b) npm init
   - c) node create
   - d) npm create

10. Which method is used to read the content of a file in Node.js?
    - a) fs.readFile
    - b) http.readFile
    - c) path.readFile
    - d) os.readFile

### Answers

1. b) A reusable piece of code
2. c) fs
3. c) require('fs')
4. b) npm install <module>
5. c) module.exports = { functionName }
6. a) http
7. c) 3
8. b) To make HTTP requests
9. b) npm init
10. a) fs.readFile

## Using Specific Node.js Module to Read Files

Node.js provides several built-in modules to perform various tasks, one of which is the `fs` (file system) module. The `fs` module allows you to interact with the file system, enabling you to read, write, and manipulate files and directories. Here's a detailed guide on how to use the `fs` module to read files, along with examples and practical applications.

### Installing Node.js

Before you start, ensure that Node.js is installed on your system. You can download it from the [Node.js website](https://nodejs.org/).

### Reading Files with the `fs` Module

The `fs` module provides multiple methods to read files, including `fs.readFile` and `fs.readFileSync`.

#### Example 1: Using `fs.readFile` (Asynchronous)

The `fs.readFile` method reads the file asynchronously. This means that Node.js will continue executing the rest of your code while it reads the file.

1. **Create a file named `readFileAsync.js`** and write the following code:
   ```javascript
   const fs = require('fs');

   fs.readFile('example.txt', 'utf8', (err, data) => {
     if (err) {
       console.error('Error reading file:', err);
       return;
     }
     console.log('File content:', data);
   });
   ```

2. **Create a file named `example.txt`** in the same directory and add some text to it.

3. **Run the script**:
   ```bash
   node readFileAsync.js
   ```
   - You should see the content of `example.txt` logged to the console.

#### Example 2: Using `fs.readFileSync` (Synchronous)

The `fs.readFileSync` method reads the file synchronously. This means that Node.js will wait until the file is read before continuing with the rest of the code.

1. **Create a file named `readFileSync.js`** and write the following code:
   ```javascript
   const fs = require('fs');

   try {
     const data = fs.readFileSync('example.txt', 'utf8');
     console.log('File content:', data);
   } catch (err) {
     console.error('Error reading file:', err);
   }
   ```

2. **Run the script**:
   ```bash
   node readFileSync.js
   ```
   - You should see the content of `example.txt` logged to the console.

### Real-World Applications

#### Example 3: Reading Configuration Files

In real-world projects, you might need to read configuration files to set up your application.

1. **Create a file named `config.json`** with the following content:
   ```json
   {
     "host": "localhost",
     "port": 8080
   }
   ```

2. **Create a file named `readConfig.js`** and write the following code:
   ```javascript
   const fs = require('fs');

   fs.readFile('config.json', 'utf8', (err, data) => {
     if (err) {
       console.error('Error reading config file:', err);
       return;
     }
     const config = JSON.parse(data);
     console.log('Config:', config);
   });
   ```

3. **Run the script**:
   ```bash
   node readConfig.js
   ```
   - You should see the content of `config.json` parsed and logged to the console.

### End of Chapter Quiz

1. What is the purpose of the `fs` module in Node.js?
   - a) To handle HTTP requests
   - b) To interact with the file system
   - c) To manage databases
   - d) To create web servers

2. Which method reads a file asynchronously in Node.js?
   - a) fs.readFileSync
   - b) fs.readFile
   - c) fs.readFileAsync
   - d) fs.read

3. What is the correct way to handle errors when using `fs.readFile`?
   - a) Using a try-catch block
   - b) Checking the error argument in the callback
   - c) Using a promise
   - d) Ignoring the error

4. Which of the following is true about `fs.readFileSync`?
   - a) It reads a file asynchronously
   - b) It reads a file synchronously
   - c) It requires a callback function
   - d) It doesn't block the event loop

5. What is the encoding parameter used for in `fs.readFile`?
   - a) To specify the file format
   - b) To specify the character encoding
   - c) To specify the file path
   - d) To specify the file name

6. How do you import the `fs` module in a Node.js file?
   - a) import 'fs'
   - b) include 'fs'
   - c) require('fs')
   - d) using 'fs'

7. What does the following code output if `example.txt` contains "Hello, Node.js"?
   ```javascript
   const fs = require('fs');

   fs.readFile('example.txt', 'utf8', (err, data) => {
     if (err) {
       console.error('Error reading file:', err);
       return;
     }
     console.log('File content:', data);
   });
   ```
   - a) Error reading file: [Error message]
   - b) Hello, Node.js
   - c) undefined
   - d) null

8. What is a common use case for reading files in Node.js applications?
   - a) Sending HTTP requests
   - b) Serving web pages
   - c) Reading configuration files
   - d) Managing databases

9. What happens if you try to read a file that doesn't exist using `fs.readFileSync`?
   - a) The code continues execution without errors
   - b) An error is thrown and the execution stops
   - c) The function returns null
   - d) A warning is logged to the console

10. How do you parse a JSON file after reading it using `fs.readFile`?
    - a) Using the `JSON.parse` method
    - b) Using the `JSON.stringify` method
    - c) Using the `JSON.read` method
    - d) Using the `JSON.convert` method

### Answers

1. b) To interact with the file system
2. b) fs.readFile
3. b) Checking the error argument in the callback
4. b) It reads a file synchronously
5. b) To specify the character encoding
6. c) require('fs')
7. b) Hello, Node.js
8. c) Reading configuration files
9. b) An error is thrown and the execution stops
10. a) Using the `JSON.parse` method

## Using `process` to Access Command Line Arguments and the Environment

Node.js provides the `process` object to interact with the current Node.js process. This object includes various properties and methods that allow you to access command line arguments and environment variables. Understanding how to use these can be crucial in real-world projects, especially for configuring applications and handling inputs dynamically.

### Accessing Command Line Arguments

Command line arguments are the values passed to your Node.js script when you run it from the terminal. You can access these arguments using the `process.argv` array.

#### Example 1: Basic Command Line Arguments

1. **Create a file named `args.js`** and write the following code:
   ```javascript
   // The first two elements are 'node' and the script name
   const args = process.argv.slice(2);

   console.log('Command line arguments:', args);
   ```

2. **Run the script with arguments**:
   ```bash
   node args.js arg1 arg2 arg3
   ```
   - You should see the output:
     ```
     Command line arguments: [ 'arg1', 'arg2', 'arg3' ]
     ```

### Accessing Environment Variables

Environment variables are key-value pairs used to configure applications. You can access these variables using `process.env`.

#### Example 2: Basic Environment Variables

1. **Create a file named `env.js`** and write the following code:
   ```javascript
   const user = process.env.USER || 'unknown';
   const home = process.env.HOME || 'not defined';

   console.log(`User: ${user}`);
   console.log(`Home Directory: ${home}`);
   ```

2. **Run the script**:
   ```bash
   node env.js
   ```
   - You should see the output displaying your environment variables.

3. **Set an environment variable and run the script**:
   ```bash
   USER=John node env.js
   ```
   - You should see the output:
     ```
     User: John
     Home Directory: [Your Home Directory]
     ```

### Practical Application in Real-World Projects

#### Example 3: Configuration Management

In real-world applications, you might need to read configuration settings from environment variables.

1. **Create a file named `config.js`** and write the following code:
   ```javascript
   const config = {
     host: process.env.DB_HOST || 'localhost',
     port: process.env.DB_PORT || 5432,
     user: process.env.DB_USER || 'user',
     password: process.env.DB_PASSWORD || 'password',
   };

   console.log('Database Configuration:', config);
   ```

2. **Run the script with environment variables**:
   ```bash
   DB_HOST=127.0.0.1 DB_USER=admin node config.js
   ```
   - You should see the output:
     ```
     Database Configuration: { host: '127.0.0.1', port: 5432, user: 'admin', password: 'password' }
     ```

### End of Chapter Quiz

1. What does `process.argv` return in Node.js?
   - a) An object of command line arguments
   - b) An array of command line arguments
   - c) A string of command line arguments
   - d) A number of command line arguments

2. What are the first two elements of `process.argv`?
   - a) The first argument and the second argument
   - b) The script name and the first argument
   - c) `node` and the script name
   - d) `node` and the first argument

3. How do you access environment variables in Node.js?
   - a) Using `process.env`
   - b) Using `process.argv`
   - c) Using `process.envVars`
   - d) Using `process.environment`

4. How do you set an environment variable in the terminal before running a Node.js script?
   - a) `set VAR_NAME=value`
   - b) `export VAR_NAME=value`
   - c) `env VAR_NAME=value`
   - d) `VAR_NAME=value`

5. What does the `||` operator do in the context of `process.env`?
   - a) It throws an error if the environment variable is not set
   - b) It sets a default value if the environment variable is not set
   - c) It concatenates environment variables
   - d) It removes the environment variable

6. What will be the output of the following code if `USER` is not set in the environment?
   ```javascript
   const user = process.env.USER || 'unknown';
   console.log(user);
   ```
   - a) null
   - b) undefined
   - c) USER
   - d) unknown

7. How can you pass multiple command line arguments to a Node.js script?
   - a) Separate them with commas
   - b) Pass them as a single string
   - c) Separate them with spaces
   - d) Use a configuration file

8. Which method would you use to access the third command line argument in a Node.js script?
   - a) `process.argv[1]`
   - b) `process.argv[2]`
   - c) `process.argv[3]`
   - d) `process.argv[4]`

9. What is the primary use of environment variables in Node.js applications?
   - a) To store user input
   - b) To configure the application
   - c) To debug the application
   - d) To handle errors

10. In the following code, what will be the value of `port` if `DB_PORT` is set to 3000?
    ```javascript
    const port = process.env.DB_PORT || 5432;
    console.log(port);
    ```
    - a) 3000
    - b) 5432
    - c) DB_PORT
    - d) undefined

### Answers

1. b) An array of command line arguments
2. c) `node` and the script name
3. a) Using `process.env`
4. d) `VAR_NAME=value`
5. b) It sets a default value if the environment variable is not set
6. d) unknown
7. c) Separate them with spaces
8. c) `process.argv[3]`
9. b) To configure the application
10. a) 3000

## Creating a Small HTTP Server Using Node.js

Node.js allows you to create an HTTP server with just a few lines of code. This server can handle HTTP requests and send responses back to the client, making it a fundamental building block for web applications. Here’s a detailed guide on how to create a small HTTP server using Node.js, complete with examples and practical applications.

### Setting Up Node.js

Before you start, ensure Node.js is installed on your system. You can download it from the [Node.js website](https://nodejs.org/).

### Creating an HTTP Server

The `http` module in Node.js provides the necessary functionality to create an HTTP server. Below is a step-by-step guide on creating a simple server.

#### Example 1: Basic HTTP Server

1. **Create a file named `server.js`** and write the following code:
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');
     res.end('Hello, World!\n');
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```

2. **Run the server**:
   ```bash
   node server.js
   ```

3. **Open your web browser** and go to `http://127.0.0.1:3000/`. You should see "Hello, World!".

### Handling Different Routes

You can extend the basic server to handle different routes and send different responses based on the request URL.

#### Example 2: Handling Routes

1. **Update `server.js`** to handle multiple routes:
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');

     if (req.url === '/') {
       res.end('Welcome to the Home Page!\n');
     } else if (req.url === '/about') {
       res.end('Welcome to the About Page!\n');
     } else {
       res.statusCode = 404;
       res.end('Page not found\n');
     }
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node server.js
   ```

3. **Test different routes** by visiting `http://127.0.0.1:3000/`, `http://127.0.0.1:3000/about`, and `http://127.0.0.1:3000/unknown`.

### Serving HTML Content

Instead of plain text, you can serve HTML content to make the responses more informative and visually appealing.

#### Example 3: Serving HTML Content

1. **Update `server.js`** to serve HTML content:
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/html');

     if (req.url === '/') {
       res.end('<h1>Welcome to the Home Page!</h1>');
     } else if (req.url === '/about') {
       res.end('<h1>Welcome to the About Page!</h1>');
     } else {
       res.statusCode = 404;
       res.end('<h1>Page not found</h1>');
     }
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node server.js
   ```

3. **Test different routes** again to see the HTML content.

### Real-World Application

#### Example 4: Basic API Server

You can also use Node.js to create a basic API server that sends JSON responses.

1. **Update `server.js`** to serve JSON content:
   ```javascript
   const http = require('http');

   const hostname = '127.0.0.1';
   const port = 3000;

   const server = http.createServer((req, res) => {
     res.setHeader('Content-Type', 'application/json');

     if (req.url === '/') {
       res.statusCode = 200;
       res.end(JSON.stringify({ message: 'Welcome to the Home Page!' }));
     } else if (req.url === '/about') {
       res.statusCode = 200;
       res.end(JSON.stringify({ message: 'Welcome to the About Page!' }));
     } else {
       res.statusCode = 404;
       res.end(JSON.stringify({ error: 'Page not found' }));
     }
   });

   server.listen(port, hostname, () => {
     console.log(`Server running at http://${hostname}:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node server.js
   ```

3. **Test the API** by using a tool like Postman or simply visiting the routes in your browser.

### End of Chapter Quiz

1. Which module is used to create an HTTP server in Node.js?
   - a) url
   - b) http
   - c) net
   - d) fs

2. What method is used to create the server in Node.js?
   - a) http.create()
   - b) http.createServer()
   - c) http.startServer()
   - d) http.listen()

3. What is the default hostname used in the example?
   - a) 127.0.0.1
   - b) localhost
   - c) 192.168.1.1
   - d) 0.0.0.0

4. What is the default port number used in the example?
   - a) 8000
   - b) 8080
   - c) 3000
   - d) 5000

5. How do you set the response status code in Node.js?
   - a) res.setStatusCode()
   - b) res.status()
   - c) res.statusCode
   - d) res.code()

6. How do you set the response header in Node.js?
   - a) res.setHeader()
   - b) res.header()
   - c) res.set()
   - d) res.headers()

7. What content type is set to serve plain text responses?
   - a) text/html
   - b) text/plain
   - c) application/json
   - d) text/xml

8. How do you handle different routes in a Node.js HTTP server?
   - a) Using if-else statements
   - b) Using switch-case statements
   - c) Using a routing library
   - d) All of the above

9. What does the `res.end()` method do in Node.js?
   - a) Starts the response
   - b) Sends the response and ends it
   - c) Ends the request
   - d) None of the above

10. What will the following code output if you visit `http://127.0.0.1:3000/`?
    ```javascript
    const http = require('http');

    const hostname = '127.0.0.1';
    const port = 3000;

    const server = http.createServer((req, res) => {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Hello, Node.js!\n');
    });

    server.listen(port, hostname, () => {
      console.log(`Server running at http://${hostname}:${port}/`);
    });
    ```
    - a) Error
    - b) Welcome to Node.js
    - c) Hello, Node.js!
    - d) Hello, World!

### Answers

1. b) http
2. b) http.createServer()
3. a) 127.0.0.1
4. c) 3000
5. c) res.statusCode
6. a) res.setHeader()
7. b) text/plain
8. d) All of the above
9. b) Sends the response and ends it
10. c) Hello, Node.js!

## Creating a Small HTTP Server Using Express.js

Express.js is a popular web application framework for Node.js that simplifies the process of building robust and scalable web servers. This guide will demonstrate how to create a small HTTP server using Express.js, complete with practical examples and applications.

### Setting Up Express.js

Before you start, ensure you have Node.js installed on your system. Then, you can install Express.js using npm (Node Package Manager).

1. **Initialize a new Node.js project**:
   ```bash
   mkdir express-server
   cd express-server
   npm init -y
   ```

2. **Install Express.js**:
   ```bash
   npm install express
   ```

### Creating an HTTP Server with Express.js

Express.js makes it easy to create an HTTP server and handle different routes and HTTP methods.

#### Example 1: Basic HTTP Server

1. **Create a file named `app.js`** and write the following code:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Run the server**:
   ```bash
   node app.js
   ```

3. **Open your web browser** and go to `http://localhost:3000/`. You should see "Hello, World!".

### Handling Different Routes and Methods

Express.js allows you to handle various routes and HTTP methods (GET, POST, PUT, DELETE) with ease.

#### Example 2: Handling Multiple Routes

1. **Update `app.js`** to handle multiple routes:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Welcome to the Home Page!');
   });

   app.get('/about', (req, res) => {
     res.send('Welcome to the About Page!');
   });

   app.get('/contact', (req, res) => {
     res.send('Welcome to the Contact Page!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Test different routes** by visiting `http://localhost:3000/`, `http://localhost:3000/about`, and `http://localhost:3000/contact`.

### Handling POST Requests and JSON Data

Express.js can handle POST requests and parse JSON data sent by clients.

#### Example 3: Handling POST Requests

1. **Update `app.js`** to handle POST requests:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   // Middleware to parse JSON data
   app.use(express.json());

   app.get('/', (req, res) => {
     res.send('Welcome to the Home Page!');
   });

   app.post('/submit', (req, res) => {
     const data = req.body;
     res.send(`Data received: ${JSON.stringify(data)}`);
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Test the POST route** using a tool like Postman:
   - Set the method to POST.
   - Enter the URL `http://localhost:3000/submit`.
   - Set the body to JSON and add some data, for example: `{ "name": "John", "age": 30 }`.
   - Send the request and check the response.

### Serving Static Files

Express.js can also serve static files such as HTML, CSS, and JavaScript.

#### Example 4: Serving Static Files

1. **Create a directory named `public`** and add an `index.html` file:
   ```html
   <!-- public/index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Home Page</title>
   </head>
   <body>
     <h1>Welcome to the Home Page!</h1>
   </body>
   </html>
   ```

2. **Update `app.js`** to serve static files:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   // Middleware to serve static files
   app.use(express.static('public'));

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

3. **Restart the server**:
   ```bash
   node app.js
   ```

4. **Visit `http://localhost:3000/`** in your web browser to see the static HTML file.

### Real-World Application

In real-world applications, you might combine routing, middleware, and static file serving to create a full-fledged web server.

#### Example 5: Basic Web Application

1. **Update `app.js`** for a more complex application:
   ```javascript
   const express = require('express');
   const path = require('path');
   const app = express();
   const port = 3000;

   // Middleware to parse JSON data
   app.use(express.json());

   // Middleware to serve static files
   app.use(express.static(path.join(__dirname, 'public')));

   app.get('/', (req, res) => {
     res.sendFile(path.join(__dirname, 'public', 'index.html'));
   });

   app.post('/submit', (req, res) => {
     const data = req.body;
     res.send(`Data received: ${JSON.stringify(data)}`);
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Visit `http://localhost:3000/`** to see the home page, and use Postman to test the POST request.

### End of Chapter Quiz

1. What module is required to use Express.js?
   - a) http
   - b) url
   - c) express
   - d) net

2. How do you create an Express.js application?
   - a) `express.createApp()`
   - b) `express()`
   - c) `new express()`
   - d) `express.createServer()`

3. What method is used to define a GET route in Express.js?
   - a) `app.get()`
   - b) `app.route()`
   - c) `app.fetch()`
   - d) `app.request()`

4. How do you start an Express.js server on a specific port?
   - a) `app.listen()`
   - b) `app.start()`
   - c) `app.run()`
   - d) `app.connect()`

5. Which middleware is used to parse JSON data in Express.js?
   - a) `express.json()`
   - b) `express.urlencoded()`
   - c) `express.static()`
   - d) `express.bodyParser()`

6. How do you serve static files in Express.js?
   - a) `app.use(express.static())`
   - b) `app.use(express.files())`
   - c) `app.use(express.serve())`
   - d) `app.use(express.assets())`

7. What is the default port number used in the examples?
   - a) 8000
   - b) 8080
   - c) 3000
   - d) 5000

8. How do you handle POST requests in Express.js?
   - a) `app.post()`
   - b) `app.send()`
   - c) `app.request()`
   - d) `app.route()`

9. What method is used to send a response back to the client in Express.js?
   - a) `res.send()`
   - b) `res.write()`
   - c) `res.end()`
   - d) `res.respond()`

10. What will the following code output if you visit `http://localhost:3000/`?
    ```javascript
    const express = require('express');
    const app = express();
    const port = 3000;

    app.get('/', (req, res) => {
      res.send('Hello, Express.js!');
    });

    app.listen(port, () => {
      console.log(`Server running at http://localhost:${port}/`);
    });
    ```
    - a) Error
    - b) Welcome to Express.js
    - c) Hello, Express.js!
    - d) Hello, World!

### Answers

1. c) express
2. b) express()
3. a) app.get()
4. a) app.listen()
5. a) express.json()
6. a) app.use(express.static())
7. c) 3000
8. a) app.post()
9. a) res.send()
10. c) Hello, Express.js!

## Creating Advanced Routes with Express.js

Express.js is a flexible web application framework for Node.js, known for its robust features for building web and mobile applications. In this guide, we will explore how to create advanced routes using Express.js, with detailed examples and practical applications.

### Setting Up Express.js

Ensure you have Node.js installed. Then, install Express.js using npm:

1. **Initialize a new Node.js project**:
   ```bash
   mkdir advanced-express-server
   cd advanced-express-server
   npm init -y
   ```

2. **Install Express.js**:
   ```bash
   npm install express
   ```

### Basic Routing Recap

First, let's quickly recap basic routing with Express.js.

#### Example 1: Basic Route

1. **Create a file named `app.js`**:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Run the server**:
   ```bash
   node app.js
   ```

3. **Visit** `http://localhost:3000/` to see "Hello, World!".

### Advanced Routing

Express.js allows for more advanced routing techniques such as route parameters, query strings, and modular route handling.

#### Example 2: Route Parameters

Route parameters allow you to capture values specified at certain positions in the URL.

1. **Update `app.js`** to include a route with parameters:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/users/:userId/books/:bookId', (req, res) => {
     res.send(`User ID: ${req.params.userId}, Book ID: ${req.params.bookId}`);
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Visit** `http://localhost:3000/users/123/books/456` to see "User ID: 123, Book ID: 456".

#### Example 3: Query Strings

Query strings provide a way to pass data to the server as part of the URL.

1. **Update `app.js`** to handle query strings:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/search', (req, res) => {
     const { query, page } = req.query;
     res.send(`Search Query: ${query}, Page: ${page}`);
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Visit** `http://localhost:3000/search?query=javascript&page=2` to see "Search Query: javascript, Page: 2".

### Modular Route Handling

Express.js allows you to separate route logic into different files to keep your code organized and maintainable.

#### Example 4: Modular Routes

1. **Create a directory named `routes`** and a file `routes/users.js`:
   ```javascript
   const express = require('express');
   const router = express.Router();

   router.get('/', (req, res) => {
     res.send('User List');
   });

   router.get('/:userId', (req, res) => {
     res.send(`User ID: ${req.params.userId}`);
   });

   module.exports = router;
   ```

2. **Update `app.js`** to use the modular routes:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   const userRoutes = require('./routes/users');

   app.use('/users', userRoutes);

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

3. **Restart the server**:
   ```bash
   node app.js
   ```

4. **Visit** `http://localhost:3000/users` to see "User List" and `http://localhost:3000/users/123` to see "User ID: 123".

### Middleware in Routes

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application’s request-response cycle.

#### Example 5: Route-Specific Middleware

1. **Update `routes/users.js`** to include middleware:
   ```javascript
   const express = require('express');
   const router = express.Router();

   router.use((req, res, next) => {
     console.log('Request URL:', req.originalUrl);
     next();
   });

   router.get('/', (req, res) => {
     res.send('User List');
   });

   router.get('/:userId', (req, res) => {
     res.send(`User ID: ${req.params.userId}`);
   });

   module.exports = router;
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Visit** `http://localhost:3000/users` and check the console for the log "Request URL: /users".

### Nested Routes

You can create nested routes to further organize your route handling.

#### Example 6: Nested Routes

1. **Update `routes/users.js`** to include nested routes:
   ```javascript
   const express = require('express');
   const router = express.Router();

   const bookRouter = express.Router({ mergeParams: true });

   bookRouter.get('/', (req, res) => {
     res.send(`Books for User ID: ${req.params.userId}`);
   });

   router.use('/:userId/books', bookRouter);

   router.get('/', (req, res) => {
     res.send('User List');
   });

   router.get('/:userId', (req, res) => {
     res.send(`User ID: ${req.params.userId}`);
   });

   module.exports = router;
   ```

2. **Restart the server**:
   ```bash
   node app.js
   ```

3. **Visit** `http://localhost:3000/users/123/books` to see "Books for User ID: 123".

### End of Chapter Quiz

1. How do you define a route with parameters in Express.js?
   - a) `app.get('/:param', ...)`
   - b) `app.route('/:param', ...)`
   - c) `app.url('/:param', ...)`
   - d) `app.path('/:param', ...)`

2. Which method is used to handle query strings in Express.js?
   - a) `req.body`
   - b) `req.params`
   - c) `req.query`
   - d) `req.search`

3. How do you use modular routes in Express.js?
   - a) `app.use(require('path'))`
   - b) `app.route(require('path'))`
   - c) `app.use('/path', require('path'))`
   - d) `app.modular('/path', require('path'))`

4. What does `req.params` contain?
   - a) The query string parameters
   - b) The request body parameters
   - c) The URL route parameters
   - d) The request headers

5. How do you create nested routes in Express.js?
   - a) Using `app.nested()`
   - b) Using multiple `app.get()` calls
   - c) Using a nested router with `express.Router()`
   - d) Using `app.useNested()`

6. What is the purpose of middleware in routes?
   - a) To handle route parameters
   - b) To parse the request body
   - c) To execute code during the request-response cycle
   - d) To handle errors

7. How do you log the request URL in a middleware function?
   - a) `console.log('Request URL:', req.url)`
   - b) `console.log('Request URL:', req.path)`
   - c) `console.log('Request URL:', req.originalUrl)`
   - d) `console.log('Request URL:', req.route)`

8. How do you serve static files in Express.js?
   - a) `app.use(express.static('public'))`
   - b) `app.serveStatic('public')`
   - c) `app.useStatic('public')`
   - d) `app.static('public')`

9. How do you handle POST requests in Express.js?
   - a) `app.post()`
   - b) `app.send()`
   - c) `app.put()`
   - d) `app.request()`

10. What will the following code output if you visit `http://localhost:3000/users/123/books`?
    ```javascript
    const express = require('express');
    const app = express();
    const port = 3000;

    const userRouter = express.Router();
    const bookRouter = express.Router({ mergeParams: true });

    bookRouter.get('/', (req, res) => {
      res.send(`Books for User ID: ${req.params.userId}`);
    });

    userRouter.use('/:userId/books', bookRouter);

    app.use('/users', userRouter);

    app.listen(port, () => {
      console.log(`Server running at http://localhost:${port}/`);
    });
    ```
    - a) Error
    - b) User ID: 123, Books: []
    - c) Books for User ID: 123
    - d) Books for User ID: undefined

### Answers

1. a) app.get('/:param', ...)
2. c) req.query
3. c) app.use('/path', require('path'))
4. c) The URL route parameters
5. c) Using a nested router with express.Router()
6. c) To execute code during the request-response cycle
7. c) console.log('Request URL:', req.originalUrl)
8. a) app.use(express.static('public'))
9. a) app.post()
10. c) Books for User ID: 123

## Using ES6 with Node.js and Babel

ES6 (ECMAScript 2015) introduces many features that make JavaScript easier to write and maintain. Node.js supports most ES6 features, but for full compatibility, especially with newer features, Babel can be used to transpile ES6 code to ES5. This guide will explain how to set up and use ES6 with Node.js using Babel-node, with examples and practical applications.

### Setting Up Babel

1. **Initialize a new Node.js project**:
   ```bash
   mkdir es6-node-project
   cd es6-node-project
   npm init -y
   ```

2. **Install Babel and necessary presets**:
   ```bash
   npm install @babel/core @babel/cli @babel/preset-env @babel/node --save-dev
   ```

3. **Create a Babel configuration file (`.babelrc`)**:
   ```json
   {
     "presets": ["@babel/preset-env"]
   }
   ```

### Writing ES6 Code

Here are some examples of ES6 features and how to use them in your Node.js project.

#### Example 1: Arrow Functions

Arrow functions provide a shorter syntax for writing functions.

**Create a file named `app.js`**:
```javascript
const greet = (name) => {
  return `Hello, ${name}!`;
};

console.log(greet('World'));
```

#### Example 2: Classes

ES6 introduces classes, which provide a more straightforward and cleaner syntax to create objects and deal with inheritance.

**Update `app.js`** to include a class:
```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, ${this.name}!`;
  }
}

const person = new Person('John');
console.log(person.greet());
```

### Running ES6 Code with Babel-node

Use Babel-node to run your ES6 code:

```bash
npx babel-node app.js
```

### ES6 Modules

ES6 introduces a standard for modules, which allows you to import and export functions, objects, or primitives.

#### Example 3: Modules

1. **Create a file named `greet.js`**:
   ```javascript
   export const greet = (name) => {
     return `Hello, ${name}!`;
   };
   ```

2. **Update `app.js`** to import the module:
   ```javascript
   import { greet } from './greet.js';

   console.log(greet('World'));
   ```

3. **Run the code**:
   ```bash
   npx babel-node app.js
   ```

### Practical Application: Building a Simple Server

Combining ES6 features with Node.js, let's build a simple HTTP server using ES6 syntax.

1. **Install Express.js**:
   ```bash
   npm install express
   ```

2. **Create a file named `server.js`**:
   ```javascript
   import express from 'express';

   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

3. **Run the server**:
   ```bash
   npx babel-node server.js
   ```

4. **Visit** `http://localhost:3000/` to see "Hello, World!".

### End of Chapter Quiz

1. What command initializes a new Node.js project?
   - a) `npm start`
   - b) `npm init -y`
   - c) `npm install`
   - d) `npm create`

2. How do you install Babel presets for ES6?
   - a) `npm install babel`
   - b) `npm install @babel/preset-env`
   - c) `npm install babel-preset`
   - d) `npm install @babel/env`

3. What is the purpose of `.babelrc` file?
   - a) To run Babel
   - b) To configure Babel presets
   - c) To initialize a Node.js project
   - d) To install dependencies

4. How do you run a file with Babel-node?
   - a) `babel app.js`
   - b) `node app.js`
   - c) `npx babel-node app.js`
   - d) `npm start`

5. What is the correct syntax for an arrow function that takes a single parameter `name` and returns a greeting?
   - a) `const greet = name => { return `Hello, ${name}!`; }`
   - b) `function greet(name) { return `Hello, ${name}!`; }`
   - c) `const greet = (name) => { return `Hello, ${name}!`; }`
   - d) `let greet = name => { return `Hello, ${name}!`; }`

6. How do you define a class in ES6?
   - a) `function className() { ... }`
   - b) `class className { constructor() { ... } }`
   - c) `class className() { ... }`
   - d) `function class className { ... }`

7. What is the correct syntax for exporting a function in ES6?
   - a) `export function greet() { ... }`
   - b) `module.exports = greet;`
   - c) `export const greet = () => { ... }`
   - d) `exports.greet = function() { ... }`

8. How do you import a module in ES6?
   - a) `const greet = require('./greet.js');`
   - b) `import greet from './greet.js';`
   - c) `import { greet } from './greet.js';`
   - d) `require('./greet.js');`

9. Which command installs Express.js?
   - a) `npm install express`
   - b) `npm install @express`
   - c) `npm install babel-express`
   - d) `npm install expressjs`

10. What is the correct syntax to start an Express.js server on port 3000?
    ```javascript
    import express from 'express';
    const app = express();
    const port = 3000;
    
    app.get('/', (req, res) => {
      res.send('Hello, World!');
    });
    
    app.listen(port, () => {
      console.log(`Server running at http://localhost:${port}/`);
    });
    ```
    - a) Correct
    - b) Incorrect

### Answers

1. b) npm init -y
2. b) npm install @babel/preset-env
3. b) To configure Babel presets
4. c) npx babel-node app.js
5. c) const greet = (name) => { return `Hello, ${name}!`; }
6. b) class className { constructor() { ... } }
7. c) export const greet = () => { ... }
8. c) import { greet } from './greet.js';
9. a) npm install express
10. a) Correct

## Using Nodemon to Develop Faster

Nodemon is a utility that helps with automatically restarting the Node.js application when file changes are detected. This is particularly useful during development, as it eliminates the need to manually restart the server every time you make a change. This guide will explain how to set up and use Nodemon, with examples and practical applications.

### Setting Up Nodemon

1. **Install Nodemon**:
   You can install Nodemon globally or as a dev dependency in your project.

   - To install globally:
     ```bash
     npm install -g nodemon
     ```

   - To install as a dev dependency:
     ```bash
     npm install --save-dev nodemon
     ```

2. **Modify the `package.json` file**:
   Open the `package.json` file and add a script to start the application using Nodemon.

   ```json
   "scripts": {
     "start": "node app.js",
     "dev": "nodemon app.js"
   }
   ```

### Writing and Running Your Node.js Application

1. **Create a file named `app.js`**:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Run the application using Nodemon**:
   Use the script defined in `package.json` to start the application in development mode.

   ```bash
   npm run dev
   ```

   This will start the server and automatically restart it whenever a file change is detected.

### Practical Application

Imagine you are developing a simple API. Nodemon can significantly speed up the development process by automatically restarting the server when changes are made.

1. **Update `app.js` to include a new route**:
   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });

   app.get('/about', (req, res) => {
     res.send('About Us');
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

2. **Save the file and observe Nodemon**:
   Nodemon will automatically restart the server, applying the changes without needing to manually restart it.

### Additional Features

Nodemon offers several command-line options and configuration settings that can be customized.

1. **Using a configuration file (`nodemon.json`)**:
   Create a `nodemon.json` file to configure Nodemon options.

   ```json
   {
     "watch": ["src"],
     "ext": "js,json",
     "ignore": ["node_modules"],
     "exec": "node --inspect app.js"
   }
   ```

   - `watch`: Directories or files to watch for changes.
   - `ext`: File extensions to watch.
   - `ignore`: Paths to ignore.
   - `exec`: Command to execute when restarting.

2. **Using Nodemon with ES6 Modules**:
   If you are using ES6 modules, you can run Nodemon with Babel.

   ```bash
   nodemon --exec babel-node app.js
   ```

### End of Chapter Quiz

1. How do you install Nodemon globally?
   - a) `npm install --save nodemon`
   - b) `npm install -g nodemon`
   - c) `npm install nodemon`
   - d) `npm install --global nodemon`

2. How do you install Nodemon as a dev dependency?
   - a) `npm install nodemon --save`
   - b) `npm install nodemon -g`
   - c) `npm install --save-dev nodemon`
   - d) `npm install --dev nodemon`

3. What script should be added to `package.json` to start the application with Nodemon?
   - a) `"start": "nodemon app.js"`
   - b) `"dev": "node app.js"`
   - c) `"start": "node app.js"`
   - d) `"dev": "nodemon app.js"`

4. What command runs the application using Nodemon defined in `package.json` scripts?
   - a) `npm start`
   - b) `npm run dev`
   - c) `nodemon app.js`
   - d) `npm run nodemon`

5. What does Nodemon do when it detects a file change?
   - a) It stops the server.
   - b) It reloads the browser.
   - c) It restarts the server.
   - d) It clears the console.

6. Which configuration file can be used to customize Nodemon settings?
   - a) `nodemon.config`
   - b) `nodemon.js`
   - c) `nodemon.json`
   - d) `config.nodemon`

7. How can you specify directories or files to watch for changes in `nodemon.json`?
   - a) `"watch": ["src"]`
   - b) `"monitor": ["src"]`
   - c) `"track": ["src"]`
   - d) `"observe": ["src"]`

8. How do you run Nodemon with ES6 modules using Babel?
   - a) `nodemon --babel app.js`
   - b) `nodemon --exec babel-node app.js`
   - c) `babel-node nodemon app.js`
   - d) `nodemon --es6 app.js`

9. What option in `nodemon.json` specifies file extensions to watch?
   - a) `files`
   - b) `extensions`
   - c) `ext`
   - d) `filetypes`

10. What command is executed when restarting the server is specified in `nodemon.json`?
    - a) `"run": "node app.js"`
    - b) `"execute": "node app.js"`
    - c) `"exec": "node --inspect app.js"`
    - d) `"start": "node --inspect app.js"`

### Answers

1. b) `npm install -g nodemon`
2. c) `npm install --save-dev nodemon`
3. d) `"dev": "nodemon app.js"`
4. b) `npm run dev`
5. c) It restarts the server.
6. c) `nodemon.json`
7. a) `"watch": ["src"]`
8. b) `nodemon --exec babel-node app.js`
9. c) `ext`
10. c) `"exec": "node --inspect app.js"`

## Using Mocha to Write a Test Suite

### Introduction to Mocha

Mocha is a JavaScript test framework running on Node.js, designed to make asynchronous testing simple. Mocha tests run serially, allowing for flexible and accurate reporting while mapping uncaught exceptions to the correct test cases. It works well with any assertion library.

### Setting Up Mocha

Before writing tests with Mocha, you'll need to set it up in your project. Here's how:

1. **Install Node.js and npm**:
   Ensure you have Node.js and npm (Node Package Manager) installed on your machine. You can download them from [Node.js official website](https://nodejs.org/).

2. **Initialize your project**:
   Create a new directory for your project and initialize it with npm.
   ```bash
   mkdir mocha-test
   cd mocha-test
   npm init -y
   ```

3. **Install Mocha**:
   Install Mocha as a development dependency.
   ```bash
   npm install --save-dev mocha
   ```

4. **Create a Test Directory**:
   Create a directory called `test` where you will write your test files.
   ```bash
   mkdir test
   ```

### Writing Your First Test

1. **Create a Test File**:
   Create a new file inside the `test` directory, for example, `test.js`.
   
2. **Write a Simple Test**:
   Here's an example of a simple test using Mocha:

   ```javascript
   // test/test.js

   const assert = require('assert');

   describe('Array', function() {
     describe('#indexOf()', function() {
       it('should return -1 when the value is not present', function() {
         assert.strictEqual([1, 2, 3].indexOf(4), -1);
       });
     });
   });
   ```

   - `describe()` is used to group related tests.
   - `it()` defines a single test case.
   - `assert` is used to perform assertions.

### Running the Tests

To run the tests, you can use the following command:
```bash
npx mocha
```

Mocha will look for test files inside the `test` directory and execute them.

### Real-World Application

Imagine you are developing an e-commerce application and you need to ensure that your shopping cart functionalities work correctly. You could write tests to verify that items can be added to the cart, the total price is calculated correctly, and items can be removed.

Here’s an example:

```javascript
// test/cartTest.js

const assert = require('assert');
const Cart = require('../src/cart'); // Assuming you have a Cart class in src/cart.js

describe('Cart', function() {
  let cart;

  beforeEach(function() {
    cart = new Cart();
  });

  describe('#addItem()', function() {
    it('should add an item to the cart', function() {
      cart.addItem({ id: 1, name: 'Laptop', price: 1000 });
      assert.strictEqual(cart.items.length, 1);
    });
  });

  describe('#getTotalPrice()', function() {
    it('should return the total price of items in the cart', function() {
      cart.addItem({ id: 1, name: 'Laptop', price: 1000 });
      cart.addItem({ id: 2, name: 'Mouse', price: 50 });
      assert.strictEqual(cart.getTotalPrice(), 1050);
    });
  });

  describe('#removeItem()', function() {
    it('should remove an item from the cart', function() {
      cart.addItem({ id: 1, name: 'Laptop', price: 1000 });
      cart.removeItem(1);
      assert.strictEqual(cart.items.length, 0);
    });
  });
});
```

In this example, we are testing the functionality of a shopping cart:

- **Adding an item**: We check if an item is added correctly.
- **Calculating the total price**: We verify if the total price is calculated correctly.
- **Removing an item**: We ensure an item can be removed from the cart.

### End of Chapter Multiple Choice Questions

1. What is Mocha primarily used for?
   - A) Building web applications
   - B) Testing JavaScript code
   - C) Managing databases
   - D) Styling websites

2. Which command is used to install Mocha as a development dependency?
   - A) npm install mocha
   - B) npm install mocha -g
   - C) npm install --save-dev mocha
   - D) npm install mocha --global

3. What does `describe()` do in a Mocha test?
   - A) Defines a single test case
   - B) Runs the test suite
   - C) Groups related tests
   - D) Installs Mocha

4. What should be included in the `it()` function in Mocha?
   - A) Test case description
   - B) Group of related tests
   - C) Node.js installation
   - D) Assertion library

5. How do you run Mocha tests?
   - A) npm start
   - B) npm test
   - C) npx mocha
   - D) node test.js

6. In the example provided, what is the purpose of `beforeEach()`?
   - A) To install dependencies
   - B) To create a new cart instance before each test
   - C) To describe the test cases
   - D) To assert the results

7. What assertion method is used to check for strict equality in the example?
   - A) assert.equal()
   - B) assert.strictEqual()
   - C) assert.deepEqual()
   - D) assert.notEqual()

8. What does the following code check? `assert.strictEqual([1, 2, 3].indexOf(4), -1);`
   - A) If the value 4 is in the array [1, 2, 3]
   - B) If the value 4 is not in the array [1, 2, 3]
   - C) If the array [1, 2, 3] is empty
   - D) If the array length is 4

9. In a real-world application, why is it important to write tests for functionalities like a shopping cart?
   - A) To reduce code redundancy
   - B) To ensure the shopping cart works as expected
   - C) To increase website speed
   - D) To manage user data

10. What is the main advantage of using Mocha for testing?
    - A) It is a complete framework for web development
    - B) It allows for asynchronous testing
    - C) It replaces the need for Node.js
    - D) It is used for styling applications

### Answers

1. B) Testing JavaScript code
2. C) npm install --save-dev mocha
3. C) Groups related tests
4. A) Test case description
5. C) npx mocha
6. B) To create a new cart instance before each test
7. B) assert.strictEqual()
8. B) If the value 4 is not in the array [1, 2, 3]
9. B) To ensure the shopping cart works as expected
10. B) It allows for asynchronous testing

## Using Different Assertion Libraries: Node's `assert` and Chai

### Introduction to Assertion Libraries

Assertion libraries are used to verify that your code behaves as expected. They provide a way to compare the actual output of your code to the expected output and throw an error if the two don't match. Two commonly used assertion libraries in the JavaScript ecosystem are Node's built-in `assert` module and the Chai assertion library.

### Node's `assert` Module

Node.js comes with a built-in module called `assert` that provides a set of assertion functions for verifying invariants.

#### Basic Usage of `assert`

1. **Installation**: No installation is needed as it is built into Node.js.
2. **Usage**:
   ```javascript
   const assert = require('assert');

   // Example: Check if two values are equal
   assert.strictEqual(1 + 1, 2); // Passes
   assert.strictEqual(1 + 1, 3); // Throws an AssertionError
   ```

#### Common Methods in `assert`

- `assert.strictEqual(actual, expected)`: Checks if `actual === expected`.
- `assert.deepStrictEqual(actual, expected)`: Checks if objects and arrays are deeply equal.
- `assert.throws(fn, error)`: Expects the function `fn` to throw an error.

### Chai Assertion Library

Chai is a popular assertion library that provides a variety of styles for assertions: Should, Expect, and Assert. It is more flexible and user-friendly compared to the built-in `assert` module.

#### Setting Up Chai

1. **Installation**:
   ```bash
   npm install chai
   ```

2. **Usage**:
   ```javascript
   const chai = require('chai');
   const assert = chai.assert; // Using Assert style
   const expect = chai.expect; // Using Expect style
   const should = chai.should(); // Using Should style
   ```

#### Common Methods in Chai

##### Assert Style
- `assert.equal(actual, expected)`: Checks if `actual == expected`.
- `assert.strictEqual(actual, expected)`: Checks if `actual === expected`.
- `assert.deepEqual(actual, expected)`: Checks if objects and arrays are deeply equal.
- `assert.throws(fn, error)`: Expects the function `fn` to throw an error.

##### Expect Style
- `expect(value).to.equal(expected)`: Checks if `value === expected`.
- `expect(value).to.have.property(name, value)`: Checks if an object has a property with the specified value.
- `expect(fn).to.throw(error)`: Expects the function `fn` to throw an error.

##### Should Style
- `value.should.equal(expected)`: Checks if `value === expected`.
- `value.should.have.property(name, value)`: Checks if an object has a property with the specified value.
- `fn.should.throw(error)`: Expects the function `fn` to throw an error.

### Real-World Application

Let's apply these assertion libraries in a real-world scenario: validating a user registration system.

#### Node's `assert` Example

```javascript
// userTest.js

const assert = require('assert');
const User = require('../src/user'); // Assuming you have a User class in src/user.js

describe('User Registration', function() {
  let user;

  beforeEach(function() {
    user = new User();
  });

  it('should register a user with valid details', function() {
    user.register({ username: 'john_doe', password: '12345' });
    assert.strictEqual(user.username, 'john_doe');
  });

  it('should throw an error for missing password', function() {
    assert.throws(() => user.register({ username: 'john_doe' }), /Password is required/);
  });
});
```

#### Chai Example

```javascript
// userTest.js

const chai = require('chai');
const expect = chai.expect;
const User = require('../src/user'); // Assuming you have a User class in src/user.js

describe('User Registration', function() {
  let user;

  beforeEach(function() {
    user = new User();
  });

  it('should register a user with valid details', function() {
    user.register({ username: 'john_doe', password: '12345' });
    expect(user.username).to.equal('john_doe');
  });

  it('should throw an error for missing password', function() {
    expect(() => user.register({ username: 'john_doe' })).to.throw('Password is required');
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary purpose of assertion libraries?
   - A) To build user interfaces
   - B) To verify that code behaves as expected
   - C) To manage databases
   - D) To style websites

2. Which of the following is a built-in module in Node.js for assertions?
   - A) Mocha
   - B) Chai
   - C) Assert
   - D) Sinon

3. What does `assert.strictEqual(1 + 1, 2)` do?
   - A) Checks if 1 + 1 is greater than 2
   - B) Checks if 1 + 1 is less than 2
   - C) Checks if 1 + 1 equals 2
   - D) Checks if 1 + 1 is not equal to 2

4. How do you install Chai in your project?
   - A) npm install chai
   - B) npm install assert
   - C) npm install mocha
   - D) npm install chai-assert

5. Which style of assertions does Chai NOT provide?
   - A) Should
   - B) Expect
   - C) Assert
   - D) Validate

6. What does `expect(value).to.equal(expected)` do in Chai?
   - A) Checks if value is less than expected
   - B) Checks if value is greater than expected
   - C) Checks if value is not equal to expected
   - D) Checks if value equals expected

7. In the context of assertions, what does `assert.throws(fn, error)` check?
   - A) If the function returns a value
   - B) If the function throws an error
   - C) If the function does not throw an error
   - D) If the function completes successfully

8. What is the command to initialize a new npm project?
   - A) npm start
   - B) npm init
   - C) npm install
   - D) npm run

9. Which assertion method is used to check deep equality of objects in Node's `assert` module?
   - A) assert.strictEqual()
   - B) assert.deepStrictEqual()
   - C) assert.deepEqual()
   - D) assert.equal()

10. Why is it important to write tests for functionalities like user registration?
    - A) To reduce server load
    - B) To ensure the user registration works as expected
    - C) To increase code complexity
    - D) To manage database connections

### Answers

1. B) To verify that code behaves as expected
2. C) Assert
3. C) Checks if 1 + 1 equals 2
4. A) npm install chai
5. D) Validate
6. D) Checks if value equals expected
7. B) If the function throws an error
8. B) npm init
9. B) assert.deepStrictEqual()
10. B) To ensure the user registration works as expected

## How to Present Long Test Suites

### Introduction

Testing is a critical part of software development, ensuring that code behaves as expected and meets requirements. Long test suites, which consist of numerous test cases, are essential for thoroughly verifying complex systems. This guide covers how to effectively organize, present, and manage long test suites using tools and best practices.

### Organizing Test Suites

1. **Modular Structure**:
   - Break down tests into smaller, manageable modules or files.
   - Group related tests together to improve readability and maintainability.
   
   Example directory structure:
   ```
   test/
   ├── auth/
   │   ├── loginTest.js
   │   └── registerTest.js
   ├── cart/
   │   ├── addItemTest.js
   │   └── removeItemTest.js
   └── user/
       ├── profileTest.js
       └── settingsTest.js
   ```

2. **Descriptive Naming**:
   - Use descriptive names for test files and test cases to clearly indicate what is being tested.
   - Example:
     ```javascript
     describe('User Registration', function() {
       it('should register a user with valid details', function() {
         // test code
       });

       it('should not register a user with a missing password', function() {
         // test code
       });
     });
     ```

3. **Setup and Teardown**:
   - Use setup (`before`, `beforeEach`) and teardown (`after`, `afterEach`) hooks to prepare the test environment and clean up after tests.
   - This reduces redundancy and keeps test cases focused.

   Example:
   ```javascript
   describe('Cart Operations', function() {
     let cart;

     beforeEach(function() {
       cart = new Cart();
     });

     afterEach(function() {
       // Clean up code
     });

     it('should add an item to the cart', function() {
       cart.addItem({ id: 1, name: 'Laptop', price: 1000 });
       assert.strictEqual(cart.items.length, 1);
     });

     it('should calculate the total price correctly', function() {
       cart.addItem({ id: 1, name: 'Laptop', price: 1000 });
       cart.addItem({ id: 2, name: 'Mouse', price: 50 });
       assert.strictEqual(cart.getTotalPrice(), 1050);
     });
   });
   ```

### Presenting Test Results

1. **Readable Output**:
   - Use a test runner like Mocha, which provides readable and organized test results.
   - Example Mocha command:
     ```bash
     npx mocha
     ```

2. **Reporting Tools**:
   - Utilize reporting tools and formats (e.g., HTML, JSON) to generate detailed test reports.
   - Mocha can be integrated with reporters like `mochawesome` for enhanced reports.
     ```bash
     npm install --save-dev mochawesome
     npx mocha --reporter mochawesome
     ```

3. **Continuous Integration (CI)**:
   - Integrate tests into CI pipelines (e.g., GitHub Actions, Travis CI) to automatically run tests on code changes and present results in a standardized manner.
   - Example GitHub Actions workflow:
     ```yaml
     name: Node.js CI

     on: [push, pull_request]

     jobs:
       build:
         runs-on: ubuntu-latest

         strategy:
           matrix:
             node-version: [12.x, 14.x, 16.x]

         steps:
         - uses: actions/checkout@v2
         - name: Use Node.js ${{ matrix.node-version }}
           uses: actions/setup-node@v2
           with:
             node-version: ${{ matrix.node-version }}
         - run: npm install
         - run: npx mocha
     ```

### Real-World Application

In a real-world e-commerce application, you might have extensive test suites for various components like user authentication, product management, and order processing.

#### Example: User Authentication Tests

```javascript
// test/auth/loginTest.js

const chai = require('chai');
const expect = chai.expect;
const Auth = require('../../src/auth'); // Assuming you have an Auth class in src/auth.js

describe('User Login', function() {
  let auth;

  beforeEach(function() {
    auth = new Auth();
  });

  it('should login a user with valid credentials', function() {
    auth.login('john_doe', 'password123');
    expect(auth.isLoggedIn).to.be.true;
  });

  it('should not login a user with invalid credentials', function() {
    expect(() => auth.login('john_doe', 'wrongpassword')).to.throw('Invalid credentials');
  });

  it('should throw an error for missing credentials', function() {
    expect(() => auth.login('john_doe')).to.throw('Credentials are required');
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary purpose of organizing tests into smaller modules?
   - A) To reduce the number of test cases
   - B) To improve readability and maintainability
   - C) To make tests run faster
   - D) To use more files

2. Which hook is used to prepare the test environment before each test case?
   - A) before
   - B) after
   - C) beforeEach
   - D) afterEach

3. What does the `describe` function do in a test suite?
   - A) Runs a single test case
   - B) Groups related test cases
   - C) Cleans up after tests
   - D) Sets up the test environment

4. How can you run Mocha tests and generate a report using `mochawesome`?
   - A) npx mocha --reporter mochawesome
   - B) npm start mochawesome
   - C) npx mochawesome --run
   - D) npm install mochawesome -g

5. Why is it important to use descriptive names for test files and test cases?
   - A) To make the code run faster
   - B) To make it easier to understand what is being tested
   - C) To reduce the number of test files
   - D) To increase the complexity of tests

6. Which command initializes a new npm project?
   - A) npm start
   - B) npm init
   - C) npm install
   - D) npm run

7. What is a benefit of integrating tests into a CI pipeline?
   - A) It makes tests run slower
   - B) It automates running tests on code changes
   - C) It removes the need for a test runner
   - D) It increases the number of test cases

8. What does the `assert.strictEqual` function do?
   - A) Checks if two values are loosely equal
   - B) Checks if two values are strictly equal
   - C) Checks if two objects are equal
   - D) Checks if two arrays are equal

9. In Chai, what does `expect(value).to.equal(expected)` do?
   - A) Checks if value is less than expected
   - B) Checks if value is greater than expected
   - C) Checks if value is equal to expected
   - D) Checks if value is not equal to expected

10. Why is it beneficial to use setup and teardown hooks in test suites?
    - A) To write more test cases
    - B) To keep test cases focused and reduce redundancy
    - C) To increase test file size
    - D) To make tests run slower

### Answers

1. B) To improve readability and maintainability
2. C) beforeEach
3. B) Groups related test cases
4. A) npx mocha --reporter mochawesome
5. B) To make it easier to understand what is being tested
6. B) npm init
7. B) It automates running tests on code changes
8. B) Checks if two values are strictly equal
9. C) Checks if value is equal to expected
10. B) To keep test cases focused and reduce redundancy

## When and How to Use Spies

### Introduction

In software testing, spies are used to monitor and record the interactions between functions or objects. They allow you to track how many times a function was called, with what arguments, and what it returned. This is particularly useful in unit testing to ensure that functions are being used as expected. 

### When to Use Spies

1. **Tracking Function Calls**:
   - To verify if a function was called and how many times.
   - To check the arguments with which a function was called.
   - To ensure that a function is called under specific conditions.

2. **Testing Callbacks**:
   - To ensure that a callback function is executed correctly.
   - To verify the behavior of asynchronous functions.

3. **Verifying Interactions Between Components**:
   - To check if one component correctly interacts with another.
   - To monitor the communication between different parts of a system.

### Setting Up Spies

To demonstrate the use of spies, we'll use Sinon.js, a popular library for creating spies, mocks, and stubs in JavaScript.

#### Installation

```bash
npm install sinon
```

### Using Spies with Sinon.js

#### Basic Example

1. **Creating a Spy**:
   ```javascript
   const sinon = require('sinon');

   function greet(name) {
     console.log('Hello, ' + name);
   }

   const spy = sinon.spy(greet);

   spy('Alice');
   console.log(spy.called); // true
   console.log(spy.calledWith('Alice')); // true
   ```

2. **Verifying Function Calls**:
   ```javascript
   const sinon = require('sinon');

   function add(a, b) {
     return a + b;
   }

   const spy = sinon.spy(add);

   const result = spy(2, 3);
   console.log(result); // 5
   console.log(spy.calledOnce); // true
   console.log(spy.calledWith(2, 3)); // true
   ```

#### Spies in Asynchronous Code

1. **Spying on Callbacks**:
   ```javascript
   const sinon = require('sinon');

   function fetchData(callback) {
     setTimeout(() => {
       callback('data');
     }, 1000);
   }

   const callback = sinon.spy();

   fetchData(callback);

   setTimeout(() => {
     console.log(callback.calledOnce); // true
     console.log(callback.calledWith('data')); // true
   }, 1500);
   ```

### Real-World Application

Let's apply spies to a real-world scenario: testing a user service that interacts with a database.

#### Example: User Service

```javascript
// userService.js

class UserService {
  constructor(database) {
    this.database = database;
  }

  getUser(id) {
    return this.database.findUserById(id);
  }

  saveUser(user) {
    this.database.saveUser(user);
  }
}

module.exports = UserService;
```

#### Test with Spies

```javascript
// userServiceTest.js

const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const UserService = require('../src/userService');

describe('UserService', function() {
  let database;
  let userService;

  beforeEach(function() {
    database = {
      findUserById: sinon.spy(),
      saveUser: sinon.spy()
    };
    userService = new UserService(database);
  });

  it('should call findUserById with correct ID', function() {
    userService.getUser(1);
    expect(database.findUserById.calledOnce).to.be.true;
    expect(database.findUserById.calledWith(1)).to.be.true;
  });

  it('should call saveUser with correct user data', function() {
    const user = { id: 1, name: 'Alice' };
    userService.saveUser(user);
    expect(database.saveUser.calledOnce).to.be.true;
    expect(database.saveUser.calledWith(user)).to.be.true;
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary purpose of using spies in testing?
   - A) To execute functions
   - B) To monitor and record function interactions
   - C) To manage databases
   - D) To style websites

2. Which library is commonly used for creating spies in JavaScript?
   - A) Mocha
   - B) Chai
   - C) Sinon
   - D) Jasmine

3. What does `spy.calledOnce` check?
   - A) If the spy was called more than once
   - B) If the spy was called exactly once
   - C) If the spy was never called
   - D) If the spy was called with specific arguments

4. How do you create a spy using Sinon?
   - A) `const spy = sinon.createSpy(function)`
   - B) `const spy = sinon.spy(function)`
   - C) `const spy = sinon.stub(function)`
   - D) `const spy = sinon.mock(function)`

5. What is the purpose of spying on a callback function?
   - A) To execute the callback function
   - B) To check if the callback function was called and with what arguments
   - C) To replace the callback function
   - D) To remove the callback function

6. How can you check if a spy was called with specific arguments?
   - A) `spy.withArgs(arguments)`
   - B) `spy.calledWith(arguments)`
   - C) `spy.argsWith(arguments)`
   - D) `spy.checkArgs(arguments)`

7. In the context of spies, what does `spy.resetHistory` do?
   - A) Clears the spy's call history
   - B) Deletes the spy
   - C) Executes the spy
   - D) Modifies the spy's arguments

8. What is the benefit of using spies in testing asynchronous functions?
   - A) To make asynchronous functions synchronous
   - B) To verify the execution and arguments of callbacks
   - C) To increase the execution speed of asynchronous functions
   - D) To prevent asynchronous functions from running

9. How can you verify that a spy was not called in Sinon?
   - A) `expect(spy.called).to.be.false`
   - B) `expect(spy.notCalled).to.be.true`
   - C) `expect(spy.wasNotCalled).to.be.true`
   - D) `expect(spy.neverCalled).to.be.false`

10. Why is it useful to spy on the interactions between components in a system?
    - A) To ensure components are interacting correctly
    - B) To increase the complexity of the system
    - C) To remove the need for testing
    - D) To make the components run faster

### Answers

1. B) To monitor and record function interactions
2. C) Sinon
3. B) If the spy was called exactly once
4. B) `const spy = sinon.spy(function)`
5. B) To check if the callback function was called and with what arguments
6. B) `spy.calledWith(arguments)`
7. A) Clears the spy's call history
8. B) To verify the execution and arguments of callbacks
9. B) `expect(spy.notCalled).to.be.true`
10. A) To ensure components are interacting correctly

## When and How to Use Stubs

### Introduction

In software testing, stubs are used to simulate the behavior of complex or external systems. They allow you to isolate the component being tested by replacing parts of the system that are not under test. This makes it easier to test specific functionality without relying on other components, which may be unpredictable or difficult to control.

### When to Use Stubs

1. **Isolating Components**:
   - To test a component in isolation from its dependencies.
   - To simulate responses from external systems, such as databases or APIs.

2. **Controlling Test Environments**:
   - To create predictable and repeatable test scenarios.
   - To simulate various conditions, such as errors or specific data responses.

3. **Improving Test Performance**:
   - To reduce the time and resources needed for testing by avoiding real network or database calls.
   - To eliminate dependencies on external systems, making tests faster and more reliable.

### Setting Up Stubs

To demonstrate the use of stubs, we'll use Sinon.js, a popular library for creating spies, mocks, and stubs in JavaScript.

#### Installation

```bash
npm install sinon
```

### Using Stubs with Sinon.js

#### Basic Example

1. **Creating a Stub**:
   ```javascript
   const sinon = require('sinon');

   function getUser(id) {
     // Simulate an API call to fetch user data
     return fetch(`/api/users/${id}`).then(response => response.json());
   }

   const stub = sinon.stub(global, 'fetch');

   stub.resolves({
     json: () => Promise.resolve({ id: 1, name: 'Alice' })
   });

   getUser(1).then(user => {
     console.log(user); // { id: 1, name: 'Alice' }
   });
   ```

2. **Controlling Behavior**:
   ```javascript
   const sinon = require('sinon');

   function getUser(id) {
     return fetch(`/api/users/${id}`).then(response => response.json());
   }

   const stub = sinon.stub(global, 'fetch');

   stub.onFirstCall().resolves({
     json: () => Promise.resolve({ id: 1, name: 'Alice' })
   });

   stub.onSecondCall().resolves({
     json: () => Promise.resolve({ id: 2, name: 'Bob' })
   });

   getUser(1).then(user => {
     console.log(user); // { id: 1, name: 'Alice' }
   });

   getUser(2).then(user => {
     console.log(user); // { id: 2, name: 'Bob' }
   });
   ```

#### Stubs in Asynchronous Code

1. **Simulating Delays and Errors**:
   ```javascript
   const sinon = require('sinon');

   function getUser(id) {
     return fetch(`/api/users/${id}`).then(response => response.json());
   }

   const stub = sinon.stub(global, 'fetch');

   // Simulate a delay
   stub.onFirstCall().resolves({
     json: () => new Promise(resolve => setTimeout(() => resolve({ id: 1, name: 'Alice' }), 1000))
   });

   // Simulate an error
   stub.onSecondCall().rejects(new Error('Network error'));

   getUser(1).then(user => {
     console.log(user); // { id: 1, name: 'Alice' } after 1 second
   });

   getUser(2).catch(error => {
     console.error(error.message); // 'Network error'
   });
   ```

### Real-World Application

Let's apply stubs to a real-world scenario: testing a payment service that interacts with a third-party payment gateway.

#### Example: Payment Service

```javascript
// paymentService.js

class PaymentService {
  constructor(paymentGateway) {
    this.paymentGateway = paymentGateway;
  }

  processPayment(amount) {
    return this.paymentGateway.charge(amount).then(response => {
      if (response.success) {
        return 'Payment successful';
      } else {
        throw new Error('Payment failed');
      }
    });
  }
}

module.exports = PaymentService;
```

#### Test with Stubs

```javascript
// paymentServiceTest.js

const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const PaymentService = require('../src/paymentService');

describe('PaymentService', function() {
  let paymentGateway;
  let paymentService;

  beforeEach(function() {
    paymentGateway = {
      charge: sinon.stub()
    };
    paymentService = new PaymentService(paymentGateway);
  });

  it('should process payment successfully', function() {
    paymentGateway.charge.resolves({ success: true });

    return paymentService.processPayment(100).then(result => {
      expect(result).to.equal('Payment successful');
    });
  });

  it('should fail to process payment', function() {
    paymentGateway.charge.resolves({ success: false });

    return paymentService.processPayment(100).catch(error => {
      expect(error.message).to.equal('Payment failed');
    });
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary purpose of using stubs in testing?
   - A) To monitor function interactions
   - B) To simulate the behavior of complex or external systems
   - C) To execute real network calls
   - D) To manage test data

2. Which library is commonly used for creating stubs in JavaScript?
   - A) Mocha
   - B) Chai
   - C) Sinon
   - D) Jasmine

3. What does `stub.resolves` do?
   - A) Sets the return value of the stub
   - B) Simulates an asynchronous success response
   - C) Simulates an error response
   - D) Resets the stub's history

4. How do you create a stub using Sinon?
   - A) `const stub = sinon.createStub(function)`
   - B) `const stub = sinon.stub(function)`
   - C) `const stub = sinon.mock(function)`
   - D) `const stub = sinon.spy(function)`

5. What is the benefit of using stubs in testing asynchronous functions?
   - A) To make asynchronous functions synchronous
   - B) To simulate various conditions and responses
   - C) To increase the execution speed of asynchronous functions
   - D) To prevent asynchronous functions from running

6. How can you simulate an error response using Sinon stubs?
   - A) `stub.rejects(error)`
   - B) `stub.errors(error)`
   - C) `stub.throws(error)`
   - D) `stub.fails(error)`

7. What is the purpose of `stub.onFirstCall` and `stub.onSecondCall`?
   - A) To make the stub execute only once or twice
   - B) To control the behavior of the stub on consecutive calls
   - C) To reset the stub after each call
   - D) To create multiple instances of the stub

8. Why is it useful to use stubs to simulate delays in testing?
   - A) To increase test execution time
   - B) To make tests less predictable
   - C) To test how the system handles delayed responses
   - D) To decrease test complexity

9. How do you restore the original function after using a stub in Sinon?
   - A) `stub.reset()`
   - B) `stub.restore()`
   - C) `stub.clear()`
   - D) `stub.undo()`

10. Why is it important to test components in isolation using stubs?
    - A) To ensure that the entire system works as expected
    - B) To simplify testing by eliminating dependencies
    - C) To increase the number of test cases
    - D) To make tests more complex

### Answers

1. B) To simulate the behavior of complex or external systems
2. C) Sinon
3. B) Simulates an asynchronous success response
4. B) `const stub = sinon.stub(function)`
5. B) To simulate various conditions and responses
6. A) `stub.rejects(error)`
7. B) To control the behavior of the stub on consecutive calls
8. C) To test how the system handles delayed responses
9. B) `stub.restore()`
10. B) To simplify testing by eliminating dependencies

## What are Hooks and When to Use Them

### Introduction

Hooks are special functions provided by testing frameworks like Mocha that allow you to set up preconditions and postconditions for your tests. They help manage the test environment by providing a structured way to prepare for tests and clean up afterward.

### Types of Hooks

1. **`before`**: Runs once before the first test in the test suite.
2. **`after`**: Runs once after the last test in the test suite.
3. **`beforeEach`**: Runs before each test in the test suite.
4. **`afterEach`**: Runs after each test in the test suite.

### When to Use Hooks

1. **Setting Up Test Environment**:
   - Use `before` and `beforeEach` hooks to set up the test environment, such as initializing variables, setting up databases, or configuring stubs and spies.

2. **Cleaning Up**:
   - Use `after` and `afterEach` hooks to clean up after tests, such as closing database connections, restoring stubs, or cleaning up temporary data.

3. **Reusing Setup Code**:
   - Hooks help avoid code duplication by allowing you to reuse setup and teardown code across multiple tests.

### Using Hooks with Mocha

#### Basic Example

1. **Using `before` and `after` Hooks**:
   ```javascript
   const chai = require('chai');
   const expect = chai.expect;

   describe('Array', function() {
     let arr;

     before(function() {
       // Runs once before all tests in this block
       arr = [1, 2, 3];
     });

     after(function() {
       // Runs once after all tests in this block
       arr = null;
     });

     it('should have a length of 3', function() {
       expect(arr.length).to.equal(3);
     });

     it('should contain 1', function() {
       expect(arr).to.include(1);
     });
   });
   ```

2. **Using `beforeEach` and `afterEach` Hooks**:
   ```javascript
   const chai = require('chai');
   const expect = chai.expect;

   describe('Math operations', function() {
     let num;

     beforeEach(function() {
       // Runs before each test in this block
       num = 5;
     });

     afterEach(function() {
       // Runs after each test in this block
       num = 0;
     });

     it('should add 5 correctly', function() {
       num += 5;
       expect(num).to.equal(10);
     });

     it('should subtract 2 correctly', function() {
       num -= 2;
       expect(num).to.equal(3);
     });
   });
   ```

### Real-World Application

Let's apply hooks to a real-world scenario: testing a user service that interacts with a database.

#### Example: User Service

```javascript
// userService.js

class UserService {
  constructor(database) {
    this.database = database;
  }

  getUser(id) {
    return this.database.findUserById(id);
  }

  saveUser(user) {
    return this.database.saveUser(user);
  }
}

module.exports = UserService;
```

#### Test with Hooks

```javascript
// userServiceTest.js

const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const UserService = require('../src/userService');

describe('UserService', function() {
  let database;
  let userService;
  let sandbox;

  before(function() {
    // Runs once before all tests
    database = {
      findUserById: sinon.stub(),
      saveUser: sinon.stub()
    };
    userService = new UserService(database);
  });

  beforeEach(function() {
    // Runs before each test
    sandbox = sinon.createSandbox();
  });

  afterEach(function() {
    // Runs after each test
    sandbox.restore();
  });

  it('should call findUserById with correct ID', function() {
    database.findUserById.resolves({ id: 1, name: 'Alice' });

    return userService.getUser(1).then(user => {
      expect(database.findUserById.calledOnce).to.be.true;
      expect(database.findUserById.calledWith(1)).to.be.true;
      expect(user).to.deep.equal({ id: 1, name: 'Alice' });
    });
  });

  it('should call saveUser with correct user data', function() {
    const user = { id: 1, name: 'Alice' };
    database.saveUser.resolves(user);

    return userService.saveUser(user).then(savedUser => {
      expect(database.saveUser.calledOnce).to.be.true;
      expect(database.saveUser.calledWith(user)).to.be.true;
      expect(savedUser).to.deep.equal(user);
    });
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the purpose of the `before` hook in Mocha?
   - A) To run before each test
   - B) To run once before all tests
   - C) To run after each test
   - D) To run once after all tests

2. When should you use the `afterEach` hook?
   - A) To set up the test environment
   - B) To clean up after each test
   - C) To run once after all tests
   - D) To run before each test

3. How many times does the `before` hook run in a test suite?
   - A) Once before each test
   - B) Once after each test
   - C) Once before all tests
   - D) Once after all tests

4. Which hook is used to avoid code duplication by reusing setup code across multiple tests?
   - A) `before`
   - B) `after`
   - C) `beforeEach`
   - D) `afterEach`

5. What is a common use case for the `after` hook?
   - A) To set up test data
   - B) To initialize variables
   - C) To clean up resources after all tests
   - D) To reset variables before each test

6. How can you restore stubs or spies after each test?
   - A) Using `beforeEach`
   - B) Using `after`
   - C) Using `afterEach`
   - D) Using `before`

7. In the context of hooks, what does `sandbox.restore()` do?
   - A) Sets up the test environment
   - B) Cleans up resources after each test
   - C) Restores the state of stubs or spies
   - D) Initializes the database

8. What is the primary benefit of using hooks in a test suite?
   - A) To make tests run faster
   - B) To ensure tests are isolated and independent
   - C) To increase code complexity
   - D) To reduce the number of tests needed

9. Which hook would you use to simulate a delay before each test?
   - A) `before`
   - B) `after`
   - C) `beforeEach`
   - D) `afterEach`

10. How do hooks help improve the reliability of tests?
    - A) By running all tests in parallel
    - B) By ensuring the test environment is properly set up and cleaned up
    - C) By reducing the number of assertions in each test
    - D) By making tests dependent on each other

### Answers

1. B) To run once before all tests
2. B) To clean up after each test
3. C) Once before all tests
4. C) `beforeEach`
5. C) To clean up resources after all tests
6. C) Using `afterEach`
7. C) Restores the state of stubs or spies
8. B) To ensure tests are isolated and independent
9. C) `beforeEach`
10. B) By ensuring the test environment is properly set up and cleaned up

## Unit Testing with Async Functions

### Introduction

Unit testing asynchronous functions is essential for ensuring that code behaves correctly when dealing with operations that take time to complete, such as network requests, file I/O, or timers. Asynchronous testing verifies that the code handles async operations correctly, ensuring promises resolve or reject as expected.

### Asynchronous Functions

Asynchronous functions can be written using callbacks, promises, or the `async/await` syntax. Proper testing of these functions involves ensuring they execute and complete as expected, including handling any errors.

### Setting Up

We'll use Mocha for the test framework and Chai for assertions.

#### Installation

```bash
npm install mocha chai
```

### Testing Callbacks

Testing functions that use callbacks involves using Mocha's `done` callback to signal when the test is complete.

```javascript
// asyncCallback.js

function fetchData(callback) {
  setTimeout(() => {
    callback(null, 'data');
  }, 100);
}

module.exports = fetchData;
```

```javascript
// asyncCallbackTest.js

const fetchData = require('./asyncCallback');
const chai = require('chai');
const expect = chai.expect;

describe('fetchData', function() {
  it('should fetch data successfully', function(done) {
    fetchData((err, data) => {
      expect(err).to.be.null;
      expect(data).to.equal('data');
      done();
    });
  });
});
```

### Testing Promises

Testing functions that return promises can be done using Mocha's built-in support for promises.

```javascript
// asyncPromise.js

function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('data');
    }, 100);
  });
}

module.exports = fetchData;
```

```javascript
// asyncPromiseTest.js

const fetchData = require('./asyncPromise');
const chai = require('chai');
const expect = chai.expect;

describe('fetchData', function() {
  it('should fetch data successfully', function() {
    return fetchData().then(data => {
      expect(data).to.equal('data');
    });
  });

  it('should handle errors', function() {
    const fetchDataWithError = () => Promise.reject(new Error('error'));
    return fetchDataWithError().catch(error => {
      expect(error.message).to.equal('error');
    });
  });
});
```

### Testing with `async/await`

Testing functions with `async/await` makes asynchronous code appear synchronous, which can simplify tests.

```javascript
// asyncAwait.js

async function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('data');
    }, 100);
  });
}

module.exports = fetchData;
```

```javascript
// asyncAwaitTest.js

const fetchData = require('./asyncAwait');
const chai = require('chai');
const expect = chai.expect;

describe('fetchData', function() {
  it('should fetch data successfully', async function() {
    const data = await fetchData();
    expect(data).to.equal('data');
  });

  it('should handle errors', async function() {
    const fetchDataWithError = async () => {
      throw new Error('error');
    };

    try {
      await fetchDataWithError();
    } catch (error) {
      expect(error.message).to.equal('error');
    }
  });
});
```

### Real-World Application

Let's apply unit testing to a real-world scenario: testing an async function that fetches user data from an API.

#### Example: User Service

```javascript
// userService.js

const axios = require('axios');

async function getUser(id) {
  const response = await axios.get(`/api/users/${id}`);
  return response.data;
}

module.exports = getUser;
```

#### Test with Mocks

We'll use Sinon to mock the axios call.

```javascript
// userServiceTest.js

const getUser = require('../src/userService');
const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const axios = require('axios');

describe('getUser', function() {
  let axiosGetStub;

  beforeEach(function() {
    axiosGetStub = sinon.stub(axios, 'get');
  });

  afterEach(function() {
    axiosGetStub.restore();
  });

  it('should fetch user data successfully', async function() {
    const user = { id: 1, name: 'Alice' };
    axiosGetStub.resolves({ data: user });

    const result = await getUser(1);
    expect(result).to.deep.equal(user);
  });

  it('should handle errors', async function() {
    axiosGetStub.rejects(new Error('Network error'));

    try {
      await getUser(1);
    } catch (error) {
      expect(error.message).to.equal('Network error');
    }
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary benefit of testing asynchronous functions?
   - A) To ensure functions execute synchronously
   - B) To verify correct handling of async operations
   - C) To increase test execution time
   - D) To avoid using callbacks

2. Which Mocha feature allows testing of callback-based functions?
   - A) `done` callback
   - B) Promises
   - C) `async/await`
   - D) Spies

3. How do you test a function that returns a promise?
   - A) Using the `done` callback
   - B) By returning the promise from the test
   - C) By using `setTimeout`
   - D) By throwing an error

4. What syntax simplifies writing tests for async functions?
   - A) Callbacks
   - B) Promises
   - C) `async/await`
   - D) `setInterval`

5. In the context of testing, what does Sinon provide?
   - A) Assertion library
   - B) Test framework
   - C) Mocking and stubbing
   - D) Browser automation

6. How do you mock an HTTP request in tests?
   - A) Using Mocha hooks
   - B) Using Sinon stubs
   - C) Using Chai assertions
   - D) Using `async/await`

7. Which method in Mocha runs once before all tests in a suite?
   - A) `before`
   - B) `beforeEach`
   - C) `after`
   - D) `afterEach`

8. What is the purpose of the `done` callback in Mocha?
   - A) To initiate the test
   - B) To signal the test is complete
   - C) To skip the test
   - D) To run the test multiple times

9. How do you handle errors in async functions using `async/await` in tests?
   - A) Using `try/catch` blocks
   - B) Using `done` callback
   - C) Using timeouts
   - D) By ignoring errors

10. Why is it important to restore stubs after each test?
    - A) To reduce test coverage
    - B) To ensure tests run in isolation
    - C) To speed up tests
    - D) To increase test complexity

### Answers

1. B) To verify correct handling of async operations
2. A) `done` callback
3. B) By returning the promise from the test
4. C) `async/await`
5. C) Mocking and stubbing
6. B) Using Sinon stubs
7. A) `before`
8. B) To signal the test is complete
9. A) Using `try/catch` blocks
10. B) To ensure tests run in isolation

## How to Write Integration Tests with a Small Node Server

### Introduction

Integration tests verify that different parts of a system work together as expected. This involves testing multiple components such as databases, APIs, and other services. In this guide, we'll focus on writing integration tests for a small Node.js server using Mocha and Chai.

### Setting Up the Node Server

We'll start by creating a simple Node.js server using Express.

#### Installing Dependencies

```bash
npm install express mocha chai chai-http
```

#### Creating the Server

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

let users = [{ id: 1, name: 'Alice' }];

app.get('/users', (req, res) => {
  res.json(users);
});

app.post('/users', (req, res) => {
  const user = req.body;
  users.push(user);
  res.status(201).json(user);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

module.exports = app;
```

### Writing Integration Tests

#### Setting Up Mocha and Chai

Create a test directory and a test file.

```bash
mkdir test
touch test/integrationTest.js
```

#### Integration Test File

```javascript
// test/integrationTest.js

const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../server');
const expect = chai.expect;

chai.use(chaiHttp);

describe('User API', function() {
  it('should retrieve all users', function(done) {
    chai.request(app)
      .get('/users')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('array');
        expect(res.body.length).to.equal(1);
        done();
      });
  });

  it('should create a new user', function(done) {
    const newUser = { id: 2, name: 'Bob' };
    chai.request(app)
      .post('/users')
      .send(newUser)
      .end((err, res) => {
        expect(res).to.have.status(201);
        expect(res.body).to.deep.equal(newUser);

        chai.request(app)
          .get('/users')
          .end((err, res) => {
            expect(res.body.length).to.equal(2);
            done();
          });
      });
  });
});
```

### Real-World Application

Let's extend our example to include more complex operations like updating and deleting users.

#### Updating the Server

```javascript
// server.js

app.put('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const userIndex = users.findIndex(user => user.id === userId);
  if (userIndex === -1) {
    return res.status(404).send('User not found');
  }
  users[userIndex] = req.body;
  res.json(users[userIndex]);
});

app.delete('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  users = users.filter(user => user.id !== userId);
  res.status(204).send();
});
```

#### Updating the Integration Tests

```javascript
// test/integrationTest.js

describe('User API', function() {
  it('should retrieve all users', function(done) {
    chai.request(app)
      .get('/users')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.an('array');
        expect(res.body.length).to.equal(1);
        done();
      });
  });

  it('should create a new user', function(done) {
    const newUser = { id: 2, name: 'Bob' };
    chai.request(app)
      .post('/users')
      .send(newUser)
      .end((err, res) => {
        expect(res).to.have.status(201);
        expect(res.body).to.deep.equal(newUser);

        chai.request(app)
          .get('/users')
          .end((err, res) => {
            expect(res.body.length).to.equal(2);
            done();
          });
      });
  });

  it('should update an existing user', function(done) {
    const updatedUser = { id: 1, name: 'Alice Updated' };
    chai.request(app)
      .put('/users/1')
      .send(updatedUser)
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.deep.equal(updatedUser);

        chai.request(app)
          .get('/users')
          .end((err, res) => {
            expect(res.body[0].name).to.equal('Alice Updated');
            done();
          });
      });
  });

  it('should delete a user', function(done) {
    chai.request(app)
      .delete('/users/1')
      .end((err, res) => {
        expect(res).to.have.status(204);

        chai.request(app)
          .get('/users')
          .end((err, res) => {
            expect(res.body.length).to.equal(1);
            expect(res.body[0].id).to.equal(2);
            done();
          });
      });
  });
});
```

### End of Chapter Multiple Choice Questions

1. What is the primary purpose of integration tests?
   - A) To test individual functions in isolation
   - B) To ensure different parts of the system work together
   - C) To check the syntax of the code
   - D) To test the user interface

2. Which library is used to make HTTP requests in the tests?
   - A) Mocha
   - B) Express
   - C) Chai
   - D) Chai-http

3. How do you verify the status code of an HTTP response in Chai?
   - A) `expect(res).status(200)`
   - B) `expect(res).to.have.status(200)`
   - C) `expect(res).equal(200)`
   - D) `expect(res).toBe(200)`

4. Which method is used to send a POST request in Chai-http?
   - A) `chai.request(app).send()`
   - B) `chai.request(app).post()`
   - C) `chai.request(app).put()`
   - D) `chai.request(app).get()`

5. What does the `done` function signify in Mocha tests?
   - A) The start of a test
   - B) The end of a test
   - C) A failed test
   - D) An ignored test

6. What status code is commonly used to indicate a successful creation of a resource?
   - A) 200
   - B) 201
   - C) 204
   - D) 404

7. How can you test updating a resource in Chai-http?
   - A) Using `chai.request(app).put()`
   - B) Using `chai.request(app).get()`
   - C) Using `chai.request(app).delete()`
   - D) Using `chai.request(app).post()`

8. Which HTTP method is used to delete a resource?
   - A) GET
   - B) POST
   - C) PUT
   - D) DELETE

9. What is the purpose of the `afterEach` hook in Mocha?
   - A) To run before each test
   - B) To run once before all tests
   - C) To run after each test
   - D) To run once after all tests

10. How do you ensure an array response in Chai?
    - A) `expect(res.body).to.be.a('object')`
    - B) `expect(res.body).to.be.a('array')`
    - C) `expect(res.body).to.equal('array')`
    - D) `expect(res.body).to.have.array`

### Answers

1. B) To ensure different parts of the system work together
2. D) Chai-http
3. B) `expect(res).to.have.status(200)`
4. B) `chai.request(app).post()`
5. B) The end of a test
6. B) 201
7. A) Using `chai.request(app).put()`
8. D) DELETE
9. C) To run after each test
10. B) `expect(res.body).to.be.a('array')`
