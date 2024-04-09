# Requesting Your Own API

In the world of software engineering, APIs (Application Programming Interfaces) play a crucial role in allowing different software systems to communicate with each other. They serve as messengers, facilitating the exchange of data and functionality between different applications, services, or even different parts of the same application.

## What is an API?

An API is essentially a set of rules and protocols that allows one piece of software to interact with another. It defines the methods and data formats that developers can use to request and receive responses from the software or service that exposes the API.

## Why Request Your Own API?

You might be wondering, why would you need to request your own API? Well, there are several scenarios where this can be incredibly useful:

1. **Modularization**: Breaking down your application into smaller, modular components allows for easier maintenance and scalability. By requesting your own API, you can create clean interfaces between these components, making your code more organized and maintainable.

2. **Reuse and Sharing**: Once you've built an API for a specific functionality within your application, you can easily reuse it in other parts of your application or even share it with other developers or teams working on different projects. This promotes code reusability and collaboration.

3. **Testing and Debugging**: Requesting your own API allows you to test and debug different parts of your application independently. You can mock responses from the API to simulate various scenarios and ensure that each component of your application behaves as expected.

4. **Scaling**: As your application grows, you may need to scale certain components to handle increased traffic or workload. By requesting your own API, you can easily distribute the workload across multiple servers or services, improving performance and reliability.

## Example: Building a Todo List Application

Let's walk through a simple example to illustrate how you might request your own API in a real-world project. Imagine we're building a todo list application, and we want to implement functionality for creating and managing tasks.

### Step 1: Designing the API

First, we need to design the API for our todo list application. We might decide on the following endpoints:

- `/tasks` (GET): Retrieve all tasks
- `/tasks/{id}` (GET): Retrieve a specific task by ID
- `/tasks` (POST): Create a new task
- `/tasks/{id}` (PUT): Update an existing task
- `/tasks/{id}` (DELETE): Delete a task

### Step 2: Implementing the API

Next, we implement the API endpoints in our backend server using a framework like Express.js (for Node.js) or Flask (for Python). Here's an example of how we might implement the `/tasks` endpoint to create a new task:

```javascript
// Express.js example
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;

let tasks = [];

app.use(bodyParser.json());

app.post('/tasks', (req, res) => {
  const { title, description } = req.body;
  const newTask = { id: tasks.length + 1, title, description };
  tasks.push(newTask);
  res.status(201).json(newTask);
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Step 3: Consuming the API

Finally, we consume the API endpoints in our frontend application to interact with the todo list functionality. We might use JavaScript and fetch API to make requests to our backend server. Here's an example of how we might create a new task using fetch:

```javascript
// Frontend JavaScript example
const createTask = async (title, description) => {
  const response = await fetch('http://localhost:3000/tasks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title, description }),
  });
  const data = await response.json();
  console.log('New task created:', data);
};

// Usage
createTask('Buy groceries', 'Milk, eggs, bread');
```

## Conclusion

In conclusion, requesting your own API is a powerful technique that allows you to create clean interfaces between different components of your application, promote code reusability and collaboration, facilitate testing and debugging, and enable scalability. By understanding how to design, implement, and consume APIs, you can build more robust and scalable software applications.

# Modifying HTML Element Style

In web development, modifying the style of HTML elements is essential for creating visually appealing and interactive web pages. CSS (Cascading Style Sheets) is the primary language used for styling HTML elements, but you can also modify styles directly using JavaScript. This allows for dynamic styling changes based on user interactions or application logic.

## Using JavaScript to Modify Styles

JavaScript provides several ways to modify the style of HTML elements dynamically. One common approach is by accessing the `style` property of an HTML element and changing its individual CSS properties.

### Example 1: Changing Background Color

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modify Style Example</title>
  <style>
    /* Initial CSS */
    .box {
      width: 100px;
      height: 100px;
      background-color: blue;
    }
  </style>
</head>
<body>

<div class="box" id="myBox"></div>

<script>
  // JavaScript code to change background color
  const box = document.getElementById('myBox');
  box.style.backgroundColor = 'red';
</script>

</body>
</html>
```

In this example, we have an HTML element with the class `box`. Initially, its background color is set to blue using CSS. Then, using JavaScript, we select the element by its ID (`myBox`) and change its background color to red.

### Example 2: Modifying Font Size

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modify Style Example</title>
  <style>
    /* Initial CSS */
    .text {
      font-size: 16px;
    }
  </style>
</head>
<body>

<p class="text" id="myText">Hello, World!</p>

<script>
  // JavaScript code to modify font size
  const text = document.getElementById('myText');
  text.style.fontSize = '24px';
</script>

</body>
</html>
```

Here, we have a paragraph element with the class `text`, initially styled with a font size of 16 pixels. Using JavaScript, we select the element by its ID (`myText`) and change its font size to 24 pixels.

## Real-World Application

Dynamic styling using JavaScript is commonly used in web applications to provide interactive user experiences. For example:

- **Form Validation**: Change the border color of input fields based on whether the input is valid or not.
- **Toggle Visibility**: Show or hide elements by modifying their `display` property.
- **Animating Elements**: Change CSS properties over time to create animations or transitions.

Understanding how to modify HTML element styles using JavaScript is fundamental for creating dynamic and engaging web applications. By combining JavaScript with CSS, developers can create visually stunning and interactive websites.

# Getting and Updating HTML Element Content

In web development, manipulating HTML element content dynamically is a common task. Whether it's displaying data fetched from a server, responding to user interactions, or updating elements based on application state changes, understanding how to get and update HTML element content is essential for building dynamic web applications.

## Getting Content: Using JavaScript to Access Element Content

JavaScript provides several methods for accessing the content of HTML elements. One common approach is to use the `innerHTML` property, which allows you to retrieve the HTML content of an element as a string.

### Example: Getting Content of a Paragraph Element

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Get Content Example</title>
</head>
<body>

<p id="myParagraph">Hello, World!</p>

<script>
  // JavaScript code to get content
  const paragraph = document.getElementById('myParagraph');
  const content = paragraph.innerHTML;
  console.log(content); // Output: Hello, World!
</script>

</body>
</html>
```

In this example, we have a paragraph element with the ID `myParagraph`. Using JavaScript, we select the element by its ID and retrieve its content using the `innerHTML` property.

## Updating Content: Using JavaScript to Modify Element Content

JavaScript also allows you to dynamically update the content of HTML elements. You can use the same `innerHTML` property to set new content for an element.

### Example: Updating Content of a Div Element

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Update Content Example</title>
</head>
<body>

<div id="myDiv">Initial Content</div>

<script>
  // JavaScript code to update content
  const div = document.getElementById('myDiv');
  div.innerHTML = 'New Content';
</script>

</body>
</html>
```

Here, we have a `div` element with the ID `myDiv`. Using JavaScript, we select the element by its ID and update its content by assigning a new value to the `innerHTML` property.

## Real-World Application

Understanding how to get and update HTML element content using JavaScript is crucial for building dynamic and interactive web applications. Here are some real-world scenarios where this knowledge is applied:

- **Fetching Data from a Server**: Retrieve data from a server using AJAX and update the content of specific elements with the received data.
- **Form Handling**: Update form fields dynamically based on user selections or input validation results.
- **Real-Time Updates**: Display real-time updates from a chat application or social media feed by dynamically updating element content.

By mastering these techniques, developers can create engaging and responsive web applications that provide users with a seamless and interactive experience.

# Modifying the DOM (Document Object Model)

In web development, the DOM (Document Object Model) is a programming interface that represents the structure of HTML documents as a tree of nodes. Modifying the DOM dynamically using JavaScript allows developers to create interactive and dynamic web pages. Understanding how to modify the DOM is crucial for building modern web applications.

## Basic DOM Manipulation

JavaScript provides several methods and properties for modifying the DOM. Here are some common techniques:

### 1. Selecting Elements

You can select HTML elements using various methods such as `getElementById`, `getElementsByClassName`, `querySelector`, and `querySelectorAll`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Selecting Elements Example</title>
</head>
<body>

<div id="myDiv">
  <p class="paragraph">Hello, World!</p>
</div>

<script>
  // JavaScript code to select elements
  const div = document.getElementById('myDiv');
  const paragraphs = document.getElementsByClassName('paragraph');
  const firstParagraph = document.querySelector('p');
  const allParagraphs = document.querySelectorAll('p');
</script>

</body>
</html>
```

### 2. Modifying Element Properties

You can modify various properties of HTML elements such as `textContent`, `innerHTML`, `style`, `className`, etc.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modifying Properties Example</title>
</head>
<body>

<p id="myParagraph">Hello, World!</p>

<script>
  // JavaScript code to modify element properties
  const paragraph = document.getElementById('myParagraph');
  paragraph.textContent = 'Goodbye, World!';
  paragraph.style.color = 'red';
</script>

</body>
</html>
```

### 3. Creating and Appending Elements

You can create new HTML elements dynamically and append them to the DOM using methods like `createElement` and `appendChild`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Creating Elements Example</title>
</head>
<body>

<div id="container"></div>

<script>
  // JavaScript code to create and append elements
  const container = document.getElementById('container');
  const paragraph = document.createElement('p');
  paragraph.textContent = 'This is a new paragraph.';
  container.appendChild(paragraph);
</script>

</body>
</html>
```

## Real-World Application

Understanding how to modify the DOM dynamically using JavaScript is crucial for building modern web applications. Here are some real-world scenarios where this knowledge is applied:

- **Interactive User Interfaces**: Creating dynamic user interfaces that respond to user interactions such as clicks, hovers, etc.
- **Form Validation**: Validating form inputs dynamically and providing feedback to users without reloading the page.
- **Real-Time Updates**: Updating content in real-time without requiring the user to refresh the page, such as live chat applications or social media feeds.

By mastering DOM manipulation techniques, developers can create engaging and interactive web applications that provide users with a seamless and dynamic experience.

# Making a GET Request with jQuery AJAX

In web development, AJAX (Asynchronous JavaScript and XML) is a technique used to send and receive data from a server asynchronously without reloading the entire web page. jQuery provides a simplified way to perform AJAX requests, making it easier for developers to interact with server-side APIs and fetch data dynamically.

## Basic Syntax of jQuery AJAX

jQuery provides the `$.ajax()` function to make AJAX requests. Here's the basic syntax:

```javascript
$.ajax({
  url: 'https://api.example.com/data',
  method: 'GET',
  success: function(response) {
    // Handle successful response
    console.log(response);
  },
  error: function(xhr, status, error) {
    // Handle error
    console.error(error);
  }
});
```

In this example:
- `url`: Specifies the URL to which the request is sent.
- `method`: Specifies the HTTP method (GET, POST, PUT, DELETE, etc.).
- `success`: Callback function to handle the successful response from the server.
- `error`: Callback function to handle errors, such as network issues or server errors.

## Example: Making a GET Request

Let's make a simple GET request to fetch data from a hypothetical API endpoint:

```javascript
$.ajax({
  url: 'https://api.example.com/data',
  method: 'GET',
  success: function(response) {
    // Handle successful response
    console.log('Data received:', response);
    // Update HTML content with the received data
    $('#output').text(JSON.stringify(response));
  },
  error: function(xhr, status, error) {
    // Handle error
    console.error('Error:', error);
  }
});
```

In this example:
- We make a GET request to `'https://api.example.com/data'`.
- If the request is successful, the `success` callback function is executed, where we log the received data and update an HTML element with the received data.
- If an error occurs, the `error` callback function is executed, where we log the error message.

## Real-World Application

Using jQuery AJAX, developers can interact with server-side APIs to fetch data dynamically and update web pages without requiring a full page reload. This is commonly used in real-world projects for various purposes:

- **Fetching Data**: Retrieving data from a server to display dynamic content, such as news articles, product listings, or user information.
- **Form Submission**: Submitting form data to a server asynchronously to validate inputs and provide feedback without refreshing the page.
- **Real-Time Updates**: Updating content in real-time, such as chat applications, social media feeds, or live sports scores.

By mastering jQuery AJAX, developers can create more dynamic and responsive web applications that provide users with a seamless browsing experience.

# Making a POST Request with jQuery AJAX

In web development, making POST requests is essential for sending data to a server. jQuery provides an easy-to-use method for making POST requests asynchronously using AJAX (Asynchronous JavaScript and XML). This allows developers to interact with server-side APIs and send data without reloading the entire web page.

## Basic Syntax of jQuery AJAX POST Request

To make a POST request with jQuery AJAX, you can use the `$.ajax()` function with the following parameters:

```javascript
$.ajax({
  url: 'https://api.example.com/data',
  method: 'POST',
  data: { key1: 'value1', key2: 'value2' },
  success: function(response) {
    // Handle successful response
    console.log(response);
  },
  error: function(xhr, status, error) {
    // Handle error
    console.error(error);
  }
});
```

In this example:
- `url`: Specifies the URL to which the request is sent.
- `method`: Specifies the HTTP method (in this case, POST).
- `data`: Specifies the data to be sent to the server. It can be an object, a string, or a serialized form.
- `success`: Callback function to handle the successful response from the server.
- `error`: Callback function to handle errors, such as network issues or server errors.

## Example: Making a POST Request

Let's make a simple POST request to send data to a hypothetical API endpoint:

```javascript
$.ajax({
  url: 'https://api.example.com/data',
  method: 'POST',
  data: { username: 'john_doe', email: 'john@example.com' },
  success: function(response) {
    // Handle successful response
    console.log('Data sent successfully:', response);
  },
  error: function(xhr, status, error) {
    // Handle error
    console.error('Error:', error);
  }
});
```

In this example:
- We make a POST request to `'https://api.example.com/data'`.
- We include data in the request body with key-value pairs for the username and email.
- If the request is successful, the `success` callback function is executed, where we log the response from the server.
- If an error occurs, the `error` callback function is executed, where we log the error message.

## Real-World Application

Making POST requests with jQuery AJAX is commonly used in real-world projects for various purposes:

- **Form Submission**: Submitting form data to a server for processing, such as user registration, login, or submitting feedback.
- **Data Creation**: Sending data to a server to create new records in a database, such as adding a new product to an e-commerce store or creating a new post in a blogging platform.
- **API Interaction**: Communicating with server-side APIs to perform actions that require data submission, such as updating user profiles or making reservations.

By mastering jQuery AJAX for making POST requests, developers can create more interactive and dynamic web applications that provide users with a seamless experience.

# Listening to DOM Events

In web development, DOM events are actions or occurrences that happen in the HTML document or browser window. JavaScript allows developers to listen for these events and execute code in response. This enables developers to create interactive and responsive web applications. Let's explore how to listen to DOM events and apply them in real-world projects.

## Basic Syntax for Event Listening

To listen to DOM events in JavaScript, you can use the `addEventListener()` method. Here's the basic syntax:

```javascript
element.addEventListener(eventType, handlerFunction);
```

- `element`: The HTML element to which you want to attach the event listener.
- `eventType`: The type of event you want to listen for, such as "click", "mouseover", "keydown", etc.
- `handlerFunction`: The function to be executed when the event occurs.

## Example: Listening to Click Events

Let's see an example of listening to a click event on a button element:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event Listening Example</title>
</head>
<body>

<button id="myButton">Click Me!</button>

<script>
  // JavaScript code to listen to click event
  const button = document.getElementById('myButton');
  
  button.addEventListener('click', function() {
    alert('Button clicked!');
  });
</script>

</body>
</html>
```

In this example:
- We select the button element with the ID "myButton".
- We add an event listener for the "click" event.
- When the button is clicked, the anonymous function (callback function) is executed, displaying an alert message.

## Real-World Application

Listening to DOM events is crucial for building interactive web applications. Here are some real-world scenarios where event listening is applied:

- **Form Validation**: Listen for "submit" events on forms to validate user input before submitting the form data to the server.
- **Dynamic Content Loading**: Listen for "scroll" events to trigger the loading of additional content as the user scrolls down a page, commonly used in infinite scroll functionality.
- **User Interactions**: Listen for "mouseover", "mouseout", "keydown", "keyup", etc., events to enhance user interactions, such as displaying tooltips, keyboard shortcuts, etc.

By mastering event listening in JavaScript, developers can create more engaging and user-friendly web applications that respond to user actions in real-time.

# Listening to User Events

In web development, listening to user events is essential for creating interactive and dynamic web applications. User events are actions performed by users, such as clicking on buttons, typing into input fields, or scrolling the page. JavaScript allows developers to listen for these events and execute code in response. Let's explore how to listen to user events and apply them in real-world projects.

## Basic Syntax for Event Listening

To listen to user events in JavaScript, you can use the `addEventListener()` method. Here's the basic syntax:

```javascript
element.addEventListener(eventType, handlerFunction);
```

- `element`: The HTML element to which you want to attach the event listener.
- `eventType`: The type of event you want to listen for, such as "click", "input", "keydown", "scroll", etc.
- `handlerFunction`: The function to be executed when the event occurs.

## Example: Listening to Click Events

Let's see an example of listening to a click event on a button element:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>User Event Listening Example</title>
</head>
<body>

<button id="myButton">Click Me!</button>

<script>
  // JavaScript code to listen to click event
  const button = document.getElementById('myButton');
  
  button.addEventListener('click', function() {
    alert('Button clicked!');
  });
</script>

</body>
</html>
```

In this example:
- We select the button element with the ID "myButton".
- We add an event listener for the "click" event.
- When the button is clicked, the anonymous function (callback function) is executed, displaying an alert message.

## Real-World Application

Listening to user events is crucial for building interactive web applications. Here are some real-world scenarios where user event listening is applied:

- **Form Interactions**: Listen for "submit", "input", or "change" events on form elements to validate user input, update form fields dynamically, or submit form data to the server.
- **User Interface Interactions**: Listen for "click", "mouseover", "mouseout", "keydown", "keyup", etc., events on UI elements to trigger actions such as opening modal windows, displaying tooltips, navigating menus, etc.
- **Scrolling and Navigation**: Listen for "scroll" events to implement features like infinite scrolling or sticky navigation bars that change appearance as the user scrolls.

By mastering user event listening in JavaScript, developers can create more engaging and interactive web applications that respond to user actions in real-time.

# AirBnB clone (Web dynamic) - Cash only mandatory

To achieve the task outlined, we'll follow these steps:

1. **Start a Flask Web Application**: We'll create a Flask web application using existing files from the `web_flask` directory, including static files, templates, `__init__.py`, and `100-hbnb.py`. We'll rename `100-hbnb.py` to `0-hbnb.py` and `100-hbnb.html` to `0-hbnb.html`. Additionally, we'll update `0-hbnb.py` to replace the existing route to `/0-hbnb/`. If `100-hbnb.html` is absent, we'll use `8-hbnb.html` instead.

2. **Avoid Asset Caching**: Flask performs asset caching by default, which can be problematic. To overcome this, we'll add a query string to each asset. Here's how:

    - In `0-hbnb.py`, we'll add a variable `cache_id` to the `render_template` function, and its value must be a UUID (`uuid.uuid4()`).
    - In `0-hbnb.html`, we'll add this `cache_id` variable as a query string to each `<link>` tag URL.

After these modifications, the Flask application will serve HTML pages with unique query strings appended to asset URLs, preventing caching issues.

Example code snippets:

```python
# 0-hbnb.py
from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.route('/0-hbnb/')
def index():
    cache_id = str(uuid.uuid4())
    return render_template('0-hbnb.html', cache_id=cache_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
```

```html
<!-- 0-hbnb.html -->
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" type="text/css" href="../static/styles/4-common.css?{{ cache_id }}" />
    <link rel="stylesheet" type="text/css" href="../static/styles/3-header.css?{{ cache_id }}" />
  </head>
  <body>
    <!-- Body content here -->
  </body>
</html>
```

With these changes, when accessing the `0-hbnb/` route, Flask will dynamically generate HTML with unique query strings for each asset URL, effectively avoiding asset caching issues.

# AirBnB clone (Web dynamic) - Select some Amenities to be comfortable! mandatory

To fulfill this task, we'll follow these steps:

1. **Replace Route and Create Template**: We'll replace the route `0-hbnb` with `1-hbnb` in the file `1-hbnb.py` (based on `0-hbnb.py`). Additionally, we'll create a new template `1-hbnb.html` (based on `0-hbnb.html`).

2. **Update HTML Template**: In the `1-hbnb.html` template, we'll:

   - Import JQuery in the `<head>` tag.
   - Import the JavaScript file `static/scripts/1-hbnb.js` in the `<head>` tag, adding the `cache_id` variable as a query string to the `<script>` tag.
   - Add a `<input type="checkbox">` tag to the `<li>` tag of each amenity.
   - Position the new checkbox 10px to the left of the Amenity name.
   - Add the attribute `data-id=":amenity_id"` to the input tags of each amenity `<li>` tag to retrieve the Amenity ID from the DOM.
   - Add the attribute `data-name=":amenity_name"` to the input tags of each amenity `<li>` tag to retrieve the Amenity name from the DOM.

3. **Write JavaScript Script**: We'll write a JavaScript script (`static/scripts/1-hbnb.js`) that will:

   - Execute only when the DOM is loaded.
   - Utilize JQuery.
   - Listen for changes on each input checkbox tag.
   - If the checkbox is checked, store the Amenity ID in a variable (dictionary or list).
   - If the checkbox is unchecked, remove the Amenity ID from the variable.
   - Update the `<h4>` tag inside the div Amenities with the list of Amenities checked.

Here's an example of how the script can be structured:

```javascript
// static/scripts/1-hbnb.js

$(document).ready(function() {
    $('input[type="checkbox"]').change(function() {
        var amenitiesChecked = [];
        $('input[type="checkbox"]:checked').each(function() {
            amenitiesChecked.push($(this).data('id'));
        });
        // Update h4 tag with list of checked amenities
        $('#amenities').text(amenitiesChecked.join(', '));
    });
});
```

By following these steps, we'll create a dynamic filtering system where users can select amenities, and the displayed amenities will update accordingly.

Remember to link the JavaScript file in the HTML template and ensure that all necessary changes are made to the Python files to incorporate the new route and template.

# AirBnB clone (Web dynamic) - Fetch places mandatory

To implement fetching places dynamically in our AirBnB clone, we'll follow these steps:

1. **Change Route and Create Template**: Replace the route `2-hbnb` with `3-hbnb` in the file `3-hbnb.py` (based on `2-hbnb.py`). Additionally, create a new template `3-hbnb.html` (based on `2-hbnb.html`).

2. **Update HTML Template**: In the `3-hbnb.html` template, we'll:

   - Import the JavaScript file `static/scripts/3-hbnb.js` in the `<head>` tag instead of `2-hbnb.js`.
   - Remove the entire Jinja section of displaying all places (all `<article>` tags).

3. **Write JavaScript Script**: We'll write a JavaScript script (`static/scripts/3-hbnb.js`) based on `2-hbnb.js`. This script will:

   - Make a request to `http://0.0.0.0:5001/api/v1/places_search/` using a POST request with Content-Type: application/json and an empty dictionary in the body.
   - Loop through the results of the request and create an `<article>` tag representing a place in the section.places.

Here's an example of how the JavaScript script can be implemented:

```javascript
// static/scripts/3-hbnb.js
$(document).ready(function() {
    // Request places data
    $.ajax({
        type: 'POST',
        url: 'http://0.0.0.0:5001/api/v1/places_search/',
        contentType: 'application/json',
        data: JSON.stringify({}),
        success: function(data) {
            // Loop through places data and create article tags
            data.forEach(function(place) {
                var article = '<article>' +
                                  '<div class="title">' +
                                      '<h2>' + place.name + '</h2>' +
                                  '</div>' +
                                  '<div class="price_by_night">' +
                                      '$' + place.price_by_night +
                                  '</div>' +
                                  '<div class="information">' +
                                      '<div class="max_guest">' +
                                          '<i class="fa fa-users fa-3x" aria-hidden="true"></i>' +
                                          '<br />' + place.max_guest + ' Guests' +
                                      '</div>' +
                                      '<div class="number_rooms">' +
                                          '<i class="fa fa-bed fa-3x" aria-hidden="true"></i>' +
                                          '<br />' + place.number_rooms + ' Bedrooms' +
                                      '</div>' +
                                      '<div class="number_bathrooms">' +
                                          '<i class="fa fa-bath fa-3x" aria-hidden="true"></i>' +
                                          '<br />' + place.number_bathrooms + ' Bathroom' +
                                      '</div>' +
                                  '</div>' +
                                  '<div class="description">' +
                                      place.description +
                                  '</div>' +
                              '</article>';
                $('.places').append(article);
            });
        }
    });
});
```

With these changes, the places will be fetched dynamically from the front-end, enhancing the user experience of our AirBnB clone application.

# AirBnB clone (Web dynamic) - Filter places by Amenity mandatory

To implement filtering places by Amenity in our AirBnB clone, we'll follow these steps:

1. **Change Route and Create Template**: Replace the route `3-hbnb` with `4-hbnb` in the file `4-hbnb.py` (based on `3-hbnb.py`). Additionally, create a new template `4-hbnb.html` (based on `3-hbnb.html`).

2. **Update HTML Template**: In the `4-hbnb.html` template, we'll:

   - Import the JavaScript file `static/scripts/4-hbnb.js` in the `<head>` tag instead of `3-hbnb.js`.

3. **Write JavaScript Script**: We'll write a JavaScript script (`static/scripts/4-hbnb.js`) based on `3-hbnb.js`. This script will:

   - Make a new POST request to `places_search` endpoint with the list of Amenities checked when the button tag is clicked.

Here's an example of how the JavaScript script can be implemented:

```javascript
// static/scripts/4-hbnb.js
$(document).ready(function() {
    // Event listener for button click
    $('button').click(function() {
        // Array to store checked amenities
        var amenitiesChecked = [];
        $('input[type="checkbox"]:checked').each(function() {
            amenitiesChecked.push($(this).data('id'));
        });

        // Make POST request to places_search endpoint with checked amenities
        $.ajax({
            type: 'POST',
            url: 'http://0.0.0.0:5001/api/v1/places_search/',
            contentType: 'application/json',
            data: JSON.stringify({ amenities: amenitiesChecked }),
            success: function(data) {
                // Handle success response - Update UI with filtered places
                console.log('Filtered places:', data);
                // Implement UI update logic here
            },
            error: function(xhr, status, error) {
                // Handle error response
                console.error('Error:', error);
            }
        });
    });
});
```

With these changes, users will be able to filter places by Amenity in our AirBnB clone application.

# AirBnB clone (Web dynamic) - States and Cities #advanced

In this advanced task, we'll extend our filtering capabilities to include States and Cities. Here's how we'll proceed:

1. **Change Route and Create Template**: Replace the route `4-hbnb` with `100-hbnb` in the file `100-hbnb.py` (based on `4-hbnb.py`). Additionally, create a new template `100-hbnb.html` (based on `4-hbnb.html`).

2. **Update HTML Template**: In the `100-hbnb.html` template, we'll:

   - Import the JavaScript file `static/scripts/100-hbnb.js` in the `<head>` tag instead of `4-hbnb.js`.
   - Add a `<input type="checkbox">` tag to all `<li>` tags of each state and city.
   - Position the new checkbox 10px to the left of the State or City name.
   - Add the attribute `data-id=":state_id"` to the input tags of each state `<li>` tag to store the State ID.
   - Add the attribute `data-name=":state_name"` to the input tags of each state `<li>` tag to store the State name.
   - Add the attribute `data-id=":city_id"` to the input tags of each city `<li>` tag to store the City ID.
   - Add the attribute `data-name=":city_name"` to the input tags of each city `<li>` tag to store the City name.

3. **Write JavaScript Script**: We'll write a JavaScript script (`static/scripts/100-hbnb.js`) based on `4-hbnb.js`. This script will:

   - Listen to changes on each input checkbox tag.
   - If the checkbox is checked, store the State or City ID in a variable (dictionary or list).
   - If the checkbox is unchecked, remove the State or City ID from the variable.
   - Update the `<h4>` tag inside the `<div>` Locations with the list of States or Cities checked.
   - When the button tag is clicked, make a new POST request to `places_search` endpoint with the list of Amenities, Cities, and States checked.

Here's an example of how the JavaScript script can be implemented:

```javascript
// static/scripts/100-hbnb.js
$(document).ready(function() {
    // Event listener for checkbox changes
    $('input[type="checkbox"]').change(function() {
        var locationsChecked = {};

        // Loop through checked checkboxes
        $('input[type="checkbox"]:checked').each(function() {
            var id = $(this).data('id');
            var name = $(this).data('name');

            // Check if it's a state or city
            if ($(this).hasClass('state')) {
                locationsChecked[id] = { 'id': id, 'name': name, 'type': 'state' };
            } else if ($(this).hasClass('city')) {
                locationsChecked[id] = { 'id': id, 'name': name, 'type': 'city' };
            }
        });

        // Update UI with list of States or Cities checked
        var locationsList = Object.values(locationsChecked).map(location => location.name);
        $('#locations').text(locationsList.join(', '));
    });

    // Event listener for button click
    $('button').click(function() {
        // Make POST request to places_search endpoint with checked amenities, cities, and states
        var amenitiesChecked = [];
        // Add code to get amenities checked
        var citiesChecked = Object.values(locationsChecked).filter(location => location.type === 'city').map(city => city.id);
        var statesChecked = Object.values(locationsChecked).filter(location => location.type === 'state').map(state => state.id);

        var requestData = {
            'amenities': amenitiesChecked,
            'cities': citiesChecked,
            'states': statesChecked
        };

        $.ajax({
            type: 'POST',
            url: 'http://0.0.0.0:5001/api/v1/places_search/',
            contentType: 'application/json',
            data: JSON.stringify(requestData),
            success: function(data) {
                // Handle success response - Update UI with filtered places
                console.log('Filtered places:', data);
                // Implement UI update logic here
            },
            error: function(xhr, status, error) {
                // Handle error response
                console.error('Error:', error);
            }
        });
    });
});
```

With these changes, users will be able to filter places by States and Cities in our AirBnB clone application.

# AirBnB clone (Web dynamic) - Reviews #advanced

In this advanced task, we'll add a new feature to show and hide reviews. Here's how we'll proceed:

1. **Change Route and Create Template**: Replace the route `100-hbnb` with `101-hbnb` in the file `101-hbnb.py` (based on `100-hbnb.py`). Additionally, create a new template `101-hbnb.html` (based on `100-hbnb.html`).

2. **Update HTML Template**: In the `101-hbnb.html` template, we'll:

   - Import the JavaScript file `static/scripts/101-hbnb.js` in the `<head>` tag instead of `100-hbnb.js`.
   - Design the list of reviews.
   - Add a `<span>` element at the right of the `<h2>` "Reviews" with value "show" and add all necessary attributes to implement the show/hide feature.

3. **Write JavaScript Script**: We'll write a JavaScript script (`static/scripts/101-hbnb.js`) based on `100-hbnb.js`. This script will:

   - Listen to clicks on the `<span>` element next to the "Reviews" `<h2>`.
   - When clicked, fetch, parse, and display reviews.
   - Change the text of the `<span>` element to "hide" if reviews are displayed.
   - If the text is "hide", remove all review elements from the DOM to hide reviews.
   - This button should work like a toggle to fetch/display and hide reviews.

Here's an example of how the JavaScript script can be implemented:

```javascript
// static/scripts/101-hbnb.js
$(document).ready(function() {
    // Event listener for span click
    $('span#toggle-reviews').click(function() {
        var reviewsContainer = $('#reviews-container');
        if ($(this).text() === 'show') {
            // Fetch and display reviews
            $.ajax({
                type: 'GET',
                url: 'http://0.0.0.0:5001/api/v1/reviews/',
                success: function(data) {
                    // Parse and display reviews
                    console.log('Fetched reviews:', data);
                    // Implement logic to display reviews in the UI
                    // For example: reviewsContainer.append(...);
                },
                error: function(xhr, status, error) {
                    console.error('Error fetching reviews:', error);
                }
            });
            $(this).text('hide');
        } else {
            // Hide reviews
            reviewsContainer.empty(); // Remove all review elements from the DOM
            $(this).text('show');
        }
    });
});
```

With these changes, users will be able to toggle the display of reviews in our AirBnB clone application.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
