## File I/O in Python: Reading from `sys.stdin` Line by Line

File I/O (Input/Output) in Python allows you to interact with files and input streams, making it possible to read from and write to files. This is a crucial skill in programming as it enables you to handle data stored in files and to process input from various sources.

### Reading from `sys.stdin` Line by Line

`sys.stdin` is a built-in file object that is analogous to a file opened in read mode. It is used to read input from the standard input, which is typically the keyboard but can be redirected from other sources. Reading from `sys.stdin` is useful when you want to process input directly from the user or from another program.

To use `sys.stdin`, you need to import the `sys` module. Here is how you can read input line by line:

```python
import sys

for line in sys.stdin:
    # Process each line
    print(line.strip())
```

### Explanation

1. **Importing the `sys` Module**:
    ```python
    import sys
    ```
    The `sys` module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

2. **Reading Input Line by Line**:
    ```python
    for line in sys.stdin:
        print(line.strip())
    ```
    The `for line in sys.stdin:` loop reads each line from the standard input. The `strip()` method is used to remove any leading or trailing whitespace characters, including the newline character at the end of each line.

### Example Usage in a Real-World Project

Imagine you're building a command-line tool that processes text input from the user. For instance, you might want to count the number of lines, words, and characters in the input text.

Here's a simple script that performs this task:

```python
import sys

line_count = 0
word_count = 0
char_count = 0

for line in sys.stdin:
    line_count += 1
    word_count += len(line.split())
    char_count += len(line)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
```

### Explanation

1. **Initializing Counters**:
    ```python
    line_count = 0
    word_count = 0
    char_count = 0
    ```
    We initialize three counters to zero. These will keep track of the number of lines, words, and characters.

2. **Reading and Processing Each Line**:
    ```python
    for line in sys.stdin:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)
    ```
    - `line_count += 1`: Increments the line count for each line read.
    - `word_count += len(line.split())`: Splits the line into words and increments the word count by the number of words in the line.
    - `char_count += len(line)`: Increments the character count by the number of characters in the line.

3. **Printing the Results**:
    ```python
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    ```
    We print the total counts for lines, words, and characters.

### Technical End of Chapter MCQ

1. Which module must be imported to use `sys.stdin`?
    - A) os
    - B) sys
    - C) io
    - D) re

2. What does `sys.stdin` represent?
    - A) Standard output
    - B) Standard error
    - C) Standard input
    - D) None of the above

3. Which method removes leading and trailing whitespace characters from a string?
    - A) strip()
    - B) split()
    - C) trim()
    - D) remove()

4. In the script to count lines, words, and characters, what does `len(line.split())` count?
    - A) Lines
    - B) Words
    - C) Characters
    - D) Whitespace

5. What does the following code do? 
    ```python
    for line in sys.stdin:
        print(line)
    ```
    - A) Reads from a file
    - B) Writes to a file
    - C) Reads input from the user and prints each line
    - D) None of the above

6. How can you remove the newline character from the end of each line read from `sys.stdin`?
    - A) Using `line.split()`
    - B) Using `line.strip()`
    - C) Using `line.remove()`
    - D) Using `line.trim()`

7. In the line counting script, what does `line_count += 1` do?
    - A) Adds 1 to the word count
    - B) Adds 1 to the line count
    - C) Adds 1 to the character count
    - D) None of the above

8. What will be the output of the following code if the input is "Hello\nWorld"?
    ```python
    import sys
    for line in sys.stdin:
        print(line.strip())
    ```
    - A) Hello World
    - B) Hello\nWorld
    - C) Hello\nWorld\n
    - D) Hello\n World\n

9. If you want to count characters including whitespaces, which method should you use?
    - A) len(line.split())
    - B) len(line.strip())
    - C) len(line)
    - D) len(line.remove())

10. Which of the following is true about `sys.stdin`?
    - A) It can only read from files
    - B) It can only read from the keyboard
    - C) It can read from any standard input stream
    - D) It can only read from other programs

### Answers

1. B) sys
2. C) Standard input
3. A) strip()
4. B) Words
5. C) Reads input from the user and prints each line
6. B) Using line.strip()
7. B) Adds 1 to the line count
8. A) Hello World
9. C) len(line)
10. C) It can read from any standard input stream

## Signal Handling in Python: Handling Keyboard Interruption (CTRL + C)

Signal handling in Python allows programs to intercept and handle signals sent to the process. A common signal to handle is the keyboard interruption signal, which occurs when a user presses `CTRL + C`. This signal, known as `SIGINT` (Signal Interrupt), can be captured and managed to perform cleanup tasks or to exit the program gracefully.

### Handling Keyboard Interruption (CTRL + C)

To handle keyboard interruption using signal handling, the `signal` module is used. Here is a step-by-step guide on how to capture and handle `SIGINT`.

### Step-by-Step Guide

1. **Import the `signal` and `sys` Modules**:
    ```python
    import signal
    import sys
    ```

2. **Define a Signal Handler Function**:
    This function will be called when `SIGINT` is received.
    ```python
    def signal_handler(sig, frame):
        print('You pressed CTRL + C!')
        sys.exit(0)
    ```

3. **Set Up the Signal Handler**:
    Use `signal.signal()` to associate `SIGINT` with your handler function.
    ```python
    signal.signal(signal.SIGINT, signal_handler)
    ```

4. **Keep the Program Running**:
    Use an infinite loop to keep the program running and able to capture the signal.
    ```python
    print('Press CTRL + C to exit.')
    while True:
        pass  # Do nothing, just wait for the signal
    ```

### Complete Example

Here is the complete code that handles keyboard interruption:

```python
import signal
import sys

def signal_handler(sig, frame):
    print('You pressed CTRL + C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press CTRL + C to exit.')
while True:
    pass  # Infinite loop to keep the program running
```

### Explanation

1. **Importing Modules**:
    ```python
    import signal
    import sys
    ```
    The `signal` module provides mechanisms to use signal handlers, and the `sys` module allows you to interact with the Python runtime environment.

2. **Defining the Handler**:
    ```python
    def signal_handler(sig, frame):
        print('You pressed CTRL + C!')
        sys.exit(0)
    ```
    - `signal_handler(sig, frame)`: This function is called when the signal is received. It prints a message and then exits the program using `sys.exit(0)`, which ensures a clean shutdown.

3. **Setting the Signal Handler**:
    ```python
    signal.signal(signal.SIGINT, signal_handler)
    ```
    This line tells the program to call `signal_handler` when `SIGINT` is received.

4. **Running the Program**:
    ```python
    print('Press CTRL + C to exit.')
    while True:
        pass
    ```
    The infinite loop keeps the program running, allowing it to capture the `CTRL + C` signal.

### Real-World Application

Signal handling is crucial in real-world projects where you need to ensure that your program can handle interruptions gracefully. For example, in a server application, you might need to close network connections or save state information before shutting down. Here’s how you can apply signal handling to perform cleanup tasks:

```python
import signal
import sys
import time

def cleanup():
    print('Cleaning up resources...')

def signal_handler(sig, frame):
    print('You pressed CTRL + C!')
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press CTRL + C to exit.')
while True:
    time.sleep(1)  # Simulate doing some work
```

In this example, `cleanup()` is a function that performs any necessary cleanup before the program exits.

### Technical End of Chapter MCQ

1. Which module is used to handle signals in Python?
    - A) os
    - B) sys
    - C) signal
    - D) interrupt

2. What signal is sent when `CTRL + C` is pressed?
    - A) SIGTERM
    - B) SIGKILL
    - C) SIGINT
    - D) SIGSTOP

3. What function is used to define a signal handler for `SIGINT`?
    - A) signal.set_handler()
    - B) signal.signal()
    - C) signal.catch()
    - D) signal.handle()

4. What does `sys.exit(0)` do in the signal handler?
    - A) Raises an error
    - B) Exits the program
    - C) Continues the program
    - D) Restarts the program

5. Where should you import the `signal` module from?
    - A) `import signal`
    - B) `from signal import handler`
    - C) `import handler`
    - D) `from handler import signal`

6. What does the following code do?
    ```python
    while True:
        pass
    ```
    - A) Stops the program
    - B) Keeps the program running indefinitely
    - C) Runs the program once
    - D) Exits the program

7. In the context of signal handling, what is the purpose of `frame` in the handler function?
    - A) To capture the frame of the video
    - B) To provide the current stack frame
    - C) To store signal information
    - D) To handle exceptions

8. What is printed when `CTRL + C` is pressed in the following code?
    ```python
    import signal
    import sys

    def signal_handler(sig, frame):
        print('Interrupted')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        pass
    ```
    - A) Exited
    - B) Interrupted
    - C) Error
    - D) Nothing

9. What does `signal.signal(signal.SIGINT, signal_handler)` do?
    - A) It stops the program
    - B) It handles the signal
    - C) It associates `SIGINT` with `signal_handler`
    - D) It raises an error

10. Why is an infinite loop used in signal handling examples?
    - A) To exit the program
    - B) To keep the program running to capture the signal
    - C) To cause an error
    - D) To handle exceptions

### Answers

1. C) signal
2. C) SIGINT
3. B) signal.signal()
4. B) Exits the program
5. A) import signal
6. B) Keeps the program running indefinitely
7. B) To provide the current stack frame
8. B) Interrupted
9. C) It associates `SIGINT` with `signal_handler`
10. B) To keep the program running to capture the signal

## Data Processing: Parsing Strings to Extract Specific Data Points

Data processing involves manipulating data to extract useful information. One common task is parsing strings to extract specific data points. Parsing strings is essential for handling data received in text format, such as logs, user input, or data files.

### Parsing Strings in Python

Python provides several methods to parse strings and extract data points. Common methods include using string methods, regular expressions, and libraries like `csv` or `json`.

### Using String Methods

String methods are straightforward and efficient for simple parsing tasks. Here's how you can use them:

1. **Splitting Strings**:
    ```python
    data = "John,Doe,30,Engineer"
    parts = data.split(',')
    first_name = parts[0]
    last_name = parts[1]
    age = parts[2]
    profession = parts[3]
    print(first_name, last_name, age, profession)
    ```

    - `split(',')`: Splits the string into a list of parts based on the comma delimiter.

2. **Finding and Slicing**:
    ```python
    data = "User: John Doe, Age: 30, Profession: Engineer"
    start = data.find("Age: ") + len("Age: ")
    end = data.find(",", start)
    age = data[start:end]
    print(age)
    ```

    - `find()`: Finds the starting index of the substring.
    - `slicing`: Extracts the substring using start and end indices.

### Using Regular Expressions

Regular expressions (regex) are powerful for more complex parsing tasks. They allow you to define patterns to search for in a string.

1. **Basic Regex Parsing**:
    ```python
    import re
    data = "User: John Doe, Age: 30, Profession: Engineer"
    match = re.search(r"Age: (\d+)", data)
    if match:
        age = match.group(1)
    print(age)
    ```

    - `re.search()`: Searches for the pattern in the string.
    - `group(1)`: Extracts the first capturing group (the digits representing the age).

2. **Extracting Multiple Data Points**:
    ```python
    data = "User: John Doe, Age: 30, Profession: Engineer"
    pattern = r"User: (\w+ \w+), Age: (\d+), Profession: (\w+)"
    match = re.search(pattern, data)
    if match:
        name = match.group(1)
        age = match.group(2)
        profession = match.group(3)
    print(name, age, profession)
    ```

    - `pattern`: Defines a regex pattern with multiple capturing groups.

### Real-World Application

Parsing strings is crucial in various applications. For example, parsing logs to extract error messages, processing CSV files to read user data, or parsing HTML to extract information from web pages.

1. **Parsing CSV Files**:
    ```python
    import csv

    with open('users.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    ```

    - `csv.reader()`: Reads CSV file row by row.

2. **Parsing JSON Data**:
    ```python
    import json

    data = '{"name": "John Doe", "age": 30, "profession": "Engineer"}'
    parsed_data = json.loads(data)
    name = parsed_data['name']
    age = parsed_data['age']
    profession = parsed_data['profession']
    print(name, age, profession)
    ```

    - `json.loads()`: Parses JSON string into a dictionary.

### Technical End of Chapter MCQ

1. Which method splits a string into a list based on a delimiter?
    - A) find()
    - B) split()
    - C) search()
    - D) group()

2. What does the following code extract?
    ```python
    data = "John,Doe,30,Engineer"
    parts = data.split(',')
    age = parts[2]
    print(age)
    ```
    - A) John
    - B) Doe
    - C) 30
    - D) Engineer

3. What does `re.search(r"Age: (\d+)", data)` return if `data = "User: John Doe, Age: 30, Profession: Engineer"`?
    - A) None
    - B) 30
    - C) Age: 30
    - D) An error

4. In the regex pattern `r"User: (\w+ \w+), Age: (\d+), Profession: (\w+)"`, what does `(\d+)` match?
    - A) Any digit
    - B) One or more digits
    - C) Any word character
    - D) One or more word characters

5. Which method is used to load a JSON string into a Python dictionary?
    - A) json.load()
    - B) json.loads()
    - C) json.dump()
    - D) json.dumps()

6. What will `parts` contain after executing `parts = "User: John Doe".split(': ')`?
    - A) ['User', 'John Doe']
    - B) ['User: John', 'Doe']
    - C) ['User:', 'John Doe']
    - D) ['User John', 'Doe']

7. What does `sys.exit(0)` do?
    - A) Exits the program
    - B) Continues the program
    - C) Restarts the program
    - D) Raises an error

8. In `re.search(r"User: (\w+ \w+)", data).group(1)`, what does `group(1)` return?
    - A) The first word
    - B) The first capturing group
    - C) The entire match
    - D) None of the above

9. What is the output of the following code?
    ```python
    import json
    data = '{"name": "John Doe", "age": 30}'
    parsed_data = json.loads(data)
    print(parsed_data['name'])
    ```
    - A) John Doe
    - B) 30
    - C) {'name': 'John Doe', 'age': 30}
    - D) An error

10. Which library is used for parsing CSV files in Python?
    - A) json
    - B) csv
    - C) re
    - D) os

### Answers

1. B) split()
2. C) 30
3. B) 30
4. B) One or more digits
5. B) json.loads()
6. A) ['User', 'John Doe']
7. A) Exits the program
8. B) The first capturing group
9. A) John Doe
10. B) csv

## Regular Expressions: Using Regular Expressions to Validate the Format of Each Line

Regular expressions (regex) are powerful tools used for pattern matching and text processing. They allow you to search, match, and manipulate strings based on defined patterns. Regex is commonly used to validate the format of strings, such as checking if an email address or phone number is in the correct format.

### Basics of Regular Expressions

A regular expression is a sequence of characters that define a search pattern. Here are some basic elements:

- **Literal Characters**: Match the exact characters (e.g., `a`, `1`, `@`).
- **Meta-characters**: Characters with special meanings (e.g., `.` matches any character, `\d` matches any digit).
- **Quantifiers**: Specify the number of occurrences (e.g., `*` for 0 or more, `+` for 1 or more, `{n}` for exactly n times).
- **Anchors**: Define the position in the string (e.g., `^` for start, `$` for end).

### Using Regular Expressions in Python

Python provides the `re` module for working with regular expressions. Common functions include:

- `re.match()`: Checks if the beginning of a string matches the pattern.
- `re.search()`: Searches the entire string for a match.
- `re.findall()`: Finds all non-overlapping matches.
- `re.sub()`: Replaces matches with a specified string.

### Validating Line Formats

To validate the format of each line, you can define a regex pattern that matches the expected format. Here’s an example of validating email addresses and phone numbers.

#### Example 1: Validating Email Addresses

An email address typically follows the format: `username@domain.extension`. Here's a regex pattern to validate email addresses:

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False

emails = ["test.email@example.com", "invalid-email@", "user@domain", "user@domain.com"]
for email in emails:
    print(f"{email}: {validate_email(email)}")
```

- `^[a-zA-Z0-9_.+-]+`: Username can contain letters, digits, dots, underscores, pluses, and hyphens.
- `@[a-zA-Z0-9-]+`: The domain part follows the `@` symbol and can contain letters, digits, and hyphens.
- `\.[a-zA-Z0-9-.]+$`: The extension follows a dot and can contain letters, digits, dots, and hyphens.

#### Example 2: Validating Phone Numbers

A phone number can have different formats, but a common one is `(XXX) XXX-XXXX`. Here's a regex pattern to validate this format:

```python
import re

def validate_phone(phone):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    if re.match(pattern, phone):
        return True
    return False

phones = ["(123) 456-7890", "123-456-7890", "(123)456-7890", "(123) 456-789O"]
for phone in phones:
    print(f"{phone}: {validate_phone(phone)}")
```

- `^\(\d{3}\) \d{3}-\d{4}$`: Matches the format `(XXX) XXX-XXXX`.
  - `^\(`: Starts with a literal `(`.
  - `\d{3}`: Matches exactly three digits.
  - `\)`: Matches a literal `)`.
  - `\d{3}-\d{4}$`: Matches three digits, a hyphen, and four digits, till the end of the string.

### Real-World Application

Regular expressions are widely used in real-world applications for data validation. For example, validating user input in web forms, parsing logs to extract information, and checking data formats in files.

### Technical End of Chapter MCQ

1. What does the regex `\d` match?
    - A) Any letter
    - B) Any digit
    - C) Any whitespace
    - D) Any special character

2. Which function checks if the beginning of a string matches a regex pattern?
    - A) re.search()
    - B) re.match()
    - C) re.findall()
    - D) re.sub()

3. What will `re.match(r'^\d{3}-\d{2}-\d{4}$', '123-45-6789')` return?
    - A) None
    - B) Match object
    - C) List of matches
    - D) Error

4. What does `+` quantifier mean in regex?
    - A) 0 or more occurrences
    - B) 1 or more occurrences
    - C) Exactly 1 occurrence
    - D) 0 or 1 occurrence

5. In the pattern `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`, what does `\.` match?
    - A) Any character
    - B) A literal dot
    - C) A digit
    - D) A letter

6. Which regex pattern matches a valid email address?
    - A) r'^[\w\.-]+@[\w\.-]+\.\w+$'
    - B) r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    - C) r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    - D) r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'

7. Which regex pattern validates phone numbers in the format `(XXX) XXX-XXXX`?
    - A) r'^\d{3} \d{3}-\d{4}$'
    - B) r'^\(\d{3}\) \d{3}-\d{4}$'
    - C) r'^\(\d{3}\)\d{3}-\d{4}$'
    - D) r'^\d{10}$'

8. What does `re.sub(r'\d', '#', 'Password123')` return?
    - A) Password123
    - B) Password###
    - C) Password
    - D) ###########

9. Which function returns all non-overlapping matches of a pattern in a string?
    - A) re.match()
    - B) re.search()
    - C) re.findall()
    - D) re.sub()

10. What does the `^` symbol in regex denote?
    - A) End of string
    - B) Any character
    - C) Start of string
    - D) Any digit

### Answers

1. B) Any digit
2. B) re.match()
3. B) Match object
4. B) 1 or more occurrences
5. B) A literal dot
6. C) r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
7. B) r'^\(\d{3}\) \d{3}-\d{4}$'
8. B) Password###
9. C) re.findall()
10. C) Start of string

## Dictionaries in Python: Counting Occurrences of Status Codes and Accumulating File Sizes

### Introduction to Dictionaries

A **dictionary** in Python is a collection of key-value pairs. Each key is unique and associated with a value. Dictionaries are useful for situations where you need to look up data quickly, similar to a real-life dictionary where you look up the meaning of a word.

### Creating a Dictionary

Here's how you create a dictionary in Python:

```python
# An empty dictionary
data = {}

# A dictionary with initial data
data = {"name": "Alice", "age": 25, "city": "Nairobi"}
```

In this dictionary:
- `"name"` is a key with the value `"Alice"`.
- `"age"` is a key with the value `25`.
- `"city"` is a key with the value `"Nairobi"`.

### Accessing Values in a Dictionary

You can access values by referring to their keys:

```python
data = {"name": "Alice", "age": 25, "city": "Nairobi"}

print(data["name"])  # Output: Alice
print(data["age"])   # Output: 25
```

### Adding and Updating Entries

You can add new key-value pairs or update existing ones:

```python
data["email"] = "alice@example.com"  # Adds a new key-value pair
data["age"] = 26                     # Updates the value for the key "age"
```

### Removing Entries

To remove a key-value pair:

```python
del data["city"]  # Removes the key "city" and its value
```

### Real-World Example: Counting Occurrences of Status Codes

Let's say you have a list of HTTP status codes from server logs, and you want to count how many times each status code appears.

Here’s how you can do it using a dictionary:

```python
# List of HTTP status codes
status_codes = [200, 404, 200, 301, 404, 500, 200, 301, 404]

# Create an empty dictionary to store the counts
status_count = {}

# Loop through each status code
for code in status_codes:
    if code in status_count:
        status_count[code] += 1
    else:
        status_count[code] = 1

print(status_count)  # Output: {200: 3, 404: 3, 301: 2, 500: 1}
```

### Example Explained

- We start with an empty dictionary `status_count`.
- We loop through each status code in the `status_codes` list.
- For each code, we check if it’s already in the dictionary.
  - If it is, we increment its count.
  - If it’s not, we add it to the dictionary with a count of 1.

### Real-World Example: Accumulating File Sizes

Imagine you have a list of files, each with a type and a size. You want to calculate the total size for each type of file.

Here's how you can do it:

```python
# List of files with type and size
files = [
    {"type": "image", "size": 2048},
    {"type": "text", "size": 512},
    {"type": "image", "size": 1024},
    {"type": "video", "size": 4096},
    {"type": "text", "size": 256}
]

# Create an empty dictionary to accumulate sizes
size_accumulator = {}

# Loop through each file
for file in files:
    file_type = file["type"]
    file_size = file["size"]
    
    if file_type in size_accumulator:
        size_accumulator[file_type] += file_size
    else:
        size_accumulator[file_type] = file_size

print(size_accumulator)  # Output: {'image': 3072, 'text': 768, 'video': 4096}
```

### Example Explained

- We start with an empty dictionary `size_accumulator`.
- We loop through each file in the `files` list.
- For each file, we extract its type and size.
- We check if the file type is already in the dictionary.
  - If it is, we add the file's size to the existing total.
  - If it’s not, we add the file type to the dictionary with its size.

### Benefits of Using Dictionaries

- **Quick Lookups:** You can retrieve values quickly using their keys.
- **Organized Data:** Keeps related data together in a structured way.
- **Flexible:** Can store different types of data, including numbers, strings, lists, and even other dictionaries.

### Summary

Dictionaries in Python are a powerful way to manage data. They allow you to count occurrences of items and accumulate values efficiently. In the examples, we used dictionaries to count HTTP status codes and to accumulate file sizes based on file types, showing their versatility in real-world applications.

### Multiple Choice Questions

1. **What is a dictionary in Python?**
   - A. A collection of ordered items.
   - B. A collection of key-value pairs.
   - C. A collection of values indexed by integers.
   - D. A collection of items of the same type.

   **Answer:** B

2. **How do you add a new key-value pair to a dictionary?**
   - A. `dict.add(key, value)`
   - B. `dict[key] = value`
   - C. `dict.append({key: value})`
   - D. `dict.update(key, value)`

   **Answer:** B

3. **How do you remove an entry from a dictionary?**
   - A. `dict.remove(key)`
   - B. `dict.pop(key)`
   - C. `del dict[key]`
   - D. `dict.delete(key)`

   **Answer:** C

4. **What will `status_count.get(404)` return if `404` is not a key in the dictionary?**
   - A. `0`
   - B. `None`
   - C. `-1`
   - D. `False`

   **Answer:** B

5. **Which method would you use to get all the keys in a dictionary?**
   - A. `dict.keys()`
   - B. `dict.get_keys()`
   - C. `dict.key_set()`
   - D. `dict.all_keys()`

   **Answer:** A

6. **What is the result of the following code?**

   ```python
   data = {"a": 1, "b": 2}
   data["c"] = data["a"] + data["b"]
   print(data)
   ```
   - A. `{"a": 1, "b": 2, "c": 3}`
   - B. `{"a": 1, "b": 2, "c": "12"}`
   - C. `{"a": 1, "b": 2, "c": "ab"}`
   - D. `{"a": 1, "b": 2, "c": 12}`

   **Answer:** A

7. **What does `dict.values()` return?**
   - A. All the keys in the dictionary.
   - B. All the values in the dictionary.
   - C. All the key-value pairs as tuples.
   - D. The total count of entries.

   **Answer:** B

8. **If a key already exists in a dictionary and you assign a new value to it, what happens?**
   - A. The new value is ignored.
   - B. The new value is added as a second entry.
   - C. The new value replaces the old one.
   - D. The program raises an error.

   **Answer:** C

9. **How can you check if a key exists in a dictionary?**
   - A. `if key in dict`
   - B. `if dict.has_key(key)`
   - C. `if key.exists(dict)`
   - D. `if dict.contains(key)`

   **Answer:** A

10. **What is the result of the following code?**

    ```python
    sizes = {"small": 10, "medium": 20}
    sizes["large"] = sizes["medium"] * 2
    print(sizes)
    ```
    - A. `{"small": 10, "medium": 20, "large": 2}`
    - B. `{"small": 10, "medium": 20, "large": "20"}`
    - C. `{"small": 10, "medium": 20, "large": 40}`
    - D. `{"small": 10, "medium": 20, "large": "medium"}`

    **Answer:** C

    ## Exception Handling in Python: Handling Errors During File Reading and Data Processing

### What is Exception Handling?

Exception handling in Python is a mechanism that lets you manage errors gracefully, without stopping the program abruptly. Instead of letting your program crash when it encounters an error, you can handle the error and take appropriate actions.

### Why Use Exception Handling?

1. **Prevent Crashes:** Keeps your program running even when it encounters an error.
2. **Debugging:** Helps you identify and fix issues in your code by catching errors.
3. **User Experience:** Provides informative error messages to users instead of cryptic error codes or stack traces.

### Basic Syntax

The basic structure for handling exceptions in Python is `try-except`:

```python
try:
    # Code that might cause an exception
    risky_operation()
except SomeException:
    # Code that runs if an exception occurs
    handle_error()
```

### Example: Handling Division by Zero

Consider a situation where you want to divide two numbers but want to avoid a crash if the divisor is zero:

```python
try:
    numerator = 10
    divisor = 0
    result = numerator / divisor
except ZeroDivisionError:
    result = None
    print("Error: Cannot divide by zero.")

print(result)  # Output: Error: Cannot divide by zero. None
```

In this example:
- The `try` block contains code that might cause a `ZeroDivisionError`.
- The `except` block catches the `ZeroDivisionError` and handles it by printing an error message and setting `result` to `None`.

### Real-World Example: Handling Errors During File Reading

When working with files, you might encounter errors like a file not existing, permissions issues, or data errors. Here's how you can handle such exceptions:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

### Example Explained

- **`FileNotFoundError`:** This exception is raised if the file you are trying to open does not exist.
- **`PermissionError`:** This exception is raised if you don’t have the required permissions to read the file.
- **`Exception`:** A general exception that catches any other errors that might occur.

### Real-World Example: Handling Data Processing Errors

When processing data, you might encounter invalid data formats or missing values. Here's how you can handle such cases:

```python
data = ["10", "20", "abc", "30"]

for item in data:
    try:
        number = int(item)
        print("Number:", number)
    except ValueError:
        print(f"Error: '{item}' is not a valid number.")
```

### Example Explained

- The `try` block attempts to convert each item in the `data` list to an integer.
- The `except` block catches the `ValueError` if the conversion fails (e.g., for the string `"abc"`), and prints an error message.

### Using `finally` for Cleanup

The `finally` block is used to specify code that should run whether an exception occurred or not. This is useful for cleanup actions like closing a file or releasing resources.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except Exception as e:
    print(f"Error: {e}")
finally:
    file.close()
    print("File closed.")
```

### Combining Multiple Exceptions

You can catch multiple exceptions by combining them in a tuple:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
```

### Example Explained

- `except (FileNotFoundError, PermissionError) as e:` catches both `FileNotFoundError` and `PermissionError`.
- The error message `e` provides details about the exception.

### Benefits of Exception Handling

- **Robust Code:** Makes your programs more robust by handling unexpected situations.
- **Improved Debugging:** Helps identify the location and cause of errors.
- **Enhanced User Experience:** Prevents users from seeing raw error messages or stack traces.

### Summary

Exception handling in Python allows you to manage errors in a controlled way. By using `try-except`, you can catch and handle specific errors, making your code more reliable and user-friendly. The examples demonstrated how to handle common errors during file reading and data processing.

### Multiple Choice Questions

1. **What does the `try` block do in exception handling?**
   - A. Defines a function
   - B. Tests code that may raise an exception
   - C. Handles exceptions
   - D. Ignores errors

   **Answer:** B

2. **What does the `except` block do in exception handling?**
   - A. Ignores errors
   - B. Defines a function
   - C. Executes code when an exception is raised
   - D. Always executes

   **Answer:** C

3. **What will happen if a `try` block raises an exception that is not caught by the corresponding `except` block?**
   - A. The program ignores the error
   - B. The program crashes
   - C. The `finally` block executes
   - D. The error is handled automatically

   **Answer:** B

4. **Which exception is raised for invalid data type conversion?**
   - A. `TypeError`
   - B. `ValueError`
   - C. `IndexError`
   - D. `KeyError`

   **Answer:** B

5. **What will be the output of the following code?**

   ```python
   try:
       print(1 / 0)
   except ZeroDivisionError:
       print("Division by zero!")
   finally:
       print("Done.")
   ```
   - A. `1 / 0`
   - B. `Division by zero!`
   - C. `Done.`
   - D. `Division by zero!` followed by `Done.`

   **Answer:** D

6. **Which exception is raised if a file does not exist?**
   - A. `FileNotFoundError`
   - B. `IOError`
   - C. `OSError`
   - D. `TypeError`

   **Answer:** A

7. **How can you catch multiple exceptions in a single `except` block?**
   - A. `except [Exception1, Exception2]:`
   - B. `except {Exception1, Exception2}:`
   - C. `except (Exception1, Exception2):`
   - D. `except <Exception1, Exception2>:`

   **Answer:** C

8. **What does the `finally` block do?**
   - A. Catches exceptions
   - B. Executes code only if no exceptions are raised
   - C. Executes code whether an exception is raised or not
   - D. Re-raises the exception

   **Answer:** C

9. **Which of the following is a general exception that can catch any error?**
   - A. `BaseException`
   - B. `RuntimeError`
   - C. `SyntaxError`
   - D. `Exception`

   **Answer:** D

10. **What will be the output of the following code if the file `data.txt` does not exist?**

    ```python
    try:
        with open("data.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Operation complete.")
    ```
    - A. `Error: File not found.`
    - B. `File not found.` followed by `Operation complete.`
    - C. `Operation complete.` followed by `File not found.`
    - D. `Error: [Errno 2] No such file or directory: 'data.txt'`

    **Answer:** B

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
