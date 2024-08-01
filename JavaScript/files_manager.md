# Creating an API with Express

Express is a web application framework for Node.js, designed for building web applications and APIs. It simplifies the process of creating server-side applications, handling requests, and defining routes.

## Objectives
By the end of this guide, you will be able to:
1. Set up an Express application.
2. Create basic routes.
3. Handle different types of requests.
4. Integrate middleware.
5. Connect to a database.
6. Deploy an Express application.

## Setting Up an Express Application

### Step 1: Install Node.js and npm
Make sure you have Node.js and npm (Node Package Manager) installed. You can download them from [Node.js official website](https://nodejs.org/).

### Step 2: Initialize a New Project
Create a new directory for your project and navigate into it using the terminal. Then, run the following command to initialize a new Node.js project:

```bash
npm init -y
```

This will create a `package.json` file with default settings.

### Step 3: Install Express
Install Express by running:

```bash
npm install express
```

### Step 4: Create the Server File
Create a file named `server.js` in your project directory. This file will contain the code to set up your server.

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

### Step 5: Run the Server
Start your server by running:

```bash
node server.js
```

You should see a message indicating that the server is running. Open your browser and go to `http://localhost:3000`. You should see "Hello, World!".

## Creating Basic Routes

Routes define the endpoints of your API and specify how the server should respond to various requests.

### Example Routes
Add the following routes to your `server.js` file:

```javascript
app.get('/api/users', (req, res) => {
  res.send('Get all users');
});

app.post('/api/users', (req, res) => {
  res.send('Add a user');
});

app.put('/api/users/:id', (req, res) => {
  res.send(`Update user with ID ${req.params.id}`);
});

app.delete('/api/users/:id', (req, res) => {
  res.send(`Delete user with ID ${req.params.id}`);
});
```

### Explanation
- `GET /api/users`: Retrieve all users.
- `POST /api/users`: Add a new user.
- `PUT /api/users/:id`: Update a user with a specific ID.
- `DELETE /api/users/:id`: Delete a user with a specific ID.

## Handling Different Types of Requests

Express makes it easy to handle different HTTP methods, such as GET, POST, PUT, and DELETE.

### Example
To handle a POST request and process the incoming data, use the `express.json()` middleware to parse JSON request bodies:

```javascript
app.use(express.json());

app.post('/api/users', (req, res) => {
  const newUser = req.body;
  res.send(`User added: ${JSON.stringify(newUser)}`);
});
```

## Integrating Middleware

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application’s request-response cycle.

### Example
Create a simple logging middleware:

```javascript
const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
};

app.use(logger);
```

## Connecting to a Database

Express can be integrated with various databases. Here, we'll use MongoDB as an example.

### Step 1: Install Mongoose
Mongoose is an ODM (Object Data Modeling) library for MongoDB and Node.js. Install it by running:

```bash
npm install mongoose
```

### Step 2: Connect to MongoDB
In your `server.js`, add the following code to connect to a MongoDB database:

```javascript
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/mydatabase', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Error connecting to MongoDB', err);
});
```

### Step 3: Define a Schema and Model
Create a `User` model:

```javascript
const userSchema = new mongoose.Schema({
  name: String,
  age: Number
});

const User = mongoose.model('User', userSchema);
```

### Step 4: Use the Model in Routes
Update your routes to use the `User` model:

```javascript
app.get('/api/users', async (req, res) => {
  const users = await User.find();
  res.send(users);
});

app.post('/api/users', async (req, res) => {
  const newUser = new User(req.body);
  await newUser.save();
  res.send(newUser);
});
```

## Deploying an Express Application

### Step 1: Prepare for Deployment
Ensure your application is production-ready by setting environment variables and configuring your server to handle production settings.

### Step 2: Use a Cloud Provider
Deploy your application using a cloud provider like Heroku, AWS, or DigitalOcean.

### Example Deployment on Heroku
1. Install the Heroku CLI.
2. Log in to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create`
4. Push your code to Heroku: `git push heroku main`

## Real-World Application Example

Consider building an API for a task management application where users can create, read, update, and delete tasks.

### Example Routes
```javascript
app.get('/api/tasks', (req, res) => {
  res.send('Get all tasks');
});

app.post('/api/tasks', (req, res) => {
  res.send('Add a task');
});

app.put('/api/tasks/:id', (req, res) => {
  res.send(`Update task with ID ${req.params.id}`);
});

app.delete('/api/tasks/:id', (req, res) => {
  res.send(`Delete task with ID ${req.params.id}`);
});
```

### Connecting to MongoDB
```javascript
const taskSchema = new mongoose.Schema({
  title: String,
  description: String,
  completed: Boolean
});

const Task = mongoose.model('Task', taskSchema);

app.get('/api/tasks', async (req, res) => {
  const tasks = await Task.find();
  res.send(tasks);
});

app.post('/api/tasks', async (req, res) => {
  const newTask = new Task(req.body);
  await newTask.save();
  res.send(newTask);
});
```

## Technical End-of-Chapter Questions

1. **What is Express?**
   - A. A web application framework for Node.js.
   - B. A database management system.
   - C. A front-end JavaScript library.
   - D. A programming language.

2. **Which command initializes a new Node.js project?**
   - A. `npm install express`
   - B. `node init -y`
   - C. `npm init -y`
   - D. `express new project`

3. **What does `app.get('/', (req, res) => { res.send('Hello, World!'); });` do?**
   - A. Handles POST requests to the root URL.
   - B. Sends 'Hello, World!' when a GET request is made to the root URL.
   - C. Logs requests to the console.
   - D. Connects to a MongoDB database.

4. **What middleware function is used to parse JSON request bodies?**
   - A. `express.urlencoded()`
   - B. `express.static()`
   - C. `express.json()`
   - D. `express.logger()`

5. **How do you start an Express server on port 3000?**
   - A. `node app.js`
   - B. `node server`
   - C. `node server.js`
   - D. `express start`

6. **Which method is used to define a schema in Mongoose?**
   - A. `mongoose.model()`
   - B. `mongoose.connect()`
   - C. `mongoose.Schema()`
   - D. `mongoose.create()`

7. **What is the purpose of middleware in Express?**
   - A. To connect to databases.
   - B. To handle static files.
   - C. To process requests and responses.
   - D. To render HTML pages.

8. **Which HTTP method is typically used to update a resource?**
   - A. GET
   - B. POST
   - C. PUT
   - D. DELETE

9. **What is the default port number used in the example server?**
   - A. 8080
   - B. 80
   - C. 3000
   - D. 5000

10. **How do you deploy an Express application to Heroku?**
    - A. `heroku deploy`
    - B. `git push heroku main`
    - C. `heroku push origin main`
    - D. `git deploy heroku main`

## Answers to Technical End-of-Chapter Questions

1. **A. A web application framework for Node.js.**
2. **C. `npm init -y`**
3. **B. Sends

 'Hello, World!' when a GET request is made to the root URL.**
4. **C. `express.json()`**
5. **C. `node server.js`**
6. **C. `mongoose.Schema()`**
7. **C. To process requests and responses.**
8. **C. PUT**
9. **C. 3000**
10. **B. `git push heroku main`**

# User Authentication

Authentication is the process of verifying the identity of a user. It's a crucial part of web application security. This guide will walk you through the basics of user authentication using JSON Web Tokens (JWT) with an Express application.

## Objectives
By the end of this guide, you will be able to:
1. Set up an Express application.
2. Implement user registration and login.
3. Use JWT for authentication.
4. Protect routes with authentication middleware.

## Setting Up an Express Application

### Step 1: Install Node.js and npm
Ensure Node.js and npm (Node Package Manager) are installed. Download them from [Node.js official website](https://nodejs.org/).

### Step 2: Initialize a New Project
Create a new directory for your project, navigate into it using the terminal, and run:

```bash
npm init -y
```

### Step 3: Install Required Packages
Install Express, bcrypt (for hashing passwords), jsonwebtoken (for generating JWTs), and mongoose (for database interaction):

```bash
npm install express bcrypt jsonwebtoken mongoose
```

### Step 4: Create the Server File
Create a file named `server.js`:

```javascript
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const app = express();
const port = 3000;

app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/auth_demo', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Error connecting to MongoDB', err);
});

// User schema and model
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

const User = mongoose.model('User', userSchema);

// Start server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```

## Implementing User Registration and Login

### User Registration

When a user registers, we need to hash their password before storing it in the database.

```javascript
// Register route
app.post('/register', async (req, res) => {
  try {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();
    res.status(201).send('User registered');
  } catch (err) {
    res.status(400).send('Error registering user');
  }
});
```

### User Login

When a user logs in, we compare the provided password with the stored hashed password and generate a JWT if they match.

```javascript
// Login route
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user) {
      return res.status(400).send('Invalid credentials');
    }
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(400).send('Invalid credentials');
    }
    const token = jwt.sign({ id: user._id }, 'your_jwt_secret', { expiresIn: '1h' });
    res.json({ token });
  } catch (err) {
    res.status(500).send('Error logging in');
  }
});
```

## Using JWT for Authentication

JWTs are used to securely transmit information between parties. When a user logs in, they receive a JWT, which they include in the Authorization header of their requests to protected routes.

### Protecting Routes with Middleware

Create a middleware function to verify JWTs:

```javascript
// Middleware to protect routes
const authenticateJWT = (req, res, next) => {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send('Access denied');
  }
  try {
    const verified = jwt.verify(token, 'your_jwt_secret');
    req.user = verified;
    next();
  } catch (err) {
    res.status(400).send('Invalid token');
  }
};
```

### Protected Route Example

Add a protected route that only authenticated users can access:

```javascript
// Protected route
app.get('/protected', authenticateJWT, (req, res) => {
  res.send('This is a protected route');
});
```

## Real-World Application Example

Consider a task management application where users need to authenticate to create and view their tasks.

### Example Routes

```javascript
app.post('/tasks', authenticateJWT, async (req, res) => {
  // Code to add a new task
  res.send('Task created');
});

app.get('/tasks', authenticateJWT, async (req, res) => {
  // Code to get user's tasks
  res.send('Tasks retrieved');
});
```

## Technical End-of-Chapter Questions

1. **What is the purpose of bcrypt in user authentication?**
   - A. Encrypt user data.
   - B. Hash passwords.
   - C. Generate JWTs.
   - D. Connect to MongoDB.

2. **Which package is used to generate JSON Web Tokens?**
   - A. express
   - B. bcrypt
   - C. mongoose
   - D. jsonwebtoken

3. **How do you protect a route in Express using JWT?**
   - A. By hashing the route.
   - B. By using a middleware function.
   - C. By storing the route in the database.
   - D. By encrypting the route.

4. **Which HTTP method is typically used for user registration?**
   - A. GET
   - B. POST
   - C. PUT
   - D. DELETE

5. **What does the `jwt.sign` function do?**
   - A. Verifies a JWT.
   - B. Decodes a JWT.
   - C. Generates a JWT.
   - D. Encrypts a JWT.

6. **How do you include the JWT in the request to a protected route?**
   - A. In the body.
   - B. In the URL.
   - C. In the Authorization header.
   - D. In a cookie.

7. **What does the `authenticateJWT` middleware function do?**
   - A. Generates a JWT.
   - B. Hashes the user's password.
   - C. Verifies the JWT and attaches the user to the request.
   - D. Connects to the database.

8. **Which status code is returned for an invalid login attempt?**
   - A. 200
   - B. 201
   - C. 400
   - D. 401

9. **What does the `express.json()` middleware do?**
   - A. Parses URL-encoded bodies.
   - B. Parses JSON request bodies.
   - C. Logs requests to the console.
   - D. Verifies JWTs.

10. **What does `bcrypt.compare` do?**
    - A. Compares the JWT with the user ID.
    - B. Compares the provided password with the stored hashed password.
    - C. Hashes the provided password.
    - D. Generates a JWT.

## Answers to Technical End-of-Chapter Questions

1. **B. Hash passwords.**
2. **D. jsonwebtoken**
3. **B. By using a middleware function.**
4. **B. POST**
5. **C. Generates a JWT.**
6. **C. In the Authorization header.**
7. **C. Verifies the JWT and attaches the user to the request.**
8. **C. 400**
9. **B. Parses JSON request bodies.**
10. **B. Compares the provided password with the stored hashed password.**

# Storing Data in MongoDB

MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. This guide will walk you through how to store data in MongoDB using Node.js and Mongoose.

## Objectives
By the end of this guide, you will be able to:
1. Set up a MongoDB database.
2. Connect to MongoDB using Mongoose.
3. Define schemas and models in Mongoose.
4. Perform CRUD (Create, Read, Update, Delete) operations.

## Setting Up MongoDB

### Step 1: Install MongoDB
Download and install MongoDB from [MongoDB's official website](https://www.mongodb.com/try/download/community).

### Step 2: Start the MongoDB Server
After installation, start the MongoDB server by running:

```bash
mongod
```

### Step 3: Install Required Packages
Create a new Node.js project and install Mongoose:

```bash
npm init -y
npm install mongoose
```

### Step 4: Connect to MongoDB
Create a file named `app.js` and set up the connection to MongoDB:

```javascript
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/mydatabase', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Error connecting to MongoDB', err);
});
```

## Defining Schemas and Models

In MongoDB, a schema defines the structure of the documents within a collection. A model is a constructor compiled from a schema.

### Step 5: Define a Schema
Define a schema for a simple user collection:

```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  age: { type: Number, required: true }
});
```

### Step 6: Create a Model
Create a model from the schema:

```javascript
const User = mongoose.model('User', userSchema);
```

## Performing CRUD Operations

### Step 7: Create a Document
Create a new user document and save it to the database:

```javascript
const createUser = async () => {
  const user = new User({
    name: 'John Doe',
    email: 'john.doe@example.com',
    age: 30
  });

  try {
    const savedUser = await user.save();
    console.log('User saved:', savedUser);
  } catch (err) {
    console.error('Error saving user:', err);
  }
};

createUser();
```

### Step 8: Read Documents
Fetch all users from the database:

```javascript
const getUsers = async () => {
  try {
    const users = await User.find();
    console.log('Users:', users);
  } catch (err) {
    console.error('Error fetching users:', err);
  }
};

getUsers();
```

### Step 9: Update a Document
Update a user's age based on their email:

```javascript
const updateUser = async (email) => {
  try {
    const updatedUser = await User.findOneAndUpdate(
      { email: email },
      { age: 35 },
      { new: true }
    );
    console.log('Updated user:', updatedUser);
  } catch (err) {
    console.error('Error updating user:', err);
  }
};

updateUser('john.doe@example.com');
```

### Step 10: Delete a Document
Delete a user based on their email:

```javascript
const deleteUser = async (email) => {
  try {
    const deletedUser = await User.findOneAndDelete({ email: email });
    console.log('Deleted user:', deletedUser);
  } catch (err) {
    console.error('Error deleting user:', err);
  }
};

deleteUser('john.doe@example.com');
```

## Real-World Application Example

Consider an e-commerce application where you need to store product information. The steps above can be adapted to create, read, update, and delete product documents in MongoDB.

### Example Product Schema and Model

```javascript
const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  price: { type: Number, required: true },
  category: { type: String, required: true }
});

const Product = mongoose.model('Product', productSchema);
```

### Example Product CRUD Operations

```javascript
// Create a new product
const createProduct = async () => {
  const product = new Product({
    name: 'Laptop',
    price: 999.99,
    category: 'Electronics'
  });

  try {
    const savedProduct = await product.save();
    console.log('Product saved:', savedProduct);
  } catch (err) {
    console.error('Error saving product:', err);
  }
};

createProduct();

// Fetch all products
const getProducts = async () => {
  try {
    const products = await Product.find();
    console.log('Products:', products);
  } catch (err) {
    console.error('Error fetching products:', err);
  }
};

getProducts();

// Update a product's price
const updateProduct = async (name) => {
  try {
    const updatedProduct = await Product.findOneAndUpdate(
      { name: name },
      { price: 899.99 },
      { new: true }
    );
    console.log('Updated product:', updatedProduct);
  } catch (err) {
    console.error('Error updating product:', err);
  }
};

updateProduct('Laptop');

// Delete a product
const deleteProduct = async (name) => {
  try {
    const deletedProduct = await Product.findOneAndDelete({ name: name });
    console.log('Deleted product:', deletedProduct);
  } catch (err) {
    console.error('Error deleting product:', err);
  }
};

deleteProduct('Laptop');
```

## Technical End-of-Chapter Questions

1. **What does the `mongoose.connect` function do?**
   - A. Creates a new schema.
   - B. Connects to a MongoDB database.
   - C. Deletes a document.
   - D. Updates a document.

2. **What is the purpose of a schema in MongoDB?**
   - A. To define the structure of the documents in a collection.
   - B. To create a new collection.
   - C. To connect to the database.
   - D. To perform CRUD operations.

3. **Which of the following is used to create a new document in MongoDB?**
   - A. `find()`
   - B. `save()`
   - C. `update()`
   - D. `delete()`

4. **How do you fetch all documents from a collection?**
   - A. `User.save()`
   - B. `User.find()`
   - C. `User.update()`
   - D. `User.delete()`

5. **What does `findOneAndUpdate` do?**
   - A. Finds and deletes a document.
   - B. Finds and updates a document.
   - C. Finds and creates a document.
   - D. Finds and reads a document.

6. **How do you delete a document based on a condition?**
   - A. `User.findOneAndDelete()`
   - B. `User.find()`
   - C. `User.save()`
   - D. `User.update()`

7. **Which package is used to interact with MongoDB in Node.js?**
   - A. `express`
   - B. `mongoose`
   - C. `bcrypt`
   - D. `jsonwebtoken`

8. **What does the `new` option in `findOneAndUpdate` do?**
   - A. Ensures a new document is created if no match is found.
   - B. Returns the updated document.
   - C. Returns the old document.
   - D. Ensures no document is deleted.

9. **What is the correct way to define a schema in Mongoose?**
   - A. `const schema = new Schema({})`
   - B. `const schema = new mongoose.Schema({})`
   - C. `const schema = new Model({})`
   - D. `const schema = new mongoose.Model({})`

10. **What type of database is MongoDB?**
    - A. Relational
    - B. NoSQL
    - C. Graph
    - D. Key-Value

## Answers to Technical End-of-Chapter Questions

1. **B. Connects to a MongoDB database.**
2. **A. To define the structure of the documents in a collection.**
3. **B. `save()`**
4. **B. `User.find()`**
5. **B. Finds and updates a document.**
6. **A. `User.findOneAndDelete()`**
7. **B. `mongoose`**
8. **B. Returns the updated document.**
9. **B. `const schema = new mongoose.Schema({})`**
10. **B. NoSQL**

# Storing Temporary Data in Redis

Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. This guide will walk you through how to store temporary data in Redis using Node.js.

## Objectives
By the end of this guide, you will be able to:
1. Set up a Redis server.
2. Connect to Redis using Node.js.
3. Perform basic Redis operations.
4. Apply Redis for caching and temporary data storage in real-world projects.

## Setting Up Redis

### Step 1: Install Redis
Download and install Redis from [Redis's official website](https://redis.io/download).

### Step 2: Start the Redis Server
After installation, start the Redis server by running:

```bash
redis-server
```

### Step 3: Install Required Packages
Create a new Node.js project and install the `redis` package:

```bash
npm init -y
npm install redis
```

### Step 4: Connect to Redis
Create a file named `app.js` and set up the connection to Redis:

```javascript
const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Connected to Redis');
});

client.on('error', (err) => {
  console.error('Error connecting to Redis', err);
});
```

## Performing Basic Redis Operations

### Step 5: Set and Get Data
Store a key-value pair in Redis and retrieve it:

```javascript
// Set a value
client.set('name', 'John Doe', redis.print);

// Get a value
client.get('name', (err, reply) => {
  if (err) throw err;
  console.log('Name:', reply);
});
```

### Step 6: Set Data with an Expiry
Store a key-value pair with a time-to-live (TTL) in Redis:

```javascript
client.setex('session_id', 3600, 'abc123', redis.print);
```

### Step 7: Delete Data
Remove a key from Redis:

```javascript
client.del('name', redis.print);
```

## Using Redis in Real-World Projects

### Example: Caching API Responses

In real-world applications, Redis can be used to cache API responses to improve performance.

```javascript
const axios = require('axios');

const fetchData = async (url) => {
  client.get(url, async (err, data) => {
    if (err) throw err;

    if (data) {
      console.log('Cache hit');
      return JSON.parse(data);
    } else {
      console.log('Cache miss');
      const response = await axios.get(url);
      client.setex(url, 3600, JSON.stringify(response.data));
      return response.data;
    }
  });
};

fetchData('https://api.example.com/data');
```

### Example: Storing Session Data

Redis can be used to store session data temporarily for web applications.

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis')(session);

app.use(session({
  store: new RedisStore({ client: client }),
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false, maxAge: 60000 } // 1 minute for demonstration
}));

app.get('/', (req, res) => {
  if (!req.session.views) {
    req.session.views = 1;
  } else {
    req.session.views++;
  }
  res.send(`Number of views: ${req.session.views}`);
});
```

## Technical End-of-Chapter Questions

1. **What does the `redis.createClient` function do?**
   - A. Starts the Redis server.
   - B. Connects to a Redis server.
   - C. Deletes a key-value pair.
   - D. Sets a key-value pair.

2. **How do you store a key-value pair in Redis?**
   - A. `client.get()`
   - B. `client.set()`
   - C. `client.delete()`
   - D. `client.create()`

3. **What does the `setex` method do?**
   - A. Sets a value with an expiry time.
   - B. Deletes a key-value pair.
   - C. Gets a value from Redis.
   - D. Expires a value immediately.

4. **How do you delete a key from Redis?**
   - A. `client.set()`
   - B. `client.get()`
   - C. `client.del()`
   - D. `client.expire()`

5. **What is the primary purpose of using Redis in web applications?**
   - A. Permanent data storage.
   - B. Temporary data storage and caching.
   - C. Running server-side scripts.
   - D. Creating databases.

6. **How can you handle a Redis connection error in Node.js?**
   - A. By using `client.on('error', callback)`.
   - B. By using `client.set()`.
   - C. By using `client.get()`.
   - D. By using `client.del()`.

7. **Which package is required to connect to Redis in Node.js?**
   - A. `mysql`
   - B. `mongodb`
   - C. `redis`
   - D. `axios`

8. **How do you check if a value is present in the Redis cache?**
   - A. `client.set()`
   - B. `client.get()`
   - C. `client.create()`
   - D. `client.delete()`

9. **What is the command to set a key with a 1-hour expiry in Redis?**
   - A. `client.set()`
   - B. `client.setex(key, 3600, value)`
   - C. `client.get()`
   - D. `client.expire()`

10. **How can Redis improve the performance of web applications?**
    - A. By providing permanent storage solutions.
    - B. By caching frequently accessed data.
    - C. By running complex algorithms.
    - D. By providing user authentication.

## Answers to Technical End-of-Chapter Questions

1. **B. Connects to a Redis server.**
2. **B. `client.set()`**
3. **A. Sets a value with an expiry time.**
4. **C. `client.del()`**
5. **B. Temporary data storage and caching.**
6. **A. By using `client.on('error', callback)`.**
7. **C. `redis`**
8. **B. `client.get()`**
9. **B. `client.setex(key, 3600, value)`**
10. **B. By caching frequently accessed data.**

# Setting Up and Using a Background Worker

A background worker is a process that runs tasks in the background without blocking the main application. This is particularly useful for tasks that take a long time to complete, such as sending emails, processing files, or making API calls. Using background workers can significantly improve the performance and responsiveness of your application.

## Objectives
By the end of this guide, you will be able to:
1. Set up a background worker.
2. Use a background worker to handle tasks.
3. Apply background workers in real-world projects.

## Setting Up a Background Worker

### Step 1: Install Required Packages
We'll use Node.js with the `bull` package, a popular library for background job processing.

```bash
npm init -y
npm install bull
npm install redis
```

### Step 2: Set Up Redis
Redis is required to manage the job queue. Make sure you have Redis installed and running.

### Step 3: Create a Job Queue
Create a file named `worker.js` to define the job queue and process the jobs.

```javascript
const Queue = require('bull');
const redis = require('redis');

// Create a connection to Redis
const client = redis.createClient();

// Create a queue
const jobQueue = new Queue('jobQueue', {
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

// Process the job queue
jobQueue.process(async (job) => {
  console.log(`Processing job with id ${job.id} and data:`, job.data);
  // Simulate a long-running task
  await new Promise(resolve => setTimeout(resolve, 5000));
  console.log(`Job ${job.id} completed`);
});

// Handle job completion
jobQueue.on('completed', (job) => {
  console.log(`Job ${job.id} has been completed`);
});

// Handle job failure
jobQueue.on('failed', (job, err) => {
  console.log(`Job ${job.id} failed with error ${err.message}`);
});
```

### Step 4: Add Jobs to the Queue
Create another file named `app.js` to add jobs to the queue.

```javascript
const Queue = require('bull');

// Create a queue
const jobQueue = new Queue('jobQueue', {
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

// Add a job to the queue
const addJobToQueue = async (data) => {
  const job = await jobQueue.add(data);
  console.log(`Job with id ${job.id} added to the queue`);
};

// Example usage
addJobToQueue({ email: 'user@example.com', message: 'Welcome to our service!' });
```

## Using Background Workers in Real-World Projects

### Example: Sending Welcome Emails

When a new user registers, we can use a background worker to send a welcome email.

1. Add a job to the queue when a user registers:

```javascript
const express = require('express');
const Queue = require('bull');

const app = express();
app.use(express.json());

const jobQueue = new Queue('jobQueue', {
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

app.post('/register', async (req, res) => {
  const { email, username } = req.body;
  // Simulate user registration logic
  console.log(`User ${username} registered with email ${email}`);
  // Add job to send welcome email
  await jobQueue.add({ email, message: `Welcome, ${username}!` });
  res.send('User registered successfully');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

2. Process the job to send the email:

```javascript
const nodemailer = require('nodemailer');
const Queue = require('bull');

const jobQueue = new Queue('jobQueue', {
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'your-email@gmail.com',
    pass: 'your-email-password'
  }
});

jobQueue.process(async (job) => {
  const { email, message } = job.data;
  await transporter.sendMail({
    from: 'your-email@gmail.com',
    to: email,
    subject: 'Welcome!',
    text: message
  });
  console.log(`Email sent to ${email}`);
});
```

## Technical End-of-Chapter Questions

1. **What is a background worker used for?**
   - A. Running tasks in the main thread.
   - B. Running tasks in the background without blocking the main application.
   - C. Storing data permanently.
   - D. Managing user sessions.

2. **Which package is commonly used for background job processing in Node.js?**
   - A. `express`
   - B. `mongoose`
   - C. `bull`
   - D. `axios`

3. **What role does Redis play in background job processing?**
   - A. It stores permanent data.
   - B. It manages the job queue.
   - C. It handles HTTP requests.
   - D. It serves static files.

4. **Which method is used to add a job to a queue in Bull?**
   - A. `queue.create()`
   - B. `queue.process()`
   - C. `queue.add()`
   - D. `queue.delete()`

5. **How do you handle job completion in Bull?**
   - A. By using the `on('complete')` event.
   - B. By using the `on('done')` event.
   - C. By using the `on('finished')` event.
   - D. By using the `on('completed')` event.

6. **What is the purpose of the `queue.process()` method in Bull?**
   - A. To add a job to the queue.
   - B. To remove a job from the queue.
   - C. To define how jobs should be processed.
   - D. To connect to Redis.

7. **How can you simulate a long-running task in a job processor?**
   - A. By using `setTimeout()`.
   - B. By using `setInterval()`.
   - C. By using `setImmediate()`.
   - D. By using `setJobTimeout()`.

8. **Which module can be used to send emails in Node.js?**
   - A. `express`
   - B. `nodemailer`
   - C. `axios`
   - D. `redis`

9. **What should you do if a job fails in Bull?**
   - A. Log the error and retry the job.
   - B. Delete the job immediately.
   - C. Ignore the job.
   - D. Restart the queue.

10. **What is the purpose of using background workers in web applications?**
    - A. To handle synchronous tasks only.
    - B. To improve performance by offloading long-running tasks.
    - C. To manage database connections.
    - D. To serve static files.

## Answers to Technical End-of-Chapter Questions

1. **B. Running tasks in the background without blocking the main application.**
2. **C. `bull`**
3. **B. It manages the job queue.**
4. **C. `queue.add()`**
5. **D. By using the `on('completed')` event.**
6. **C. To define how jobs should be processed.**
7. **A. By using `setTimeout()`.**
8. **B. `nodemailer`**
9. **A. Log the error and retry the job.**
10. **B. To improve performance by offloading long-running tasks.**
