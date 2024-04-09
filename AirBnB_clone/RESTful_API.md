# Understanding RESTful APIs: Principles, Implementation, and Real-World Applications

In the rapidly evolving landscape of web development, understanding the fundamentals of RESTful APIs is essential for building modern, scalable, and interoperable applications. Representational State Transfer (REST) is not merely a set of guidelines but an architectural style that governs the design of networked applications. This note delves into the key principles of REST, explores its real-world implementation, and demonstrates its application in various projects.

## 1. What REST means

REST, which stands for Representational State Transfer, is an architectural style used for designing networked applications. It is based on a set of principles that define how distributed systems should behave and interact with each other over the web. Here's a breakdown of what REST entails:

### Key Principles of REST:

1. **Client-Server Architecture:** REST separates the client and server into two distinct parts, allowing them to evolve independently. This improves scalability and simplifies the overall architecture.

2. **Statelessness:** Each request from a client to the server must contain all the information necessary to understand the request, meaning the server does not need to store any session state about the client. This enhances reliability and scalability.

3. **Uniform Interface:** RESTful systems should have a uniform interface, which means that similar endpoints across different resources should share the same syntax and behavior. This simplifies the client's understanding of how to interact with the server.

4. **Cacheability:** Responses from the server should explicitly indicate whether they can be cached or not. Caching improves performance and reduces the load on the server.

5. **Layered System:** A client may not be aware of whether it is interacting with the actual server or an intermediary, such as a load balancer or proxy server. This enhances flexibility and scalability by allowing intermediaries to be added or removed without affecting the client-server interaction.

### How REST is Applied in Real-World Projects:

**Example: Building a RESTful API for a Blogging Platform**

Consider a scenario where you're tasked with developing a RESTful API for a blogging platform. Here's how you can apply REST principles:

1. **Resource Identification:** Identify the main resources of your application, such as posts, users, and comments.

2. **Uniform Resource Locator (URL) Structure:** Design URLs that represent resources and their actions in a hierarchical manner. For example:
   - `/posts`: Retrieve all posts
   - `/posts/{id}`: Retrieve a specific post by its ID
   - `/users/{id}/posts`: Retrieve posts created by a specific user

3. **HTTP Methods:** Use HTTP methods to perform actions on resources:
   - `GET`: Retrieve resource(s)
   - `POST`: Create a new resource
   - `PUT`: Update an existing resource
   - `DELETE`: Delete a resource

4. **Status Codes:** Respond with appropriate HTTP status codes to indicate the success or failure of requests:
   - `200 OK`: Successful retrieval
   - `201 Created`: Successful resource creation
   - `404 Not Found`: Resource not found
   - `500 Internal Server Error`: Server-side error

5. **Stateless Communication:** Ensure that each request to the server contains all the necessary information. For example, authentication tokens can be included in the request headers.

By adhering to REST principles, you can develop a scalable, maintainable, and interoperable API that can be easily consumed by various clients, such as web browsers, mobile apps, and other servers. This promotes a clear and consistent interaction between clients and servers, enhancing the overall user experience of your application.

## 2. What API means

API, which stands for Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information. 

### Key Components of an API:

1. **Endpoints:** An endpoint is a specific URL or URI that an API exposes, representing a particular resource or action. For example:
   - `https://api.example.com/users`: Endpoint for retrieving user data
   - `https://api.example.com/posts`: Endpoint for retrieving post data

2. **Methods:** APIs use HTTP methods to specify the actions that can be performed on resources:
   - `GET`: Retrieves data from the server
   - `POST`: Creates new data on the server
   - `PUT`: Updates existing data on the server
   - `DELETE`: Removes data from the server

3. **Parameters:** APIs often accept parameters in requests to filter, sort, or paginate data. Parameters are usually passed as part of the URL query string or in the request body.

4. **Response Format:** APIs return data in a specific format, commonly JSON (JavaScript Object Notation) or XML (eXtensible Markup Language). JSON is lightweight, human-readable, and easy to parse, making it the preferred choice for many modern APIs.

### How APIs are Applied in Real-World Projects:

**Example: Integrating a Payment Gateway**

Consider a scenario where you're building an e-commerce website and need to integrate a payment gateway to process transactions. Here's how APIs are involved:

1. **Integration with Payment Gateway API:** You would use the payment gateway's API to facilitate communication between your website and the payment provider's servers. This involves sending payment details securely to the gateway and receiving confirmation of successful transactions.

2. **Endpoint Usage:** The payment gateway API provides endpoints for various actions, such as initiating payments, querying transaction status, and managing customer information. For instance:
   - `POST https://api.paymentgateway.com/payments`: Endpoint for initiating a payment
   - `GET https://api.paymentgateway.com/payments/{id}`: Endpoint for retrieving payment status

3. **HTTP Methods:** You would use appropriate HTTP methods to interact with the API. For example:
   - `POST`: Used to send payment details and initiate transactions
   - `GET`: Used to retrieve transaction status or retrieve payment history

4. **Handling Responses:** The payment gateway API returns responses in a predefined format, such as JSON. Your website's backend would parse these responses to extract relevant information, such as transaction IDs or payment statuses.

By leveraging APIs, you can seamlessly integrate third-party services into your applications, extending their functionality and providing enhanced user experiences. APIs facilitate interoperability between different systems, allowing developers to focus on building core features without reinventing the wheel.

## 3. What are other types of APIs

While RESTful APIs are common in modern web development, there are other types of APIs that serve different purposes and use different communication protocols. Here are some notable examples:

### 1. SOAP APIs (Simple Object Access Protocol):

SOAP is a protocol for exchanging structured information in the implementation of web services. SOAP APIs use XML as the messaging format and typically operate over HTTP or SMTP. SOAP APIs are known for their strong adherence to standards and support for advanced features such as security and transactions.

**Example Usage:** Integrating with enterprise systems or legacy applications that require robust security and transaction support.

### 2. GraphQL APIs:

GraphQL is a query language for APIs that enables clients to request only the data they need, in the format they specify. Unlike REST APIs, which expose a fixed set of endpoints, GraphQL APIs have a single endpoint and allow clients to define the structure of their requests. This provides greater flexibility and efficiency in data fetching.

**Example Usage:** Building client applications that require fine-grained control over the data they retrieve, such as social media feeds or data-intensive applications.

### 3. gRPC APIs:

gRPC is a high-performance, open-source RPC (Remote Procedure Call) framework developed by Google. It uses Protocol Buffers as the interface definition language (IDL) and HTTP/2 as the transport protocol. gRPC APIs enable efficient communication between distributed systems and support features such as authentication, load balancing, and bidirectional streaming.

**Example Usage:** Building microservices architectures or distributed systems where performance and scalability are critical.

### 4. WebSockets:

WebSockets is a protocol that enables full-duplex communication between a client and a server over a single, long-lived connection. Unlike traditional HTTP requests, which are stateless and short-lived, WebSockets allow for real-time, bidirectional communication between clients and servers. WebSockets are commonly used in applications that require low-latency, interactive features such as chat applications or real-time collaboration tools.

**Example Usage:** Implementing real-time features in web applications, such as live chat or multiplayer games.

### 5. File Transfer APIs:

File Transfer APIs enable the transfer of files between different systems or devices. These APIs typically use protocols such as FTP (File Transfer Protocol), SFTP (SSH File Transfer Protocol), or HTTP(S) for file transmission. File Transfer APIs are commonly used in applications that involve sharing or synchronizing files, such as cloud storage services or content management systems.

**Example Usage:** Integrating with cloud storage providers to upload or download files programmatically.

By understanding the different types of APIs available, developers can choose the most suitable option for their specific use case, taking into account factors such as performance, scalability, and ease of use. Each type of API offers its own advantages and trade-offs, allowing developers to tailor their solutions to meet the unique requirements of their projects.

## 4. What is a REST API

A REST API (Representational State Transfer Application Programming Interface) is a type of web API that follows the principles of REST architectural style. It allows different software applications to communicate with each other over the internet, enabling them to exchange data and perform various actions.

### Key Components of a REST API:

1. **Resources:** In a REST API, everything is treated as a resource, which can be a piece of data or an object. Each resource is uniquely identified by a URI (Uniform Resource Identifier), and multiple representations of the resource can exist, such as JSON or XML.

2. **HTTP Methods:** REST APIs use HTTP methods to perform actions on resources:
   - `GET`: Retrieve data from the server.
   - `POST`: Create new data on the server.
   - `PUT`: Update existing data on the server.
   - `DELETE`: Remove data from the server.
   - `PATCH`: Update partial data on the server.
   - `HEAD`: Retrieve metadata about a resource.
   - `OPTIONS`: Retrieve information about the communication options available for a resource.

3. **Uniform Interface:** REST APIs have a uniform interface, meaning that they use standard methods and data formats for communication. This simplifies the interaction between clients and servers and allows for easy integration with different systems.

4. **Statelessness:** REST APIs are stateless, which means that each request from a client to the server contains all the information necessary to understand the request. The server does not store any client state between requests, improving scalability and reliability.

### Example Code Snippets:

Here's an example of how you might implement a simple REST API using Node.js and Express.js:

```javascript
const express = require('express');
const app = express();
const port = 3000;

let books = [
    { id: 1, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald' },
    { id: 2, title: 'To Kill a Mockingbird', author: 'Harper Lee' },
];

app.use(express.json());

// Get all books
app.get('/books', (req, res) => {
    res.json(books);
});

// Get a specific book by ID
app.get('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('Book not found');
    res.json(book);
});

// Create a new book
app.post('/books', (req, res) => {
    const book = {
        id: books.length + 1,
        title: req.body.title,
        author: req.body.author
    };
    books.push(book);
    res.status(201).json(book);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

In this example, we define routes for retrieving all books, retrieving a specific book by ID, and creating a new book. We use HTTP methods (`GET` and `POST`) to perform these actions, adhering to REST principles.

By understanding REST APIs and how to implement them, developers can build scalable and interoperable web services that can be easily consumed by clients across different platforms and devices.

## 5. How to request REST API

Requesting a REST API involves sending HTTP requests to the API's endpoints in order to retrieve, create, update, or delete resources. Here's how you can make requests to a REST API using various methods:

### 1. GET Request:

A `GET` request is used to retrieve data from the server. It is commonly used to fetch information about a specific resource or a collection of resources.

```http
GET /api/books HTTP/1.1
Host: example.com
```

In this example, we are making a `GET` request to the `/api/books` endpoint to retrieve a list of books from the server.

### 2. POST Request:

A `POST` request is used to create new data on the server. It typically includes the data to be created in the request body.

```http
POST /api/books HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger"
}
```

In this example, we are making a `POST` request to the `/api/books` endpoint to create a new book with the title "The Catcher in the Rye" and the author "J.D. Salinger".

### 3. PUT Request:

A `PUT` request is used to update existing data on the server. It typically includes the updated data in the request body.

```http
PUT /api/books/3 HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "title": "1984",
    "author": "George Orwell"
}
```

In this example, we are making a `PUT` request to the `/api/books/3` endpoint to update the book with ID 3 to have the title "1984" and the author "George Orwell".

### 4. DELETE Request:

A `DELETE` request is used to remove data from the server.

```http
DELETE /api/books/2 HTTP/1.1
Host: example.com
```

In this example, we are making a `DELETE` request to the `/api/books/2` endpoint to delete the book with ID 2 from the server.

### Example Code Snippet:

Here's an example of how you might make requests to a REST API using JavaScript and the Fetch API:

```javascript
// GET request
fetch('https://api.example.com/books')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/books', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: 'The Catcher in the Rye',
        author: 'J.D. Salinger'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));

// PUT request
fetch('https://api.example.com/books/3', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: '1984',
        author: 'George Orwell'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));

// DELETE request
fetch('https://api.example.com/books/2', {
    method: 'DELETE'
})
.then(response => console.log('Deleted'))
.catch(error => console.error('Error:', error));
```

In this example, we use the Fetch API to make `GET`, `POST`, `PUT`, and `DELETE` requests to a fictional REST API endpoint for managing books. The responses from the server are logged to the console for demonstration purposes.

## 6. What CORS means

CORS, which stands for Cross-Origin Resource Sharing, is a security feature implemented by web browsers to prevent malicious websites from making unauthorized requests to resources on other domains. 

### How CORS Works:

When a web page makes a request to a different domain (known as a cross-origin request), the browser typically blocks the request by default due to the Same-Origin Policy, which restricts scripts from accessing resources from domains other than the one that served the page. CORS allows servers to specify which domains are allowed to access their resources, enabling cross-origin requests in a controlled manner.

### Example:

Suppose you have a web application hosted on `https://example.com` that needs to fetch data from an API hosted on `https://api.example.com`.

1. The web application makes a request to the API endpoint `https://api.example.com/data`.
2. The browser sends a preflight request (OPTIONS) to the API server to determine if the actual request is safe to send. This preflight request includes information such as the HTTP method and headers.
3. The API server responds with CORS headers specifying which origins are allowed to access its resources. If `https://example.com` is allowed, the server responds with an `Access-Control-Allow-Origin` header set to `https://example.com`.
4. If the server approves the request, the browser sends the actual request (GET, POST, etc.) to the API server.
5. The API server responds with the requested data.

### CORS Headers:

CORS headers are used to control access to resources on a server. The following are common CORS headers:

- **Access-Control-Allow-Origin:** Specifies which origins are allowed to access the resource. It can be set to a specific domain, '*', or a list of domains.
- **Access-Control-Allow-Methods:** Specifies which HTTP methods are allowed when accessing the resource.
- **Access-Control-Allow-Headers:** Specifies which HTTP headers can be used during the actual request.
- **Access-Control-Allow-Credentials:** Indicates whether the resource supports credentials such as cookies or authorization headers.
- **Access-Control-Max-Age:** Specifies how long the results of a preflight request can be cached.

### Example Code Snippet (Express.js Middleware):

Here's an example of how you can implement CORS handling in an Express.js application:

```javascript
const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors()); // Enable CORS for all routes

// Your routes and middleware here

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

In this example, we use the `cors` middleware to enable CORS for all routes in the Express.js application. This allows requests from any origin to access the server's resources.

By understanding CORS and how to implement it in web applications, developers can ensure secure communication between different domains while still allowing controlled access to resources. This is essential for building modern web applications that interact with APIs and services hosted on different domains.

## 7. Which is the HTTP method to retrieve resource(s)

The HTTP method used to retrieve resource(s) from a server is the `GET` method. 

### How the `GET` method works:

When a client sends a `GET` request to a server, it is asking the server to retrieve a specific resource or a collection of resources. The server processes the request and responds with the requested data, typically in the form of a response body.

### Example:

Suppose you have a web application that needs to fetch a list of books from a server. You would use a `GET` request to retrieve this data.

```http
GET /api/books HTTP/1.1
Host: example.com
```

In this example, the client is making a `GET` request to the `/api/books` endpoint on the `example.com` server to retrieve a list of books.

### Real-world application:

In a real-world project, you might use the `GET` method to retrieve various types of data from a server, such as:

- Fetching user profiles from a social media API
- Retrieving product information from an e-commerce website
- Getting weather data from a weather API
- Accessing news articles from a news website's API

### Example Code Snippet (using Fetch API in JavaScript):

Here's an example of how you can make a `GET` request to retrieve data from a server using the Fetch API in JavaScript:

```javascript
fetch('https://api.example.com/books')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

In this example, we use the Fetch API to send a `GET` request to the `/books` endpoint on the `api.example.com` server. Once the server responds, we parse the JSON data and log it to the console.

By understanding the `GET` method and how to use it to retrieve data from servers, developers can effectively fetch resources from APIs and integrate them into their web applications. This is a fundamental aspect of building modern, data-driven web applications.

## 8. Which is the HTTP method to create a resource

The HTTP method used to create a resource on a server is the `POST` method.

### How the `POST` method works:

When a client sends a `POST` request to a server, it is asking the server to create a new resource based on the data provided in the request body. The server processes the request, creates the resource, and typically responds with a confirmation or a representation of the newly created resource.

### Example:

Suppose you have a web application where users can submit a new blog post. You would use a `POST` request to send the data for the new blog post to the server for creation.

```http
POST /api/posts HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "title": "New Blog Post",
    "content": "This is the content of the new blog post."
}
```

In this example, the client is making a `POST` request to the `/api/posts` endpoint on the `example.com` server to create a new blog post with the specified title and content.

### Real-world application:

In real-world projects, the `POST` method is commonly used for various purposes, such as:

- Creating new user accounts on a website
- Submitting form data, such as registration or contact forms
- Adding new items to a shopping cart in an e-commerce application
- Uploading files or images to a server
- Adding comments or reviews to a blog or product page

### Example Code Snippet (using Fetch API in JavaScript):

Here's an example of how you can make a `POST` request to create a new resource on a server using the Fetch API in JavaScript:

```javascript
fetch('https://api.example.com/posts', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: 'New Blog Post',
        content: 'This is the content of the new blog post.'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

In this example, we use the Fetch API to send a `POST` request to the `/posts` endpoint on the `api.example.com` server. We include the `Content-Type` header to indicate that the request body contains JSON data. Once the server responds, we parse the JSON data and log it to the console.

By understanding the `POST` method and how to use it to create resources on servers, developers can effectively add new data to their applications, enabling dynamic content creation and user interaction. This is essential for building modern, data-driven web applications.

## 9. Which is the HTTP method to update a resource

The HTTP method used to update an existing resource on a server is the `PUT` method.

### How the `PUT` method works:

When a client sends a `PUT` request to a server, it is asking the server to replace the existing resource with the data provided in the request body. The server processes the request, updates the resource, and typically responds with a confirmation or a representation of the updated resource.

### Example:

Suppose you have a web application where users can edit their profile information. You would use a `PUT` request to send the updated profile data to the server for modification.

```http
PUT /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "Updated Name",
    "email": "updated@example.com"
}
```

In this example, the client is making a `PUT` request to the `/api/users/123` endpoint on the `example.com` server to update the profile information for the user with ID 123.

### Real-world application:

In real-world projects, the `PUT` method is commonly used for various purposes, such as:

- Updating user profiles with new information
- Editing existing content, such as blog posts or articles
- Modifying settings or preferences in a user account
- Updating product details or inventory in an e-commerce application

### Example Code Snippet (using Fetch API in JavaScript):

Here's an example of how you can make a `PUT` request to update a resource on a server using the Fetch API in JavaScript:

```javascript
fetch('https://api.example.com/users/123', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'Updated Name',
        email: 'updated@example.com'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

In this example, we use the Fetch API to send a `PUT` request to the `/users/123` endpoint on the `api.example.com` server. We include the `Content-Type` header to indicate that the request body contains JSON data. Once the server responds, we parse the JSON data and log it to the console.

By understanding the `PUT` method and how to use it to update resources on servers, developers can effectively modify existing data in their applications, enabling users to interact with and manage their content. This is essential for building dynamic and user-friendly web applications.

## 10. Which is the HTTP method to delete a resource

The HTTP method used to delete an existing resource on a server is the `DELETE` method.

### How the `DELETE` method works:

When a client sends a `DELETE` request to a server, it is asking the server to remove the specified resource. The server processes the request, deletes the resource, and typically responds with a confirmation or a success message.

### Example:

Suppose you have a web application where users can delete their blog posts. You would use a `DELETE` request to send the request to the server for deletion.

```http
DELETE /api/posts/456 HTTP/1.1
Host: example.com
```

In this example, the client is making a `DELETE` request to the `/api/posts/456` endpoint on the `example.com` server to delete the blog post with ID 456.

### Real-world application:

In real-world projects, the `DELETE` method is commonly used for various purposes, such as:

- Removing user accounts from a website
- Deleting outdated or irrelevant content, such as comments or posts
- Managing items in a user's cart or wishlist in an e-commerce application
- Cleaning up resources in a database or storage system

### Example Code Snippet (using Fetch API in JavaScript):

Here's an example of how you can make a `DELETE` request to delete a resource on a server using the Fetch API in JavaScript:

```javascript
fetch('https://api.example.com/posts/456', {
    method: 'DELETE'
})
.then(response => {
    if (response.ok) {
        console.log('Resource deleted successfully');
    } else {
        console.error('Error:', response.status);
    }
})
.catch(error => console.error('Error:', error));
```

In this example, we use the Fetch API to send a `DELETE` request to the `/posts/456` endpoint on the `api.example.com` server. Once the server responds, we check if the response is successful (status code 200-299) and log a success message. If there's an error, we log the status code to the console.

By understanding the `DELETE` method and how to use it to remove resources from servers, developers can effectively manage and clean up data in their applications, ensuring a well-maintained and efficient system. This is essential for building robust and scalable web applications.

# AirBnB clone (RESTful API) - Improve storage

In this task, we are required to update `DBStorage` and `FileStorage` classes in the `storage_get_count` branch, adding two new methods:

1. A method to retrieve one object:
   - Prototype: `def get(self, cls, id)`
   - Parameters:
     - `cls`: class representing the object type
     - `id`: string representing the object ID
   - Returns the object based on the class and its ID, or None if not found

2. A method to count the number of objects in storage:
   - Prototype: `def count(self, cls=None)`
   - Parameters:
     - `cls`: class representing the object type (optional)
   - Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.

We need to add new tests for these two methods in each storage engine.

Here's an example of how the test script `test_get_count.py` can be implemented:

```python
#!/usr/bin/python3
"""Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
```

And here's an example output of running the test script:

```
All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
```

Finally, remember to make a pull request on GitHub.com and ask at least one peer to review and merge it.

# AirBnB clone (RESTful API) - Status of your API

To start our API, we will create our first endpoint to return the status of the API.

Here's how you can achieve this:

1. **Setting up the project structure:**
   - Create a folder named `api` at the root of the project with an empty file `__init__.py`.
   - Inside the `api` folder, create a subfolder named `v1`.
   - Inside the `v1` folder, create an empty file `__init__.py`.
   - Create a file named `app.py` inside the `v1` folder.

2. **Implementation of `app.py`:**
   ```python
   # v1/app.py
   from flask import Flask
   from models import storage
   from api.v1.views import app_views

   app = Flask(__name__)
   app.register_blueprint(app_views)
   
   @app.teardown_appcontext
   def teardown_db(exception):
       """Close storage"""
       storage.close()

   if __name__ == "__main__":
       host = os.getenv("HBNB_API_HOST", "0.0.0.0")
       port = int(os.getenv("HBNB_API_PORT", 5000))
       app.run(host=host, port=port, threaded=True)
   ```

3. **Setting up the views:**
   - Inside the `v1` folder, create a subfolder named `views`.
   - Inside the `views` folder, create an empty file `__init__.py`.
   - Create a file named `index.py` inside the `views` folder.

4. **Implementation of `index.py`:**
   ```python
   # v1/views/index.py
   from api.v1.views import app_views
   from flask import jsonify

   @app_views.route('/status', methods=['GET'])
   def api_status():
       """API status"""
       return jsonify({"status": "OK"})
   ```

With these implementations, we have set up our API with a `/status` endpoint that returns a JSON response with the status "OK".

Remember to set up your environment variables `HBNB_API_HOST` and `HBNB_API_PORT` as needed before running the Flask server.

# AirBnB clone (RESTful API) - Some stats?

To retrieve the number of each object type, we will create an endpoint `/api/v1/stats`.

Here's how you can implement it:

1. **Implementation in `index.py`:**
   
   ```python
   # v1/views/index.py
   from api.v1.views import app_views
   from flask import jsonify
   from models import storage

   @app_views.route('/stats', methods=['GET'])
   def api_stats():
       """Retrieves the number of each object by type"""
       stats = {
           "amenities": storage.count("Amenity"),
           "cities": storage.count("City"),
           "places": storage.count("Place"),
           "reviews": storage.count("Review"),
           "states": storage.count("State"),
           "users": storage.count("User")
       }
       return jsonify(stats)
   ```

This implementation utilizes the `count()` method from the `storage` engine to retrieve the count of each object type. The counts are then returned as a JSON response.

Now, when you make a GET request to `/api/v1/stats`, you will receive a JSON response containing the counts of amenities, cities, places, reviews, states, and users.

# AirBnB clone (RESTful API) - Not found

To handle 404 errors and return a JSON-formatted response with a "Not found" message, you can implement the following handler in `api/v1/app.py`:

```python
# api/v1/app.py
from flask import jsonify
from api.v1.views import app_views

@app_views.app_errorhandler(404)
def not_found(error):
    """Handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404
```

This handler uses Flask's `app_errorhandler` decorator to handle 404 errors. When a 404 error occurs, it returns a JSON response with the message "Not found" and a 404 status code.

Now, when you make a request to a non-existing endpoint, such as `/api/v1/nop`, you will receive a JSON response with the "Not found" error message and a 404 status code.

# AirBnB clone (RESTful API) - State

To handle State objects and perform CRUD operations, you can create a new view in `api/v1/views/states.py`. Make sure to import this new file in `api/v1/views/__init__.py`. Here's how you can implement the required actions:

```python
# api/v1/views/states.py
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a new State object"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    return jsonify({})
```

This code defines routes for retrieving all states, retrieving a specific state by ID, creating a new state, updating an existing state, and deleting a state. It handles JSON input for creating and updating states and returns JSON responses.

Ensure to import `states.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - City

To handle City objects and perform CRUD operations, you can create a new view in `api/v1/views/cities.py`. Make sure to import this new file in `api/v1/views/__init__.py`. Here's how you can implement the required actions:

```python
# api/v1/views/cities.py
from flask import jsonify, abort, request
from models import storage
from models.city import City
from api.v1.views import app_views

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    return jsonify({})

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Creates a new City object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    city = City(**data)
    city.state_id = state_id
    city.save()
    return jsonify(city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict())
```

This code defines routes for retrieving all cities of a state, retrieving a specific city by ID, creating a new city associated with a state, updating an existing city, and deleting a city. It handles JSON input for creating and updating cities and returns JSON responses.

Ensure to import `cities.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - Amenity

To handle Amenity objects and perform CRUD operations, create a new view in `api/v1/views/amenities.py`. Also, update `api/v1/views/__init__.py` to import this new file. Here's how you can implement the required actions:

```python
# api/v1/views/amenities.py
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = [amenity.to_dict() for amenity in storage.all(Amenity).values()]
    return jsonify(amenities)

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    return jsonify({})

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a new Amenity object"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """Updates an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())
```

This code defines routes for retrieving all amenities, retrieving a specific amenity by ID, creating a new amenity, updating an existing amenity, and deleting an amenity. It handles JSON input for creating and updating amenities and returns JSON responses.

Ensure to import `amenities.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - User

To manage User objects and perform CRUD operations, create a new view in `api/v1/views/users.py`. Also, update `api/v1/views/__init__.py` to import this new file. Here's how you can implement the required actions:

```python
# api/v1/views/users.py
from flask import jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({})

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a new User object"""
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
```

This code defines routes for retrieving all users, retrieving a specific user by ID, creating a new user, updating an existing user, and deleting a user. It handles JSON input for creating and updating users and returns JSON responses.

Ensure to import `users.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - Place

To manage Place objects and perform CRUD operations, create a new view in `api/v1/views/places.py`. Also, update `api/v1/views/__init__.py` to import this new file. Here's how you can implement the required actions:

```python
# api/v1/views/places.py
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from api.v1.views import app_views

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)

@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    return jsonify({})

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Creates a new Place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    user_id = data['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if 'name' not in data:
        abort(400, description="Missing name")
    place = Place(city_id=city_id, user_id=user_id, **data)
    place.save()
    return jsonify(place.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict())
```

This code defines routes for retrieving all places of a city, retrieving a specific place by ID, creating a new place, updating an existing place, and deleting a place. It handles JSON input for creating and updating places and returns JSON responses.

Ensure to import `places.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - Reviews

To manage Review objects and perform CRUD operations, create a new view in `api/v1/views/places_reviews.py`. Also, update `api/v1/views/__init__.py` to import this new file. Here's how you can implement the required actions:

```python
# api/v1/views/places_reviews.py
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from api.v1.views import app_views

@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Retrieves a Review object by ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Deletes a Review object by ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    return jsonify({})

@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """Creates a new Review"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    user_id = data['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if 'text' not in data:
        abort(400, description="Missing text")
    review = Review(place_id=place_id, user_id=user_id, **data)
    review.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Updates a Review object by ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())
```

This code defines routes for retrieving all reviews of a place, retrieving a specific review by ID, creating a new review, updating an existing review, and deleting a review. It handles JSON input for creating and updating reviews and returns JSON responses.

Ensure to import `places_reviews.py` in `api/v1/views/__init__.py` to register these routes with the Flask application.

# AirBnB clone (RESTful API) - HTTP Access Control (CORS)

To enable Cross-Origin Resource Sharing (CORS) in your Flask API, you'll need to use the `CORS` class from the `flask_cors` module. Here's how you can do it:

1. Install `flask_cors` using pip:

```bash
$ pip3 install flask_cors
```

2. Update `api/v1/app.py` to include CORS configuration:

```python
# api/v1/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

In this code:
- We import the `CORS` class from `flask_cors`.
- We create a Flask app instance and pass it to the `CORS` constructor, along with the desired CORS settings.
- The `resources` parameter specifies which resources are allowed to access the API. Here, we allow all resources (`/*`) from the origin `0.0.0.0`.

By setting up CORS in this way, you ensure that your API responds with the appropriate CORS headers, allowing web clients from any origin to access your API's resources.

Now, when you make HTTP requests to your API, you should see the `Access-Control-Allow-Origin` header in the response, indicating that CORS is properly configured.

# AirBnB clone (RESTful API) - Place - Amenity

To manage the relationship between Place objects and Amenity objects in your AirBnB clone RESTful API, you'll create a new view called `places_amenities.py`. This view will handle various RESTFul API actions related to linking amenities with places.

Here's what you need to do:

1. Create a new view file `places_amenities.py`:

```python
# api/v1/views/places_amenities.py
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def get_place_amenities(place_id):
    """Retrieve the list of all Amenity objects of a Place"""
    # Your implementation here

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """Delete an Amenity object from a Place"""
    # Your implementation here

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def link_place_amenity(place_id, amenity_id):
    """Link an Amenity object to a Place"""
    # Your implementation here
```

2. Update `api/v1/views/__init__.py` to import the new file:

```python
# api/v1/views/__init__.py
from api.v1.views.places_amenities import *
```

3. Depending on the storage type (`DBStorage` or `FileStorage`), implement the logic to handle the CRUD operations for the link between Place and Amenity objects.

   - If using `DBStorage`, you'll need to list, create, and delete Amenity objects from the `amenities` relationship.
   - If using `FileStorage`, you'll need to list, add, and remove Amenity IDs in the list `amenity_ids` of a Place object.

4. Implement the following API endpoints:

   - **GET /api/v1/places/<place_id>/amenities**: Retrieves the list of all Amenity objects of a Place. If the place_id is not linked to any Place object, raise a 404 error.
   - **DELETE /api/v1/places/<place_id>/amenities/<amenity_id>**: Deletes an Amenity object from a Place. Ensure to handle error cases as specified.
   - **POST /api/v1/places/<place_id>/amenities/<amenity_id>**: Links an Amenity object to a Place. Ensure to handle error cases as specified.

By implementing these endpoints, you'll be able to manage the relationship between Place and Amenity objects efficiently in your AirBnB clone RESTful API.

# AirBnB clone (RESTful API) - Security Improvements!

In the current implementation of the AirBnB clone RESTful API, the User object stores the user's password in plain text, which poses a significant security risk. To address this issue and enhance security, several improvements need to be made:

1. Update the `to_dict()` method of the `BaseModel` class to remove the `password` key from the dictionary returned by the method, except when it's used by `FileStorage` to save data to disk. This can be achieved by setting a default parameter for the `to_dict()` method.

2. Implement a mechanism to hash the password to an MD5 value each time a new User object is created or the password is updated. This ensures that passwords are stored securely and cannot be easily compromised.

3. Modify the storage mechanism to store the hashed password instead of the plain text password:
   - For `DBStorage`, ensure that the password stored in the database is hashed to an MD5 value before saving.
   - For `FileStorage`, ensure that the password stored in the file is hashed to an MD5 value before saving.

Here's how you can implement these improvements:

1. Update the `to_dict()` method in `models/base_model.py`:
   
```python
def to_dict(self, exclude_password=True):
    """Return a dictionary representation of the instance."""
    dictionary = self.__dict__.copy()
    if exclude_password:
        dictionary.pop('password', None)
    # Add additional logic if needed
    return dictionary
```

2. Implement password hashing in the `User` model in `models/user.py`:
   
```python
import hashlib

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize User object."""
        super().__init__(*args, **kwargs)

        # Hash the password if provided
        if 'password' in kwargs:
            self.password = hashlib.md5(kwargs['password'].encode()).hexdigest()

    def update_password(self, new_password):
        """Update user's password."""
        self.password = hashlib.md5(new_password.encode()).hexdigest()
```

3. Modify the storage mechanisms (`DBStorage` and `FileStorage`) to handle password hashing accordingly.

By implementing these security improvements, you enhance the security of the AirBnB clone API by ensuring that user passwords are stored securely and cannot be easily compromised even if the database or file storage is compromised.

# AirBnB clone (RESTful API) - Search

To enhance the functionality of the AirBnB clone RESTful API, a new endpoint `POST /api/v1/places_search` needs to be implemented in the `api/v1/views/places.py` file. This endpoint will retrieve all Place objects based on the JSON data provided in the body of the request.

The JSON data can contain three optional keys:

1. `states`: A list of State IDs.
2. `cities`: A list of City IDs.
3. `amenities`: A list of Amenity IDs.

Here are the search rules:

- If the HTTP request body is not valid JSON, raise a 400 error with the message "Not a JSON".
- If the JSON body is empty or each list of all keys is empty, retrieve all Place objects.
- If the `states` list is not empty, the results should include all Place objects for each State ID listed.
- If the `cities` list is not empty, the results should include all Place objects for each City ID listed.
- The `states` and `cities` keys are inclusive. Search results should include all Place objects in storage related to each City in every State listed in `states`, plus every City listed individually in `cities`, unless that City was already included by `states`.
- If the `amenities` list is not empty, limit search results to only Place objects having all Amenity IDs listed. The `amenities` key is exclusive, acting as a filter on the results generated by `states` and `cities`, or on all Place if `states` and `cities` are both empty or missing.

Here's an example of how to use the `POST /api/v1/places_search` endpoint:

```bash
curl -X POST http://0.0.0.0:5000/api/v1/places_search -H "Content-Type: application/json" -d '{"states": ["2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", "459e021a-e794-447d-9dd2-e03b7963f7d2"], "cities": ["5976f0e7-5c5f-4949-aae0-90d68fd239c0"]}'
```

This request will retrieve Place objects based on the provided State IDs and City IDs.

By implementing this search functionality, users can now search for Place objects based on specific criteria, such as State, City, and Amenities, providing a more comprehensive and flexible user experience.

## Conclusion

In conclusion, mastering the concepts of RESTful APIs equips developers with the necessary tools to architect robust and efficient systems. By adhering to REST principles such as client-server separation, statelessness, and a uniform interface, developers can design scalable and maintainable APIs that promote interoperability and enhance user experiences. Whether it's building a blogging platform, integrating a payment gateway, or managing user data, the versatility and effectiveness of RESTful APIs make them indispensable in today's web development landscape. As developers continue to harness the power of REST, they pave the way for innovation and progress in the digital realm.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
