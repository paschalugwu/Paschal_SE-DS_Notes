# Introduction to Declaring API Routes in a Flask App

Flask is a lightweight web framework in Python that is used to build web applications easily. One of its powerful features is the ability to create APIs. An API (Application Programming Interface) allows different software systems to communicate with each other. In this note, we will learn how to declare API routes in a Flask app.

## Setting Up Flask

Before we begin, ensure you have Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

Once Flask is installed, you can create a simple Flask app. Here’s a basic example to get you started:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we import Flask, create an instance of the Flask class, and define a route using the `@app.route('/')` decorator. This route corresponds to the home page of our web application, which returns "Hello, World!" when accessed.

## Declaring API Routes

API routes are similar to regular routes, but they typically return data in JSON format rather than HTML. Let’s create a few API routes.

### Example 1: Basic API Route

Here’s an example of a basic API route that returns a JSON response:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_api():
    response = {
        'message': 'Hello, API!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, the `/api/hello` route returns a JSON response with a simple message. The `jsonify` function converts our dictionary into a JSON response.

### Example 2: API Route with Parameters

Sometimes, you may want your API to accept parameters. Here’s an example of an API route that takes a parameter from the URL:

```python
@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    response = {
        'message': f'Hello, {name}!'
    }
    return jsonify(response)
```

In this example, the `<name>` part of the route is a parameter. When you access `/api/greet/John`, it will return `{"message": "Hello, John!"}`.

### Example 3: API Route with Query Parameters

You can also accept query parameters in your API routes. Here’s how:

```python
from flask import request

@app.route('/api/square', methods=['GET'])
def square():
    number = request.args.get('number', default=1, type=int)
    response = {
        'result': number ** 2
    }
    return jsonify(response)
```

In this example, the `/api/square` route takes a query parameter `number` and returns its square. If you access `/api/square?number=4`, it will return `{"result": 16}`.

### Example 4: API Route with POST Method

APIs often need to handle POST requests, where data is sent to the server in the request body. Here’s an example:

```python
@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    response = {
        'result': result
    }
    return jsonify(response)
```

In this example, the `/api/add` route expects a POST request with a JSON body containing `num1` and `num2`. It returns their sum in the response.

### Example 5: API Route with Error Handling

It’s important to handle errors gracefully in your API routes. Here’s an example:

```python
@app.route('/api/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        numerator = data.get('numerator')
        denominator = data.get('denominator')
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        result = numerator / denominator
        response = {
            'result': result
        }
    except (ValueError, TypeError) as e:
        response = {
            'error': str(e)
        }
        return jsonify(response), 400
    return jsonify(response)
```

In this example, the `/api/divide` route handles division and checks for errors such as division by zero. If an error occurs, it returns a JSON response with an error message and a 400 status code.

## Real-World Application: Building a Simple To-Do API

Let’s apply what we’ve learned to build a simple To-Do API. This API will allow users to create, read, update, and delete to-do items.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = request.get_json()
    todos[todo_id] = todo
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos.pop(todo_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we have four routes:
1. `GET /api/todos` - Retrieves all to-do items.
2. `POST /api/todos` - Adds a new to-do item.
3. `PUT /api/todos/<int:todo_id>` - Updates a to-do item by ID.
4. `DELETE /api/todos/<int:todo_id>` - Deletes a to-do item by ID.

## Technical End-of-Chapter MCQ

1. What is the purpose of the `@app.route` decorator in Flask?
    a) To start the Flask app  
    b) To define a route for a specific URL  
    c) To install Flask  
    d) To configure the app  

2. What does the `jsonify` function do in Flask?
    a) Converts a JSON response to a dictionary  
    b) Converts a dictionary to a JSON response  
    c) Starts the Flask app  
    d) Defines a route  

3. How do you extract a query parameter named `name` from the URL in Flask?
    a) `request.get('name')`  
    b) `request.args.get('name')`  
    c) `request.params.get('name')`  
    d) `request.query.get('name')`  

4. What HTTP method is used to retrieve data from a server in Flask?
    a) POST  
    b) PUT  
    c) GET  
    d) DELETE  

5. How do you define a route that takes a URL parameter named `id` in Flask?
    a) `@app.route('/item/<id>')`  
    b) `@app.route('/item/:id')`  
    c) `@app.route('/item/<int:id>')`  
    d) `@app.route('/item/{id}')`  

6. Which method is used to get JSON data from a request body in Flask?
    a) `request.json()`  
    b) `request.data()`  
    c) `request.get_json()`  
    d) `request.get_data()`  

7. What status code is typically returned for a successful POST request?
    a) 200  
    b) 201  
    c) 204  
    d) 404  

8. What does the `methods` parameter in the `@app.route` decorator specify?
    a) The HTTP methods that the route can handle  
    b) The number of routes  
    c) The data format  
    d) The app configuration  

9. How do you handle errors in a Flask route?
    a) Using a try-except block  
    b) Using an if-else block  
    c) Using a for loop  
    d) Using a while loop  

10. Which function is used to run a Flask app?
    a) `app.start()`  
    b) `app.init()`  
    c) `app.run()`  
    d) `app.execute()`  

## Answers

1. b) To define a route for a specific URL  
2. b) Converts a dictionary to a JSON response  
3. b) `request.args.get('name')`  
4. c) GET  
5. c) `@app.route('/item/<int:id>')`  
6. c) `request.get_json()`  
7. b) 201  
8. a) The HTTP methods that the route can handle  
9. a) Using a try-except block  
10. c) `app.run()`  

# Getting and Setting Cookies in Flask

Cookies are small pieces of data that are stored on the client side and sent to the server with every request. They are commonly used to manage user sessions, store preferences, and track user behavior. In this note, we will learn how to get and set cookies in a Flask application.

## Setting Up Flask

Before we begin, ensure you have Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

Once Flask is installed, you can create a simple Flask app. Here’s a basic example to get you started:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we import Flask, create an instance of the Flask class, and define a route using the `@app.route('/')` decorator. This route corresponds to the home page of our web application, which returns "Hello, World!" when accessed.

## Setting Cookies

To set a cookie in Flask, you use the `set_cookie` method on the response object. Here’s an example:

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('username', 'John Doe')
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, when you visit the `/setcookie` route, the server responds with a message "Cookie is set" and sets a cookie named `username` with the value `John Doe`.

### Setting Cookie Expiration

You can also set an expiration time for a cookie. Here’s how you do it:

```python
@app.route('/setcookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('username', 'John Doe', max_age=60*60*24)  # 1 day
    return response
```

In this example, the `max_age` parameter is set to 60*60*24 seconds, which is equivalent to one day.

## Getting Cookies

To get a cookie in Flask, you use the `request.cookies` attribute. Here’s an example:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username: {username}'

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, when you visit the `/getcookie` route, the server retrieves the value of the `username` cookie and displays it.

## Deleting Cookies

To delete a cookie, you use the `set_cookie` method with an expiration time in the past. Here’s an example:

```python
@app.route('/deletecookie')
def delete_cookie():
    response = make_response("Cookie is deleted")
    response.set_cookie('username', '', expires=0)
    return response
```

In this example, when you visit the `/deletecookie` route, the server deletes the `username` cookie by setting its expiration time to 0.

## Real-World Application: User Preferences

Let’s apply what we’ve learned to build a simple application that stores user preferences in cookies. For this example, we will create a web page that allows users to set their preferred background color.

```python
from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

template = """
<!doctype html>
<html>
<head>
    <title>User Preferences</title>
    <style>
        body {
            background-color: {{ background_color }};
        }
    </style>
</head>
<body>
    <h1>Set Your Background Color</h1>
    <form action="/setcolor" method="post">
        <input type="color" name="color" value="{{ background_color }}">
        <input type="submit" value="Set Color">
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    background_color = request.cookies.get('background_color', '#FFFFFF')
    return render_template_string(template, background_color=background_color)

@app.route('/setcolor', methods=['POST'])
def set_color():
    color = request.form.get('color')
    response = make_response(render_template_string(template, background_color=color))
    response.set_cookie('background_color', color, max_age=60*60*24*30)  # 30 days
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we create a simple HTML template that allows users to select a background color. The selected color is stored in a cookie named `background_color`. When the user revisits the page, the background color is retrieved from the cookie and applied to the page.

## Technical End-of-Chapter MCQ

1. What method is used to set a cookie in Flask?
    a) `set_cookie`  
    b) `add_cookie`  
    c) `create_cookie`  
    d) `insert_cookie`  

2. How do you get a cookie in Flask?
    a) `request.cookies.get('cookie_name')`  
    b) `request.cookies['cookie_name']`  
    c) `request.get_cookie('cookie_name')`  
    d) `request.get('cookie_name')`  

3. What parameter is used to set the expiration time of a cookie?
    a) `expires`  
    b) `max_age`  
    c) `timeout`  
    d) `expiry`  

4. How do you delete a cookie in Flask?
    a) `response.delete_cookie('cookie_name')`  
    b) `response.clear_cookie('cookie_name')`  
    c) `response.set_cookie('cookie_name', '', max_age=0)`  
    d) `response.set_cookie('cookie_name', '', expires=0)`  

5. What is the default value returned by `request.cookies.get('cookie_name')` if the cookie does not exist?
    a) `None`  
    b) `False`  
    c) `''`  
    d) `0`  

6. What module do you need to import to use cookies in Flask?
    a) `flask.cookie`  
    b) `flask.sessions`  
    c) `flask.request`  
    d) `flask`  

7. In which object do you set a cookie in Flask?
    a) `request`  
    b) `session`  
    c) `response`  
    d) `cookie`  

8. How do you specify the path of a cookie in Flask?
    a) `response.set_cookie('cookie_name', 'value', path='/')`  
    b) `response.set_cookie('cookie_name', 'value', location='/')`  
    c) `response.set_cookie('cookie_name', 'value', dir='/')`  
    d) `response.set_cookie('cookie_name', 'value', folder='/')`  

9. How do you access all cookies sent with a request in Flask?
    a) `request.cookies.get_all()`  
    b) `request.cookies`  
    c) `request.get_cookies()`  
    d) `request.all_cookies()`  

10. What status code is typically returned when a cookie is successfully set in Flask?
    a) 200  
    b) 201  
    c) 204  
    d) 302  

## Answers

1. a) `set_cookie`  
2. a) `request.cookies.get('cookie_name')`  
3. b) `max_age`  
4. d) `response.set_cookie('cookie_name', '', expires=0)`  
5. a) `None`  
6. d) `flask`  
7. c) `response`  
8. a) `response.set_cookie('cookie_name', 'value', path='/')`  
9. b) `request.cookies`  
10. a) 200  

# Retrieving Request Form Data in Flask

In web applications, retrieving form data submitted by users is a common task. Flask provides convenient ways to handle form data through the `request` object. In this note, we will learn how to retrieve request form data in a Flask application.

## Setting Up Flask

Before we begin, ensure you have Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

Once Flask is installed, you can create a simple Flask app. Here’s a basic example to get you started:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we import Flask, create an instance of the Flask class, and define a route using the `@app.route('/')` decorator. This route corresponds to the home page of our web application, which returns "Hello, World!" when accessed.

## Retrieving Form Data

To retrieve form data submitted by a user, you can use the `request` object's `form` attribute. Here’s how you can handle a simple form submission:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f'Username: {username}, Password: {password}'
    else:
        return 'Submit your form'

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we define a route `/submit` that handles both GET and POST requests. When a POST request is made (typically from a form submission), we retrieve the `username` and `password` fields from the form data using `request.form.get()`.

## Handling File Uploads

Flask also supports handling file uploads along with form data. Here’s an example of how you can handle file uploads:

```python
from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, the route `/upload` accepts POST requests with a file upload field named `file`. The file is saved to the specified upload folder using `secure_filename` to prevent any malicious file uploads.

## Real-World Application: Contact Form Submission

Let’s apply what we’ve learned to build a simple contact form submission feature. This feature will accept user input for name, email, and message, and send it to a specified email address.

```python
from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Send email
        sender_email = 'your_email@example.com'
        receiver_email = 'recipient_email@example.com'
        password = 'your_password'
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'New Contact Form Submission'
        
        body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        
        return 'Message sent successfully'
    else:
        return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we create a contact form that accepts `name`, `email`, and `message` from the user. When the form is submitted (POST request), the data is retrieved using `request.form.get()` and sent via email using the `smtplib` library.

## Technical End-of-Chapter MCQ

1. How do you retrieve form data submitted via POST request in Flask?
    a) `request.args.get('field_name')`  
    b) `request.form['field_name']`  
    c) `request.get_form_data('field_name')`  
    d) `request.data.get('field_name')`  

2. Which HTTP methods can be used to submit form data in Flask?
    a) GET  
    b) POST  
    c) PUT  
    d) DELETE  

3. How do you access a specific form field named `email` from a POST request in Flask?
    a) `request.form['email']`  
    b) `request.get_form_field('email')`  
    c) `request.form.get('email')`  
    d) `request.data['email']`  

4. What module do you need to import to handle file uploads in Flask?
    a) `flask.file`  
    b) `flask.upload`  
    c) `flask.request`  
    d) `werkzeug.utils`  

5. How do you handle a file upload in Flask?
    a) `request.file.get('file')`  
    b) `request.files['file']`  
    c) `request.get_file('file')`  
    d) `request.upload('file')`  

6. What method is used to save an uploaded file in Flask?
    a) `file.save('/path/to/save')`  
    b) `save_file('file', '/path/to/save')`  
    c) `save_file('/path/to/save')`  
    d) `file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))`  

7. How do you handle missing form fields in Flask?
    a) Use a try-except block  
    b) Use an if-else statement  
    c) Use a while loop  
    d) Use a for loop  

8. What is the default encoding type for form submissions in HTML?
    a) `application/json`  
    b) `text/html`  
    c) `multipart/form-data`  
    d) `application/x-www-form-urlencoded`  

9. How do you specify the action attribute in an HTML form to submit to a Flask route `/submit`?
    a) `<form action="/submit" method="POST">`  
    b) `<form action="/submit">`  
    c) `<form method="POST">`  
    d) `<form action="/submit" enctype="multipart/form-data">`  

10. What is the primary use of handling form data in real-world Flask applications?
    a) Displaying static content  
    b) Interacting with databases  
    c) Processing payments  
    d) Sending emails  

## Answers

1. b) `request.form['field_name']`  
2. b) POST  
3. c) `request.form.get('email')`  
4. d) `werkzeug.utils`  
5. b) `request.files['file']`  
6. d) `file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))`  
7. b) Use an if-else statement  
8. d) `application/x-www-form-urlencoded`  
9. a) `<form action="/submit" method="POST">`  
10. b) Interacting with databases  

# Returning Various HTTP Status Codes in Flask

HTTP status codes are important indicators returned by a server in response to a client's request. They provide information about the status of the request and can convey success, error, redirection, and other conditions. In this note, we will learn how to return various HTTP status codes in a Flask application.

## Setting Up Flask

Before we begin, ensure you have Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

Once Flask is installed, you can create a simple Flask app. Here’s a basic example to get you started:

```python
from flask import Flask, abort, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we import Flask, create an instance of the Flask class, and define a route using the `@app.route('/')` decorator. This route corresponds to the home page of our web application, which returns "Hello, World!" when accessed.

## Returning HTTP Status Codes

### Success Codes (2xx)

To return a success status code, you can simply return the desired response along with the appropriate status code. Here’s an example:

```python
@app.route('/success')
def success():
    return 'Operation successful', 200
```

In this example, visiting the route `/success` will return the message "Operation successful" with a status code `200`, indicating the request was successful.

### Redirect Codes (3xx)

To redirect a client to a different URL, you can use Flask's `redirect` function along with a redirect status code. Here’s how you can implement a redirection:

```python
from flask import redirect, url_for

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('home')), 302
```

In this example, visiting the route `/redirect` will redirect the client to the home page (`/`) with a status code `302`, indicating a temporary redirect.

### Client Error Codes (4xx)

To handle client errors (e.g., page not found, unauthorized access), you can use Flask's `abort` function. Here’s an example:

```python
@app.route('/unauthorized')
def unauthorized():
    abort(401)
```

In this example, visiting the route `/unauthorized` will abort the request with a status code `401`, indicating unauthorized access.

### Server Error Codes (5xx)

To handle server errors (e.g., internal server error), you can return an error message along with the appropriate status code. Here’s an example:

```python
@app.route('/server_error')
def server_error():
    return 'Internal Server Error', 500
```

In this example, visiting the route `/server_error` will return the message "Internal Server Error" with a status code `500`, indicating an internal server error.

## Real-World Application: Error Handling

Let’s apply what we’ve learned to implement error handling in a Flask application. We will create custom error handlers for 404 (Not Found) and 500 (Internal Server Error) status codes.

```python
@app.errorhandler(404)
def not_found_error(error):
    return 'Page Not Found', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Internal Server Error', 500
```

In this example, if a 404 error occurs (page not found), the `not_found_error` function will handle it and return "Page Not Found" with a status code `404`. Similarly, if a 500 error occurs (internal server error), the `internal_server_error` function will handle it and return "Internal Server Error" with a status code `500`.

## Technical End-of-Chapter MCQ

1. Which HTTP status code is used to indicate a successful request in Flask?
    a) 100  
    b) 200  
    c) 300  
    d) 400  

2. How do you return a custom status message along with a status code in Flask?
    a) `return 'Message', code`  
    b) `return code: 'Message'`  
    c) `send_status(code, 'Message')`  
    d) `set_status(code), 'Message'`  

3. Which Flask function is used to perform a redirect?
    a) `forward()`  
    b) `redirect()`  
    c) `move()`  
    d) `route_to()`  

4. What status code is typically used for a temporary redirect in Flask?
    a) 200  
    b) 301  
    c) 302  
    d) 404  

5. How do you handle a client error in Flask?
    a) `abort(code)`  
    b) `redirect(code)`  
    c) `error(code)`  
    d) `return code`  

6. What is the default status code returned by Flask for successful responses?
    a) 200  
    b) 300  
    c) 400  
    d) 500  

7. Which decorator is used to handle errors in Flask?
    a) `@handle_error`  
    b) `@error_handler`  
    c) `@app.errorhandler(code)`  
    d) `@handle_exception(code)`  

8. How do you return a 404 error in Flask?
    a) `return 'Not Found', 404`  
    b) `abort(404)`  
    c) `raise_error(404)`  
    d) `error(404)`  

9. What HTTP status code indicates an internal server error in Flask?
    a) 401  
    b) 404  
    c) 500  
    d) 503  

10. In which scenario would you use a 500 status code in Flask?
    a) Page not found  
    b) Access denied  
    c) Successful form submission  
    d) Internal server error  

## Answers

1. b) 200  
2. a) `return 'Message', code`  
3. b) `redirect()`  
4. c) 302  
5. a) `abort(code)`  
6. a) 200  
7. c) `@app.errorhandler(code)`  
8. a) `return 'Not Found', 404`  
9. c) 500  
10. d) Internal server error  
