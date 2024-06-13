# Mastering Asynchronous Python: A Comprehensive Guide

# Async and Await Syntax in Python

## Introduction

Async and await are keywords in Python that are used to write asynchronous code. Asynchronous programming allows for tasks to run concurrently, which can improve the efficiency of programs that perform I/O-bound operations, such as reading from a file, querying a database, or making network requests.

## 1. Understanding Asynchronous Programming

### 1.1 What is Asynchronous Programming?

Asynchronous programming allows a program to perform other tasks while waiting for an operation to complete. This is particularly useful for I/O-bound tasks where the program would otherwise be idle while waiting for an external resource.

### 1.2 Synchronous vs. Asynchronous

- **Synchronous**: Tasks are executed one after the other, and each task waits for the previous one to finish before starting.
  
  ```python
  def fetch_data():
      result = get_data_from_server()
      process_data(result)
      save_to_database(result)
  ```

- **Asynchronous**: Tasks can run concurrently, meaning that while waiting for one task to complete, another task can start.

  ```python
  async def fetch_data():
      result = await get_data_from_server()
      await process_data(result)
      await save_to_database(result)
  ```

## 2. The `async` and `await` Keywords

### 2.1 `async` Keyword

The `async` keyword is used to define a function as asynchronous. This means that the function can run concurrently with other asynchronous functions.

```python
async def say_hello():
    print("Hello, World!")
```

### 2.2 `await` Keyword

The `await` keyword is used to pause the execution of an asynchronous function until the awaited task is complete. It can only be used inside an `async` function.

```python
async def get_data():
    data = await fetch_data_from_server()
    print(data)
```

## 3. Writing Asynchronous Functions

### 3.1 Basic Example

Here’s a simple example of using `async` and `await`:

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}")

async def main():
    await greet("Alice")
    await greet("Bob")

# Run the main function
asyncio.run(main())
```

### 3.2 Real-World Example: Fetching Data from a URL

```python
import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "http://example.com"
    content = await fetch_url(url)
    print(content)

# Run the main function
asyncio.run(main())
```

In this example, `aiohttp` is used to perform asynchronous HTTP requests. `fetch_url` is an asynchronous function that fetches the content of a URL.

### 3.3 Multiple Asynchronous Calls

You can perform multiple asynchronous tasks concurrently using `asyncio.gather`.

```python
async def main():
    url1 = "http://example.com/1"
    url2 = "http://example.com/2"
    url3 = "http://example.com/3"

    results = await asyncio.gather(fetch_url(url1), fetch_url(url2), fetch_url(url3))
    for result in results:
        print(result)

asyncio.run(main())
```

## 4. Using `asyncio` for Asynchronous Operations

### 4.1 Creating an Event Loop

The `asyncio.run` function creates an event loop and runs the asynchronous function until it completes.

```python
async def say_hello():
    print("Hello!")

asyncio.run(say_hello())
```

### 4.2 Managing Concurrency

`asyncio` provides tools for managing concurrency, such as `asyncio.gather`, `asyncio.sleep`, and `asyncio.create_task`.

- **`asyncio.gather`**: Run multiple asynchronous tasks concurrently and wait for all of them to complete.

  ```python
  async def main():
      await asyncio.gather(task1(), task2(), task3())
  ```

- **`asyncio.sleep`**: Pause the execution of an asynchronous function for a specified amount of time.

  ```python
  async def task():
      await asyncio.sleep(2)
      print("Task completed")
  ```

- **`asyncio.create_task`**: Schedule a coroutine to run concurrently with other tasks.

  ```python
  async def main():
      task1 = asyncio.create_task(greet("Alice"))
      task2 = asyncio.create_task(greet("Bob"))
      await task1
      await task2
  ```

## 5. Asynchronous I/O with `aiohttp`

### 5.1 Making HTTP Requests

`aiohttp` is a library for making asynchronous HTTP requests.

```python
import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    content = await fetch_url("http://example.com")
    print(content)

asyncio.run(main())
```

### 5.2 Downloading Multiple URLs

```python
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["http://example.com/1", "http://example.com/2", "http://example.com/3"]
    results = await asyncio.gather(*[download(url) for url in urls])
    for content in results:
        print(content)

asyncio.run(main())
```

## 6. Error Handling in Asynchronous Code

### 6.1 Using `try` and `except`

Asynchronous functions can use `try` and `except` for error handling.

```python
async def fetch_data():
    try:
        response = await aiohttp.ClientSession().get("http://example.com")
        data = await response.text()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(fetch_data())
```

### 6.2 Handling Multiple Errors

When running multiple tasks, you can handle errors for each task individually.

```python
async def fetch(url):
    try:
        response = await aiohttp.ClientSession().get(url)
        data = await response.text()
        return data
    except Exception as e:
        return f"Error fetching {url}: {e}"

async def main():
    urls = ["http://example.com/1", "http://example.com/2", "http://example.com/3"]
    results = await asyncio.gather(*[fetch(url) for url in urls])
    for result in results:
        print(result)

asyncio.run(main())
```

## 7. Practical Use Cases

### 7.1 Web Scraping

Asynchronous code can be used for web scraping to fetch data from multiple pages simultaneously.

```python
async def scrape_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [f"http://example.com/page/{i}" for i in range(1, 6)]
    results = await asyncio.gather(*[scrape_page(url) for url in urls])
    for content in results:
        print(content)

asyncio.run(main())
```

### 7.2 Chat Application

In a chat application, asynchronous programming can handle multiple client connections concurrently.

```python
import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

## 8. Testing Asynchronous Code

### 8.1 Using `pytest-asyncio`

`pytest-asyncio` is a plugin for `pytest` that allows testing of asynchronous code.

```python
import pytest
import asyncio

async def async_function():
    await asyncio.sleep(1)
    return "Hello, async!"

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == "Hello, async!"
```

## 9. Multiple Choice Questions (MCQs)

### 1. What does the `async` keyword do in Python?
a. Defines a synchronous function  
b. Defines an asynchronous function  
c. Suspends function execution  
d. None of the above  

### 2. Which keyword is used to pause the execution of an asynchronous function?
a. `yield`  
b. `return`  
c. `await`  
d. `pass`  

### 3. What library is commonly used for asynchronous HTTP requests in Python?
a. `requests`  
b. `aiohttp`  
c. `urllib`  
d. `http.client`  

### 4. What function is used to run an asynchronous function in an event loop?
a. `asyncio.run`  
b. `asyncio.execute`  
c. `asyncio.call`  
d. `asyncio.loop`  

### 5. What does `asyncio.gather` do?
a. Pauses the event loop  
b. Schedules multiple asynchronous tasks concurrently  
c. Stops all running tasks  
d. None of the above  

### 6. How can you handle errors in an asynchronous function?
a. Using `try` and `except`  
b.

 Using `if` and `else`  
c. Using `await` and `async`  
d. Using `raise` and `except`  

### 7. Which of the following is true about `await`?
a. It can be used in any function  
b. It can only be used inside an `async` function  
c. It blocks the entire program until the task is complete  
d. None of the above  

### 8. What is the purpose of `asyncio.create_task`?
a. To run a synchronous function concurrently  
b. To create a new task that runs concurrently with other tasks  
c. To pause an asynchronous function  
d. To stop an event loop  

### 9. How can you run multiple asynchronous tasks and wait for all of them to complete?
a. Using `asyncio.run`  
b. Using `asyncio.sleep`  
c. Using `asyncio.gather`  
d. Using `asyncio.wait`  

### 10. Which statement is true about `asyncio`?
a. It can only run one task at a time  
b. It can manage multiple asynchronous tasks concurrently  
c. It is used to run synchronous code  
d. It requires a special Python interpreter  

## Answers

1. **b. Defines an asynchronous function**
2. **c. `await`**
3. **b. `aiohttp`**
4. **a. `asyncio.run`**
5. **b. Schedules multiple asynchronous tasks concurrently**
6. **a. Using `try` and `except`**
7. **b. It can only be used inside an `async` function**
8. **b. To create a new task that runs concurrently with other tasks**
9. **c. Using `asyncio.gather`**
10. **b. It can manage multiple asynchronous tasks concurrently**

# Executing an Async Program with `asyncio`

## Introduction to `asyncio`

`asyncio` is a Python library used for writing asynchronous programs. Asynchronous programming allows tasks to run concurrently, making it efficient for I/O-bound operations such as network requests, file operations, and more.

## 1. Setting Up an Async Program

### 1.1 Importing `asyncio`

To use `asyncio`, you need to import it at the beginning of your Python script.

```python
import asyncio
```

### 1.2 Writing an Async Function

Define asynchronous functions using the `async` keyword. These functions can use `await` to pause execution until a task completes.

```python
async def greet():
    await asyncio.sleep(1)
    print("Hello, World!")
```

## 2. Executing an Async Program

### 2.1 Running an Async Function

To run an async function, use `asyncio.run()` which creates an event loop, runs the function, and closes the loop when the function completes.

```python
async def main():
    await greet()

asyncio.run(main())
```

### 2.2 Example: Async Program with Multiple Tasks

You can run multiple async tasks concurrently using `asyncio.gather()`.

```python
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())
```

## 3. Practical Application: Asynchronous HTTP Requests

### 3.1 Using `aiohttp` for Async HTTP Requests

`aiohttp` is a popular library for asynchronous HTTP requests in Python.

```python
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "http://example.com"
    content = await fetch_url(url)
    print(content)

asyncio.run(main())
```

### 3.2 Running Multiple HTTP Requests Concurrently

```python
async def fetch_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(url) for url in urls]
        return await asyncio.gather(*tasks)

async def main():
    urls = ["http://example.com/1", "http://example.com/2", "http://example.com/3"]
    results = await fetch_urls(urls)
    for result in results:
        print(result)

asyncio.run(main())
```

## 4. Error Handling in Async Programs

### 4.1 Handling Errors with `try` and `except`

You can use `try` and `except` blocks to handle errors in async functions.

```python
async def fetch_data(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        print(f"Error fetching data: {e}")

async def main():
    url = "http://invalid-url.com"
    data = await fetch_data(url)
    if data:
        print(data)

asyncio.run(main())
```

## 5. Multiple Choice Questions (MCQs)

### 1. What does `asyncio.run()` do?
a. Executes synchronous functions  
b. Runs an asynchronous function in an event loop  
c. Pauses execution of a function  
d. Imports the `asyncio` module  

### 2. How do you define an asynchronous function in Python?
a. Using the `sync` keyword  
b. Using the `async` keyword  
c. Using the `await` keyword  
d. Using the `def` keyword  

### 3. Which library is commonly used for asynchronous HTTP requests in Python?
a. `requests`  
b. `aiohttp`  
c. `http.client`  
d. `urllib`  

### 4. What keyword is used to pause the execution of an asynchronous function until a task completes?
a. `await`  
b. `async`  
c. `run`  
d. `pause`  

### 5. How can you run multiple asynchronous tasks concurrently and wait for all of them to complete?
a. Using `asyncio.execute()`  
b. Using `asyncio.gather()`  
c. Using `asyncio.await()`  
d. Using `asyncio.run()`  

### 6. What does `asyncio.gather()` do?
a. Pauses the event loop  
b. Runs tasks sequentially  
c. Runs tasks concurrently and waits for all to complete  
d. Stops all running tasks  

### 7. How can you handle errors in an asynchronous function?
a. Using `if` and `else`  
b. Using `raise` and `except`  
c. Using `async` and `await`  
d. Using `try` and `except`  

### 8. Which function creates an event loop and runs an asynchronous function until it completes?
a. `asyncio.create_task()`  
b. `asyncio.loop()`  
c. `asyncio.gather()`  
d. `asyncio.run()`  

### 9. What is the purpose of `asyncio.create_task()`?
a. To define an asynchronous function  
b. To create a new task that runs concurrently with other tasks  
c. To schedule a task to run sequentially  
d. To handle errors in asynchronous functions  

### 10. What is the benefit of using `asyncio` in Python programs?
a. It makes programs run faster  
b. It allows for concurrent execution of tasks  
c. It simplifies code syntax  
d. It replaces `requests` for HTTP requests  

## Answers

1. **b. Runs an asynchronous function in an event loop**
2. **b. Using the `async` keyword**
3. **b. `aiohttp`**
4. **a. `await`**
5. **b. Using `asyncio.gather()`**
6. **c. Runs tasks concurrently and waits for all to complete**
7. **d. Using `try` and `except`**
8. **d. `asyncio.run()`**
9. **b. To create a new task that runs concurrently with other tasks**
10. **b. It allows for concurrent execution of tasks**

# Running Concurrent Coroutines in Python

## Introduction to Concurrent Coroutines

Coroutines in Python are a type of function that allow you to pause execution and resume it later. When coroutines run concurrently, they can perform multiple tasks at once without blocking the main thread. This is particularly useful for I/O-bound operations like reading from a file, making network requests, or any operation that would normally block the execution of a program.

## 1. Understanding Coroutines

### 1.1 What is a Coroutine?

A coroutine is a function that can suspend its execution before reaching the return statement and can indirectly pass control to other coroutines for some time.

```python
import asyncio

async def simple_coroutine():
    print("Start coroutine")
    await asyncio.sleep(1)
    print("End coroutine")
```

### 1.2 Differences Between Functions and Coroutines

- **Functions**: Execute from start to finish without interruption.
- **Coroutines**: Can pause execution (`await`) and resume later, allowing other tasks to run concurrently.

## 2. Running Concurrent Coroutines

### 2.1 Using `asyncio.gather()`

`asyncio.gather()` runs multiple coroutines concurrently and waits for them to finish.

```python
async def task_1():
    print("Start task 1")
    await asyncio.sleep(2)
    print("End task 1")

async def task_2():
    print("Start task 2")
    await asyncio.sleep(1)
    print("End task 2")

async def main():
    await asyncio.gather(task_1(), task_2())

asyncio.run(main())
```

### 2.2 Example: Fetching Multiple URLs Concurrently

```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net"
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
```

### 2.3 Using `asyncio.create_task()`

`asyncio.create_task()` schedules a coroutine to run concurrently with other coroutines.

```python
async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def main():
    task = asyncio.create_task(say_hello())
    print("Task started")
    await task

asyncio.run(main())
```

### 2.4 Example: Downloading Multiple Files Concurrently

```python
async def download_file(url):
    print(f"Starting download from {url}")
    await asyncio.sleep(3)  # Simulate a download
    print(f"Finished download from {url}")

async def main():
    tasks = [
        asyncio.create_task(download_file("http://example.com/file1")),
        asyncio.create_task(download_file("http://example.com/file2")),
        asyncio.create_task(download_file("http://example.com/file3"))
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

## 3. Practical Application: Chat Server

### 3.1 Implementing a Simple Chat Server

Using `asyncio`, you can build a simple chat server where multiple clients can send and receive messages concurrently.

```python
import asyncio

clients = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected with {addr}")
    clients.append(writer)
    try:
        while True:
            data = await reader.read(100)
            message = data.decode()
            if not message:
                break
            for client in clients:
                if client != writer:
                    client.write(data)
                    await client.drain()
    except asyncio.CancelledError:
        pass
    finally:
        print(f"Disconnected {addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

### 3.2 Connecting to the Chat Server

You can create a simple client to connect to the chat server and send messages.

```python
async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    while True:
        message = input("Enter message: ")
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
        print(f"Received: {data.decode()}")

asyncio.run(tcp_client())
```

## 4. Error Handling in Concurrent Coroutines

### 4.1 Using `try` and `except`

Errors in concurrent coroutines can be caught using `try` and `except` blocks.

```python
async def faulty_task():
    try:
        raise ValueError("An error occurred")
    except ValueError as e:
        print(f"Caught error: {e}")

async def main():
    await faulty_task()

asyncio.run(main())
```

### 4.2 Handling Errors in Multiple Tasks

Errors in one task do not stop other tasks from running.

```python
async def faulty_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def safe_task():
    await asyncio.sleep(1)
    print("Task completed safely")

async def main():
    tasks = [
        asyncio.create_task(faulty_task()),
        asyncio.create_task(safe_task())
    ]
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())
```

## 5. Debugging Concurrent Coroutines

### 5.1 Enabling Debug Mode

You can enable debug mode in `asyncio` to get detailed logs.

```python
asyncio.run(main(), debug=True)
```

### 5.2 Using Logging

Use the `logging` module for better insights into the coroutine execution.

```python
import logging

logging.basicConfig(level=logging.DEBUG)

async def task():
    logging.debug("Starting task")
    await asyncio.sleep(1)
    logging.debug("Finished task")

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())
```

## 6. Multiple Choice Questions (MCQs)

### 1. What is the purpose of `asyncio.gather()`?
a. To run multiple coroutines concurrently and wait for all to finish  
b. To pause the execution of a coroutine  
c. To create a new coroutine  
d. To start an event loop  

### 2. How do you schedule a coroutine to run concurrently with other coroutines?
a. Using `await`  
b. Using `asyncio.run()`  
c. Using `asyncio.create_task()`  
d. Using `asyncio.gather()`  

### 3. Which of the following statements about coroutines is true?
a. They block the main thread while running  
b. They run sequentially like regular functions  
c. They can pause execution and resume later  
d. They cannot be used for I/O-bound operations  

### 4. What does `asyncio.run()` do?
a. Creates an event loop and runs a coroutine until it completes  
b. Pauses the execution of the main thread  
c. Creates a new coroutine  
d. Handles errors in coroutines  

### 5. How can you handle errors in an asynchronous function?
a. Using `asyncio.create_task()`  
b. Using `await` and `async`  
c. Using `try` and `except`  
d. Using `asyncio.gather()`  

### 6. Which of the following is used to run multiple HTTP requests concurrently?
a. `asyncio.create_task()`  
b. `asyncio.run()`  
c. `asyncio.gather()`  
d. `asyncio.sleep()`  

### 7. How can you enable debug mode in `asyncio`?
a. `asyncio.enable_debug()`  
b. `asyncio.run(main(), debug=True)`  
c. `asyncio.start_debug()`  
d. `asyncio.enable_log()`  

### 8. What is a coroutine?
a. A type of synchronous function  
b. A function that can pause execution and resume later  
c. A built-in Python module  
d. A blocking I/O operation  

### 9. What does `asyncio.create_task()` return?
a. An event loop  
b. A running coroutine  
c. A task that runs concurrently with other tasks  
d. An error handler  

### 10. Why are coroutines useful in Python?
a. They simplify complex algorithms  
b. They replace the need for threading  
c. They allow for concurrent execution of I/O-bound operations  
d. They make code run faster without any changes  

## Answers

1. **a. To run multiple coroutines concurrently and wait for all to finish**
2. **c. Using `asyncio.create_task()`**
3. **c. They can pause execution and resume later**
4. **a. Creates an event loop and runs a coroutine until it completes**
5. **c. Using `try` and `except`**
6. **c. `asyncio.gather()`**
7. **b. `asyncio.run(main(), debug=True)`**
8. **b. A function that can pause execution and resume later**
9. **c. A task that runs concurrently with other tasks**
10. **c. They allow for concurrent execution of I/O-bound operations**

# Creating `asyncio` Tasks in Python

## Introduction to `asyncio` Tasks

Tasks in `asyncio` are used to run coroutines concurrently. They allow you to schedule coroutines to run as soon as possible while other tasks are awaiting, enabling efficient handling of I/O-bound operations and cooperative multitasking.

## 1. Understanding `asyncio` Tasks

### 1.1 What is an `asyncio` Task?

An `asyncio` Task is a wrapper for a coroutine. It allows the coroutine to run concurrently with other coroutines, making it possible to perform multiple operations at the same time.

```python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")
```

### 1.2 Differences Between Coroutines and Tasks

- **Coroutines**: Defined using `async def` and must be awaited to run.
- **Tasks**: Created to run coroutines concurrently and are managed by the event loop.

## 2. Creating and Running Tasks

### 2.1 Using `asyncio.create_task()`

To run a coroutine concurrently, wrap it in a Task using `asyncio.create_task()`.

```python
async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def main():
    task = asyncio.create_task(say_hello())
    print("Task created")
    await task

asyncio.run(main())
```

### 2.2 Example: Running Multiple Tasks Concurrently

You can create multiple tasks to run different coroutines at the same time.

```python
async def print_numbers():
    for i in range(1, 4):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in 'abc':
        print(letter)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await asyncio.gather(task1, task2)

asyncio.run(main())
```

### 2.3 Example: Downloading Files Concurrently

```python
import aiohttp

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(f"Downloaded {len(content)} characters from {url}")

async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net"
    ]
    tasks = [asyncio.create_task(download_file(url)) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

## 3. Managing Task Lifecycle

### 3.1 Cancelling a Task

You can cancel a running task using the `cancel()` method. This raises a `CancelledError` inside the coroutine, allowing it to clean up before stopping.

```python
async def long_running_task():
    try:
        while True:
            print("Running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled")

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(3)
    task.cancel()
    await task

asyncio.run(main())
```

### 3.2 Waiting for Task Completion

You can use `await` to wait for a task to complete. This ensures that the coroutine has finished before the program continues.

```python
async def task_1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task_2():
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())
    await task1
    await task2

asyncio.run(main())
```

### 3.3 Returning Values from Tasks

Tasks can return values which can be awaited and used in other parts of your program.

```python
async def calculate_sum(x, y):
    await asyncio.sleep(1)
    return x + y

async def main():
    task = asyncio.create_task(calculate_sum(5, 7))
    result = await task
    print(f"Sum: {result}")

asyncio.run(main())
```

## 4. Error Handling in Tasks

### 4.1 Handling Exceptions

Exceptions in tasks can be caught and handled using `try` and `except` blocks.

```python
async def faulty_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def main():
    task = asyncio.create_task(faulty_task())
    try:
        await task
    except ValueError as e:
        print(f"Caught error: {e}")

asyncio.run(main())
```

### 4.2 Using `return_exceptions` in `asyncio.gather()`

When using `asyncio.gather()`, you can pass `return_exceptions=True` to handle exceptions without stopping other tasks.

```python
async def task_1():
    raise ValueError("Task 1 failed")

async def task_2():
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    tasks = [
        asyncio.create_task(task_1()),
        asyncio.create_task(task_2())
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(results)

asyncio.run(main())
```

## 5. Practical Application: Parallel Data Processing

### 5.1 Example: Processing Data Concurrently

Imagine you have a list of numbers and you want to process them concurrently.

```python
async def process_number(number):
    await asyncio.sleep(1)
    return number * 2

async def main():
    numbers = [1, 2, 3, 4, 5]
    tasks = [asyncio.create_task(process_number(n)) for n in numbers]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

## 6. Multiple Choice Questions (MCQs)

### 1. What is an `asyncio` Task used for?
a. To pause the execution of a coroutine  
b. To run coroutines concurrently  
c. To replace the need for threads  
d. To handle synchronous code  

### 2. How do you create a task in `asyncio`?
a. Using `asyncio.run()`  
b. Using `await`  
c. Using `asyncio.create_task()`  
d. Using `asyncio.task()`  

### 3. What does `asyncio.create_task()` return?
a. A coroutine  
b. A task that runs concurrently  
c. An event loop  
d. A blocking I/O operation  

### 4. Which method is used to cancel a running task?
a. `stop()`  
b. `pause()`  
c. `cancel()`  
d. `end()`  

### 5. How can you handle exceptions in an `asyncio` task?
a. Using `asyncio.cancel()`  
b. Using `asyncio.gather()`  
c. Using `try` and `except`  
d. Using `asyncio.create_task()`  

### 6. How do you run multiple tasks concurrently?
a. Using `asyncio.run()`  
b. Using `asyncio.gather()`  
c. Using `await`  
d. Using `asyncio.sleep()`  

### 7. What happens if a task raises an exception?
a. The program stops immediately  
b. The exception is raised inside the coroutine and can be caught  
c. The event loop stops running  
d. The task runs to completion despite the exception  

### 8. How do you get the result of a task?
a. Using `await`  
b. Using `asyncio.gather()`  
c. Using `asyncio.run()`  
d. Using `asyncio.create_task()`  

### 9. What is the purpose of `asyncio.gather(*tasks, return_exceptions=True)`?
a. To cancel all tasks if one fails  
b. To collect results of tasks even if some raise exceptions  
c. To run tasks sequentially  
d. To block until all tasks are complete  

### 10. Why use `asyncio` tasks instead of threads for I/O-bound operations?
a. They are simpler to write  
b. They can run synchronous code  
c. They allow better resource management without blocking  
d. They are only used for CPU-bound tasks  

## Answers

1. **b. To run coroutines concurrently**
2. **c. Using `asyncio.create_task()`**
3. **b. A task that runs concurrently**
4. **c. `cancel()`**
5. **c. Using `try` and `except`**
6. **b. Using `asyncio.gather()`**
7. **b. The exception is raised inside the coroutine and can be caught**
8. **a. Using `await`**
9. **b. To collect results of tasks even if some raise exceptions**
10. **c. They allow better resource management without blocking**

# Using the `random` Module in Python

The `random` module in Python is used to generate pseudo-random numbers for various purposes, such as simulations, games, or random sampling. This note covers the essential functions provided by the `random` module and how they can be applied in real-world scenarios.

## 1. Importing the `random` Module

To use the `random` module, you need to import it at the beginning of your code:

```python
import random
```

## 2. Generating Random Numbers

### 2.1 Random Integers

Use `random.randint(a, b)` to generate a random integer between `a` and `b` (inclusive).

```python
random_integer = random.randint(1, 10)
print(random_integer)  # Output: Random integer between 1 and 10
```

### 2.2 Random Floats

Use `random.random()` to generate a random float between 0.0 and 1.0.

```python
random_float = random.random()
print(random_float)  # Output: Random float between 0.0 and 1.0
```

Use `random.uniform(a, b)` to generate a random float between `a` and `b`.

```python
random_uniform = random.uniform(1.0, 10.0)
print(random_uniform)  # Output: Random float between 1.0 and 10.0
```

## 3. Random Choices from a Sequence

### 3.1 Random Element

Use `random.choice(sequence)` to select a random element from a non-empty sequence like a list or a string.

```python
colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
print(random_color)  # Output: Randomly selected color from the list
```

### 3.2 Random Sample

Use `random.sample(sequence, k)` to get a list of `k` unique elements from the sequence.

```python
numbers = list(range(1, 11))
sample_numbers = random.sample(numbers, 3)
print(sample_numbers)  # Output: 3 unique random numbers from 1 to 10
```

### 3.3 Random Choices with Replacement

Use `random.choices(sequence, k)` to get a list of `k` elements from the sequence, with replacement (elements can repeat).

```python
numbers = list(range(1, 6))
choices_numbers = random.choices(numbers, k=3)
print(choices_numbers)  # Output: 3 random numbers from 1 to 5 (with possible repetition)
```

### 3.4 Randomly Shuffling a List

Use `random.shuffle(list)` to shuffle the elements of a list in place.

```python
cards = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(cards)
print(cards)  # Output: List of cards shuffled
```

## 4. Using Seeds for Reproducibility

Random functions can produce the same results if you set the same seed using `random.seed()`. This is useful for debugging and testing.

```python
random.seed(42)
print(random.randint(1, 10))  # Output: Same random number each time the code runs
```

## 5. Practical Applications

### 5.1 Simulating a Dice Roll

```python
def roll_dice():
    return random.randint(1, 6)

dice_roll = roll_dice()
print(f"Dice roll: {dice_roll}")  # Output: Random integer between 1 and 6
```

### 5.2 Generating Random Passwords

```python
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

password = generate_password(12)
print(f"Generated password: {password}")  # Output: Random password of length 12
```

### 5.3 Selecting a Random Prize Winner

```python
participants = ['Alice', 'Bob', 'Charlie', 'Diana']
winner = random.choice(participants)
print(f"The winner is: {winner}")  # Output: Random participant from the list
```

### 5.4 Creating Random Data for Testing

```python
def generate_random_data(n):
    return [random.uniform(0, 100) for _ in range(n)]

random_data = generate_random_data(5)
print(random_data)  # Output: List of 5 random floats between 0 and 100
```

### 5.5 Random Walk Simulation

```python
def random_walk(steps):
    position = 0
    for _ in range(steps):
        step = random.choice([-1, 1])
        position += step
    return position

final_position = random_walk(100)
print(f"Final position after 100 steps: {final_position}")  # Output: Final position on the number line
```

## 6. Technical Multiple Choice Questions

### 1. Which function generates a random integer between two values?
a. `random.choice()`  
b. `random.randint()`  
c. `random.random()`  
d. `random.uniform()`  

### 2. How do you generate a random float between 0.0 and 1.0?
a. `random.randint(0, 1)`  
b. `random.uniform(0, 1)`  
c. `random.random()`  
d. `random.choice()`  

### 3. Which function selects a random element from a list?
a. `random.sample()`  
b. `random.choices()`  
c. `random.choice()`  
d. `random.randint()`  

### 4. What does `random.shuffle()` do?
a. Returns a new shuffled list  
b. Sorts the list in ascending order  
c. Shuffles the list in place  
d. Selects a random element from the list  

### 5. What is the purpose of `random.seed()`?
a. To reset the random number generator  
b. To get the current state of the random number generator  
c. To make random number generation reproducible  
d. To shuffle a list  

### 6. Which method allows picking multiple random elements from a list, allowing duplicates?
a. `random.sample()`  
b. `random.choices()`  
c. `random.choice()`  
d. `random.shuffle()`  

### 7. What is the output of `random.uniform(5, 10)`?
a. Random integer between 5 and 10  
b. Random float between 0.0 and 1.0  
c. Random float between 5.0 and 10.0  
d. Random element from the list `[5, 10]`  

### 8. How can you generate a random password of length 8?
a. `random.randint(1, 8)`  
b. `random.choices(string.ascii_letters, k=8)`  
c. `random.choice(string.ascii_letters)`  
d. `random.uniform(1, 8)`  

### 9. To select a unique set of 3 random numbers from a list of 10 numbers, which function is used?
a. `random.choice()`  
b. `random.sample()`  
c. `random.shuffle()`  
d. `random.choices()`  

### 10. How do you get a random letter from the string `'abc'`?
a. `random.randint(1, 3)`  
b. `random.choice('abc')`  
c. `random.sample('abc', 1)`  
d. `random.uniform('a', 'c')`  

## Answers

1. **b. `random.randint()`**
2. **c. `random.random()`**
3. **c. `random.choice()`**
4. **c. Shuffles the list in place**
5. **c. To make random number generation reproducible**
6. **b. `random.choices()`**
7. **c. Random float between 5.0 and 10.0**
8. **b. `random.choices(string.ascii_letters, k=8)`**
9. **b. `random.sample()`**
10. **b. `random.choice('abc')**

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
