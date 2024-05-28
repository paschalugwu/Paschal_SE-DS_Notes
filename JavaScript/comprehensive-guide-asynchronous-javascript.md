# Comprehensive Guide to Asynchronous JavaScript Programming

Asynchronous programming is a fundamental aspect of modern JavaScript development, allowing for efficient handling of tasks that may take time to complete, such as network requests, file operations, and database queries. Understanding asynchronous concepts such as Promises, async/await, and error handling techniques like Throw/Try is essential for building robust and responsive applications. In this guide, we'll delve into these concepts, exploring their usage, benefits, and real-world applications.

## Promises in JavaScript

### Introduction to Promises

Promises in JavaScript are used to handle asynchronous operations. They are a way to execute code that might take some time to complete, like fetching data from a server, without blocking the rest of the code from running.

### How Promises Work

A Promise represents a value that may be available now, in the future, or never. It has three states:
1. **Pending**: The initial state, neither fulfilled nor rejected.
2. **Fulfilled**: The operation completed successfully.
3. **Rejected**: The operation failed.

### Creating a Promise

To create a Promise, you use the `Promise` constructor, which takes a function with two parameters: `resolve` and `reject`.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // Simulating an asynchronous operation
  setTimeout(() => {
    const success = true; // Change to false to simulate an error
    if (success) {
      resolve('Operation was successful!');
    } else {
      reject('Operation failed.');
    }
  }, 1000);
});
```

### Using Promises

Promises have methods to handle the outcome of the asynchronous operation:
- `.then()`: Runs when the promise is fulfilled.
- `.catch()`: Runs when the promise is rejected.
- `.finally()`: Runs when the promise is settled (fulfilled or rejected).

```javascript
myPromise
  .then((message) => {
    console.log(message); // "Operation was successful!"
  })
  .catch((error) => {
    console.error(error); // "Operation failed."
  })
  .finally(() => {
    console.log('Promise is settled.'); // Runs no matter what
  });
```

### Why Use Promises

Promises make it easier to work with asynchronous code by avoiding callback hell, which is when you have many nested callback functions. Promises also provide a cleaner and more readable way to handle asynchronous operations.

### Real-World Example: Fetching Data from an API

Consider a scenario where you need to fetch user data from a remote server. Using promises, you can handle the asynchronous request like this:

```javascript
function fetchUserData(userId) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { id: userId, name: 'John Doe' }; // Simulated data
      resolve(data);
    }, 2000); // Simulate network delay
  });
}

fetchUserData(1)
  .then((user) => {
    console.log(user); // { id: 1, name: 'John Doe' }
  })
  .catch((error) => {
    console.error('Error fetching user data:', error);
  });
```

### Applying Promises in Real-World Projects

In real-world projects, promises are used for tasks such as:
- Fetching data from APIs
- Reading files
- Performing network requests
- Managing multiple asynchronous operations concurrently

### End of Chapter MCQs

1. What is the initial state of a Promise?
   - A) Fulfilled
   - B) Rejected
   - C) Pending
   - D) Settled

2. Which method is used to handle a fulfilled Promise?
   - A) .catch()
   - B) .then()
   - C) .finally()
   - D) .done()

3. What does the `.catch()` method handle?
   - A) Fulfilled Promises
   - B) Pending Promises
   - C) Rejected Promises
   - D) Settled Promises

4. What is the purpose of the `resolve` function in a Promise?
   - A) To create a new Promise
   - B) To handle errors
   - C) To indicate a successful completion
   - D) To continue a chain of promises

5. What happens when you call `.finally()` on a Promise?
   - A) It runs only if the Promise is fulfilled.
   - B) It runs only if the Promise is rejected.
   - C) It runs regardless of the Promise's outcome.
   - D) It runs only if the Promise is still pending.

6. How can you simulate an asynchronous operation using Promises?
   - A) By using the `await` keyword
   - B) By using the `setTimeout` function inside a Promise
   - C) By using a synchronous function inside a Promise
   - D) By using the `try` and `catch` blocks

7. What is a common use case for Promises in web development?
   - A) To create variables
   - B) To handle click events
   - C) To fetch data from APIs
   - D) To manipulate the DOM

8. What will be logged if a Promise is rejected and there is no `.catch()` method?
   - A) Nothing
   - B) The error message will be logged
   - C) The success message will be logged
   - D) An unhandled Promise rejection warning

9. What does the `Promise` constructor require as an argument?
   - A) Two functions: `resolve` and `reject`
   - B) One function: `execute`
   - C) No arguments
   - D) A single `resolve` function

10. Which Promise method allows you to run multiple promises and wait for all of them to settle?
    - A) Promise.allSettled()
    - B) Promise.any()
    - C) Promise.race()
    - D) Promise.resolve()

### Answers

1. C) Pending
2. B) .then()
3. C) Rejected Promises
4. C) To indicate a successful completion
5. C) It runs regardless of the Promise's outcome.
6. B) By using the `setTimeout` function inside a Promise
7. C) To fetch data from APIs
8. D) An unhandled Promise rejection warning
9. A) Two functions: `resolve` and `reject`
10. A) Promise.allSettled()

## How to Use the `then`, `resolve`, and `catch` Methods in JavaScript

### Introduction

When dealing with asynchronous operations in JavaScript, promises provide a powerful way to manage such tasks. Three essential methods associated with promises are `then`, `resolve`, and `catch`. Understanding these methods is crucial for handling asynchronous code efficiently.

### The `then` Method

The `then` method is used to specify what should happen after a promise is fulfilled (resolved). It takes two optional arguments: a callback function for the resolved case and a callback function for the rejected case.

**Syntax:**

```javascript
promise.then(onFulfilled, onRejected);
```

**Example:**

```javascript
let promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Success!"), 1000);
});

promise.then(
  (result) => console.log(result), // "Success!"
  (error) => console.log(error)
);
```

### The `resolve` Method

The `resolve` method is used within the promise constructor to mark the promise as fulfilled and pass a result value. This is the function you call when your asynchronous operation completes successfully.

**Syntax:**

```javascript
resolve(value);
```

**Example:**

```javascript
let promise = new Promise((resolve, reject) => {
  let success = true; // Change to false to simulate an error
  if (success) {
    resolve("Operation was successful!");
  } else {
    reject("Operation failed.");
  }
});

promise.then((result) => console.log(result)); // "Operation was successful!"
```

### The `catch` Method

The `catch` method is used to handle errors (rejections) in promises. It takes a single callback function that is executed if the promise is rejected.

**Syntax:**

```javascript
promise.catch(onRejected);
```

**Example:**

```javascript
let promise = new Promise((resolve, reject) => {
  setTimeout(() => reject("Something went wrong!"), 1000);
});

promise.catch((error) => console.error(error)); // "Something went wrong!"
```

### Combining `then`, `resolve`, and `catch`

These methods can be combined to create a clean and efficient workflow for handling both the success and failure of asynchronous operations.

**Example:**

```javascript
let promise = new Promise((resolve, reject) => {
  let success = true; // Change to false to simulate an error
  if (success) {
    resolve("Operation was successful!");
  } else {
    reject("Operation failed.");
  }
});

promise
  .then((result) => console.log(result)) // "Operation was successful!"
  .catch((error) => console.error(error)); // If success = false: "Operation failed."
```

### Real-World Example: Fetching Data from an API

Consider a scenario where you need to fetch data from an API. Using promises, you can handle the asynchronous request as follows:

```javascript
function fetchData(apiUrl) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true; // Simulated condition
      if (success) {
        resolve({ data: "Sample Data" });
      } else {
        reject("Failed to fetch data.");
      }
    }, 2000); // Simulate network delay
  });
}

fetchData("https://api.example.com/data")
  .then((response) => {
    console.log("Data fetched:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

### End of Chapter MCQs

1. What does the `then` method handle in a promise?
   - A) Only resolved promises
   - B) Only rejected promises
   - C) Both resolved and rejected promises
   - D) Pending promises

2. What arguments does the `then` method take?
   - A) One callback for rejection
   - B) One callback for resolution
   - C) Two callbacks: one for resolution and one for rejection
   - D) No arguments

3. What is the purpose of the `resolve` method?
   - A) To handle errors
   - B) To delay the promise
   - C) To mark the promise as fulfilled
   - D) To reject the promise

4. What does the `catch` method handle?
   - A) Fulfilled promises
   - B) Rejected promises
   - C) Pending promises
   - D) Both fulfilled and rejected promises

5. How do you call a function when a promise is fulfilled?
   - A) Using `resolve()`
   - B) Using `then()`
   - C) Using `catch()`
   - D) Using `finally()`

6. What will the `catch` method do if a promise is resolved?
   - A) It will throw an error
   - B) It will be ignored
   - C) It will execute the callback
   - D) It will change the promise state

7. How can you handle both fulfillment and rejection of a promise?
   - A) Using only `then()`
   - B) Using only `catch()`
   - C) Using both `then()` and `catch()`
   - D) Using `finally()`

8. What is the output of the following code snippet?

```javascript
let promise = new Promise((resolve, reject) => {
  reject("Error occurred");
});

promise
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

   - A) "Error occurred"
   - B) undefined
   - C) No output
   - D) Syntax error

9. Which method is used to handle errors in a promise chain?
   - A) then()
   - B) resolve()
   - C) catch()
   - D) reject()

10. What happens if you don't add a `catch` method to a promise that gets rejected?
    - A) The error will be swallowed
    - B) The error will crash the program
    - C) The error will be logged to the console
    - D) The error will cause an unhandled rejection warning

### Answers

1. C) Both resolved and rejected promises
2. C) Two callbacks: one for resolution and one for rejection
3. C) To mark the promise as fulfilled
4. B) Rejected promises
5. B) Using `then()`
6. B) It will be ignored
7. C) Using both `then()` and `catch()`
8. A) "Error occurred"
9. C) catch()
10. D) The error will cause an unhandled rejection warning

## How to Use Every Method of the Promise Object

### Introduction

The Promise object in JavaScript provides a way to handle asynchronous operations. Promises have several methods that help in managing the flow of these operations. Understanding how to use each method can significantly improve your ability to write efficient asynchronous code.

### Methods of the Promise Object

1. **Promise.resolve(value)**
2. **Promise.reject(reason)**
3. **Promise.all(iterable)**
4. **Promise.race(iterable)**
5. **Promise.allSettled(iterable)**
6. **Promise.any(iterable)**

### 1. Promise.resolve(value)

The `Promise.resolve(value)` method returns a Promise that is resolved with the given value. If the value is a promise, it will be returned as is.

**Syntax:**

```javascript
Promise.resolve(value);
```

**Example:**

```javascript
let resolvedPromise = Promise.resolve("Resolved value");

resolvedPromise.then((value) => {
  console.log(value); // "Resolved value"
});
```

### 2. Promise.reject(reason)

The `Promise.reject(reason)` method returns a Promise that is rejected with the given reason.

**Syntax:**

```javascript
Promise.reject(reason);
```

**Example:**

```javascript
let rejectedPromise = Promise.reject("Error occurred");

rejectedPromise.catch((error) => {
  console.error(error); // "Error occurred"
});
```

### 3. Promise.all(iterable)

The `Promise.all(iterable)` method takes an iterable of promises and returns a single Promise that resolves when all the promises in the iterable have resolved or rejects if any of the promises reject.

**Syntax:**

```javascript
Promise.all(iterable);
```

**Example:**

```javascript
let promise1 = Promise.resolve(3);
let promise2 = 42;
let promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values); // [3, 42, "foo"]
});
```

### 4. Promise.race(iterable)

The `Promise.race(iterable)` method returns a Promise that resolves or rejects as soon as one of the promises in the iterable resolves or rejects.

**Syntax:**

```javascript
Promise.race(iterable);
```

**Example:**

```javascript
let promise1 = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, 'one');
});

let promise2 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'two');
});

Promise.race([promise1, promise2]).then((value) => {
  console.log(value); // "two"
});
```

### 5. Promise.allSettled(iterable)

The `Promise.allSettled(iterable)` method returns a Promise that resolves after all of the given promises have either resolved or rejected, with an array of objects that each describe the outcome of each promise.

**Syntax:**

```javascript
Promise.allSettled(iterable);
```

**Example:**

```javascript
let promise1 = Promise.resolve('Success');
let promise2 = Promise.reject('Failure');

Promise.allSettled([promise1, promise2]).then((results) => {
  results.forEach((result) => console.log(result.status));
  // "fulfilled"
  // "rejected"
});
```

### 6. Promise.any(iterable)

The `Promise.any(iterable)` method takes an iterable of Promise objects and, as soon as one of the promises in the iterable fulfills, returns a single promise that resolves with the value from that promise. If no promises in the iterable fulfill (if all of the given promises are rejected), then the returned promise is rejected with an AggregateError, a new subclass of Error that groups together individual errors.

**Syntax:**

```javascript
Promise.any(iterable);
```

**Example:**

```javascript
let promise1 = Promise.reject('Error 1');
let promise2 = Promise.resolve('Success');
let promise3 = Promise.reject('Error 3');

Promise.any([promise1, promise2, promise3]).then((value) => {
  console.log(value); // "Success"
}).catch((error) => {
  console.error(error);
});
```

### Real-World Example: Fetching Multiple APIs

Imagine you need to fetch data from multiple APIs and combine the results. You can use `Promise.all` to wait for all requests to complete:

```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(`Data from ${url}`);
    }, Math.random() * 2000);
  });
}

let api1 = fetchData("https://api1.example.com");
let api2 = fetchData("https://api2.example.com");
let api3 = fetchData("https://api3.example.com");

Promise.all([api1, api2, api3]).then((results) => {
  console.log(results);
  // ["Data from https://api1.example.com", "Data from https://api2.example.com", "Data from https://api3.example.com"]
});
```

### End of Chapter MCQs

1. What does `Promise.resolve(value)` do?
   - A) Creates a rejected promise with the given value.
   - B) Creates a pending promise.
   - C) Creates a resolved promise with the given value.
   - D) Cancels the promise.

2. What does `Promise.reject(reason)` do?
   - A) Creates a resolved promise.
   - B) Creates a pending promise.
   - C) Creates a rejected promise with the given reason.
   - D) Cancels the promise.

3. What is the output of `Promise.all([Promise.resolve(1), Promise.resolve(2)])`?
   - A) A promise that resolves with [1, 2]
   - B) A promise that rejects immediately
   - C) A promise that resolves with [1]
   - D) A promise that remains pending

4. What does `Promise.race([promise1, promise2])` do?
   - A) Resolves or rejects with the value from the fastest promise
   - B) Resolves or rejects with the value from the slowest promise
   - C) Waits for all promises to resolve
   - D) Cancels the faster promise

5. What does `Promise.allSettled([promise1, promise2])` return?
   - A) A promise that resolves with an array of results of the input promises
   - B) A promise that rejects with an array of results of the input promises
   - C) A promise that resolves with the result of the fastest promise
   - D) A promise that resolves with the result of the slowest promise

6. What does `Promise.any([promise1, promise2, promise3])` do if all promises reject?
   - A) Resolves with an array of errors
   - B) Rejects with an AggregateError
   - C) Remains pending
   - D) Resolves with the first rejected promise

7. How does `Promise.all` behave when one of the promises in the iterable rejects?
   - A) It waits for all promises to settle
   - B) It immediately rejects with that reason
   - C) It ignores the rejected promise
   - D) It resolves with an array of fulfilled promises

8. In the `Promise.race` method, what happens if the first promise rejects?
   - A) The entire race rejects immediately
   - B) The race waits for other promises to resolve
   - C) The race continues with the remaining promises
   - D) The race resolves with an undefined value

9. What does `Promise.resolve(Promise.resolve('value'))` return?
   - A) A rejected promise
   - B) A pending promise
   - C) A resolved promise with the value 'value'
   - D) An error

10. How does `Promise.allSettled` handle multiple promises?
    - A) It resolves with an array of all fulfilled promise values
    - B) It rejects with an array of all rejection reasons
    - C) It resolves with an array of objects describing the outcomes of all promises
    - D) It remains pending until the last promise settles

### Answers

1. C) Creates a resolved promise with the given value.
2. C) Creates a rejected promise with the given reason.
3. A) A promise that resolves with [1, 2]
4. A) Resolves or rejects with the value from the fastest promise
5. A) A promise that resolves with an array of results of the input promises
6. B) Rejects with an AggregateError
7. B) It immediately rejects with that reason
8. A) The entire race rejects immediately
9. C) A resolved promise with the value 'value'
10. C) It resolves with an array of objects describing the outcomes of all promises

## Throw / Try

### Introduction

In JavaScript, error handling is an essential part of writing robust and reliable code. Errors can occur for various reasons, such as incorrect user input, network failures, or unexpected behavior in the code. JavaScript provides the `throw` statement to create custom errors and the `try...catch` statement to handle these errors gracefully.

### The `throw` Statement

The `throw` statement allows you to create and throw an error. This can be useful for generating custom error messages based on specific conditions in your code.

**Syntax:**

```javascript
throw expression;
```

**Example:**

```javascript
function checkNumber(num) {
  if (num > 10) {
    throw new Error("Number is too large");
  }
  return num;
}

try {
  console.log(checkNumber(15));
} catch (error) {
  console.error(error.message); // "Number is too large"
}
```

### The `try...catch` Statement

The `try...catch` statement is used to handle errors that occur in your code. It allows you to try a block of code and catch any errors that are thrown, preventing your program from crashing.

**Syntax:**

```javascript
try {
  // Code that may throw an error
} catch (error) {
  // Code to handle the error
}
```

**Example:**

```javascript
try {
  let result = someFunction();
  console.log(result);
} catch (error) {
  console.error("An error occurred: " + error.message);
}
```

### Real-World Example: Form Validation

Consider a web form where users input their age. You want to ensure that the age is a positive number and less than 120. You can use `throw` to create a custom error if the input is invalid and `try...catch` to handle these errors.

**Example:**

```javascript
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new TypeError("Age must be a number");
  }
  if (age <= 0) {
    throw new RangeError("Age must be a positive number");
  }
  if (age > 120) {
    throw new RangeError("Age must be less than 120");
  }
  return true;
}

try {
  validateAge(130);
} catch (error) {
  console.error("Validation error: " + error.message);
}
```

### Nested `try...catch` Blocks

You can nest `try...catch` blocks to handle different levels of errors. This can be useful in complex applications where different parts of the code might throw different types of errors.

**Example:**

```javascript
try {
  try {
    let data = fetchDataFromAPI();
    console.log(data);
  } catch (apiError) {
    console.error("API Error: " + apiError.message);
    throw new Error("Failed to fetch data from API");
  }
} catch (error) {
  console.error("General Error: " + error.message);
}
```

### The `finally` Clause

The `finally` clause can be used with `try...catch` to execute code regardless of whether an error was thrown or not. This is useful for cleanup operations.

**Syntax:**

```javascript
try {
  // Code that may throw an error
} catch (error) {
  // Code to handle the error
} finally {
  // Code to run regardless of error
}
```

**Example:**

```javascript
function readFile(filePath) {
  try {
    let fileContent = openFile(filePath);
    console.log(fileContent);
  } catch (error) {
    console.error("Error reading file: " + error.message);
  } finally {
    closeFile(filePath);
    console.log("File closed");
  }
}
```

### End of Chapter MCQs

1. What does the `throw` statement do in JavaScript?
   - A) Catches an error
   - B) Throws an error
   - C) Resolves a promise
   - D) Starts a try block

2. Which block is used to handle errors in JavaScript?
   - A) `try`
   - B) `catch`
   - C) `finally`
   - D) `error`

3. What is the purpose of the `finally` block?
   - A) To throw an error
   - B) To catch an error
   - C) To execute code regardless of an error
   - D) To resolve a promise

4. What will the following code output?
   ```javascript
   try {
     throw new Error("Something went wrong");
   } catch (error) {
     console.error(error.message);
   }
   ```
   - A) `undefined`
   - B) `Something went wrong`
   - C) `Error: Something went wrong`
   - D) `null`

5. Which of the following is a valid way to create a custom error?
   - A) `throw "Error message";`
   - B) `catch "Error message";`
   - C) `error "Error message";`
   - D) `finally "Error message";`

6. What type of error will be thrown by this code?
   ```javascript
   throw new TypeError("Invalid type");
   ```
   - A) `RangeError`
   - B) `ReferenceError`
   - C) `SyntaxError`
   - D) `TypeError`

7. In which block would you handle an error thrown in a `try` block?
   - A) `try`
   - B) `catch`
   - C) `finally`
   - D) `throw`

8. What does the following code do?
   ```javascript
   try {
     let result = someFunction();
   } catch (error) {
     console.error("Error: " + error.message);
   } finally {
     console.log("Execution finished");
   }
   ```
   - A) It only runs the `try` block
   - B) It runs the `try` block, then `catch` if there's an error, then `finally`
   - C) It skips the `try` block and runs `catch` and `finally`
   - D) It only runs the `finally` block

9. What will be logged by this code?
   ```javascript
   try {
     let num = 1;
     num.toUpperCase();
   } catch (error) {
     console.error("Caught an error: " + error.message);
   }
   ```
   - A) `Caught an error: toUpperCase is not a function`
   - B) `Caught an error: undefined`
   - C) `Caught an error: 1`
   - D) `Caught an error: num`

10. When is the `finally` block executed?
    - A) Only when there is no error
    - B) Only when there is an error
    - C) Always, regardless of whether there is an error or not
    - D) Never

### Answers

1. B) Throws an error
2. B) `catch`
3. C) To execute code regardless of an error
4. B) `Something went wrong`
5. A) `throw "Error message";`
6. D) `TypeError`
7. B) `catch`
8. B) It runs the `try` block, then `catch` if there's an error, then `finally`
9. A) `Caught an error: toUpperCase is not a function`
10. C) Always, regardless of whether there is an error or not

## The `await` Operator

### Introduction

The `await` operator is used in JavaScript to wait for a Promise to settle (either resolve or reject) and returns the result of the Promise. It can only be used inside an `async` function. The `await` operator makes asynchronous code look and behave more like synchronous code, making it easier to read and understand.

### Using `await` with Promises

When you use `await` with a Promise, it pauses the execution of the `async` function until the Promise is settled.

**Example:**

```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  console.log("Waiting...");
  await delay(2000);
  console.log("Done!");
}

run();
```

In this example, the `run` function waits for 2 seconds before printing "Done!" to the console.

### Handling Errors with `await`

When a Promise rejects, you can catch the error using a `try...catch` block.

**Example:**

```javascript
function getData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error("Failed to fetch data")), 1000);
  });
}

async function fetchData() {
  try {
    const data = await getData();
    console.log(data);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

fetchData();
```

Here, `fetchData` will catch the error from `getData` and log the error message.

### Using `await` with Multiple Promises

You can use `await` with multiple Promises, either sequentially or concurrently.

**Sequential Execution:**

```javascript
async function sequentialTasks() {
  const result1 = await task1();
  const result2 = await task2(result1);
  return result2;
}
```

**Concurrent Execution:**

```javascript
async function concurrentTasks() {
  const [result1, result2] = await Promise.all([task1(), task2()]);
  return [result1, result2];
}
```

Using `Promise.all` with `await` runs `task1` and `task2` concurrently, making the code more efficient.

### Real-World Example: Fetching Data from an API

Imagine you need to fetch user data from an API and then fetch their posts.

**Example:**

```javascript
async function getUser(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const user = await response.json();
  return user;
}

async function getPosts(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
  const posts = await response.json();
  return posts;
}

async function displayUserAndPosts(userId) {
  try {
    const user = await getUser(userId);
    console.log("User:", user);

    const posts = await getPosts(userId);
    console.log("Posts:", posts);
  } catch (error) {
    console.error("Error fetching data:", error.message);
  }
}

displayUserAndPosts(1);
```

In this example, `displayUserAndPosts` fetches user data and their posts, handling any errors that might occur.

### End of Chapter MCQs

1. What does the `await` operator do in JavaScript?
   - A) It creates a new Promise.
   - B) It pauses the execution of an `async` function until the Promise is settled.
   - C) It rejects a Promise.
   - D) It runs a function asynchronously.

2. Where can the `await` operator be used?
   - A) Inside any function.
   - B) Inside a `try` block.
   - C) Inside an `async` function.
   - D) Inside a `catch` block.

3. What will happen if a Promise passed to `await` is rejected and there is no `try...catch` block?
   - A) The error will be ignored.
   - B) The function will throw an unhandled promise rejection error.
   - C) The function will continue execution.
   - D) The Promise will be resolved automatically.

4. How can you handle errors when using the `await` operator?
   - A) Using a `finally` block.
   - B) Using a `then` method.
   - C) Using a `try...catch` block.
   - D) Using an `if` statement.

5. What is the return value of an `async` function?
   - A) A Promise.
   - B) An array.
   - C) A string.
   - D) A number.

6. How do you execute multiple Promises concurrently with `await`?
   - A) Using `await` in a `for` loop.
   - B) Using `Promise.all` with `await`.
   - C) Using multiple `await` statements sequentially.
   - D) Using `await` in a `while` loop.

7. What does the following code log after 2 seconds?
   ```javascript
   async function delay(ms) {
     return new Promise(resolve => setTimeout(resolve, ms));
   }

   async function run() {
     console.log("Start");
     await delay(2000);
     console.log("End");
   }

   run();
   ```
   - A) `Start`
   - B) `End`
   - C) `Start` then `End` after 2 seconds
   - D) `End` then `Start` after 2 seconds

8. How can you fetch data from an API using `await`?
   - A) By using `await fetch()` and `await response.json()`.
   - B) By using `await XMLHttpRequest()`.
   - C) By using `await API.get()`.
   - D) By using `await setTimeout()`.

9. What is the purpose of using `await` with `Promise.all`?
   - A) To run Promises sequentially.
   - B) To run Promises concurrently and wait for all to resolve.
   - C) To catch errors in Promises.
   - D) To log the result of Promises.

10. Which statement is true about `await`?
    - A) It can be used outside of `async` functions.
    - B) It converts a Promise into a synchronous operation.
    - C) It is part of the ES5 standard.
    - D) It pauses the execution of the `async` function and waits for the Promise to resolve or reject.

### Answers

1. B) It pauses the execution of an `async` function until the Promise is settled.
2. C) Inside an `async` function.
3. B) The function will throw an unhandled promise rejection error.
4. C) Using a `try...catch` block.
5. A) A Promise.
6. B) Using `Promise.all` with `await`.
7. C) `Start` then `End` after 2 seconds.
8. A) By using `await fetch()` and `await response.json()`.
9. B) To run Promises concurrently and wait for all to resolve.
10. D) It pauses the execution of the `async` function and waits for the Promise to resolve or reject.

## How to Use an `async` Function

### Introduction

An `async` function is a function that is declared with the `async` keyword, enabling the use of the `await` operator within it. `async` functions simplify the structure of asynchronous code, making it more readable and easier to write. When an `async` function is called, it returns a Promise.

### Declaring an `async` Function

To create an `async` function, you simply add the `async` keyword before the function declaration.

**Example:**

```javascript
async function fetchData() {
  // Code goes here
}
```

### Using the `await` Operator

Inside an `async` function, you can use the `await` keyword to pause the execution of the function until a Promise is settled (resolved or rejected).

**Example:**

```javascript
async function fetchData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data = await response.json();
  console.log(data);
}

fetchData();
```

In this example, `await fetch('https://jsonplaceholder.typicode.com/todos/1')` pauses the execution of `fetchData` until the fetch Promise is resolved. Then, `await response.json()` pauses the execution again until the response is converted to JSON.

### Handling Errors

To handle errors in an `async` function, use a `try...catch` block.

**Example:**

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchData();
```

In this example, if any error occurs during the fetch or the conversion to JSON, it is caught in the `catch` block and logged to the console.

### Returning Values

An `async` function always returns a Promise. If the function returns a value, that value is wrapped in a Promise.

**Example:**

```javascript
async function getNumber() {
  return 42;
}

getNumber().then(number => {
  console.log(number); // 42
});
```

Here, `getNumber` returns a Promise that resolves to 42. Using `.then`, we can log the resolved value.

### Awaiting Multiple Promises

You can use `await` with multiple Promises either sequentially or concurrently.

**Sequential Execution:**

```javascript
async function fetchSequential() {
  const response1 = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const data1 = await response1.json();
  
  const response2 = await fetch('https://jsonplaceholder.typicode.com/todos/2');
  const data2 = await response2.json();
  
  console.log(data1, data2);
}

fetchSequential();
```

**Concurrent Execution:**

```javascript
async function fetchConcurrent() {
  const promise1 = fetch('https://jsonplaceholder.typicode.com/todos/1');
  const promise2 = fetch('https://jsonplaceholder.typicode.com/todos/2');
  
  const [response1, response2] = await Promise.all([promise1, promise2]);
  
  const data1 = await response1.json();
  const data2 = await response2.json();
  
  console.log(data1, data2);
}

fetchConcurrent();
```

In the sequential example, `response2` is fetched only after `response1` is fully processed. In the concurrent example, both fetch requests are initiated at the same time, making the code more efficient.

### Real-World Example: Fetching and Displaying User Data

Imagine you need to fetch user data and their posts from an API and display them.

**Example:**

```javascript
async function getUser(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const user = await response.json();
  return user;
}

async function getUserPosts(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
  const posts = await response.json();
  return posts;
}

async function displayUserData(userId) {
  try {
    const user = await getUser(userId);
    console.log('User:', user);

    const posts = await getUserPosts(userId);
    console.log('Posts:', posts);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

displayUserData(1);
```

In this example, `displayUserData` fetches the user data and their posts concurrently, handling any potential errors.

### End of Chapter MCQs

1. What does the `async` keyword do in JavaScript?
   - A) It creates a synchronous function.
   - B) It allows the use of `await` inside the function.
   - C) It throws an error when used.
   - D) It pauses the function execution.

2. What is the return type of an `async` function?
   - A) A number.
   - B) A string.
   - C) An array.
   - D) A Promise.

3. Where can the `await` keyword be used?
   - A) Inside any function.
   - B) Inside a `try` block.
   - C) Inside an `async` function.
   - D) Inside a `for` loop.

4. How do you handle errors in an `async` function?
   - A) Using a `finally` block.
   - B) Using a `try...catch` block.
   - C) Using an `if` statement.
   - D) Using `await` directly.

5. What happens when an `async` function returns a value?
   - A) The function returns `undefined`.
   - B) The function returns the value directly.
   - C) The function returns a Promise that resolves to the value.
   - D) The function throws an error.

6. How can you run multiple Promises concurrently in an `async` function?
   - A) Using a `for` loop.
   - B) Using `Promise.all` with `await`.
   - C) Using nested `await` statements.
   - D) Using `await` in a `while` loop.

7. What will be logged to the console after 2 seconds in the following code?
   ```javascript
   async function delay(ms) {
     return new Promise(resolve => setTimeout(resolve, ms));
   }

   async function run() {
     console.log("Start");
     await delay(2000);
     console.log("End");
   }

   run();
   ```
   - A) `Start`
   - B) `End`
   - C) `Start` then `End` after 2 seconds
   - D) `End` then `Start` after 2 seconds

8. What does the `await` operator do when used with a Promise?
   - A) It ignores the Promise.
   - B) It pauses the execution until the Promise is resolved or rejected.
   - C) It immediately rejects the Promise.
   - D) It converts the Promise into a string.

9. How can you fetch data from an API using `await` in an `async` function?
   - A) By using `await fetch()` and `await response.json()`.
   - B) By using `await XMLHttpRequest()`.
   - C) By using `await API.get()`.
   - D) By using `await setTimeout()`.

10. Which statement is true about `async` functions?
    - A) They can only return strings.
    - B) They are part of the ES5 standard.
    - C) They automatically handle all errors.
    - D) They always return a Promise.

### Answers

1. B) It allows the use of `await` inside the function.
2. D) A Promise.
3. C) Inside an `async` function.
4. B) Using a `try...catch` block.
5. C) The function returns a Promise that resolves to the value.
6. B) Using `Promise.all` with `await`.
7. C) `Start` then `End` after 2 seconds.
8. B) It pauses the execution until the Promise is resolved or rejected.
9. A) By using `await fetch()` and `await response.json()`.
10. D) They always return a Promise.

## 0. Keep every promise you make and only make promises you can keep

To return a Promise using the function `getResponseFromAPI()`, you can follow the example below. This function doesn't take any parameters and simply returns a new Promise object.

### Example Code

```javascript
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // You can add any asynchronous operation here if needed
    resolve('Response from API');
  });
}

export default getResponseFromAPI;
```

### Explanation

In this example, `getResponseFromAPI` returns a Promise that immediately resolves with the string 'Response from API'. This simulates an API call that successfully returns a response.

### Testing

```javascript
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);  // true
```

### End of Chapter MCQs

1. What does the `getResponseFromAPI` function return?
   - A) A string
   - B) An object
   - C) A Promise
   - D) An error

2. What method is used to resolve a Promise?
   - A) finish
   - B) complete
   - C) resolve
   - D) end

3. In the example code, what does the Promise resolve with?
   - A) An error message
   - B) A number
   - C) A string
   - D) An object

4. What does the `instanceof` operator check in the testing code?
   - A) If `response` is a function
   - B) If `response` is a string
   - C) If `response` is a Promise
   - D) If `response` is null

5. What keyword is used to create a Promise object?
   - A) new
   - B) create
   - C) construct
   - D) build

## 1. Don't make a promise...if you know you can't keep it

To return a promise based on a boolean parameter, use the `getFullResponseFromAPI(success)` function. When `success` is true, resolve the promise with an object. When `success` is false, reject the promise with an error object.

### Example Code

```javascript
function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({
        status: 200,
        body: 'Success'
      });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}

export default getFullResponseFromAPI;
```

### Explanation

In this example, `getFullResponseFromAPI` takes a boolean parameter `success`. If `success` is true, it resolves the Promise with an object containing `status` and `body`. If `success` is false, it rejects the Promise with an error object.

### Testing

```javascript
import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));  // Promise { { status: 200, body: 'Success' } }
console.log(getFullResponseFromAPI(false)); // Promise { <rejected> Error: The fake API is not working currently }
```

### End of Chapter MCQs

1. What does the `getFullResponseFromAPI` function take as a parameter?
   - A) A string
   - B) An object
   - C) A boolean
   - D) A number

2. What does the function return when the parameter is `true`?
   - A) An error message
   - B) An object with status and body
   - C) A string
   - D) null

3. What does the function return when the parameter is `false`?
   - A) A resolved Promise
   - B) A string
   - C) An object with status and body
   - D) A rejected Promise with an error

4. What is the status code in the resolved Promise object?
   - A) 404
   - B) 500
   - C) 200
   - D) 201

5. What error message is returned when the Promise is rejected?
   - A) 'Success'
   - B) 'Failed'
   - C) 'The fake API is not working currently'
   - D) 'Error occurred'

### Answers

**0. Keep every promise you make and only make promises you can keep**
1. C) A Promise
2. C) resolve
3. C) A string
4. C) If `response` is a Promise
5. A) new

**1. Don't make a promise...if you know you can't keep it**
1. C) A boolean
2. B) An object with status and body
3. D) A rejected Promise with an error
4. C) 200
5. C) 'The fake API is not working currently'

## 2. Catch me if you can!

To handle a promise with different outcomes, we will use the `handleResponseFromAPI` function. This function will append three handlers to a given promise:

1. When the promise resolves, it returns an object with the attributes `status: 200` and `body: 'success'`.
2. When the promise rejects, it returns an empty `Error` object.
3. For every resolution, it logs "Got a response from the API" to the console.

### Example Code

```javascript
function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch(() => {
      return new Error();
    });
}

export default handleResponseFromAPI;
```

### Explanation

In this example, `handleResponseFromAPI` takes a `promise` as a parameter and uses `.then()` to handle the resolved state and `.catch()` to handle the rejected state. It logs a message and returns specific objects based on the promise's outcome.

### Testing

```javascript
import handleResponseFromAPI from "./2-then";

const promise = Promise.resolve();
handleResponseFromAPI(promise); // Logs: Got a response from the API

const promise2 = Promise.reject();
handleResponseFromAPI(promise2); // No log, returns an empty Error object
```

### End of Chapter MCQs

1. What does the `handleResponseFromAPI` function take as a parameter?
   - A) A string
   - B) An object
   - C) A promise
   - D) A number

2. What does the function return when the promise resolves?
   - A) An error message
   - B) An object with status and body
   - C) A string
   - D) null

3. What does the function return when the promise rejects?
   - A) A resolved Promise
   - B) A string
   - C) An empty Error object
   - D) An object with status and body

4. What message is logged when the promise resolves?
   - A) 'Failed'
   - B) 'The fake API is not working currently'
   - C) 'Got a response from the API'
   - D) 'Error occurred'

5. What method is used to handle promise rejections?
   - A) .then()
   - B) .finally()
   - C) .catch()
   - D) .resolve()

## 3. Handle multiple successful promises

To handle multiple successful promises and log the results, we will use the `handleProfileSignup` function. This function will import `uploadPhoto` and `createUser` from `utils.js`, resolve all promises collectively, and log the results. If any error occurs, it logs "Signup system offline" to the console.

### Example Code

```javascript
import { uploadPhoto, createUser } from './utils.js';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const [photo, user] = results;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
```

### Explanation

In this example, `handleProfileSignup` uses `Promise.all` to handle multiple promises returned by `uploadPhoto` and `createUser`. When all promises resolve, it logs the combined results. If any promise is rejected, it logs an error message.

### Testing

```javascript
import handleProfileSignup from "./3-all";

handleProfileSignup(); // Logs: photo-profile-1 Guillaume Salva or 'Signup system offline'
```

### End of Chapter MCQs

1. What does the `handleProfileSignup` function import?
   - A) handleResponseFromAPI
   - B) getResponseFromAPI
   - C) uploadPhoto and createUser
   - D) handleResponse

2. What method is used to collectively resolve all promises?
   - A) .then()
   - B) .all()
   - C) .catch()
   - D) .finally()

3. What is logged when all promises resolve successfully?
   - A) 'Signup system offline'
   - B) An error message
   - C) The combined result of photo body and user name
   - D) A success message

4. What message is logged in the event of an error?
   - A) 'Error occurred'
   - B) 'Failed'
   - C) 'The fake API is not working currently'
   - D) 'Signup system offline'

5. Which method is used to handle errors in the function?
   - A) .then()
   - B) .finally()
   - C) .catch()
   - D) .resolve()

### Answers

**2. Catch me if you can!**
1. C) A promise
2. B) An object with status and body
3. C) An empty Error object
4. C) 'Got a response from the API'
5. C) .catch()

**3. Handle multiple successful promises**
1. C) uploadPhoto and createUser
2. B) .all()
3. C) The combined result of photo body and user name
4. D) 'Signup system offline'
5. C) .catch()

## 4. Simple Promise

To create a simple promise, we will define a function `signUpUser` that takes two parameters: `firstName` and `lastName`. This function will return a resolved promise with an object containing the provided `firstName` and `lastName`.

### Example Code

```javascript
function signUpUser(firstName, lastName) {
  return Promise.resolve({
    firstName: firstName,
    lastName: lastName
  });
}

export default signUpUser;
```

### Explanation

In this example, the `signUpUser` function uses `Promise.resolve()` to create a resolved promise that contains an object with `firstName` and `lastName` properties.

### Testing

```javascript
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan")); // Logs: Promise { { firstName: 'Bob', lastName: 'Dylan' } }
```

### End of Chapter MCQs

1. What does the `signUpUser` function return?
   - A) A rejected promise
   - B) A resolved promise
   - C) An object
   - D) A string

2. What object does the promise resolve with?
   - A) { firstName: value }
   - B) { lastName: value }
   - C) { firstName: value, lastName: value }
   - D) {}

3. What is the purpose of `Promise.resolve()` in the `signUpUser` function?
   - A) To handle errors
   - B) To delay execution
   - C) To create a resolved promise
   - D) To create a rejected promise

4. What are the parameters of the `signUpUser` function?
   - A) firstName and age
   - B) firstName and lastName
   - C) firstName and email
   - D) lastName and age

5. How would you call the `signUpUser` function with "Alice" and "Smith" as arguments?
   - A) signUpUser("Alice")
   - B) signUpUser("Smith")
   - C) signUpUser("Alice", "Smith")
   - D) signUpUser({ firstName: "Alice", lastName: "Smith" })

## 5. Reject the Promises

To create a promise that always rejects, we will define a function `uploadPhoto` that takes a `fileName` parameter and returns a promise that rejects with an error message stating that the file cannot be processed.

### Example Code

```javascript
function uploadPhoto(fileName) {
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}

export default uploadPhoto;
```

### Explanation

In this example, the `uploadPhoto` function uses `Promise.reject()` to create a rejected promise with an error message. The error message includes the provided `fileName`.

### Testing

```javascript
import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg')); // Logs: Promise { <rejected> Error: guillaume.jpg cannot be processed }
```

### End of Chapter MCQs

1. What does the `uploadPhoto` function return?
   - A) A resolved promise
   - B) A rejected promise
   - C) An object
   - D) A string

2. What parameter does the `uploadPhoto` function accept?
   - A) fileName
   - B) fileType
   - C) fileSize
   - D) fileContent

3. What error message does the promise reject with?
   - A) `${fileName} cannot be found`
   - B) `${fileName} cannot be processed`
   - C) `Error: file not supported`
   - D) `File upload failed`

4. What method is used to create a rejected promise?
   - A) Promise.resolve()
   - B) Promise.all()
   - C) Promise.reject()
   - D) Promise.race()

5. What is logged when `uploadPhoto('example.jpg')` is called?
   - A) Promise { <resolved> { firstName: 'example', lastName: 'jpg' } }
   - B) Promise { <resolved> {} }
   - C) Promise { <rejected> Error: example.jpg cannot be processed }
   - D) Promise { <rejected> Error: File upload failed }

### Answers

**4. Simple Promise**
1. B) A resolved promise
2. C) { firstName: value, lastName: value }
3. C) To create a resolved promise
4. B) firstName and lastName
5. C) signUpUser("Alice", "Smith")

**5. Reject the Promises**
1. B) A rejected promise
2. A) fileName
3. B) `${fileName} cannot be processed`
4. C) Promise.reject()
5. C) Promise { <rejected> Error: example.jpg cannot be processed }

## 6. Handle Multiple Promises

To handle multiple promises, we'll import two functions: `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`.

```javascript
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
    // Call the signUpUser and uploadPhoto functions
    const promise1 = signUpUser(firstName, lastName);
    const promise2 = uploadPhoto(fileName);

    // Wait for all promises to settle
    return Promise.allSettled([promise1, promise2])
        .then(results => {
            // Map the results to an array of objects
            return results.map(result => ({
                status: result.status,
                value: result.status === 'fulfilled' ? result.value : result.reason
            }));
        });
}
```

The `handleProfileSignup` function takes three arguments: `firstName`, `lastName`, and `fileName`. It calls the `signUpUser` function with `firstName` and `lastName`, and the `uploadPhoto` function with `fileName`. Then, it waits for both promises to settle using `Promise.allSettled()`. Finally, it maps the results to an array of objects containing the status and value or error returned by each promise.

## 7. Load Balancer

For the load balancer function, we'll write and export a function named `loadBalancer` that accepts two promises: `chinaDownload` and `USDownload`. It returns the value of the promise that resolves first.

```javascript
export default function loadBalancer(chinaDownload, USDownload) {
    // Return the value of the promise that resolves first
    return Promise.race([chinaDownload, USDownload]);
}
```

The `loadBalancer` function utilizes `Promise.race()` to return the value of the first resolved promise, either `chinaDownload` or `USDownload`. This simulates a load balancer where the function returns the value from the fastest available source.

These functionalities can be applied in real-world projects where asynchronous operations need to be managed efficiently, such as handling user authentication or downloading resources from multiple servers.

---

### End of Chapter MCQs

**6. Handle Multiple Promises**
1. What functions are imported in the `handleProfileSignup` function?
   - A) `uploadPhoto` and `downloadFile`
   - B) `signUpUser` and `downloadFile`
   - C) `uploadPhoto` and `signUpUser`
   - D) `createUser` and `uploadImage`

2. How many promises are awaited in the `handleProfileSignup` function?
   - A) One
   - B) Two
   - C) Three
   - D) None

3. What method is used to handle multiple promises in `handleProfileSignup`?
   - A) `Promise.resolve()`
   - B) `Promise.all()`
   - C) `Promise.any()`
   - D) `Promise.allSettled()`

**7. Load Balancer**
1. What does the `loadBalancer` function return?
   - A) The value of the China promise
   - B) The value of the US promise
   - C) The value of the promise that resolves first
   - D) An array of resolved promises

2. Which method is used to implement a load balancer in the `loadBalancer` function?
   - A) `Promise.resolve()`
   - B) `Promise.all()`
   - C) `Promise.race()`
   - D) `Promise.any()`

3. How many promises are passed as arguments to the `loadBalancer` function?
   - A) One
   - B) Two
   - C) Three
   - D) None

### Answers

**6. Handle Multiple Promises**
1. C) `uploadPhoto` and `signUpUser`
2. B) Two
3. D) `Promise.allSettled()`

**7. Load Balancer**
1. C) The value of the promise that resolves first
2. C) `Promise.race()`
3. B) Two

## Error Handling in JavaScript

Error handling is a crucial aspect of software development, ensuring that unexpected issues are managed gracefully. In JavaScript, errors can occur due to various reasons, such as invalid inputs, network failures, or logical errors in the code. Understanding how to handle errors effectively can make your code more robust and maintainable.

### 1. Throw Error / Try Catch

The `try...catch` statement in JavaScript allows you to handle errors gracefully by trying a block of code and catching any errors that occur within it.

Here's how you can implement error handling for a division function:

```javascript
// 8-try.js
export default function divideFunction(numerator, denominator) {
    try {
        if (denominator === 0) {
            throw new Error('cannot divide by 0');
        }
        return numerator / denominator;
    } catch (error) {
        throw error;
    }
}
```

In this example:
- We define a function `divideFunction` that takes two arguments: `numerator` and `denominator`.
- Inside the function, we use a `try...catch` block to handle errors.
- If the `denominator` is equal to 0, we throw a new `Error` with the message "cannot divide by 0".
- Otherwise, we return the result of dividing `numerator` by `denominator`.

### 2. Throw an Error

You can also create custom error handling functions to manage errors and provide meaningful feedback to users.

Here's how you can implement a function called `guardrail` to handle errors thrown by another function:

```javascript
// 9-try.js
export default function guardrail(mathFunction) {
    const queue = [];
    try {
        queue.push(mathFunction());
    } catch (error) {
        queue.push(error.toString());
    } finally {
        queue.push('Guardrail was processed');
    }
    return queue;
}
```

In this example:
- We define a function `guardrail` that takes a `mathFunction` as an argument.
- Inside the function, we create an empty array called `queue` to store the results and error messages.
- We execute the `mathFunction` inside a `try` block and push its result to the `queue`.
- If an error occurs, we catch it and push the error message to the `queue`.
- Finally, we always push the message "Guardrail was processed" to the `queue`.
- The `queue` array is then returned.

### Real-World Application

Error handling is essential in real-world projects to ensure that applications behave predictably and provide useful feedback to users. For example, in a web application, error handling can prevent crashes and display friendly error messages to users when something goes wrong, enhancing user experience and overall reliability.

### End of Chapter MCQ

1. What is the purpose of the `try...catch` statement in JavaScript?
   a) To execute code synchronously
   b) To handle asynchronous operations
   c) To handle errors gracefully
   d) To define custom functions

2. When should you throw an error in JavaScript?
   a) Only for network-related issues
   b) Only for logical errors in the code
   c) For unexpected situations or invalid inputs
   d) Never, errors should be handled silently

3. What happens if an error occurs inside the `try` block and there is no corresponding `catch` block?
   a) The error is ignored
   b) The program crashes
   c) The `finally` block is executed
   d) The error is caught by the global error handler

4. Which keyword is used to throw an error in JavaScript?
   a) break
   b) throw
   c) catch
   d) try

5. What does the `finally` block in a `try...catch` statement do?
   a) Executes only if an error occurs
   b) Executes only if no error occurs
   c) Always executes, regardless of errors
   d) Executes asynchronously

6. In the `guardrail` function, what is the purpose of the `finally` block?
   a) To catch errors thrown by the `mathFunction`
   b) To execute after the `try` block, regardless of errors
   c) To define custom error messages
   d) To prevent errors from occurring

7. What does the `mathFunction` argument represent in the `guardrail` function?
   a) A mathematical operation
   b) An error handling function
   c) An array of numbers
   d) A message queue

8. Which message is added to the queue if an error occurs in the `guardrail` function?
   a) 'Error: cannot divide by 0'
   b) 'Guardrail was processed'
   c) 'Error: mathFunction is not a function'
   d) 'Guardrail function failed'

9. How does the `guardrail` function handle errors thrown by the `mathFunction`?
   a) By ignoring errors
   b) By crashing the program
   c) By adding error messages to the queue
   d) By returning undefined

10. What is the benefit of using error handling in JavaScript?
   a) It makes code execution faster
   b) It improves code readability
   c) It enhances user experience and application reliability
   d) It allows for easier debugging

### Answers

1. c) To handle errors gracefully
2. c) For unexpected situations or invalid inputs
3. b) The program crashes
4. b) throw
5. c) Always executes, regardless of errors
6. b) To execute after the `try` block, regardless of errors
7. a) A mathematical operation
8. b) 'Guardrail was processed'
9. c) By adding error messages to the queue
10. c) It enhances user experience and application reliability

## Asynchronous Programming with Await/Async

Asynchronous programming is crucial in modern web development, allowing JavaScript to perform tasks such as network requests, file operations, and other I/O-bound operations efficiently without blocking the main thread. The `await` and `async` keywords in JavaScript provide a more readable and concise way to work with asynchronous code compared to traditional callback or promise-based approaches.

### Using Await/Async for Asynchronous Operations

To illustrate how `await` and `async` can be used, let's consider an example where we need to upload a user's photo and create a user profile asynchronously.

```javascript
// 100-await.js
import { uploadPhoto, createUser } from './utils.js';

async function asyncUploadUser() {
    try {
        const photoResponse = await uploadPhoto();
        const userResponse = await createUser();
        
        return {
            photo: photoResponse,
            user: userResponse
        };
    } catch (error) {
        console.error(error);
        return {
            photo: null,
            user: null
        };
    }
}

export default asyncUploadUser;
```

In this example:
- We define an asynchronous function `asyncUploadUser` using the `async` keyword.
- Inside the function, we use `await` to wait for the completion of the `uploadPhoto` and `createUser` functions.
- If both functions execute successfully, we return an object containing the responses from both functions.
- If any error occurs during execution, we catch it and return an object with both values set to `null`.

### Real-World Application

In real-world projects, asynchronous programming with `await` and `async` is commonly used for tasks such as:
- Making HTTP requests to fetch data from APIs.
- Reading and writing files asynchronously.
- Interacting with databases.
- Performing background tasks without blocking the main thread, such as animations or long-running computations.

### End of Chapter MCQ

1. What is the purpose of `await` in JavaScript?
   a) To define asynchronous functions
   b) To wait for the completion of asynchronous operations
   c) To handle errors in asynchronous code
   d) To execute code synchronously

2. Which keyword is used to declare an asynchronous function in JavaScript?
   a) await
   b) async
   c) function
   d) Promise

3. What does the `async` keyword do in JavaScript?
   a) It makes a function asynchronous
   b) It defines a promise
   c) It waits for the completion of asynchronous operations
   d) It throws an error

4. How is error handling typically done in async/await functions?
   a) Using try...catch blocks
   b) Using if...else statements
   c) Using switch statements
   d) By returning error objects

5. In the provided example, what happens if one of the async functions fails?
   a) An error is thrown and the program crashes
   b) The function returns an object with null values
   c) The program continues execution without any interruption
   d) The function returns undefined

6. Which function is responsible for uploading the user's photo in the example?
   a) createUser
   b) uploadPhoto
   c) asyncUploadUser
   d) utils.js

7. How does the `asyncUploadUser` function handle errors thrown by async functions?
   a) By ignoring errors
   b) By returning an empty object
   c) By catching errors and logging them
   d) By crashing the program

8. What is the benefit of using async/await for asynchronous programming?
   a) It simplifies error handling
   b) It improves performance
   c) It makes code more readable and maintainable
   d) It allows for parallel execution of tasks

9. Which JavaScript feature was introduced to make asynchronous code easier to work with?
   a) Callbacks
   b) Promises
   c) Generators
   d) Arrow functions

10. In a real-world application, where could async/await be particularly useful?
   a) Performing simple arithmetic calculations
   b) Handling user interface events
   c) Making HTTP requests to fetch data from an API
   d) Defining constants and variables

### Answers

1. b) To wait for the completion of asynchronous operations
2. b) async
3. a) It makes a function asynchronous
4. a) Using try...catch blocks
5. b) The function returns an object with null values
6. b) uploadPhoto
7. c) By catching errors and logging them
8. c) It makes code more readable and maintainable
9. b) Promises
10. c) Making HTTP requests to fetch data from an API

## Conclusion

Mastering asynchronous JavaScript programming is crucial for building modern, responsive, and efficient web applications. By understanding Promises, async/await, error handling techniques, and async functions, developers can write cleaner, more maintainable code that effectively manages asynchronous tasks. Continuously practicing and applying these concepts will enhance your proficiency in JavaScript development and empower you to create high-quality software products.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
