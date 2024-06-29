# Unit Testing vs. Integration Testing

## Introduction

Testing is a crucial part of software development. It ensures that the code you write works as expected. Two fundamental types of testing are **unit testing** and **integration testing**. Understanding the difference between these types of testing helps you write better code and build more reliable software.

---

## Unit Testing

### Definition
Unit testing involves testing individual components of software, like functions, methods, or classes, in isolation from the rest of the application. The goal is to verify that each unit works correctly on its own.

### Characteristics
- **Isolated**: Tests one unit (a single function or method) at a time.
- **Fast**: Since tests are isolated, they run quickly.
- **Independent**: Each test should be independent of others.

### Example Code Snippet
Let's say we have a simple function that adds two numbers:

```python
# adder.py
def add(a, b):
    return a + b
```

A unit test for this function might look like:

```python
# test_adder.py
import unittest
from adder import add

class TestAdder(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

### Application in Real-World Projects
- **Library Development**: Ensuring each function or method in a library works correctly before integration.
- **Refactoring**: Safely changing code by validating that the behavior of individual units remains unchanged.

---

## Integration Testing

### Definition
Integration testing involves testing multiple components or units of software together to ensure they work correctly as a group. The goal is to identify issues that occur when units interact with each other.

### Characteristics
- **Combined**: Tests multiple units together.
- **Detects Interface Issues**: Identifies problems at the boundaries between units.
- **Broader Scope**: Checks overall system behavior rather than individual units.

### Example Code Snippet
Suppose we have a `Calculator` class that uses the `add` function:

```python
# calculator.py
from adder import add

class Calculator:
    def add_numbers(self, a, b):
        return add(a, b)
```

An integration test might look like:

```python
# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add_numbers(self):
        calc = Calculator()
        self.assertEqual(calc.add_numbers(1, 2), 3)
        self.assertEqual(calc.add_numbers(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### Application in Real-World Projects
- **System Development**: Validating that different parts of a system (e.g., database interactions, APIs) work together as expected.
- **Deployment Testing**: Ensuring that integrated components function correctly in staging or production environments.

---

## Comparison

| Aspect                | Unit Testing                            | Integration Testing                   |
|-----------------------|-----------------------------------------|---------------------------------------|
| **Scope**             | Individual unit                         | Multiple units or whole system        |
| **Focus**             | Isolated functionality                  | Interactions between units            |
| **Speed**             | Fast                                    | Slower than unit tests                |
| **Complexity**        | Simpler                                 | More complex due to dependencies      |
| **Error Detection**   | Errors in specific units                | Errors in interactions between units  |

---

## Practical Example: Building a Web Application

### Unit Test Example
Testing a function that formats user input in a web form:

```python
# formatter.py
def format_username(username):
    return username.strip().lower()
```

Unit test:

```python
# test_formatter.py
import unittest
from formatter import format_username

class TestFormatter(unittest.TestCase):
    def test_format_username(self):
        self.assertEqual(format_username(" User "), "user")
        self.assertEqual(format_username("ADMIN"), "admin")

if __name__ == '__main__':
    unittest.main()
```

### Integration Test Example
Testing the integration of a login system:

```python
# login.py
from formatter import format_username

class LoginSystem:
    def __init__(self, users):
        self.users = users

    def login(self, username):
        formatted_username = format_username(username)
        return formatted_username in self.users
```

Integration test:

```python
# test_login.py
import unittest
from login import LoginSystem

class TestLoginSystem(unittest.TestCase):
    def test_login(self):
        users = {"user1", "admin"}
        login_system = LoginSystem(users)
        self.assertTrue(login_system.login(" user1 "))
        self.assertFalse(login_system.login(" guest "))

if __name__ == '__main__':
    unittest.main()
```

---

## End-of-Chapter Quiz

1. **What is the primary focus of unit testing?**
   - a) Testing individual units of code in isolation
   - b) Testing the integration of multiple components
   - c) Testing the user interface
   - d) Testing the entire application

2. **What type of test is usually faster?**
   - a) Integration test
   - b) System test
   - c) Unit test
   - d) Acceptance test

3. **Which of the following is a characteristic of integration testing?**
   - a) Tests one function at a time
   - b) Tests multiple units together
   - c) Runs quickly
   - d) Requires no dependencies

4. **In unit testing, why should tests be independent?**
   - a) To ensure they run faster
   - b) To avoid dependency on other tests
   - c) To simplify integration testing
   - d) To make them easier to read

5. **What does integration testing primarily aim to detect?**
   - a) Errors in individual functions
   - b) Errors in user interfaces
   - c) Errors in the interaction between units
   - d) Errors in test scripts

6. **Which testing method is likely to identify a problem in the interaction between a login function and a database?**
   - a) Unit testing
   - b) Integration testing
   - c) System testing
   - d) Performance testing

7. **Why are integration tests typically slower than unit tests?**
   - a) They test more lines of code
   - b) They require more sophisticated test environments
   - c) They involve multiple components interacting
   - d) They use more advanced algorithms

8. **What kind of errors are unit tests best at catching?**
   - a) Logical errors in isolated functions
   - b) Configuration errors
   - c) Errors in the communication between systems
   - d) User interface errors

9. **Which type of test would you use to ensure that a method that calculates tax works correctly on its own?**
   - a) Integration test
   - b) Unit test
   - c) System test
   - d) Performance test

10. **If a unit test fails, what does this indicate?**
    - a) An issue in the integration between components
    - b) An issue with a specific unit of code
    - c) A problem with the test script itself
    - d) A user interface problem

### Answers

1. a) Testing individual units of code in isolation
2. c) Unit test
3. b) Tests multiple units together
4. b) To avoid dependency on other tests
5. c) Errors in the interaction between units
6. b) Integration testing
7. c) They involve multiple components interacting
8. a) Logical errors in isolated functions
9. b) Unit test
10. b) An issue with a specific unit of code

# Common Testing Patterns: Mocking, Parametrization, and Fixtures

## Introduction

Effective testing in software development often involves using various patterns to streamline tests and handle complex scenarios. Three common testing patterns are **mocking**, **parametrization**, and **fixtures**. Each pattern helps in different aspects of testing, making tests more robust and maintainable.

---

## Mocking

### Definition
Mocking is the practice of creating mock objects that simulate the behavior of real objects in a controlled way. It allows you to test code without relying on external dependencies.

### Use Cases
- **Simulate External Systems**: When testing a function that interacts with a database or an API, you can use mocks to simulate these interactions.
- **Isolate Units**: Mocks help isolate the unit under test from its dependencies, making the test more focused and easier to debug.

### Example Code Snippet
Imagine you have a function that sends a message using an external messaging service:

```python
# messaging_service.py
class MessagingService:
    def send_message(self, message):
        # Simulate sending a message to an external service
        pass
```

You want to test a function that uses this service:

```python
# notifier.py
from messaging_service import MessagingService

class Notifier:
    def __init__(self):
        self.service = MessagingService()

    def notify(self, message):
        self.service.send_message(message)
```

A test with mocking might look like:

```python
# test_notifier.py
import unittest
from unittest.mock import MagicMock
from notifier import Notifier

class TestNotifier(unittest.TestCase):
    def test_notify(self):
        notifier = Notifier()
        notifier.service = MagicMock()
        notifier.notify("Hello")

        notifier.service.send_message.assert_called_once_with("Hello")

if __name__ == '__main__':
    unittest.main()
```

### Application in Real-World Projects
- **Testing External Interactions**: Mocking API calls or database interactions to ensure the code works as expected without relying on the actual systems.
- **Simulating Conditions**: Creating mock responses for services that may have varying conditions or states.

---

## Parametrization

### Definition
Parametrization is the technique of running the same test with different inputs and expected outputs. It allows you to test various scenarios with minimal code duplication.

### Use Cases
- **Testing Multiple Scenarios**: Ensure that a function handles different inputs correctly.
- **Data-Driven Testing**: Useful when you have a range of data sets to validate the behavior of your code.

### Example Code Snippet
Suppose you have a function that checks if a number is even:

```python
# utils.py
def is_even(number):
    return number % 2 == 0
```

A parametrized test might look like:

```python
# test_utils.py
import pytest
from utils import is_even

@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (5, False)
])
def test_is_even(input, expected):
    assert is_even(input) == expected
```

### Application in Real-World Projects
- **Handling Edge Cases**: Running tests with boundary values and edge cases.
- **Validating Business Logic**: Ensuring functions work correctly across a wide range of input conditions.

---

## Fixtures

### Definition
Fixtures are functions that provide a fixed baseline environment for tests. They set up the state before a test runs and clean it up afterward.

### Use Cases
- **Setup and Teardown**: Preparing necessary resources like databases, files, or network connections before tests and cleaning them up afterward.
- **Reusability**: Sharing setup code among multiple tests to avoid duplication.

### Example Code Snippet
Suppose you have a database that needs to be set up for testing:

```python
# database.py
class Database:
    def connect(self):
        # Simulate a database connection
        pass

    def disconnect(self):
        # Simulate closing the database connection
        pass

    def query(self, query):
        # Simulate querying the database
        return "result"
```

You can use fixtures to set up the database connection:

```python
# test_database.py
import pytest
from database import Database

@pytest.fixture
def db():
    database = Database()
    database.connect()
    yield database
    database.disconnect()

def test_query(db):
    result = db.query("SELECT * FROM table")
    assert result == "result"
```

### Application in Real-World Projects
- **Consistent Environments**: Ensuring tests run in a consistent environment by setting up and tearing down required resources.
- **Resource Management**: Managing connections and states that are costly to create and destroy repeatedly.

---

## End-of-Chapter Quiz

1. **What is the purpose of mocking in testing?**
   - a) To run tests faster
   - b) To simulate real objects in a controlled way
   - c) To increase test coverage
   - d) To generate random test data

2. **When would you use parametrization in testing?**
   - a) To test the interaction between multiple systems
   - b) To test the same function with different inputs
   - c) To set up and tear down environments
   - d) To mock external services

3. **What does a mock object do?**
   - a) Replaces the real object and simulates its behavior
   - b) Generates real data for tests
   - c) Measures the performance of code
   - d) Cleans up after tests

4. **Which of the following is a characteristic of fixtures in testing?**
   - a) Running the same test with different inputs
   - b) Setting up the environment before tests run
   - c) Mocking external dependencies
   - d) Generating random test data

5. **What is the main advantage of using parametrized tests?**
   - a) They are easier to write
   - b) They handle edge cases automatically
   - c) They allow testing multiple scenarios with minimal code duplication
   - d) They mock external systems

6. **Why might you use a fixture in a test?**
   - a) To change the input data dynamically
   - b) To simulate an external API
   - c) To set up a database connection before tests run
   - d) To run tests in parallel

7. **What is a common use of mocking in tests?**
   - a) To increase test performance
   - b) To simulate the behavior of components that are not yet implemented
   - c) To create actual data for tests
   - d) To verify the user interface

8. **What does the `yield` statement do in a fixture?**
   - a) Starts the test execution
   - b) Cleans up resources after tests run
   - c) Provides the setup resource and waits for the test to complete
   - d) Generates multiple test cases

9. **Which testing pattern would you use to ensure a function behaves correctly with a variety of input values?**
   - a) Mocking
   - b) Parametrization
   - c) Fixtures
   - d) Stubbing

10. **How do fixtures help in managing resources in tests?**
    - a) By mocking external services
    - b) By setting up and tearing down resources like databases
    - c) By running tests with different parameters
    - d) By generating random test data

### Answers

1. b) To simulate real objects in a controlled way
2. b) To test the same function with different inputs
3. a) Replaces the real object and simulates its behavior
4. b) Setting up the environment before tests run
5. c) They allow testing multiple scenarios with minimal code duplication
6. c) To set up a database connection before tests run
7. b) To simulate the behavior of components that are not yet implemented
8. c) Provides the setup resource and waits for the test to complete
9. b) Parametrization
10. b) By setting up and tearing down resources like databases

# Parameterizing a Unit Test for `utils.access_nested_map`

## Introduction

When writing unit tests, it's important to ensure that your tests are concise and cover a variety of cases. Parametrizing tests allows you to run the same test logic with different inputs and expected outputs, reducing code duplication and making your tests easier to maintain.

In this note, we'll focus on parameterizing a unit test for the `utils.access_nested_map` function. We'll create a class `TestAccessNestedMap` that inherits from `unittest.TestCase`, and use the `@parameterized.expand` decorator to test multiple input scenarios.

---

## `utils.access_nested_map` Function

The `utils.access_nested_map` function allows access to nested dictionaries using a sequence of keys (path). It retrieves the value located at the end of the path within the nested dictionary.

### Example Usage
```python
def access_nested_map(nested_map, path):
    for key in path:
        nested_map = nested_map[key]
    return nested_map

# Example:
nested_map = {"a": {"b": 2}}
path = ("a", "b")
print(access_nested_map(nested_map, path))  # Output: 2
```

---

## Writing the Test Class

We'll create a test class `TestAccessNestedMap` that inherits from `unittest.TestCase`. Inside this class, we'll write a method `test_access_nested_map` decorated with `@parameterized.expand` to test multiple inputs.

### Step-by-Step Implementation

1. **Import Required Modules**:
   ```python
   import unittest
   from parameterized import parameterized
   from utils import access_nested_map
   ```

2. **Define the Test Class**:
   ```python
   class TestAccessNestedMap(unittest.TestCase):
       @parameterized.expand([
           ({"a": 1}, ("a",), 1),
           ({"a": {"b": 2}}, ("a",), {"b": 2}),
           ({"a": {"b": 2}}, ("a", "b"), 2)
       ])
       def test_access_nested_map(self, nested_map, path, expected):
           self.assertEqual(access_nested_map(nested_map, path), expected)

   if __name__ == '__main__':
       unittest.main()
   ```

### Explanation

- **Parameterization**:
  - The `@parameterized.expand` decorator is used to run the test method `test_access_nested_map` with different sets of arguments. Each tuple in the list represents a test case with `nested_map`, `path`, and the expected result.
- **Test Method**:
  - The `test_access_nested_map` method takes `nested_map`, `path`, and `expected` as arguments and asserts that the result of `access_nested_map(nested_map, path)` is equal to `expected`.

### Application in Real-World Projects

Using parameterized tests is particularly useful when you need to validate the behavior of a function across a wide range of inputs. This approach helps in:
- **Ensuring Comprehensive Coverage**: Testing all possible edge cases and typical scenarios.
- **Reducing Code Duplication**: Avoiding repetitive test code by reusing the same test logic with different data.

---

## End-of-Chapter Quiz

1. **What does parameterizing a test allow you to do?**
   - a) Write longer test methods
   - b) Run the same test logic with different inputs
   - c) Ignore certain test cases
   - d) Mock external dependencies

2. **Which decorator is used to parameterize tests in Python?**
   - a) @pytest.mark.parametrize
   - b) @parameterized.expand
   - c) @unittest.parameterize
   - d) @mock.parameterize

3. **In the provided example, what does the `path` argument represent?**
   - a) A file path
   - b) A sequence of keys to access nested dictionary values
   - c) The output value
   - d) The expected result

4. **What does the `assertEqual` method do in the test?**
   - a) Compares two values for equality
   - b) Sets up the test environment
   - c) Mocks a function call
   - d) Expands the test parameters

5. **Why is parameterization useful in unit testing?**
   - a) It makes tests faster
   - b) It reduces code duplication
   - c) It increases the number of test files
   - d) It eliminates the need for assertions

6. **What is the purpose of the `utils.access_nested_map` function?**
   - a) To map nested lists
   - b) To access nested values in a dictionary
   - c) To sort nested dictionaries
   - d) To flatten nested dictionaries

7. **What does the `@parameterized.expand` decorator do?**
   - a) Runs the test method with different sets of arguments
   - b) Expands the test method into multiple methods
   - c) Mocks the test method
   - d) Measures the performance of the test method

8. **Which of the following is a correct test case for `access_nested_map`?**
   - a) ({"a": 1}, ("a", "b"), 1)
   - b) ({"a": {"b": 2}}, ("a",), 2)
   - c) ({"a": {"b": 2}}, ("a", "b"), 2)
   - d) ({"a": {"b": 2}}, ("b", "a"), {"b": 2})

9. **In the context of the provided example, what is `expected`?**
   - a) The input value
   - b) The path to the nested dictionary
   - c) The expected result of the function
   - d) The function being tested

10. **How many lines of code should the body of the test method be, according to the task?**
    - a) No more than 1 line
    - b) No more than 2 lines
    - c) No more than 5 lines
    - d) No more than 10 lines

### Answers

1. b) Run the same test logic with different inputs
2. b) @parameterized.expand
3. b) A sequence of keys to access nested dictionary values
4. a) Compares two values for equality
5. b) It reduces code duplication
6. b) To access nested values in a dictionary
7. a) Runs the test method with different sets of arguments
8. c) ({"a": {"b": 2}}, ("a", "b"), 2)
9. c) The expected result of the function
10. b) No more than 2 lines

# Parameterizing a Unit Test for Exception Handling in `utils.access_nested_map`

## Introduction

When writing unit tests, it's crucial to test not only the expected successful outputs but also how your code handles errors and exceptions. This helps ensure that your functions behave correctly under various conditions and handle edge cases gracefully.

In this note, we'll extend our tests for the `utils.access_nested_map` function to handle scenarios where accessing a key raises a `KeyError`. We'll use the `assertRaises` context manager within a parameterized test to validate that the function raises exceptions as expected.

---

## `utils.access_nested_map` Function

The `utils.access_nested_map` function retrieves a value from a nested dictionary based on a sequence of keys (path). If any key in the path does not exist, it should raise a `KeyError`.

### Example Function Definition
```python
def access_nested_map(nested_map, path):
    for key in path:
        nested_map = nested_map[key]
    return nested_map
```

---

## Writing the Exception Test

We'll create an additional test method in our `TestAccessNestedMap` class to handle scenarios where a `KeyError` should be raised. We'll use `@parameterized.expand` to test multiple cases and `assertRaises` to check for exceptions.

### Step-by-Step Implementation

1. **Import Required Modules**:
   ```python
   import unittest
   from parameterized import parameterized
   from utils import access_nested_map
   ```

2. **Define the Test Class with Exception Handling**:
   ```python
   class TestAccessNestedMap(unittest.TestCase):
       @parameterized.expand([
           ({"a": 1}, ("a",), 1),
           ({"a": {"b": 2}}, ("a",), {"b": 2}),
           ({"a": {"b": 2}}, ("a", "b"), 2)
       ])
       def test_access_nested_map(self, nested_map, path, expected):
           self.assertEqual(access_nested_map(nested_map, path), expected)

       @parameterized.expand([
           ({}, ("a",), KeyError),
           ({"a": 1}, ("a", "b"), KeyError)
       ])
       def test_access_nested_map_exception(self, nested_map, path, exception):
           with self.assertRaises(exception) as context:
               access_nested_map(nested_map, path)
           self.assertEqual(str(context.exception), f"'{path[-1]}'")

   if __name__ == '__main__':
       unittest.main()
   ```

### Explanation

- **Test for Expected Values**:
  - The `test_access_nested_map` method remains the same, testing that valid inputs return expected values.
- **Test for Exceptions**:
  - The `test_access_nested_map_exception` method tests that a `KeyError` is raised when trying to access non-existent keys in the nested map.
  - The `@parameterized.expand` decorator is used to run this test with different sets of arguments.
  - The `assertRaises` context manager checks if the `KeyError` is raised, and `self.assertEqual` verifies that the exception message matches the expected key.

### Application in Real-World Projects

Testing for exceptions ensures that your code fails gracefully and provides meaningful error messages. This is especially important for functions that interact with user inputs or external systems where unexpected values or states are likely.

---

## End-of-Chapter Quiz

1. **What does the `assertRaises` context manager do in a test?**
   - a) Checks for specific output values
   - b) Tests that a specific exception is raised
   - c) Mocks function calls
   - d) Generates test data

2. **Which decorator is used to parameterize tests in Python?**
   - a) @pytest.mark.parametrize
   - b) @parameterized.expand
   - c) @unittest.parameterize
   - d) @mock.parameterize

3. **In the provided test, what is the purpose of `path`?**
   - a) A sequence of keys to access nested dictionary values
   - b) The output value
   - c) The expected result
   - d) The function being tested

4. **What does the `str(context.exception)` expression return?**
   - a) The type of the exception
   - b) The string representation of the exception message
   - c) The function output
   - d) The name of the test method

5. **Why is parameterization useful in unit testing?**
   - a) It makes tests faster
   - b) It reduces code duplication
   - c) It increases the number of test files
   - d) It eliminates the need for assertions

6. **What is tested by the `test_access_nested_map_exception` method?**
   - a) That the function returns correct values
   - b) That the function raises `KeyError` for invalid paths
   - c) That the function executes within a time limit
   - d) That the function can access all keys

7. **What is the expected result of accessing `nested_map` with a non-existent key?**
   - a) A default value
   - b) An empty dictionary
   - c) A `KeyError`
   - d) A `ValueError`

8. **Which of the following test cases would raise a `KeyError`?**
   - a) ({"a": 1}, ("a",), 1)
   - b) ({"a": {"b": 2}}, ("a", "b"), 2)
   - c) ({}, ("a",), KeyError)
   - d) ({"a": {"b": 2}}, ("a",), {"b": 2})

9. **What does the `path[-1]` expression represent in the test?**
   - a) The first key in the path
   - b) The last key in the path
   - c) The full path as a string
   - d) The length of the path

10. **How many lines of code should the body of the `test_access_nested_map_exception` method be, according to the task?**
    - a) No more than 1 line
    - b) No more than 2 lines
    - c) No more than 5 lines
    - d) No more than 10 lines

### Answers

1. b) Tests that a specific exception is raised
2. b) @parameterized.expand
3. a) A sequence of keys to access nested dictionary values
4. b) The string representation of the exception message
5. b) It reduces code duplication
6. b) That the function raises `KeyError` for invalid paths
7. c) A `KeyError`
8. c) ({}, ("a",), KeyError)
9. b) The last key in the path
10. b) No more than 2 lines

# Mocking HTTP Calls in Unit Tests

## Introduction

When testing functions that make HTTP requests, it's essential to ensure the tests don't rely on actual external services. Mocking HTTP calls allows you to simulate responses and test how your function handles different scenarios without making real network requests. This approach makes tests faster and more reliable.

In this note, we'll focus on mocking HTTP calls for the `utils.get_json` function. We'll use `unittest.mock.patch` to replace `requests.get` with a mock object that simulates various responses.

---

## `utils.get_json` Function

The `utils.get_json` function retrieves JSON data from a specified URL. Typically, it makes an HTTP GET request and returns the JSON response.

### Example Function Definition
```python
import requests

def get_json(url):
    response = requests.get(url)
    return response.json()
```

---

## Writing the Test Class

We'll create a test class `TestGetJson` that inherits from `unittest.TestCase`. Inside this class, we'll write a method `test_get_json` decorated with `@parameterized.expand` to test multiple scenarios using mocked HTTP responses.

### Step-by-Step Implementation

1. **Import Required Modules**:
   ```python
   import unittest
   from unittest.mock import patch, Mock
   from parameterized import parameterized
   from utils import get_json
   ```

2. **Define the Test Class with Mocking**:
   ```python
   class TestGetJson(unittest.TestCase):
       @parameterized.expand([
           ("http://example.com", {"payload": True}),
           ("http://holberton.io", {"payload": False})
       ])
       @patch('utils.requests.get')
       def test_get_json(self, test_url, test_payload, mock_get):
           # Create a mock response object with a json method
           mock_response = Mock()
           mock_response.json.return_value = test_payload
           
           # Set the mock object to be returned by requests.get
           mock_get.return_value = mock_response
           
           # Call the function and verify the result
           result = get_json(test_url)
           self.assertEqual(result, test_payload)
           
           # Ensure requests.get was called exactly once with the test URL
           mock_get.assert_called_once_with(test_url)

   if __name__ == '__main__':
       unittest.main()
   ```

### Explanation

- **Mocking `requests.get`**:
  - We use `@patch('utils.requests.get')` to replace `requests.get` with a mock object. This prevents actual HTTP requests and allows us to simulate responses.
- **Creating Mock Response**:
  - `Mock()` creates a mock object, and we set its `json` method to return `test_payload`.
- **Testing Function Output**:
  - We call `get_json(test_url)` and use `self.assertEqual(result, test_payload)` to verify that it returns the expected payload.
- **Verifying HTTP Call**:
  - `mock_get.assert_called_once_with(test_url)` checks that `requests.get` was called exactly once with `test_url`.

### Application in Real-World Projects

Mocking HTTP calls is essential for testing functions that interact with APIs or external services. It allows developers to:
- **Isolate Tests**: Ensure that tests do not depend on external systems or network conditions.
- **Test Edge Cases**: Simulate various responses, including errors, without requiring real endpoints.
- **Improve Test Performance**: Run tests faster since no actual network communication is involved.

---

## End-of-Chapter Quiz

1. **What does mocking an HTTP call allow you to do in unit tests?**
   - a) Perform real network requests
   - b) Simulate HTTP responses without making actual requests
   - c) Reduce the need for parameterization
   - d) Increase the complexity of tests

2. **Which module is used to mock HTTP calls in the provided example?**
   - a) requests
   - b) unittest.mock
   - c) json
   - d) parameterized

3. **In the provided test, what does `mock_get.return_value` represent?**
   - a) The actual HTTP response
   - b) The expected output of `get_json`
   - c) A mock response object
   - d) The test URL

4. **What does the `@patch('utils.requests.get')` decorator do?**
   - a) Replaces the `get_json` function with a mock
   - b) Replaces `requests.get` with a mock
   - c) Modifies the `test_get_json` method
   - d) Configures the mock response object

5. **Why is it important to mock HTTP calls in unit tests?**
   - a) To make tests faster
   - b) To verify that the actual API works
   - c) To avoid writing assertions
   - d) To increase the number of test cases

6. **What does the `mock_response.json.return_value` line do?**
   - a) Sets up the mock response to return a specific JSON payload
   - b) Calls the actual API
   - c) Retrieves the JSON payload from the test URL
   - d) Creates a new test URL

7. **Which method checks if the mock was called with specific arguments?**
   - a) assertEqual
   - b) assert_called_once_with
   - c) assertTrue
   - d) assertRaises

8. **What is the purpose of the `@parameterized.expand` decorator in the test?**
   - a) To mock HTTP responses
   - b) To run the test method with multiple sets of inputs
   - c) To create mock objects
   - d) To modify the function being tested

9. **Which of the following is a valid test case for `get_json`?**
   - a) ("http://example.com", {"payload": True})
   - b) ("http://example.com", {"payload": True}, "http://holberton.io")
   - c) ({"payload": True}, "http://example.com")
   - d) ("http://example.com", {"payload": True}, KeyError)

10. **How many times should `requests.get` be called per input in the test?**
    - a) Twice
    - b) Once
    - c) Three times
    - d) Zero times

### Answers

1. b) Simulate HTTP responses without making actual requests
2. b) unittest.mock
3. c) A mock response object
4. b) Replaces `requests.get` with a mock
5. a) To make tests faster
6. a) Sets up the mock response to return a specific JSON payload
7. b) assert_called_once_with
8. b) To run the test method with multiple sets of inputs
9. a) ("http://example.com", {"payload": True})
10. b) Once

# Parameterize and Patch Tests with `memoize`

## Introduction

Memoization is an optimization technique used to cache the results of expensive function calls and reuse the cached result when the same inputs occur again. This can significantly improve performance, especially for functions that are called frequently with the same arguments.

In this note, we'll explore how to test a memoized property using parameterization and patching. We'll focus on ensuring that the memoized property returns the correct result and that the underlying method is called only once, even when the property is accessed multiple times.

---

## `utils.memoize` Decorator

The `utils.memoize` decorator caches the result of a method so that subsequent calls to the method with the same arguments return the cached result instead of recomputing it.

### Example Implementation of `memoize`
```python
def memoize(fn):
    cache = {}
    def memoized_fn(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoized_fn
```

---

## Writing the Test Class

We'll create a test class `TestMemoize` that inherits from `unittest.TestCase`. Inside this class, we'll write a method `test_memoize` to test the memoization behavior.

### Step-by-Step Implementation

1. **Import Required Modules**:
   ```python
   import unittest
   from unittest.mock import patch
   from utils import memoize
   ```

2. **Define the Test Class and Mocking**:
   ```python
   class TestMemoize(unittest.TestCase):
       def test_memoize(self):
           # Define a test class to demonstrate memoization
           class TestClass:
               def a_method(self):
                   return 42

               @memoize
               def a_property(self):
                   return self.a_method()

           # Create an instance of the test class
           test_instance = TestClass()

           # Patch the a_method to track calls
           with patch.object(test_instance, 'a_method', wraps=test_instance.a_method) as mock_method:
               # Call the memoized property twice
               result1 = test_instance.a_property()
               result2 = test_instance.a_property()

               # Check the results
               self.assertEqual(result1, 42)
               self.assertEqual(result2, 42)

               # Ensure a_method was called only once
               mock_method.assert_called_once()

   if __name__ == '__main__':
       unittest.main()
   ```

### Explanation

- **Test Class and Memoization**:
  - `TestClass` defines a method `a_method` and a memoized property `a_property`.
  - The `memoize` decorator ensures that `a_property` caches the result of `a_method`.
- **Mocking the Method**:
  - `patch.object` is used to wrap `test_instance.a_method`, allowing us to track how many times it is called.
- **Testing Memoization**:
  - `test_instance.a_property()` is called twice.
  - We verify that `a_property` returns the correct result and that `a_method` is called only once.

### Application in Real-World Projects

Memoization is particularly useful for:
- **Optimizing Performance**: Reducing redundant calculations by caching results.
- **Expensive Operations**: Caching results of database queries or complex computations to avoid repeated execution.
- **Improving Efficiency**: Enhancing the efficiency of frequently called functions or methods.

---

## End-of-Chapter Quiz

1. **What is the purpose of memoization in programming?**
   - a) To write more complex code
   - b) To cache function results for faster access
   - c) To simplify function arguments
   - d) To increase the frequency of function calls

2. **What does the `memoize` decorator do in the provided example?**
   - a) Logs all function calls
   - b) Caches the function results
   - c) Modifies the function's return type
   - d) Changes the function signature

3. **Which module is used to mock a method in the provided test?**
   - a) requests
   - b) unittest.mock
   - c) functools
   - d) parameterized

4. **In the provided test, what is `patch.object` used for?**
   - a) To replace the memoize decorator
   - b) To mock the return value of `a_property`
   - c) To wrap and track calls to `a_method`
   - d) To create a new instance of `TestClass`

5. **What is verified by `mock_method.assert_called_once()`?**
   - a) That `a_property` was called twice
   - b) That `a_method` was called only once
   - c) That `a_method` was never called
   - d) That the `memoize` decorator was applied correctly

6. **What does `self.assertEqual(result1, 42)` check in the test?**
   - a) That `a_method` returns 42
   - b) That `a_property` is not memoized
   - c) That `a_property` returns the cached result
   - d) That `result1` is a string

7. **Why is the `memoize` decorator useful in real-world projects?**
   - a) To add additional functionality to functions
   - b) To reduce the number of unit tests
   - c) To optimize performance by avoiding redundant calculations
   - d) To increase the complexity of code

8. **What does the `*args` argument in `memoized_fn(*args)` allow for?**
   - a) Only positional arguments
   - b) Only keyword arguments
   - c) Both positional and keyword arguments
   - d) No arguments at all

9. **How many times should `a_property` be called in the test?**
   - a) Never
   - b) Once
   - c) Twice
   - d) Three times

10. **Which part of the test demonstrates the effectiveness of memoization?**
    - a) Defining the `TestClass`
    - b) Calling `a_method`
    - c) Using `patch.object`
    - d) Verifying that `a_method` is called only once when accessing `a_property` multiple times

### Answers

1. b) To cache function results for faster access
2. b) Caches the function results
3. b) unittest.mock
4. c) To wrap and track calls to `a_method`
5. b) That `a_method` was called only once
6. c) That `a_property` returns the cached result
7. c) To optimize performance by avoiding redundant calculations
8. c) Both positional and keyword arguments
9. c) Twice
10. d) Verifying that `a_method` is called only once when accessing `a_property` multiple times

# Parameterize and Patch as Decorators in Unit Testing

## Introduction

When testing classes and methods that interact with external services or APIs, it's crucial to ensure that tests don't depend on actual network calls. This is achieved by mocking such interactions. Using decorators like `@patch` and `@parameterized.expand`, we can simulate different scenarios and verify the functionality without making real HTTP requests.

In this note, we'll focus on testing the `GithubOrgClient` class, specifically the `org` method. We'll use `@patch` to mock HTTP calls and `@parameterized.expand` to test multiple cases.

---

## `client.GithubOrgClient` Class

The `GithubOrgClient` class is designed to interact with GitHub’s API, particularly to retrieve information about GitHub organizations.

### Example Implementation
```python
import requests

class GithubOrgClient:
    BASE_URL = "https://api.github.com/orgs/"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        url = f"{self.BASE_URL}{self.org_name}"
        return self.get_json(url)

    @staticmethod
    def get_json(url):
        response = requests.get(url)
        return response.json()
```

---

## Writing the Test Class

We'll create a test class `TestGithubOrgClient` that inherits from `unittest.TestCase`. Inside this class, we'll write a method `test_org` decorated with `@parameterized.expand` to test multiple organizations and `@patch` to mock the `get_json` method.

### Step-by-Step Implementation

1. **Import Required Modules**:
   ```python
   import unittest
   from unittest.mock import patch, Mock
   from parameterized import parameterized
   from client import GithubOrgClient
   ```

2. **Define the Test Class with Parameterized and Patching**:
   ```python
   class TestGithubOrgClient(unittest.TestCase):
       @parameterized.expand([
           ("google", {"login": "google"}),
           ("abc", {"login": "abc"})
       ])
       @patch('client.GithubOrgClient.get_json')
       def test_org(self, org_name, expected_response, mock_get_json):
           # Configure the mock to return the expected response
           mock_get_json.return_value = expected_response

           # Create an instance of GithubOrgClient
           client = GithubOrgClient(org_name)
           
           # Call the org method
           result = client.org()

           # Check the result
           self.assertEqual(result, expected_response)

           # Verify get_json was called with the correct URL
           expected_url = f"https://api.github.com/orgs/{org_name}"
           mock_get_json.assert_called_once_with(expected_url)

   if __name__ == '__main__':
       unittest.main()
   ```

### Explanation

- **Parameterized Tests**:
  - `@parameterized.expand` allows us to run `test_org` with different `org_name` and `expected_response` values.
- **Mocking the Method**:
  - `@patch('client.GithubOrgClient.get_json')` replaces `get_json` with a mock, preventing actual HTTP calls.
- **Configuring the Mock**:
  - `mock_get_json.return_value = expected_response` sets the mock's return value to simulate different responses.
- **Testing `org` Method**:
  - We create a `GithubOrgClient` instance and call `org()`, then compare the result to the expected response.
- **Verifying URL**:
  - `mock_get_json.assert_called_once_with(expected_url)` ensures `get_json` was called with the correct URL.

### Application in Real-World Projects

Using decorators like `@patch` and `@parameterized.expand` is essential for:
- **Mocking External Dependencies**: Simulating API responses without making real network requests.
- **Testing Multiple Scenarios**: Easily running tests with different inputs and expected outputs.
- **Isolating Tests**: Ensuring tests do not depend on external services, making them more reliable and faster.

---

## End-of-Chapter Quiz

1. **What is the main purpose of using `@patch` in unit tests?**
   - a) To run tests faster
   - b) To modify function signatures
   - c) To mock external dependencies
   - d) To change the return type of functions

2. **Which method in the `GithubOrgClient` class is being mocked in the test?**
   - a) org
   - b) __init__
   - c) get_json
   - d) requests.get

3. **What does `@parameterized.expand` help with in the provided test?**
   - a) Mocking HTTP calls
   - b) Running the test with multiple sets of inputs
   - c) Changing the class definition
   - d) Increasing the test coverage

4. **What argument does `mock_get_json.assert_called_once_with(expected_url)` verify?**
   - a) That `get_json` was called twice
   - b) That `get_json` was called with the expected URL
   - c) That `org` was called with the expected URL
   - d) That `org` returns the correct value

5. **In the test, what is `mock_get_json.return_value` used for?**
   - a) To verify the expected output
   - b) To set the return value of the `org` method
   - c) To configure the mock to return the expected response
   - d) To change the URL used in the HTTP call

6. **Why is `@patch('client.GithubOrgClient.get_json')` used in the test?**
   - a) To replace `get_json` with a mock object
   - b) To modify the `org` method
   - c) To change the base URL
   - d) To cache the results

7. **What does `client.org()` return in the test?**
   - a) The actual response from the GitHub API
   - b) The value of `mock_get_json.return_value`
   - c) The organization name
   - d) The base URL

8. **Which of the following is an example of a parameterized input used in the test?**
   - a) ("http://example.com", {"payload": True})
   - b) ("google", {"login": "google"})
   - c) ({"payload": True}, "google")
   - d) ("github", "login")

9. **What is verified by `self.assertEqual(result, expected_response)` in the test?**
   - a) That the `org` method returns the expected organization information
   - b) That `mock_get_json` returns the expected URL
   - c) That `org` was called once
   - d) That `get_json` was called with the correct URL

10. **How many times should `get_json` be called for each parameterized input?**
    - a) Zero times
    - b) Once
    - c) Twice
    - d) Three times

### Answers

1. c) To mock external dependencies
2. c) get_json
3. b) Running the test with multiple sets of inputs
4. b) That `get_json` was called with the expected URL
5. c) To configure the mock to return the expected response
6. a) To replace `get_json` with a mock object
7. b) The value of `mock_get_json.return_value`
8. b) ("google", {"login": "google"})
9. a) That the `org` method returns the expected organization information
10. b) Once

# Mocking a property 

To effectively cover mocking a property, specifically `GithubOrgClient._public_repos_url`, we'll utilize the `patch` context manager from `unittest.mock`. This approach allows us to replace the behavior of dependencies temporarily during testing, ensuring that our tests are isolated and predictable.

### Understanding the Scenario

The `_public_repos_url` property in `GithubOrgClient` likely computes a URL based on some internal state or configuration. To test this property without relying on its actual dependencies, we'll mock those dependencies using `patch` and verify that `_public_repos_url` behaves as expected.

### Example Implementation

Here’s how you can implement the test:

```python
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        # Example known payload that GithubOrgClient.org returns
        known_payload = {
            "login": "example",
            "public_repos": 10,
            "repos_url": "https://api.github.com/orgs/example/repos"
        }
        
        # Mocking GithubOrgClient.org to return known_payload
        with patch.object(GithubOrgClient, 'org', return_value=known_payload):
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("example")
            
            # Access the mocked property _public_repos_url
            result = client._public_repos_url
            
            # Define the expected result based on known_payload
            expected_result = "https://api.github.com/orgs/example/repos"
            
            # Assert that the result matches the expected URL
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
```

### Explanation

- **Mocking with `patch`**: 
  - `patch.object(GithubOrgClient, 'org', return_value=known_payload)` mocks the `org` method of `GithubOrgClient` to return `known_payload` when called.
  
- **Testing `_public_repos_url`**:
  - `client._public_repos_url` accesses the mocked property `_public_repos_url` of `GithubOrgClient`.
  
- **Verification**:
  - `self.assertEqual(result, expected_result)` verifies that the result of `_public_repos_url` matches the expected URL from `known_payload`.

### Real-World Application

Mocking properties is crucial in unit testing scenarios where properties derive their values from complex calculations or external data sources:
- **Dependency Isolation**: Ensures tests focus solely on the behavior of the property without being affected by external factors.
- **Predictable Testing**: Provides control over the property’s output, allowing comprehensive testing of various scenarios.

---

## End-of-Chapter Quiz

1. **What is the primary purpose of mocking a property in unit testing?**
   - a) To modify the property's behavior permanently
   - b) To simulate the property's behavior without its dependencies
   - c) To increase the property's efficiency
   - d) To change the property's data type

2. **Which context manager is commonly used to mock properties in Python unittests?**
   - a) `unittest.mock.mock_property`
   - b) `unittest.mock.patch`
   - c) `unittest.mock.mock_object`
   - d) `unittest.mock.replace`

3. **What does `patch.object(GithubOrgClient, 'org', return_value=known_payload)` do in the provided test?**
   - a) Replaces the `GithubOrgClient` class with `known_payload`
   - b) Mocks the `org` method of `GithubOrgClient` to return `known_payload`
   - c) Deletes the `org` method from `GithubOrgClient`
   - d) Updates the `org` method in `GithubOrgClient` with `known_payload`

4. **Why is mocking `_public_repos_url` beneficial in unit testing?**
   - a) To increase the property's visibility
   - b) To simulate different return values from `GithubOrgClient.org`
   - c) To eliminate the need for `GithubOrgClient.org`
   - d) To reduce the number of unit tests required

5. **What is `client._public_repos_url` testing in the provided test?**
   - a) The `org` method of `GithubOrgClient`
   - b) The `_public_repos_url` property of `GithubOrgClient`
   - c) The `GithubOrgClient` class initialization
   - d) The `known_payload` data structure

6. **What does `self.assertEqual(result, expected_result)` verify in the test?**
   - a) That `known_payload` matches `expected_result`
   - b) That `_public_repos_url` returns the correct value based on `known_payload`
   - c) That `org` returns the correct URL for `GithubOrgClient`
   - d) That `client` is correctly initialized with `GithubOrgClient`

7. **In the provided test, what is `known_payload` used to represent?**
   - a) The `GithubOrgClient` instance
   - b) The expected result of `_public_repos_url`
   - c) The `org` method of `GithubOrgClient`
   - d) The `client` initialization

8. **How many times is `GithubOrgClient.org` called in the provided test?**
   - a) Zero times
   - b) Once
   - c) Twice
   - d) Three times

9. **What does `patch.object(GithubOrgClient, 'org', return_value=known_payload)` prevent in the test?**
   - a) The execution of `GithubOrgClient.org`
   - b) The creation of `known_payload`
   - c) The deletion of `GithubOrgClient`
   - d) The modification of `client`

10. **Which part of the test demonstrates the use of the `patch` context manager?**
    - a) Accessing `client._public_repos_url`
    - b) Creating `known_payload`
    - c) Initializing `GithubOrgClient`
    - d) Mocking `GithubOrgClient.org`

### Answers

1. b) To simulate the property's behavior without its dependencies
2. b) `unittest.mock.patch`
3. b) Mocks the `org` method of `GithubOrgClient` to return `known_payload`
4. b) To simulate different return values from `GithubOrgClient.org`
5. b) The `_public_repos_url` property of `GithubOrgClient`
6. b) That `_public_repos_url` returns the correct value based on `known_payload`
7. b) The expected result of `_public_repos_url`
8. b) Once
9. a) The execution of `GithubOrgClient.org`
10. d) Mocking `GithubOrgClient.org`

# More patching 

To effectively test the `GithubOrgClient.public_repos` method using mocking, we'll utilize both `@patch` as a decorator and `patch` as a context manager from `unittest.mock`. These techniques allow us to replace dependencies temporarily during testing and verify that our code behaves as expected without relying on external services.

### Understanding the Scenario

The `GithubOrgClient.public_repos` method likely retrieves a list of repositories associated with a GitHub organization. To test this method without making actual API calls, we'll mock both `get_json` (which fetches data from an external API) and `_public_repos_url` (which likely constructs the URL for fetching repositories).

### Example Implementation

Here’s how you can implement the test:

```python
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch('client.GithubOrgClient.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', return_value="https://api.github.com/orgs/example/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        # Example payload that get_json returns
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        
        # Mocking get_json to return payload
        mock_get_json.return_value = payload
        
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example")
        
        # Call the public_repos method
        repos = client.public_repos()
        
        # Define the expected result based on payload
        expected_repos = ["repo1", "repo2", "repo3"]
        
        # Assert that the result matches the expected list of repo names
        self.assertEqual(repos, expected_repos)
        
        # Verify that mock_get_json was called once
        mock_get_json.assert_called_once()
        
        # Verify that mock_public_repos_url was called once
        mock_public_repos_url.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

### Explanation

- **Mocking with `@patch` and `patch.object`**: 
  - `@patch('client.GithubOrgClient.get_json')` mocks the `get_json` method of `GithubOrgClient` to return `payload`.
  - `@patch.object(GithubOrgClient, '_public_repos_url', return_value="https://api.github.com/orgs/example/repos")` mocks the `_public_repos_url` property of `GithubOrgClient` to return a specific URL.
  
- **Testing `public_repos` Method**:
  - `client.public_repos()` calls the `public_repos` method of `GithubOrgClient`.
  
- **Verification**:
  - `self.assertEqual(repos, expected_repos)` ensures that the returned list of repository names matches the expected list.
  - `mock_get_json.assert_called_once()` verifies that `get_json` was called exactly once.
  - `mock_public_repos_url.assert_called_once()` verifies that `_public_repos_url` was called exactly once.

### Real-World Application

Testing methods like `public_repos` with mocked dependencies ensures:
- **Isolated Testing**: Ensures tests are independent of external services, making them faster and more reliable.
- **Behavior Verification**: Validates that the method returns the expected results based on different payloads.
- **Edge Case Testing**: Facilitates testing of various scenarios without relying on real API responses.

---

## End-of-Chapter Quiz

1. **What is the primary purpose of using `@patch` as a decorator in unit testing?**
   - a) To modify the behavior of the method being tested
   - b) To replace the implementation of the method being tested
   - c) To mock external dependencies temporarily
   - d) To enhance the performance of unit tests

2. **Which method in the `GithubOrgClient` class is being mocked in the provided test?**
   - a) public_repos
   - b) _public_repos_url
   - c) get_json
   - d) org

3. **What does `@patch.object(GithubOrgClient, '_public_repos_url', return_value="https://api.github.com/orgs/example/repos")` do in the test?**
   - a) Replaces the `GithubOrgClient` class with `https://api.github.com/orgs/example/repos`
   - b) Mocks the `_public_repos_url` property of `GithubOrgClient` to return `"https://api.github.com/orgs/example/repos"`
   - c) Deletes the `_public_repos_url` property from `GithubOrgClient`
   - d) Updates the `_public_repos_url` property in `GithubOrgClient` with `"https://api.github.com/orgs/example/repos"`

4. **Why is mocking `_public_repos_url` beneficial in unit testing?**
   - a) To increase the property's visibility
   - b) To simulate different return values from `GithubOrgClient.get_json`
   - c) To eliminate the need for `GithubOrgClient.get_json`
   - d) To reduce the number of unit tests required

5. **What is `client.public_repos()` testing in the provided test?**
   - a) The `_public_repos_url` property of `GithubOrgClient`
   - b) The `public_repos` method of `GithubOrgClient`
   - c) The initialization of `client` with `GithubOrgClient`
   - d) The `get_json` method of `GithubOrgClient`

6. **What does `self.assertEqual(repos, expected_repos)` verify in the test?**
   - a) That `get_json` returns the correct value based on `payload`
   - b) That `_public_repos_url` returns the correct value based on `payload`
   - c) That `public_repos` returns the correct list of repository names based on `payload`
   - d) That `client` is correctly initialized with `GithubOrgClient`

7. **In the provided test, what is `payload` used to represent?**
   - a) The `GithubOrgClient` instance
   - b) The expected result of `public_repos`
   - c) The `_public_repos_url` property of `GithubOrgClient`
   - d) The `client` initialization

8. **How many times is `GithubOrgClient.get_json` called in the provided test?**
   - a) Zero times
   - b) Once
   - c) Twice
   - d) Three times

9. **What does `patch('client.GithubOrgClient.get_json')` prevent in the test?**
   - a) The execution of `GithubOrgClient.get_json`
   - b) The creation of `payload`
   - c) The deletion of `GithubOrgClient`
   - d) The modification of `client`

10. **Which part of the test demonstrates the use of `patch` as a decorator?**
    - a) Accessing `client.public_repos()`
    - b) Creating `payload`
    - c) Initializing `GithubOrgClient`
    - d) Mocking `GithubOrgClient.get_json`

### Answers

1. c) To mock external dependencies temporarily
2. c) get_json
3. b) Mocks the `_public_repos_url` property of `GithubOrgClient` to return `"https://api.github.com/orgs/example/repos"`
4. b) To simulate different return values from `GithubOrgClient.get_json`
5. b) The `public_repos` method of `GithubOrgClient`
6. c) That `public_repos` returns the correct list of repository names based on `payload`
7. b) The expected result of `public_repos`
8. b) Once
9. a) The execution of `GithubOrgClient.get_json`
10. d) Mocking `GithubOrgClient.get_json`

# Parameterize 

To effectively test the `GithubOrgClient.has_license` method using parameterization, we'll create a unit test that checks if a repository has a specific license key. This involves setting up different inputs and expected outputs to validate the method's behavior.

### Example Implementation

Here’s how you can implement the test using parameterization:

```python
import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch.object(GithubOrgClient, 'get_json')
    def test_has_license(self, mock_get_json):
        # Parametrize inputs
        test_inputs = [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]
        
        for repo_data, license_key, expected_result in test_inputs:
            # Mock get_json to return repo_data for each iteration
            mock_get_json.return_value = repo_data
            
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("example")
            
            # Call has_license method with license_key
            result = client.has_license(license_key)
            
            # Assert that the result matches the expected outcome
            self.assertEqual(result, expected_result)
            
            # Verify that get_json was called exactly once
            mock_get_json.assert_called_once()
            
            # Reset mock for the next iteration
            mock_get_json.reset_mock()

if __name__ == '__main__':
    unittest.main()
```

### Explanation

- **Mocking with `@patch.object`**: 
  - `@patch.object(GithubOrgClient, 'get_json')` mocks the `get_json` method of `GithubOrgClient` to return different `repo_data` for each test case.

- **Parameterization**:
  - `test_inputs` is a list of tuples where each tuple contains `repo_data`, `license_key`, and `expected_result`.
  - `repo_data` simulates the response from `get_json` for each test case.
  - `license_key` is the input parameter for `has_license`.
  - `expected_result` is the expected output of `has_license` for each test case.

- **Testing `has_license` Method**:
  - `client.has_license(license_key)` calls the `has_license` method of `GithubOrgClient`.

- **Verification**:
  - `self.assertEqual(result, expected_result)` ensures that the returned result from `has_license` matches the expected outcome for each test case.
  - `mock_get_json.assert_called_once()` verifies that `get_json` was called exactly once during each test iteration.
  - `mock_get_json.reset_mock()` resets the mock to prepare it for the next test case iteration.

### Real-World Application

Testing `has_license` with different inputs and expected outputs ensures:
- **Coverage**: Different scenarios are tested, ensuring the method works correctly across various conditions.
- **Validation**: The method's logic is validated without relying on real data from external sources.
- **Efficiency**: Tests run quickly since they don't make actual API calls or interact with external systems.

---

## End-of-Chapter Quiz

1. **What is the primary purpose of parameterizing a unit test?**
   - a) To modify the behavior of the method being tested
   - b) To replace the implementation of the method being tested
   - c) To test a method with multiple inputs and expected outputs
   - d) To enhance the performance of unit tests

2. **What does `@patch.object(GithubOrgClient, 'get_json')` do in the test?**
   - a) Mocks the `GithubOrgClient` class
   - b) Mocks the `get_json` method of `GithubOrgClient`
   - c) Deletes the `get_json` method from `GithubOrgClient`
   - d) Calls the `get_json` method of `GithubOrgClient`

3. **Why is `mock_get_json.assert_called_once()` used in the test?**
   - a) To ensure `get_json` is called exactly once per test case
   - b) To reset `get_json` after each test case
   - c) To modify the behavior of `get_json`
   - d) To enhance the performance of the test

4. **In the provided parameterization, what is `repo_data` used to simulate?**
   - a) The `GithubOrgClient` instance
   - b) The expected result of `has_license`
   - c) The `_public_repos_url` property of `GithubOrgClient`
   - d) The response from `get_json`

5. **What does `mock_get_json.reset_mock()` do in the test?**
   - a) Resets the `GithubOrgClient` class
   - b) Resets the `get_json` method of `GithubOrgClient`
   - c) Calls `get_json` again
   - d) Deletes `get_json` from `GithubOrgClient`

6. **What is `test_inputs` used for in the test?**
   - a) To initialize `GithubOrgClient`
   - b) To parametrize inputs and expected outputs for `has_license`
   - c) To call `has_license` with different arguments
   - d) To mock `get_json` with different responses

7. **How many times is `GithubOrgClient.get_json` called in each iteration of the test?**
   - a) Zero times
   - b) Once
   - c) Twice
   - d) Three times

8. **What does `self.assertEqual(result, expected_result)` verify in the test?**
   - a) That `get_json` returns the correct value based on `repo_data`
   - b) That `has_license` returns the correct value based on `repo_data`
   - c) That `_public_repos_url` returns the correct value based on `repo_data`
   - d) That `client` is correctly initialized with `GithubOrgClient`

9. **Which part of the test demonstrates the use of `@patch.object`?**
   - a) Accessing `client.has_license(license_key)`
   - b) Creating `test_inputs`
   - c) Initializing `GithubOrgClient`
   - d) Mocking `get_json` with different responses

10. **What is the purpose of parameterizing `test_inputs` in the provided test?**
    - a) To modify the behavior of `has_license`
    - b) To replace the implementation of `has_license`
    - c) To test `has_license` with multiple inputs and expected outputs
    - d) To enhance the performance of `has_license`

### Answers

1. c) To test a method with multiple inputs and expected outputs
2. b) Mocks the `get_json` method of `GithubOrgClient`
3. a) To ensure `get_json` is called exactly once per test case
4. d) The response from `get_json`
5. b) Resets the `get_json` method of `GithubOrgClient`
6. b) To parametrize inputs and expected outputs for `has_license`
7. b) Once
8. b) That `has_license` returns the correct value based on `repo_data`
9. d) Mocking `get_json` with different responses
10. c) To test `has_license` with multiple inputs and expected outputs

# Integration test: fixtures 

To prepare for an integration test of the `GithubOrgClient.public_repos` method using fixtures and mocking external requests, we'll set up the test environment to simulate real-world scenarios without actually making external API calls. Here’s how you can implement it:

### Example Implementation

```python
import unittest
from unittest.mock import patch, Mock
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient

class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mock requests.get to return example payloads from fixtures
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect to return appropriate fixture based on URL
        def mock_requests_get(url):
            if url == 'https://api.github.com/orgs/testorg':
                return Mock(json=lambda: org_payload)
            elif url == 'https://api.github.com/orgs/testorg/repos':
                return Mock(json=lambda: repos_payload)
            else:
                return Mock(json=lambda: [])
        
        cls.mock_get.side_effect = mock_requests_get

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher after tests are done
        cls.get_patcher.stop()

    @parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                         [(org_payload, repos_payload, expected_repos, apache2_repos)])
    def test_public_repos(self):
        # Initialize GithubOrgClient with 'testorg'
        client = GithubOrgClient('testorg')

        # Call public_repos method
        repos = client.public_repos()

        # Assert that the returned repos match expected_repos
        self.assertEqual(repos, expected_repos)

if __name__ == '__main__':
    unittest.main()
```

### Explanation

- **`setUpClass` Method**:
  - `setUpClass` is a class method in `unittest.TestCase` that is called before any tests in the class are run. Here, it sets up the mocking of `requests.get` to return predefined payloads from `fixtures.py`.
  - `patch('requests.get')` creates a patcher that mocks `requests.get` method.
  - `mock_requests_get` function defines the behavior of the mock:
    - It returns `org_payload` when `requests.get` is called with `'https://api.github.com/orgs/testorg'`.
    - It returns `repos_payload` when called with `'https://api.github.com/orgs/testorg/repos'`.
    - Returns an empty list otherwise.
  - `cls.mock_get.side_effect = mock_requests_get` assigns `mock_requests_get` as the side effect of `cls.mock_get`.

- **`tearDownClass` Method**:
  - `tearDownClass` stops the `get_patcher` patcher after all tests in the class have run, ensuring cleanup.

- **`test_public_repos` Method**:
  - `@parameterized_class` decorates the class to parameterize it with fixtures:
    - `org_payload`: Payload returned for organization data.
    - `repos_payload`: Payload returned for repositories data.
    - `expected_repos`: Expected list of repositories from `public_repos` method.
    - `apache2_repos`: Example of repositories with Apache 2 license.
  - Inside `test_public_repos`, it initializes `GithubOrgClient` with `'testorg'`.
  - Calls `public_repos` method to retrieve repositories.
  - Asserts that the retrieved repositories match `expected_repos`.

### Real-World Application

- **Integration Testing**: Tests `GithubOrgClient.public_repos` method in a realistic scenario by mocking external requests.
- **Fixture Usage**: Uses predefined fixtures (`org_payload`, `repos_payload`, etc.) to simulate API responses.
- **Scalability**: Easily scales to test different scenarios by adding more fixtures or modifying existing ones in `fixtures.py`.

---

## End-of-Chapter Quiz

1. **What is the purpose of using `@parameterized_class` in the provided test?**
   - a) To parameterize individual test methods
   - b) To parameterize the entire test class
   - c) To mock external requests
   - d) To simulate API responses

2. **What does `setUpClass` method do in the test class?**
   - a) Starts the patcher for `requests.get`
   - b) Stops the patcher for `requests.get`
   - c) Initializes `GithubOrgClient` instance
   - d) Asserts the returned repositories

3. **Why is `tearDownClass` method used in the test class?**
   - a) To initialize `GithubOrgClient` instance
   - b) To assert the returned repositories
   - c) To stop the patcher for `requests.get`
   - d) To mock `requests.get` method

4. **Which method defines the behavior of mocked `requests.get` in the test?**
   - a) `test_public_repos`
   - b) `setUpClass`
   - c) `mock_requests_get`
   - d) `tearDownClass`

5. **What does `cls.mock_get.side_effect = mock_requests_get` do in the test?**
   - a) Initializes `GithubOrgClient` instance
   - b) Asserts the returned repositories
   - c) Defines behavior of `requests.get`
   - d) Stops the patcher for `requests.get`

6. **How many times is `requests.get` called during each test iteration?**
   - a) Zero times
   - b) Once
   - c) Twice
   - d) Thrice

7. **What is the primary purpose of using `@parameterized_class` decorator in the test?**
   - a) To replace the implementation of `public_repos`
   - b) To enhance the performance of the test
   - c) To test `public_repos` with multiple input data
   - d) To mock external API calls

8. **Which file contains the predefined fixtures used in the test?**
   - a) `client.py`
   - b) `test_integration.py`
   - c) `fixtures.py`
   - d) `test_fixtures.py`

9. **What is `org_payload` used to simulate in the test?**
   - a) The expected result of `public_repos`
   - b) The `GithubOrgClient` instance
   - c) The behavior of `requests.get`
   - d) The response from `public_repos`

10. **What is the expected outcome of running the provided test?**
    - a) To verify the behavior of `requests.get`
    - b) To ensure `public_repos` returns the correct repositories
    - c) To mock external API calls
    - d) To initialize `GithubOrgClient` instance

### Answers

1. b) To parameterize the entire test class
2. a) Starts the patcher for `requests.get`
3. c) To stop the patcher for `requests.get`
4. c) `mock_requests_get`
5. c) Defines behavior of `requests.get`
6. c) Twice
7. c) To test `public_repos` with multiple input data
8. c) `fixtures.py`
9. d) The response from `public_repos`
10. b) To ensure `public_repos` returns the correct repositories

# Integration tests

## Integration Tests

Integration tests ensure that different pieces of an application work together as expected. For testing `GithubOrgClient.public_repos`, we need to verify that it integrates correctly with external data sources, but without making real HTTP requests. Instead, we use fixtures to simulate responses.

### Example Implementation

### Fixtures
We'll use predefined fixtures to simulate external API responses. Assume these are defined in `fixtures.py`:

```python
# fixtures.py

org_payload = {"login": "testorg", "id": 1}
repos_payload = [
    {"name": "repo1", "license": {"key": "apache-2.0"}},
    {"name": "repo2", "license": {"key": "mit"}},
    {"name": "repo3", "license": {"key": "apache-2.0"}}
]
expected_repos = ["repo1", "repo2", "repo3"]
apache2_repos = ["repo1", "repo3"]
```

### Integration Test Implementation

We'll create a test class to test `GithubOrgClient.public_repos` and `GithubOrgClient.public_repos` with license filtering.

```python
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient

class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect to return appropriate fixture based on URL
        def mock_requests_get(url):
            if url == 'https://api.github.com/orgs/testorg':
                return Mock(json=lambda: org_payload)
            elif url == 'https://api.github.com/orgs/testorg/repos':
                return Mock(json=lambda: repos_payload)
            return Mock(json=lambda: [])
        
        cls.mock_get.side_effect = mock_requests_get

    @classmethod
    def tearDownClass(cls):
        """Stop the mock."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method without filtering by license."""
        client = GithubOrgClient('testorg')
        repos = client.public_repos()
        self.assertEqual(repos, expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method filtering by 'apache-2.0' license."""
        client = GithubOrgClient('testorg')
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, apache2_repos)

if __name__ == '__main__':
    unittest.main()
```

### Explanation

- **`setUpClass` Method**:
  - Mocks `requests.get` to return fixtures based on the URL.
  - The `mock_requests_get` function uses `side_effect` to simulate different API responses:
    - Returns `org_payload` for the organization data.
    - Returns `repos_payload` for the repositories list.
    - Returns an empty list for other URLs.

- **`tearDownClass` Method**:
  - Stops the patcher for `requests.get` after the tests complete.

- **`test_public_repos` Method**:
  - Tests `public_repos` method without any filtering.
  - Checks if the method returns the complete list of repositories as expected.

- **`test_public_repos_with_license` Method**:
  - Tests `public_repos` method with a license filter (`license="apache-2.0"`).
  - Ensures only repositories with the specified license are returned.

### Real-World Application

- **Testing Integration**: Ensures `public_repos` integrates correctly with the GitHub API.
- **Simulating Real Data**: Uses fixtures to simulate real responses, helping verify the method's behavior under different scenarios.
- **Efficiency**: Prevents making actual HTTP requests, speeding up tests and avoiding API rate limits.

---

## End-of-Chapter Quiz

1. **What does the `setUpClass` method do in the test class?**
   - a) Initializes the `GithubOrgClient` instance
   - b) Stops the patcher for `requests.get`
   - c) Mocks `requests.get` to return predefined payloads
   - d) Tests the `public_repos` method

2. **What URL is used to mock the organization data response?**
   - a) `'https://api.github.com/orgs/testorg/repos'`
   - b) `'https://api.github.com/orgs/testorg'`
   - c) `'https://api.github.com/repos'`
   - d) `'https://api.github.com/orgs'`

3. **Which method is tested by `test_public_repos`?**
   - a) `public_repos` with a license filter
   - b) `requests.get`
   - c) `public_repos` without any filter
   - d) `setUpClass`

4. **What does the `tearDownClass` method do?**
   - a) Starts the patcher for `requests.get`
   - b) Stops the patcher for `requests.get`
   - c) Asserts the returned repositories
   - d) Mocks `requests.get`

5. **What does `client.public_repos(license="apache-2.0")` do in the test?**
   - a) Returns all repositories without filtering
   - b) Returns repositories with MIT license
   - c) Returns repositories with Apache 2.0 license
   - d) Returns repositories with no license

6. **How is the side effect of `requests.get` defined in the test?**
   - a) By patching `requests.post`
   - b) By defining `mock_requests_get`
   - c) By using `tearDownClass`
   - d) By calling `public_repos`

7. **Which fixture is used to simulate the repository data response?**
   - a) `org_payload`
   - b) `repos_payload`
   - c) `expected_repos`
   - d) `apache2_repos`

8. **What is the expected output of `test_public_repos_with_license`?**
   - a) All repositories
   - b) Repositories with Apache 2.0 license
   - c) Repositories with no license
   - d) Repositories with MIT license

9. **What is checked by `self.assertEqual(repos, apache2_repos)`?**
   - a) That `public_repos` returns no repositories
   - b) That `public_repos` returns all repositories
   - c) That `public_repos` returns repositories with Apache 2.0 license
   - d) That `public_repos` returns repositories with no license

10. **What does the `patch` decorator do in the test?**
    - a) Stops the patcher for `requests.get`
    - b) Defines the side effect for `requests.get`
    - c) Mocks `requests.get` method
    - d) Tests `public_repos` method

### Answers

1. c) Mocks `requests.get` to return predefined payloads
2. b) `'https://api.github.com/orgs/testorg'`
3. c) `public_repos` without any filter
4. b) Stops the patcher for `requests.get`
5. c) Returns repositories with Apache 2.0 license
6. b) By defining `mock_requests_get`
7. b) `repos_payload`
8. b) Repositories with Apache 2.0 license
9. c) That `public_repos` returns repositories with Apache 2.0 license
10. c) Mocks `requests.get` method
