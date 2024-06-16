# Python Type Annotations and Validation with mypy

## Introduction

Python 3 introduced type annotations, which allow developers to specify the expected types of function parameters and return values. This feature enhances code readability and helps catch type-related errors at runtime. Additionally, tools like mypy can be used to validate the type annotations and ensure that the code adheres to the specified types. This note will cover the basics of type annotations, how to use them to specify function signatures and variable types, and how to validate your code with mypy.

# Type Annotations in Python 3

Type annotations in Python allow you to specify the types of variables, function parameters, and return values. They improve code readability and help catch errors early in development. Although Python remains dynamically typed, these annotations help tools like linters and IDEs provide better support and early detection of potential issues.

## 1. Introduction to Type Annotations

### 1.1 What are Type Annotations?

Type annotations provide a way to indicate what types a function or variable is expected to handle. For example, if a function is meant to receive an integer and return a string, annotations can make this clear.

Here's a simple example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example:
- `name: str` means the `name` parameter should be a string.
- `-> str` indicates the function returns a string.

### 1.2 Basic Syntax

Type annotations use a colon (`:`) to specify the type of a variable or parameter, and an arrow (`->`) to indicate the return type of a function.

- **Variables**:
  ```python
  age: int = 25
  name: str = "Alice"
  ```
- **Function Parameters**:
  ```python
  def increment(x: int) -> int:
      return x + 1
  ```

### 1.3 Benefits of Type Annotations

- **Improved Readability**: Makes it clear what types are expected.
- **Error Detection**: Tools can catch type-related errors before runtime.
- **Documentation**: Serves as in-line documentation for developers.

## 2. Applying Type Annotations in Real-World Projects

### 2.1 Data Processing Example

Let's consider a function that processes a list of numbers and returns a list of their squares:

```python
from typing import List

def square_numbers(numbers: List[int]) -> List[int]:
    return [n * n for n in numbers]
```

- `numbers: List[int]` specifies that `numbers` should be a list of integers.
- `-> List[int]` indicates the function returns a list of integers.

### 2.2 API Response Example

Suppose we are working with a function that fetches user data from an API and returns a dictionary:

```python
from typing import Dict

def fetch_user_data(user_id: int) -> Dict[str, str]:
    # Simulate API response
    return {
        "id": str(user_id),
        "name": "John Doe"
    }
```

- `user_id: int` indicates that `user_id` should be an integer.
- `-> Dict[str, str]` indicates the function returns a dictionary with string keys and string values.

### 2.3 Working with Custom Types

You can define your own types for better readability and to simplify complex type annotations.

```python
from typing import List, Tuple

Point = Tuple[float, float]

def calculate_distance(points: List[Point]) -> float:
    p1, p2 = points
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
```

Here:
- `Point = Tuple[float, float]` defines `Point` as a tuple of two floats.
- `points: List[Point]` specifies that `points` should be a list of `Point` tuples.

### 2.4 Example with Optional Types

Sometimes a function parameter or return value can be of a specified type or `None`. This is where `Optional` is useful.

```python
from typing import Optional

def get_username(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
```

- `-> Optional[str]` indicates the function may return a string or `None`.

## 3. Common Annotations and Usage

### 3.1 Built-in Types

- `int`, `str`, `float`, `bool`: Basic types.
- `List[T]`: List of items of type `T`.
- `Dict[K, V]`: Dictionary with keys of type `K` and values of type `V`.
- `Tuple[T1, T2, ...]`: Tuple with items of specified types.

### 3.2 More Complex Types

- `Optional[T]`: Either `T` or `None`.
- `Union[T1, T2, ...]`: Value of type `T1`, `T2`, etc.
- `Any`: Can be any type.

### 3.3 Advanced Types

- `Callable[[T1, T2], R]`: A function that takes parameters of types `T1`, `T2`, etc., and returns a value of type `R`.

```python
from typing import Callable

def apply_function(f: Callable[[int, int], int], x: int, y: int) -> int:
    return f(x, y)

def add(a: int, b: int) -> int:
    return a + b

print(apply_function(add, 3, 4))  # Output: 7
```

- `Iterable[T]`: Any iterable type of `T`.

```python
from typing import Iterable

def print_elements(elements: Iterable[str]) -> None:
    for element in elements:
        print(element)
```

## 4. Checking and Enforcing Type Annotations

### 4.1 Static Type Checking

Tools like `mypy` can check if the types are consistent without running the code.

```bash
mypy your_script.py
```

### 4.2 Runtime Type Checking

You can use libraries like `typeguard` to enforce types at runtime.

```python
from typeguard import typechecked

@typechecked
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(2, 3))  # Correct usage
# print(multiply(2, "three"))  # Raises a TypeError at runtime
```

## 5. Multiple Choice Questions (MCQs)

### 1. What is the primary purpose of type annotations in Python?
a. To force Python to be statically typed  
b. To improve code readability and error detection  
c. To enhance the performance of the Python interpreter  
d. To replace comments in code  

### 2. Which of the following is a correct type annotation for a function that accepts a list of strings and returns an integer?
a. `def process(data: List[int]) -> int:`  
b. `def process(data: List[str]) -> int:`  
c. `def process(data: List[str]) -> str:`  
d. `def process(data: List[int]) -> str:`  

### 3. In the following function, what type is specified for the `name` parameter?
   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```
a. `int`  
b. `str`  
c. `float`  
d. `bool`  

### 4. How would you annotate a function that might return a string or `None`?
a. `def get_value() -> Optional[str]:`  
b. `def get_value() -> Union[str, None]:`  
c. Both a and b  
d. None of the above  

### 5. What does `Callable[[int, int], int]` represent in type annotations?
a. A function that takes an integer and returns an integer  
b. A function that takes two integers and returns an integer  
c. A function that returns two integers  
d. An integer  

### 6. How do you indicate a variable can be any type?
a. `var: Any`  
b. `var: Optional`  
c. `var: All`  
d. `var: object`  

### 7. Which tool can be used to check type annotations without running the code?
a. `pytest`  
b. `mypy`  
c. `flake8`  
d. `typeguard`  

### 8. What is the type of `data` in this function?
   ```python
   def display(data: Dict[str, int]) -> None:
       pass
   ```
a. List of strings  
b. Dictionary with string keys and integer values  
c. List of integers  
d. Dictionary with integer keys and string values  

### 9. How would you annotate a function that processes an iterable of strings and returns a list of strings?
a. `def process(data: Iterable[str]) -> List[str]:`  
b. `def process(data: List[str]) -> Iterable[str]:`  
c. `def process(data: str) -> List[str]:`  
d. `def process(data: List[str]) -> str:`  

### 10. What does the `typeguard` library do?
a. Checks types at runtime  
b. Formats code according to PEP 8  
c. Provides static type checking  
d. Manages Python virtual environments  

## Answers

1. **b. To improve code readability and error detection**
2. **b. `def process(data: List[str]) -> int:`**
3. **b. `str`**
4. **c. Both a and b**
5. **b. A function that takes two integers and returns an integer**
6. **a. `var: Any`**
7. **b. `mypy`**
8. **b. Dictionary with string keys and integer values**
9. **a. `def process(data: Iterable[str]) -> List[str]:`**


10. **a. Checks types at runtime**

# Using Type Annotations to Specify Function Signatures and Variable Types

Type annotations in Python provide a way to explicitly declare the expected types of variables, function parameters, and return values. This clarity can improve code quality, reduce bugs, and make the codebase easier to maintain.

## 1. Specifying Variable Types

Type annotations can be used to specify the types of variables at the point of their declaration.

### 1.1 Basic Variable Annotations

```python
# Integer variable
age: int = 30

# String variable
name: str = "Alice"

# Floating-point variable
height: float = 5.9

# Boolean variable
is_student: bool = True
```

### 1.2 Using Complex Types

```python
from typing import List, Dict, Tuple

# List of integers
scores: List[int] = [85, 90, 75]

# Dictionary with string keys and integer values
student_ages: Dict[str, int] = {"Alice": 20, "Bob": 22}

# Tuple of a string and an integer
person: Tuple[str, int] = ("Charlie", 25)
```

## 2. Specifying Function Signatures

Function signatures can be annotated to specify the types of parameters and the return type. This helps in documenting the expected types and enables tools to catch type-related errors.

### 2.1 Simple Function Signatures

```python
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

- `x: int`, `y: int`: Specifies that `x` and `y` are integers.
- `-> int`: Indicates the function returns an integer.

### 2.2 Functions with Complex Types

```python
from typing import List

def calculate_average(scores: List[int]) -> float:
    return sum(scores) / len(scores)
```

- `scores: List[int]`: Indicates `scores` should be a list of integers.
- `-> float`: Specifies that the function returns a floating-point number.

### 2.3 Functions with Optional Types

Use `Optional` when a parameter or return value can be a specific type or `None`.

```python
from typing import Optional

def find_student(name: str) -> Optional[int]:
    students = {"Alice": 1, "Bob": 2}
    return students.get(name)
```

- `-> Optional[int]`: Indicates the function may return an integer or `None`.

### 2.4 Functions with Multiple Return Types

Use `Union` to indicate a function can return more than one type.

```python
from typing import Union

def get_value(flag: bool) -> Union[int, str]:
    if flag:
        return 100
    else:
        return "One hundred"
```

- `-> Union[int, str]`: Specifies that the function can return either an integer or a string.

### 2.5 Functions Returning Multiple Values

Use `Tuple` to specify a function that returns multiple values.

```python
from typing import Tuple

def split_name(full_name: str) -> Tuple[str, str]:
    parts = full_name.split()
    return parts[0], parts[1]
```

- `-> Tuple[str, str]`: Indicates the function returns a tuple with two strings.

### 2.6 Using Callable for Function Types

Use `Callable` to specify the type of a function parameter.

```python
from typing import Callable

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)

def add(a: int, b: int) -> int:
    return a + b

result = apply_operation(5, 3, add)
print(result)  # Output: 8
```

- `operation: Callable[[int, int], int]`: Indicates `operation` is a function that takes two integers and returns an integer.

## 3. Type Annotations in Real-World Projects

### 3.1 Data Analysis Function

Suppose you have a function that analyzes a dataset and returns the summary:

```python
from typing import List, Dict

def analyze_data(data: List[Dict[str, float]]) -> Dict[str, float]:
    total = 0
    count = 0
    for record in data:
        total += record["value"]
        count += 1
    return {
        "total": total,
        "average": total / count
    }
```

- `data: List[Dict[str, float]]`: Specifies `data` is a list of dictionaries, where each dictionary has string keys and floating-point values.
- `-> Dict[str, float]`: Indicates the function returns a dictionary with string keys and floating-point values.

### 3.2 Web API Handler

Consider a function that processes an API response:

```python
from typing import Union, Dict

def handle_response(response: Union[str, Dict[str, str]]) -> str:
    if isinstance(response, str):
        return f"Received error: {response}"
    else:
        return f"Success: User {response['username']} found"
```

- `response: Union[str, Dict[str, str]]`: Specifies `response` can be a string or a dictionary with string keys and string values.
- `-> str`: Indicates the function returns a string.

## 4. Practical Applications

### 4.1 Validating User Input

When creating functions that process user input, type annotations help ensure the data is handled correctly.

```python
def validate_age(age: int) -> bool:
    return 0 <= age <= 120
```

- `age: int`: Indicates `age` should be an integer.
- `-> bool`: Specifies that the function returns a boolean.

### 4.2 Configuration Management

Managing application configurations often involves complex data structures. Type annotations can clarify expected types.

```python
from typing import Dict, Any

def load_config(config: Dict[str, Any]) -> None:
    # Process configuration
    print(config)

config = {
    "debug": True,
    "max_connections": 100,
    "server": "localhost"
}
load_config(config)
```

- `config: Dict[str, Any]`: Specifies `config` is a dictionary with string keys and values of any type.

## 5. Multiple Choice Questions (MCQs)

### 1. What does `age: int` specify in the following code?
   ```python
   age: int = 30
   ```
a. The variable `age` is a constant.  
b. The variable `age` is expected to be an integer.  
c. The variable `age` is expected to be a string.  
d. The variable `age` is optional.  

### 2. Which type annotation is used to specify a function that takes a list of integers and returns a floating-point number?
a. `def compute(values: List[int]) -> str:`  
b. `def compute(values: List[int]) -> float:`  
c. `def compute(values: List[int]) -> int:`  
d. `def compute(values: List[str]) -> float:`  

### 3. What does the following function signature indicate?
   ```python
   def find_item(items: List[str], key: str) -> Optional[str]:
   ```
a. The function `find_item` returns an integer or `None`.  
b. The function `find_item` returns a string or `None`.  
c. The function `find_item` returns a list of strings.  
d. The function `find_item` returns a boolean.  

### 4. How do you specify a function that can return either an integer or a string?
a. `-> Optional[int, str]`  
b. `-> Union[int, str]`  
c. `-> Either[int, str]`  
d. `-> List[int, str]`  

### 5. What is the correct annotation for a function parameter that can be a string or `None`?
a. `name: Optional[str]`  
b. `name: Union[str, None]`  
c. Both a and b  
d. None of the above  

### 6. Which of the following indicates a function that returns a dictionary with string keys and floating-point values?
a. `-> Dict[str, int]`  
b. `-> Dict[int, float]`  
c. `-> Dict[str, float]`  
d. `-> Dict[str, Any]`  

### 7. How do you annotate a function that takes a parameter of type `Callable[[int, int], int]`?
a. `operation: Callable[int, int]`  
b. `operation: Callable[[int, int], int]`  
c. `operation: Function[int, int]`  
d. `operation: Function[[int, int], int]`  

### 8. What does `from typing import List` allow you to do?
a. Use `List` as a built-in type for type annotations.  
b. Use `List` to declare lists with type hints.  
c. Create custom list classes.  
d. Import a list of types.  

### 9. What is the purpose of using `Optional` in type annotations?
a. To indicate a parameter is required.  
b. To indicate a parameter can be of multiple types.  
c. To indicate a parameter can be of a specified type or `None`.  
d. To indicate a parameter is deprecated.  

### 10. In the function `def process(data: Dict[str, Any]) -> None:`, what does `Any` represent?
a. A specific type of

 data  
b. A function type  
c. Any type of data  
d. A list of types  

## Answers

1. **b. The variable `age` is expected to be an integer.**
2. **b. `def compute(values: List[int]) -> float:`**
3. **b. The function `find_item` returns a string or `None`.**
4. **b. `-> Union[int, str]`**
5. **c. Both a and b**
6. **c. `-> Dict[str, float]`**
7. **b. `operation: Callable[[int, int], int]`**
8. **b. Use `List` to declare lists with type hints.**
9. **c. To indicate a parameter can be of a specified type or `None`.**
10. **c. Any type of data**

# Duck Typing in Python

Duck typing is a concept in Python that focuses on what an object can do rather than what it is. This means that the suitability of an object for a particular use is determined by the methods it supports and the operations it can perform, rather than its inheritance from a specific class.

## 1. Understanding Duck Typing

### 1.1 What is Duck Typing?

The term "duck typing" comes from the phrase: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In programming, this means that if an object behaves like a certain type, it can be used as that type, regardless of its actual class.

### 1.2 Example of Duck Typing

Consider a function that processes any object that can "quack":

```python
def make_it_quack(duck):
    duck.quack()

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack!
make_it_quack(p)  # Output: I'm quacking like a duck!
```

In this example, both the `Duck` and `Person` classes have a `quack` method, so they can both be used with the `make_it_quack` function, despite not being related through inheritance.

## 2. Applying Duck Typing in Real-World Projects

### 2.1 File-like Objects

Duck typing allows using any object that behaves like a file (has `read` and `write` methods) with functions that expect file-like objects.

```python
def process_file(file_obj):
    data = file_obj.read()
    print("Processing:", data)

class FileMock:
    def read(self):
        return "Mock file content"

mock_file = FileMock()
process_file(mock_file)  # Output: Processing: Mock file content
```

Here, `process_file` works with any object that has a `read` method, regardless of whether it is a real file or a mock object.

### 2.2 Using Duck Typing with Collections

Duck typing can be applied to collections if they support iteration, regardless of their specific type.

```python
def sum_elements(elements):
    total = 0
    for element in elements:
        total += element
    return total

# Works with lists
print(sum_elements([1, 2, 3]))  # Output: 6

# Works with tuples
print(sum_elements((4, 5, 6)))  # Output: 15

# Works with custom iterable objects
class CustomIterable:
    def __iter__(self):
        return iter([7, 8, 9])

print(sum_elements(CustomIterable()))  # Output: 24
```

### 2.3 Custom Objects with Specific Methods

Duck typing allows using custom objects with methods that match the expected interface, even if they are not from a known class.

```python
class StringBuffer:
    def __init__(self):
        self.content = ""
    
    def write(self, text):
        self.content += text
    
    def __str__(self):
        return self.content

def append_text(writer, text):
    writer.write(text)

buffer = StringBuffer()
append_text(buffer, "Hello, world!")
print(buffer)  # Output: Hello, world!
```

The `append_text` function works with any object that has a `write` method.

## 3. Advantages of Duck Typing

- **Flexibility**: Allows using objects based on their behavior rather than their class.
- **Code Reuse**: Functions can work with a broader range of objects.
- **Simpler Interfaces**: Reduces the need for complex inheritance hierarchies.

## 4. Drawbacks of Duck Typing

- **Less Predictability**: Errors may occur if an object does not fully support the expected interface.
- **Late Detection of Errors**: Type-related issues may not be detected until runtime.

## 5. Duck Typing in Design Patterns

### 5.1 Adapter Pattern

The adapter pattern allows converting one interface to another that a client expects. Duck typing can be used to adapt objects to expected interfaces without modifying their code.

```python
class Bird:
    def tweet(self):
        print("Tweet!")

class DuckAdapter:
    def __init__(self, bird):
        self.bird = bird
    
    def quack(self):
        self.bird.tweet()

bird = Bird()
duck_like_bird = DuckAdapter(bird)
make_it_quack(duck_like_bird)  # Output: Tweet!
```

## 6. Practical Example: Logging System

Consider a logging system that can write logs to different outputs such as files, databases, or mock objects.

```python
class FileLogger:
    def write_log(self, message):
        print(f"Writing to file: {message}")

class DatabaseLogger:
    def write_log(self, message):
        print(f"Writing to database: {message}")

def log_message(logger, message):
    logger.write_log(message)

file_logger = FileLogger()
db_logger = DatabaseLogger()

log_message(file_logger, "File log entry")  # Output: Writing to file: File log entry
log_message(db_logger, "Database log entry")  # Output: Writing to database: Database log entry
```

## 7. Type Checking with Duck Typing

### 7.1 `hasattr` Function

You can use the `hasattr` function to check if an object supports the required methods before using it.

```python
def process(obj):
    if hasattr(obj, 'read'):
        print("Processing as a file:", obj.read())
    elif hasattr(obj, 'quack'):
        print("Processing as a duck:", obj.quack())
    else:
        print("Unsupported object")
```

## 8. Multiple Choice Questions (MCQs)

### 1. What does the term "duck typing" refer to in Python?
a. A method to explicitly check types at runtime  
b. A way to define types using duck-like syntax  
c. An approach where the suitability of an object is determined by its methods and properties  
d. A specific class inheritance pattern  

### 2. In the following code, which of the classes can be used with the `make_it_quack` function?
   ```python
   def make_it_quack(duck):
       duck.quack()
   
   class Duck:
       def quack(self):
           print("Quack!")
   
   class Car:
       def drive(self):
           print("Vroom!")
   ```
a. Only `Duck`  
b. Only `Car`  
c. Both `Duck` and `Car`  
d. Neither `Duck` nor `Car`  

### 3. What does the following function check for?
   ```python
   def process_file(file_obj):
       if hasattr(file_obj, 'read'):
           print("This is a file-like object")
   ```
a. If `file_obj` is an instance of a specific class  
b. If `file_obj` has a `read` method  
c. If `file_obj` is a file  
d. If `file_obj` is empty  

### 4. How does duck typing enhance code flexibility?
a. By enforcing strict type checking  
b. By allowing objects with similar methods to be used interchangeably  
c. By requiring objects to inherit from a common superclass  
d. By avoiding runtime type errors  

### 5. Which of the following best describes the drawback of duck typing?
a. It enforces too strict type constraints.  
b. It can lead to late detection of type-related errors.  
c. It makes code less reusable.  
d. It requires a lot of boilerplate code.  

### 6. What would be the output of the following code?
   ```python
   def make_it_quack(duck):
       duck.quack()
   
   class ToyDuck:
       def quack(self):
           print("Squeak!")
   
   toy = ToyDuck()
   make_it_quack(toy)
   ```
a. `Quack!`  
b. `Squeak!`  
c. `Error: Method not found`  
d. No output  

### 7. Which function can be used to check if an object has a specific method in Python?
a. `isinstance`  
b. `issubclass`  
c. `hasattr`  
d. `type`  

### 8. In duck typing, what is the primary focus when using an object?
a. The class of the object  
b. The name of the object  
c. The methods and properties the object supports  
d. The module where the object is defined  

### 9. What is the purpose of the `append_text` function in the following code?
   ```python
   class StringBuffer:
       def __init__(self):
           self.content = ""
       
       def write(self, text):
           self.content += text
   
   def append_text(writer, text):
       writer.write(text)
   
   buffer = StringBuffer()
   append_text(buffer, "Hello, world!")
   print(buffer)
   ```
a. To append text to a string  
b. To create a new string buffer  
c. To write text to a file  
d. To call a function  

### 10. How does duck typing relate to the adapter design pattern?
a. It enforces strict type compatibility  
b. It allows adapting one interface to another by matching method signatures  
c. It requires objects to be of the same class  
d. It limits flexibility by restricting object types  

## Answers

1. **c. An approach where the suitability of an object is determined by its methods and properties**
2. **a. Only `Duck`**
3. **b. If `file_obj` has a `read` method**
4. **b. By allowing objects with similar methods to be used interchangeably**
5. **b. It can lead to late detection of type-related errors**
6. **b. `Squeak!`**
7. **c. `hasattr`**
8. **c. The methods and properties the object supports**
9. **a. To append text to a string**
10. **b. It allows adapting one interface to another by matching method signatures**

# Validating Your Code with `mypy`

`mypy` is a static type checker for Python that helps ensure the correctness of your type annotations. It checks the code for type errors without running it, which can help catch bugs early in the development process.

## 1. What is `mypy`?

`mypy` is a tool that checks Python code for type consistency based on the type annotations provided in the code. It doesn’t execute the code but analyzes it to ensure that the types used are correct according to the annotations.

### Why Use `mypy`?

- **Catch Errors Early**: Detects type-related errors before running the code.
- **Improve Code Quality**: Ensures type safety and reduces bugs.
- **Enhance Code Documentation**: Type annotations serve as documentation, making the code easier to understand.

## 2. Installing `mypy`

To use `mypy`, you need to install it. You can do this using `pip`:

```bash
pip install mypy
```

## 3. Basic Usage of `mypy`

Once installed, you can use `mypy` to check your Python files for type correctness.

### Example

Consider the following Python script, `example.py`:

```python
def add(x: int, y: int) -> int:
    return x + y

result = add(10, "20")
```

To check this file with `mypy`, run:

```bash
mypy example.py
```

### Output

```text
example.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

The output shows a type error on line 4 because the function `add` expects both arguments to be integers, but a string is passed as the second argument.

## 4. Validating Functions with `mypy`

### 4.1 Function Annotations

`mypy` checks if the function parameters and return types match the provided type annotations.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

message = greet(123)
```

Running `mypy`:

```bash
mypy example.py
```

Output:

```text
example.py:4: error: Argument 1 to "greet" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

### 4.2 Optional Types

When using `Optional`, `mypy` ensures that the function handles the possibility of `None` values properly.

```python
from typing import Optional

def process(value: Optional[int]) -> int:
    if value is None:
        return 0
    return value * 2

result = process(None)
```

No error here since `None` is handled correctly.

## 5. Validating Variables and Collections

### 5.1 Variables

`mypy` checks that variables match their declared types.

```python
age: int = "twenty"
```

Output:

```text
example.py:1: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

### 5.2 Collections

For collections, `mypy` checks that all elements match the specified types.

```python
from typing import List

numbers: List[int] = [1, 2, "three"]
```

Output:

```text
example.py:3: error: List item 2 has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## 6. Using `mypy` with Complex Types

### 6.1 Nested Types

`mypy` can validate nested types like lists of dictionaries.

```python
from typing import List, Dict

data: List[Dict[str, int]] = [{"key": 1}, {"key": "value"}]
```

Output:

```text
example.py:4: error: Dict entry 0 has incompatible type "str": "int"; expected "str": "int"
Found 1 error in 1 file (checked 1 source file)
```

### 6.2 Custom Classes

`mypy` checks if custom classes match expected types.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def print_person(person: Person) -> str:
    return f"{person.name} is {person.age} years old."

p = Person("Alice", "twenty")
```

Output:

```text
example.py:9: error: Argument 2 to "Person" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## 7. Advanced Features

### 7.1 Type Inference

`mypy` can infer types even without explicit annotations, but explicit annotations are always preferred for clarity.

```python
def multiply(x, y):
    return x * y

result: int = multiply(10, "20")
```

Output:

```text
example.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

### 7.2 Ignoring Type Checking

Sometimes, you might want to bypass type checking for specific lines or files.

```python
value: int = "ignore"  # type: ignore
```

## 8. Integrating `mypy` in Projects

### 8.1 Configuration File

You can create a configuration file, `mypy.ini`, to customize how `mypy` checks your code.

```ini
[mypy]
ignore_missing_imports = True
strict = True
```

### 8.2 Running `mypy` in Continuous Integration

You can integrate `mypy` into CI/CD pipelines to automatically check for type errors.

```yaml
# Example GitHub Actions workflow
name: mypy-check

on: [push, pull_request]

jobs:
  mypy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        pip install mypy
    - name: Run mypy
      run: |
        mypy .
```

## 9. Practical Example: API Client

### 9.1 API Client Code

```python
from typing import Dict, Any

def fetch_data(api_endpoint: str) -> Dict[str, Any]:
    # Simulated API response
    return {"status": "success", "data": {"id": 123, "name": "Example"}}

response = fetch_data("/api/data")
```

### 9.2 Running `mypy`

Run `mypy` to validate the API client:

```bash
mypy api_client.py
```

If the types are consistent, `mypy` will show no errors. Otherwise, it will indicate where the issues are.

## 10. Multiple Choice Questions (MCQs)

### 1. What does `mypy` do?
a. Executes Python code to check for errors  
b. Analyzes Python code for type correctness without executing it  
c. Compiles Python code into a binary  
d. Checks Python code for syntax errors  

### 2. How can you install `mypy`?
a. `install mypy`  
b. `python -m mypy`  
c. `pip install mypy`  
d. `python setup.py mypy`  

### 3. What type of error does the following `mypy` output indicate?
   ```text
   example.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
   ```
a. Syntax error  
b. Type mismatch error  
c. Runtime error  
d. Import error  

### 4. Which of the following files can be checked by `mypy`?
a. Files with `.py` extension  
b. Files with `.txt` extension  
c. Only files with type annotations  
d. Only files that import `mypy`  

### 5. What does `from typing import List` enable in type annotations?
a. Use of list as a keyword  
b. Import of `list` function  
c. Use of `List` for type hints  
d. Declaration of list variables  

### 6. How does `mypy` handle functions without type annotations?
a. Ignores them  
b. Infers types and checks for consistency  
c. Treats them as errors  
d. Converts them to typed functions  

### 7. What is the purpose of `# type: ignore` in a Python script?
a. To ignore a line during execution  
b. To disable type checking for a specific line  
c. To mark a line as deprecated  
d. To skip a line for debugging  

### 8. Which configuration file can customize `mypy` checks?
a. `mypy.ini`  
b. `config.yml`  
c. `settings.py`  
d. `setup.cfg`  

### 9. How does `mypy` help in a continuous integration pipeline?
a. By executing tests automatically  
b. By converting Python code to another language  
c. By checking for type errors automatically  
d. By merging code branches  

### 10. What

 does `Dict[str, Any]` represent in a type annotation?
a. A dictionary with string keys and values of any type  
b. A dictionary with any type of keys and values  
c. A list of strings and any type of elements  
d. A dictionary with string keys and values of the same type  

## Answers

1. **b. Analyzes Python code for type correctness without executing it**
2. **c. `pip install mypy`**
3. **b. Type mismatch error**
4. **a. Files with `.py` extension**
5. **c. Use of `List` for type hints**
6. **b. Infers types and checks for consistency**
7. **b. To disable type checking for a specific line**
8. **a. `mypy.ini`**
9. **c. By checking for type errors automatically**
10. **a. A dictionary with string keys and values of any type**

## Conclusion

In this note, we have covered the basics of type annotations in Python 3 and how to use them to specify function signatures and variable types. We have also discussed duck typing, which allows for flexible typing in Python. Furthermore, we have shown how to validate your code with mypy to ensure that it adheres to the specified types. By following these best practices, you can write more robust and maintainable code in Python.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
