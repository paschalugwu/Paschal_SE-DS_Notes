## Application Server vs. Web Server

### Introduction:

In the realm of web development and software engineering, understanding the distinction between application servers and web servers is crucial. Both play vital roles in serving web applications, but they serve different purposes and handle different aspects of the web ecosystem.

### Web Server:

A web server is essentially a piece of software that serves web content to clients over the HTTP protocol. Its primary responsibility is to handle requests from clients (such as web browsers) and respond with the appropriate resources, typically HTML files, images, CSS stylesheets, and JavaScript files.

#### Example Code Snippet (using Node.js and Express.js):

```javascript
const express = require('express');
const app = express();

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Define a route to handle incoming HTTP GET requests
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

In this example, we're using Express.js, a popular web application framework for Node.js, to create a simple web server. The `express.static` middleware serves static files (like images and CSS) from the 'public' directory, while the `app.get` method defines a route for handling incoming GET requests to the root URL ('/'). When a client accesses the root URL, the server responds with the text 'Hello, world!'.

### Application Server:

An application server, on the other hand, is responsible for executing the logic of the web application itself. It provides an environment for running server-side code, processing business logic, interacting with databases, and generating dynamic content to be served by the web server.

#### Example Code Snippet (using Node.js and Express.js with MongoDB):

```javascript
const express = require('express');
const mongoose = require('mongoose');
const app = express();

// Connect to MongoDB database
mongoose.connect('mongodb://localhost/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => {
  console.log('Connected to MongoDB');
})
.catch((err) => {
  console.error('Error connecting to MongoDB', err);
});

// Define a schema for a user object
const userSchema = new mongoose.Schema({
  name: String,
  email: String
});

// Define a model based on the schema
const User = mongoose.model('User', userSchema);

// Define a route to handle POST requests to create a new user
app.post('/users', async (req, res) => {
  const { name, email } = req.body;
  const user = new User({ name, email });

  try {
    await user.save();
    res.status(201).send('User created successfully');
  } catch (err) {
    res.status(400).send('Error creating user');
  }
});

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

In this example, we're still using Express.js, but now we're also incorporating MongoDB, a popular NoSQL database. We define a schema for a user object using Mongoose, a MongoDB object modeling tool for Node.js. Then, we create a route to handle POST requests for creating a new user. When a client sends a POST request to '/users' with JSON data containing a name and email, the server creates a new user object and saves it to the MongoDB database.

### Real-World Applications:

Understanding the distinction between web servers and application servers is essential for building robust and scalable web applications. In a typical web application architecture, the web server (e.g., Nginx, Apache) handles static content delivery and acts as a reverse proxy, while the application server (e.g., Node.js, Django, Ruby on Rails) executes the application logic and interacts with databases and other services.

By mastering the concepts of web servers and application servers, developers can design efficient and maintainable architectures for a wide range of web projects, from simple static websites to complex web applications with dynamic content and user interactions.

## What is a PID? How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04

### PID (Process ID):

A PID, or Process ID, is a unique identifier assigned to each running process in a computer system. It is a numerical value used by the operating system to keep track of processes and manage their execution. PIDs are crucial for various system management tasks, such as process monitoring, termination, and resource allocation.

#### Real-World Application:

In a web server environment, understanding PIDs is essential for managing and troubleshooting server processes. For example, when serving a web application using Gunicorn and Nginx, each Gunicorn worker process is assigned a unique PID. By monitoring these PIDs, administrators can track the health and performance of the application, identify bottlenecks, and troubleshoot issues such as memory leaks or high CPU usage.

### Serving a Flask Application with Gunicorn and Nginx on Ubuntu 16.04:

#### Step 1: Install Flask and Gunicorn

First, ensure that you have Python and pip installed on your Ubuntu 16.04 server. Then, install Flask and Gunicorn using pip:

```bash
pip install flask gunicorn
```

#### Step 2: Write Your Flask Application

Create a Python file (e.g., `app.py`) and write your Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
```

#### Step 3: Run Your Flask Application with Gunicorn

Use Gunicorn to serve your Flask application. Run the following command in your terminal:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

This command tells Gunicorn to bind to all available network interfaces (`0.0.0.0`) on port `8000` and serve the Flask application defined in the `app` module.

#### Step 4: Install and Configure Nginx

Install Nginx on your Ubuntu 16.04 server:

```bash
sudo apt-get update
sudo apt-get install nginx
```

After installation, configure Nginx to proxy requests to your Gunicorn server. Create a new Nginx configuration file (e.g., `myapp`) in the `/etc/nginx/sites-available/` directory with the following content:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Replace `your_domain.com` with your actual domain name.

#### Step 5: Enable Your Nginx Configuration and Restart Nginx

Create a symbolic link to your Nginx configuration file in the `/etc/nginx/sites-enabled/` directory:

```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
```

Then, test the Nginx configuration and restart Nginx:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

Now, your Flask application should be accessible via Nginx at your domain name.

#### Real-World Application:

This setup demonstrates a common architecture for deploying Flask applications in a production environment. Gunicorn serves as the application server, handling incoming requests and executing the Flask application code, while Nginx acts as a reverse proxy, forwarding client requests to Gunicorn and serving static files efficiently. By understanding and implementing this setup, developers can deploy scalable and reliable Flask applications capable of handling high traffic loads.

## Running Gunicorn

### Introduction:

Gunicorn, which stands for "Green Unicorn," is a popular WSGI (Web Server Gateway Interface) HTTP server for Python web applications. It is commonly used to deploy web applications written in frameworks like Flask and Django. Gunicorn is known for its simplicity, reliability, and ability to handle concurrent requests efficiently.

### How to Run Gunicorn:

To run a Python web application using Gunicorn, follow these steps:

#### Step 1: Install Gunicorn

Before running Gunicorn, ensure it is installed on your system. You can install it using pip, the Python package manager:

```bash
pip install gunicorn
```

#### Step 2: Navigate to Your Application Directory

Navigate to the directory where your Python web application is located. This could be a Flask or Django project directory.

```bash
cd /path/to/your/application
```

#### Step 3: Run Gunicorn

To run Gunicorn, use the following command:

```bash
gunicorn --bind 0.0.0.0:8000 <your_application_module>:<application_instance>
```

- Replace `<your_application_module>` with the Python module where your application is defined.
- Replace `<application_instance>` with the variable name of your application instance within the specified module.

For example, if you have a Flask application defined in a module named `app` and the application instance is named `app`, you would run:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

#### Step 4: Access Your Application

Once Gunicorn is running, your application should be accessible at the specified host and port. Open a web browser and navigate to `http://your_server_ip:8000` to access your application.

### Real-World Application:

Running Gunicorn is a common practice when deploying Python web applications in production environments. By using Gunicorn, developers can ensure their applications are served reliably and efficiently, capable of handling multiple concurrent requests without sacrificing performance. Gunicorn is often used alongside web servers like Nginx or Apache, which act as reverse proxies to route incoming requests to Gunicorn.

In real-world projects, deploying applications with Gunicorn enables developers to build scalable and robust web services, powering a wide range of web applications, APIs, and microservices. Whether it's a small-scale web application or a large-scale enterprise solution, Gunicorn provides the foundation for serving Python web applications with ease and reliability.

## Be Careful with the Way Flask Manages Slash in Route - strict_slashes

### Introduction:

When defining routes in a Flask application, it's essential to understand how Flask manages trailing slashes in URLs. By default, Flask treats URLs with and without trailing slashes differently, which can affect how routes are matched and how requests are handled. Understanding this behavior is crucial for designing consistent and predictable URL structures in Flask applications.

### strict_slashes Setting:

Flask provides a configuration option called `strict_slashes` to control how trailing slashes are handled in route definitions. When `strict_slashes` is set to `True` (the default behavior), Flask will enforce strict matching of routes based on the presence or absence of a trailing slash in the requested URL.

#### Example Code Snippet:

```python
from flask import Flask

app = Flask(__name__)

# Route definition with strict_slashes=False
@app.route('/example', strict_slashes=False)
def example_route():
    return 'This route matches both "/example" and "/example/"'

if __name__ == '__main__':
    app.run()
```

In this example, we define a route `/example` with `strict_slashes=False`. This means that the route will match both `/example` and `/example/`, regardless of whether a trailing slash is present in the requested URL. Without setting `strict_slashes=False`, Flask would consider `/example` and `/example/` as distinct routes.

### Real-World Application:

Understanding and properly managing trailing slashes in route definitions is essential for designing clean and user-friendly URL structures in Flask applications. In real-world projects, consistent URL structures enhance the usability and maintainability of web applications, making it easier for users and search engines to navigate and understand the application's content.

By leveraging the `strict_slashes` setting and carefully considering how routes are defined, developers can ensure that their Flask applications handle URL variations gracefully, providing a seamless browsing experience for users. Whether it's building RESTful APIs, serving web pages, or designing complex routing systems, mastering the management of trailing slashes in Flask routes is a fundamental aspect of web development with Flask.

## Upstart Documentation

### Introduction:

Upstart is an event-based init system for Unix-like operating systems. It is used to manage services, processes, and daemons during system boot and throughout the system's runtime. Upstart provides a simple and flexible mechanism for starting, stopping, and managing system services, enabling administrators to configure and control the behavior of these services efficiently.

### Key Concepts:

#### Jobs:

In Upstart, a job refers to a task or service that Upstart manages. Each job is defined by a configuration file located in the `/etc/init` directory. The configuration file specifies various parameters and actions associated with the job, such as when to start the job, what conditions must be met for it to start, and what actions to take when starting, stopping, or restarting the job.

#### Events:

Events are triggers that initiate actions within Upstart. Jobs can respond to events by defining event handlers in their configuration files. Events can be system events (e.g., system startup, system shutdown) or custom events generated by other jobs or external processes.

#### States:

Jobs in Upstart can be in one of several states, indicating their current status. Common states include:

- **Running:** The job is currently running.
- **Stopped:** The job has been stopped and is not running.
- **Starting:** The job is in the process of starting.
- **Stopping:** The job is in the process of stopping.

### Example Upstart Configuration:

Below is an example Upstart configuration file (`example.conf`) for a hypothetical service named `example-service`:

```conf
description "Example Service"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
respawn limit 10 5

pre-start script
    # Actions to be performed before starting the service
end script

exec /usr/bin/example-service --config /etc/example-service/config.conf
```

In this configuration:

- The `description` directive provides a brief description of the service.
- The `start on` and `stop on` directives specify the conditions under which the service should start and stop, respectively. In this case, the service starts on runlevels 2, 3, 4, and 5, and stops on runlevels other than these.
- The `respawn` directive indicates that the service should automatically restart if it exits unexpectedly. The `respawn limit` directive specifies the maximum number of respawns allowed within a specific time period.
- The `pre-start script` section contains any actions to be performed before starting the service. This could include setting up environment variables or checking prerequisites.
- The `exec` directive specifies the command to execute to start the service.

### Real-World Application:

Upstart is commonly used in Unix-like operating systems to manage system services and daemons. It is especially prevalent in distributions such as Ubuntu, where it serves as the default init system. Understanding Upstart and its configuration enables administrators to effectively manage services and ensure the smooth operation of their systems. By defining and configuring Upstart jobs, administrators can automate the startup and management of services, improve system reliability, and streamline system administration tasks.

## Setting Up Production with Gunicorn

### Introduction:

Setting up a production environment with Gunicorn involves configuring Gunicorn to serve your Flask application on a production server. Gunicorn acts as a WSGI server, handling incoming requests and executing your Flask application code. This setup ensures that your application can handle production-level traffic and maintain performance and reliability.

### Requirements:

1. **Install Gunicorn and Required Libraries:** Install Gunicorn and any other libraries required by your Flask application on your production server.

2. **Use Flask Application Object Named "app":** Ensure that your Flask application object is named "app." This is necessary for Gunicorn to serve your application correctly.

3. **Serve Content from Same Route as Previous Task:** Serve the same content from the same route (`/airbnb-onepage/`) as in the previous task using Gunicorn. Bind the Gunicorn instance to localhost listening on port 5000, with your Flask application object as the entry point.

4. **Ensure Port 6000 is Free:** Make sure nothing is listening on port 6000, as the checker will bind a Gunicorn instance to that port to check your code.

### Example:

#### Terminal 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```

#### Terminal 2:

```bash
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

### Real-World Application:

Setting up production with Gunicorn is a common practice in deploying Flask applications for production use. By configuring Gunicorn to serve Flask applications, developers can ensure that their applications are ready to handle production-level traffic and maintain performance and reliability under load. This setup is essential for deploying web applications to production environments, where stability and scalability are critical factors.

## Serving a Page with Nginx

### Introduction:

Configuring Nginx to serve a page from a specific route involves setting up Nginx as a reverse proxy to forward requests to the application server listening on a specific port. This setup allows Nginx to handle incoming HTTP requests and serve the appropriate content from the application server.

### Requirements:

1. **Serve Page Locally and on Public IP:** Configure Nginx to serve the page both locally and on its public IP address on port 80.
   
2. **Proxy Requests to Port 5000:** Nginx should proxy requests to the process listening on port 5000, where the Gunicorn server is running.

3. **Nginx Configuration File:** Include your Nginx configuration file as `2-app_server-nginx_config`.

### Notes:

- To test this setup, you'll need to have your application server (listening on port 5000) running.
  
- In a production environment, the application server would be configured to start upon system startup in a system initialization script.
  
- You may need to reboot your server using the command `sudo reboot` to make Nginx publicly accessible after configuration changes.

### Example:

#### On the Server:

#### Window 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
```

#### Window 2:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

#### On the Local Terminal:

```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
```

### Real-World Application:

Configuring Nginx to serve a page from a specific route is a common practice in web server administration. By setting up Nginx as a reverse proxy, administrators can distribute incoming requests to backend application servers, providing load balancing, caching, and security features. This setup enables efficient handling of web traffic and ensures high availability and performance for web applications deployed in production environments.

## Adding a Route with Query Parameters

### Introduction:

Expanding our web application involves adding another service for Gunicorn to handle. In the `AirBnB_clone_v2/web_flask/6-number_odd_or_even` directory, the route `/number_odd_or_even/<int:n>` is already defined to render a page telling you whether an integer is odd or even. We'll configure Nginx to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/<int:n>` to a Gunicorn instance listening on port 5001.

### Requirements:

1. **Serve Page Locally and on Public IP:** Configure Nginx to serve this page both locally and on its public IP address on port 80.
   
2. **Proxy Requests to Port 5001:** Nginx should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/<int:n>` to the process listening on port 5001.

3. **Nginx Configuration File:** Include your Nginx configuration file as `3-app_server-nginx_config`.

### Tips:

- To configure Nginx, you can refer to articles/docs on understanding Nginx server and location block selection algorithms, understanding Nginx location blocks rewrite rules, and Nginx reverse proxy.

- To spin up a Gunicorn instance as a detached process, you can use the terminal multiplexer utility tmux. For example, `tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'`. To terminate the background process, you can use `kill <PID>`.

### Example:

#### Terminal 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
1684
1688
```

#### Terminal 2:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 5 is odd</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2$
```

#### Local Machine:

```bash
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>vagrant@ubuntu-xenial:~$
```

### Real-World Application:

Configuring Nginx to proxy requests to multiple Gunicorn instances listening on different ports allows for the expansion of web applications to handle various routes and services. This setup is commonly used in real-world projects to scale web applications and efficiently distribute incoming requests based on their URLs. By properly configuring Nginx and Gunicorn, developers can ensure that their web applications are robust, scalable, and capable of handling dynamic content and user interactions.

## Serving Your API with Nginx

### Introduction:

Now, let's serve what you built for the AirBnB clone v3 - RESTful API on `web-01`. This involves setting up Nginx so that the route `/api/` points to a Gunicorn instance listening on port 5002.

### Requirements:

1. **Clone AirBnB_clone_v3:** Begin by cloning your AirBnB_clone_v3 repository.

2. **Configure Nginx:** Setup Nginx so that the route `/api/` points to a Gunicorn instance listening on port 5002. Ensure that Nginx serves this page both locally and on its public IP on port 80.

3. **Test Your Setup:** Bind Gunicorn to `api/v1/app.py` and test your setup by making API requests to ensure proper functioning.

### Example:

#### Terminal 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1:5002/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
```

#### Local Terminal:

```bash
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
vagrant@ubuntu-xenial:~$
```

### Real-World Application:

Configuring Nginx to route requests to a specific Gunicorn instance for serving an API is a common practice in web development. This setup allows for efficient handling of API requests, separation of concerns, and scalability. By properly configuring Nginx and Gunicorn, developers can ensure that their APIs are robust, performant, and accessible to clients over the internet.

## Serving Your AirBnB Clone

### Introduction:

Now, let's serve what you built for the AirBnB clone - Web dynamic on `web-01`. This involves setting up Nginx to properly serve both dynamic content and static assets for your web application.

### Requirements:

1. **Clone AirBnB_clone_v4:** Begin by cloning your AirBnB_clone_v4 repository.

2. **Configure Gunicorn:** Your Gunicorn instance should serve content from `web_dynamic/2-hbnb.py` on port 5003.

3. **Setup Nginx:** Configure Nginx so that the route `/` points to your Gunicorn instance. Additionally, ensure that Nginx properly serves the static assets found in `web_dynamic/static/` to enable proper rendering of your web page.

4. **Update JavaScript File:** Reconfigure `web_dynamic/static/scripts/2-hbnb.js` to point to the correct IP address of your server.

5. **Verification:** Use Developer Tools in your favorite browser to verify that there are no errors.

### Example:

#### Terminal:

```bash
# Clone AirBnB_clone_v4
ubuntu@229-web-01:~/AirBnB_clone_v4$ git clone [your repository URL]

# Start Gunicorn instance
ubuntu@229-web-01:~/AirBnB_clone_v4$ gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app

# Configure Nginx
ubuntu@229-web-01:~/AirBnB_clone_v4$ sudo nano /etc/nginx/sites-available/default

# Add configuration for serving dynamic content and static assets
server {
    listen 80;
    server_name _;
    
    location / {
        proxy_pass http://localhost:5003;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /path/to/your/AirBnB_clone_v4/web_dynamic/static/;
    }
}

# Restart Nginx
ubuntu@229-web-01:~/AirBnB_clone_v4$ sudo systemctl restart nginx
```

### Real-World Application:

Setting up Nginx to serve a web application involves configuring it to proxy requests to a Gunicorn instance for dynamic content and serve static assets directly. This setup ensures efficient handling of both dynamic and static resources, leading to a smooth user experience. By following this configuration, developers can deploy their web applications securely and reliably on production servers, making them accessible to users over the internet.

## Deploying Your Application with systemd

### Introduction:

Once you have configured your application server, it's essential to set it up to run automatically when Linux boots. This ensures that your Gunicorn processes start up as part of the system initialization process, saving you from manually restarting them after server downtime. In this task, we'll use systemd, a system initialization daemon for the Linux OS, to achieve this.

### Requirements:

1. **Write systemd Script:** Create a systemd script that starts a Gunicorn process to serve the same content as in the previous task (`web_dynamic/2-hbnb.py`).
   
2. **Worker Processes:** Configure the Gunicorn process to spawn 3 worker processes for handling requests.

3. **Logging:** Ensure that errors are logged in `/tmp/airbnb-error.log` and access logs are stored in `/tmp/airbnb-access.log`.

4. **Port Binding:** Bind the Gunicorn process to port 5003.

5. **Systemd Script Storage:** Store your systemd script in the appropriate directory on `web-01`.

6. **Start Systemd Service:** Start the systemd service and leave it running to handle incoming requests.

7. **Upload to GitHub:** Upload the `gunicorn.service` file to GitHub for version control.

### Example:

#### Systemd Script (`gunicorn.service`):

```bash
[Unit]
Description=Gunicorn instance to serve AirBnB clone v4
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/path/to/your/AirBnB_clone_v4/web_dynamic
ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:5003 2-hbnb:app
StandardOutput=file:/tmp/airbnb-access.log
StandardError=file:/tmp/airbnb-error.log

[Install]
WantedBy=multi-user.target
```

#### Terminal:

```bash
# Move the systemd script to the appropriate directory
ubuntu@web-01:~$ sudo mv gunicorn.service /etc/systemd/system/

# Reload systemd to load the new service
ubuntu@web-01:~$ sudo systemctl daemon-reload

# Start the Gunicorn service
ubuntu@web-01:~$ sudo systemctl start gunicorn

# Check the status of the service
ubuntu@web-01:~$ sudo systemctl status gunicorn
```

### Real-World Application:

Using systemd to manage your application server's lifecycle is a common practice in real-world projects. It ensures that your server processes start automatically upon system boot, reducing manual intervention and potential downtime. By logging errors and access information, you can monitor the health of your application and troubleshoot issues effectively. Additionally, storing the systemd script in the appropriate directory ensures that it's executed reliably, providing a seamless experience for both users and administrators.

## Implementing Gunicorn Reload Script for No Downtime

### Introduction:

Maintaining high uptime is crucial for internet-based businesses to ensure continuous service availability to customers. However, application servers often need to restart to update with new code or configuration changes, resulting in downtime. To mitigate this, application servers are designed with a master/workers infrastructure, where the master manages requests and workers process them. Updating an application without downtime involves gracefully shutting down old workers and starting new ones with updated code or configuration.

### Requirements:

Write a Bash script to reload Gunicorn gracefully, ensuring no service interruption.

### Example:

#### Reload Script (`4-reload_gunicorn_no_downtime`):

```bash
#!/usr/bin/env bash

# Get the process IDs of Gunicorn instances
gunicorn_pids=$(pgrep gunicorn)

# Check if Gunicorn instances are running
if [ -n "$gunicorn_pids" ]; then
    # Send graceful reload signal to each Gunicorn instance
    for pid in $gunicorn_pids; do
        kill -s HUP $pid
    done
    echo "Gunicorn reloaded gracefully."
else
    echo "No Gunicorn instances found running."
fi
```

#### Terminal:

```bash
sylvain@ubuntu$ ./4-reload_gunicorn_no_downtime
Gunicorn reloaded gracefully.
sylvain@ubuntu$
```

### Real-World Application:

Automating the process of reloading Gunicorn gracefully ensures seamless updates to your application without causing downtime. By gracefully restarting worker processes, requests are handled smoothly without interruption, maintaining high uptime and minimizing customer impact. This script can be integrated into deployment pipelines or executed manually when updates are required, ensuring a reliable and uninterrupted service for end-users.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
