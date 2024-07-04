# Personally Identifiable Information (PII)

## Introduction
Personally Identifiable Information (PII) is any data that could potentially identify a specific individual. This information is crucial because it can be used to identify, contact, or locate a person, either alone or combined with other data.

## Examples of PII

1. **Full Name**:
    - **Example**: John Doe
    - **Application**: Used in social media profiles, official documents, and personal identification.

2. **Social Security Number (SSN)**:
    - **Example**: 123-45-6789
    - **Application**: Used in tax filings, credit applications, and government records.

3. **Email Address**:
    - **Example**: johndoe@example.com
    - **Application**: Used for communication, account registration, and authentication.

4. **Phone Number**:
    - **Example**: (555) 555-5555
    - **Application**: Used for contact, verification, and customer service.

5. **Home Address**:
    - **Example**: 123 Main Street, Anytown, USA
    - **Application**: Used for shipping, billing, and identification purposes.

6. **Driver’s License Number**:
    - **Example**: D1234567
    - **Application**: Used for driving records, identification, and verification.

7. **Passport Number**:
    - **Example**: 987654321
    - **Application**: Used for international travel, identification, and visa applications.

8. **Credit Card Information**:
    - **Example**: 4111 1111 1111 1111
    - **Application**: Used for financial transactions, online shopping, and billing.

9. **Date of Birth**:
    - **Example**: January 1, 2000
    - **Application**: Used for age verification, identification, and security questions.

10. **Biometric Data**:
    - **Example**: Fingerprints, facial recognition
    - **Application**: Used for security, access control, and identification.

## Real-World Application
### Example Project: Secure E-commerce Website

When building a secure e-commerce website, it's important to understand how to handle PII to protect users' data.

**Steps**:
1. **User Registration**:
    - Collect full name, email address, phone number, and home address.
    - Example Code Snippet (Python):
      ```python
      user_data = {
          "full_name": "John Doe",
          "email": "johndoe@example.com",
          "phone": "555-555-5555",
          "address": "123 Main Street, Anytown, USA"
      }
      ```

2. **Payment Processing**:
    - Collect credit card information.
    - Ensure data is encrypted and securely stored.
    - Example Code Snippet (Python):
      ```python
      from cryptography.fernet import Fernet

      key = Fernet.generate_key()
      cipher_suite = Fernet(key)

      credit_card_number = "4111111111111111"
      encrypted_cc = cipher_suite.encrypt(credit_card_number.encode())

      print(f"Encrypted Credit Card: {encrypted_cc}")
      ```

3. **Authentication**:
    - Use email and password for login.
    - Example Code Snippet (Python):
      ```python
      def authenticate_user(email, password):
          # Dummy function to authenticate user
          if email == "johndoe@example.com" and password == "securepassword":
              return "Authentication successful"
          else:
              return "Authentication failed"
      
      print(authenticate_user("johndoe@example.com", "securepassword"))
      ```

## Chapter End Questions

1. Which of the following is an example of PII?
   a) Favorite color
   b) Email address
   c) Number of pets
   d) Preferred vacation destination

2. Why is PII important?
   a) It can be used to identify a person.
   b) It can be used to decorate a website.
   c) It is used for website analytics.
   d) It can be used to set website themes.

3. What should be done to protect PII in an e-commerce website?
   a) Display it on the home page.
   b) Encrypt it and store securely.
   c) Share it with third-party advertisers.
   d) Ignore it.

4. Which of the following is NOT PII?
   a) Home address
   b) Social Security Number
   c) Credit card number
   d) Favorite movie

5. What information is typically collected during user registration on a website?
   a) Date of birth
   b) Email address
   c) Phone number
   d) All of the above

6. What is a common use of biometric data?
   a) Identifying movie preferences
   b) Access control and security
   c) Collecting survey responses
   d) Determining favorite foods

7. How should credit card information be handled in a secure system?
   a) Written down and stored in a safe
   b) Encrypted and securely stored
   c) Sent via email
   d) Posted on social media

8. Which of the following is used for age verification?
   a) Passport number
   b) Driver’s license number
   c) Date of birth
   d) Email address

9. What is the main reason to use encryption for PII?
   a) To speed up data processing
   b) To enhance user experience
   c) To protect sensitive information
   d) To improve website design

10. Which PII is often used for online shopping and billing?
    a) Social Security Number
    b) Credit card information
    c) Favorite food
    d) Preferred vacation destination

## Answers

1. b) Email address
2. a) It can be used to identify a person.
3. b) Encrypt it and store securely.
4. d) Favorite movie
5. d) All of the above
6. b) Access control and security
7. b) Encrypted and securely stored
8. c) Date of birth
9. c) To protect sensitive information
10. b) Credit card information

# Implementing a Log Filter to Obfuscate PII Fields

## Introduction
Logging is an essential part of software development for monitoring and debugging. However, logs can contain Personally Identifiable Information (PII) that must be protected. Implementing a log filter to obfuscate PII fields ensures sensitive information is not exposed in logs.

## Steps to Implement a Log Filter

1. **Identify PII Fields**:
   - Determine which fields in your logs contain PII.
   - Examples: email addresses, phone numbers, credit card numbers.

2. **Create an Obfuscation Function**:
   - Define how PII fields will be obfuscated (e.g., replacing characters with asterisks).

3. **Integrate the Filter into Your Logging System**:
   - Apply the obfuscation function to PII fields before logging the data.

### Example Project: Logging User Information with PII Obfuscation

#### Step 1: Identify PII Fields
In this example, we will identify `email`, `phone`, and `credit_card` as PII fields.

#### Step 2: Create an Obfuscation Function
Define a function to obfuscate PII fields.
```python
def obfuscate_pii(data):
    if "email" in data:
        data["email"] = obfuscate_email(data["email"])
    if "phone" in data:
        data["phone"] = obfuscate_phone(data["phone"])
    if "credit_card" in data:
        data["credit_card"] = obfuscate_credit_card(data["credit_card"])
    return data

def obfuscate_email(email):
    local, domain = email.split("@")
    obfuscated_local = local[0] + "***" + local[-1]
    return obfuscated_local + "@" + domain

def obfuscate_phone(phone):
    return phone[:3] + "****" + phone[-2:]

def obfuscate_credit_card(credit_card):
    return credit_card[:4] + "********" + credit_card[-4:]
```

#### Step 3: Integrate the Filter into Your Logging System
Apply the obfuscation function to PII fields before logging.
```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def log_user_info(user_data):
    obfuscated_data = obfuscate_pii(user_data)
    logging.info(f"User Data: {obfuscated_data}")

# Example user data containing PII
user_data = {
    "email": "john.doe@example.com",
    "phone": "555-123-4567",
    "credit_card": "4111111111111111"
}

# Log user data with PII obfuscation
log_user_info(user_data)
```

## Real-World Application
In a real-world project, you might have various user data logs. Ensuring that PII is obfuscated before logging helps in maintaining user privacy and complying with data protection regulations like GDPR.

### Example Application in an E-commerce System
Consider an e-commerce system where user purchase transactions are logged. Obfuscating PII ensures that sensitive information like email addresses, phone numbers, and credit card numbers are not exposed in logs.

## Chapter End Questions

1. What is the purpose of a log filter in the context of PII?
   a) To enhance log readability
   b) To protect sensitive information
   c) To speed up logging
   d) To improve system performance

2. Which of the following is an example of PII?
   a) User's shopping cart contents
   b) User's email address
   c) User's purchase history
   d) User's preferred language

3. In the obfuscation function for emails, which part of the email is typically masked?
   a) The domain
   b) The entire email
   c) The local part (before the @ symbol)
   d) The top-level domain

4. How should a phone number be obfuscated in logs?
   a) Replace with random numbers
   b) Mask middle digits with asterisks
   c) Remove it entirely
   d) Convert to a hash

5. Which Python module is commonly used for logging?
   a) os
   b) sys
   c) logging
   d) random

6. In the provided code, what does the function `obfuscate_pii` do?
   a) Logs PII fields
   b) Identifies PII fields
   c) Obfuscates PII fields
   d) Deletes PII fields

7. What is the output of obfuscating the email "jane.doe@example.com" using the given `obfuscate_email` function?
   a) j***e@example.com
   b) j****e@example.com
   c) j***e@****.com
   d) ja***doe@example.com

8. When logging user data, why is it important to obfuscate credit card information?
   a) To reduce log file size
   b) To comply with data protection regulations
   c) To make logs more readable
   d) To prevent data loss

9. In the example code, which function is responsible for logging the user data?
   a) obfuscate_pii
   b) obfuscate_email
   c) log_user_info
   d) logging.info

10. What is the main benefit of obfuscating PII before logging it?
    a) Improved system performance
    b) Enhanced user experience
    c) Protection of user privacy
    d) Easier debugging

## Answers

1. b) To protect sensitive information
2. b) User's email address
3. c) The local part (before the @ symbol)
4. b) Mask middle digits with asterisks
5. c) logging
6. c) Obfuscates PII fields
7. a) j***e@example.com
8. b) To comply with data protection regulations
9. c) log_user_info
10. c) Protection of user privacy

# Encrypting a Password and Checking the Validity of an Input Password

## Introduction
Password encryption is a critical aspect of security in software development. It ensures that passwords are stored securely and protects user data from unauthorized access. Checking the validity of an input password against the stored encrypted password is essential for authentication.

## Steps to Encrypt a Password and Validate an Input Password

1. **Choose a Secure Hashing Algorithm**:
   - Use a hashing algorithm designed for password security, such as bcrypt.

2. **Encrypt the Password**:
   - Hash the password using the chosen algorithm.

3. **Store the Hashed Password**:
   - Save the hashed password in the database instead of the plain text password.

4. **Validate the Input Password**:
   - Hash the input password and compare it with the stored hashed password.

### Example Project: User Authentication System

#### Step 1: Choose a Secure Hashing Algorithm
For this example, we will use the `bcrypt` library in Python.

#### Step 2: Encrypt the Password
Hash the password using bcrypt.
```python
import bcrypt

def encrypt_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# Example usage
plain_password = "my_secure_password"
hashed_password = encrypt_password(plain_password)
print(f"Encrypted Password: {hashed_password}")
```

#### Step 3: Store the Hashed Password
Store the hashed password in the database. For simplicity, we will just print it here.

#### Step 4: Validate the Input Password
Hash the input password and compare it with the stored hashed password.
```python
def check_password(plain_password, hashed_password):
    # Check if the input password matches the hashed password
    return bcrypt.checkpw(plain_password.encode(), hashed_password)

# Example usage
input_password = "my_secure_password"
is_valid = check_password(input_password, hashed_password)
print(f"Password Valid: {is_valid}")
```

## Real-World Application
In a real-world project, such as a web application with user accounts, password encryption and validation are crucial for securing user data. When a user registers, their password is encrypted and stored. During login, the input password is validated against the stored hashed password.

### Example Application in a Web Application
Consider a web application where users register and log in. Passwords are encrypted and stored securely to protect user data. During login, the input password is validated to authenticate the user.

## Chapter End Questions

1. Which algorithm is recommended for hashing passwords in the example?
   a) MD5
   b) SHA-1
   c) bcrypt
   d) AES

2. What is the purpose of generating a salt in password encryption?
   a) To make the password longer
   b) To make each hashed password unique
   c) To shorten the encryption time
   d) To convert the password to uppercase

3. How is the input password validated against the stored hashed password?
   a) By comparing the plain text password with the hashed password
   b) By re-hashing the input password and comparing it with the stored hash
   c) By storing both the plain text and hashed password
   d) By converting the hashed password back to plain text

4. What library is used in the example to encrypt passwords?
   a) hashlib
   b) crypt
   c) bcrypt
   d) pycrypto

5. Why is it important to store only the hashed password instead of the plain text password?
   a) To reduce storage space
   b) To speed up the login process
   c) To protect user data from unauthorized access
   d) To make the password easy to remember

6. In the provided code, what does the `bcrypt.gensalt()` function do?
   a) Generates a random password
   b) Encrypts the password
   c) Generates a salt for hashing
   d) Converts the password to a hash

7. What is the output of the `check_password` function if the input password is correct?
   a) True
   b) False
   c) The hashed password
   d) The plain text password

8. How is the hashed password stored in a database?
   a) As plain text
   b) As a hashed value
   c) As an encrypted value
   d) As a binary value

9. What happens if an attacker gains access to the hashed passwords in the database?
   a) They can immediately use the passwords
   b) They can decrypt the passwords
   c) They will still need to crack the hashes
   d) They can use the passwords to create new accounts

10. Why is bcrypt preferred over MD5 for password hashing?
    a) bcrypt is faster
    b) bcrypt is easier to implement
    c) bcrypt is more secure
    d) bcrypt produces shorter hashes

## Answers

1. c) bcrypt
2. b) To make each hashed password unique
3. b) By re-hashing the input password and comparing it with the stored hash
4. c) bcrypt
5. c) To protect user data from unauthorized access
6. c) Generates a salt for hashing
7. a) True
8. b) As a hashed value
9. c) They will still need to crack the hashes
10. c) bcrypt is more secure

# Authenticating to a Database Using Environment Variables

## Introduction
Authenticating to a database using environment variables is a secure method to manage sensitive credentials. Environment variables keep sensitive information like database usernames and passwords out of your source code, reducing the risk of exposure.

## Steps to Authenticate to a Database Using Environment Variables

1. **Set Up Environment Variables**:
   - Store database credentials in environment variables.

2. **Access Environment Variables in Your Code**:
   - Use a library or built-in functions to access environment variables.

3. **Use Environment Variables to Connect to the Database**:
   - Pass the credentials retrieved from the environment variables to your database connection setup.

### Example Project: Connecting to a MySQL Database

#### Step 1: Set Up Environment Variables
Set environment variables for your database credentials.
- On a Unix-based system, add the following to your `.bashrc` or `.bash_profile`:
  ```sh
  export DB_HOST='localhost'
  export DB_USER='myuser'
  export DB_PASSWORD='mypassword'
  export DB_NAME='mydatabase'
  ```

- On Windows, set environment variables through the System Properties.

#### Step 2: Access Environment Variables in Your Code
Use the `os` library in Python to access the environment variables.
```python
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
```

#### Step 3: Use Environment Variables to Connect to the Database
Use the credentials to connect to the MySQL database using a library like `mysql-connector-python`.
```python
import mysql.connector
import os

# Accessing environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connecting to the database
try:
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    if connection.is_connected():
        print("Successfully connected to the database")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        connection.close()
        print("Database connection closed")
```

## Real-World Application
In real-world projects, managing database credentials securely is crucial. Environment variables allow you to separate configuration from code, making it easier to change credentials without modifying your source code and reducing the risk of accidental exposure.

### Example Application in a Web Application
Consider a web application that connects to a database to retrieve user data. By storing the database credentials in environment variables, you ensure that sensitive information is not hardcoded in your application, enhancing security and making it easier to manage different environments (development, testing, production).

## Chapter End Questions

1. Why is it recommended to use environment variables for database credentials?
   a) To improve application performance
   b) To keep sensitive information secure and separate from source code
   c) To make the code more readable
   d) To enable faster database connections

2. Which Python library is used to access environment variables?
   a) sys
   b) os
   c) env
   d) configparser

3. How do you set an environment variable in a Unix-based system?
   a) Use the `set` command
   b) Add an entry to the `.bashrc` or `.bash_profile`
   c) Modify the `hosts` file
   d) Use the `envconfig` tool

4. In the provided code, what does the `os.getenv('DB_HOST')` function do?
   a) Sets the environment variable `DB_HOST`
   b) Gets the value of the environment variable `DB_HOST`
   c) Deletes the environment variable `DB_HOST`
   d) Checks if the environment variable `DB_HOST` is set

5. Why is it important to close the database connection?
   a) To free up database resources
   b) To save application memory
   c) To prevent unauthorized access
   d) To speed up subsequent connections

6. What should you do if the database connection fails?
   a) Retry the connection immediately
   b) Log the error and notify the user
   c) Ignore the error and continue
   d) Restart the application

7. Which of the following is a benefit of using environment variables for database credentials?
   a) Hardcoding credentials in the source code
   b) Making credentials easily accessible to unauthorized users
   c) Simplifying the process of changing credentials
   d) Exposing credentials to the version control system

8. How do you access the environment variable `DB_PASSWORD` in Python?
   a) `os.environ['DB_PASSWORD']`
   b) `os.getenv('DB_PASSWORD')`
   c) `os.environ.get('DB_PASSWORD')`
   d) All of the above

9. What is the purpose of the `mysql.connector.connect` function in the provided code?
   a) To create a new MySQL database
   b) To establish a connection to the MySQL database
   c) To close the connection to the MySQL database
   d) To execute SQL queries

10. Which of the following is a common practice when using environment variables?
    a) Storing them in the source code repository
    b) Keeping them secret and not sharing them publicly
    c) Hardcoding them in the application code
    d) Ignoring them for local development

## Answers

1. b) To keep sensitive information secure and separate from source code
2. b) os
3. b) Add an entry to the `.bashrc` or `.bash_profile`
4. b) Gets the value of the environment variable `DB_HOST`
5. a) To free up database resources
6. b) Log the error and notify the user
7. c) Simplifying the process of changing credentials
8. d) All of the above
9. b) To establish a connection to the MySQL database
10. b) Keeping them secret and not sharing them publicly

# Efficient and Secure Data Logging with Python

## Introduction
In this guide, we will learn how to create a secure and efficient data logging system in Python. This includes creating a log filter to obfuscate Personally Identifiable Information (PII), implementing a custom log formatter, setting up a logger, connecting to a secure database, and filtering data from the database before logging it.

## 0. Regex-ing

### Function: `filter_datum`
This function uses regular expressions to obfuscate specified fields in a log message.

#### Arguments:
- `fields`: A list of strings representing all fields to obfuscate.
- `redaction`: A string representing by what the field will be obfuscated.
- `message`: A string representing the log line.
- `separator`: A string representing by which character is separating all fields in the log line.

#### Implementation:
```python
import re

def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(f'{field}=[^{separator}]+' for field in fields)
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)
```

## 1. Log Formatter

### Class: `RedactingFormatter`
This class extends `logging.Formatter` to filter values in incoming log records using the `filter_datum` function.

#### Implementation:
```python
import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record):
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
```

## 2. Create Logger

### Function: `get_logger`
This function creates and configures a logger to handle user data logging.

#### Implementation:
```python
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def get_logger():
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
```

## 3. Connect to Secure Database

### Function: `get_db`
This function connects to a secure MySQL database using credentials stored in environment variables.

#### Implementation:
```python
import mysql.connector
import os

def get_db():
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )
```

## 4. Read and Filter Data

### Function: `main`
This function retrieves all rows from the `users` table in the database, formats the data, and logs it using the configured logger.

#### Implementation:
```python
def main():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    
    logger = get_logger()

    for row in cursor.fetchall():
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; ssn={row[3]}; password={row[4]}; ip={row[5]}; last_login={row[6]}; user_agent={row[7]};"
        logger.info(message)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
```

## Chapter End Questions

1. What does the `filter_datum` function use to obfuscate specified fields in a log message?
   a) String replacement
   b) Regular expressions
   c) Loop iteration
   d) Conditional statements

2. Which class in the provided code extends `logging.Formatter`?
   a) LoggingHandler
   b) RedactingFormatter
   c) LogFilter
   d) FormatterHandler

3. What is the purpose of the `RedactingFormatter` class?
   a) To change log levels
   b) To format log messages
   c) To filter values in log records
   d) To handle log propagation

4. In the `get_logger` function, what type of handler is added to the logger?
   a) FileHandler
   b) StreamHandler
   c) HTTPHandler
   d) SocketHandler

5. Which environment variable is NOT used in the `get_db` function?
   a) PERSONAL_DATA_DB_USERNAME
   b) PERSONAL_DATA_DB_PASSWORD
   c) PERSONAL_DATA_DB_PORT
   d) PERSONAL_DATA_DB_HOST

6. What library is used to connect to the MySQL database in the `get_db` function?
   a) psycopg2
   b) pymysql
   c) mysql-connector-python
   d) sqlite3

7. What should be the output of the `filter_datum` function if the message is `name=John; email=john@example.com;` and the field to obfuscate is `name`?
   a) `name=***; email=john@example.com;`
   b) `name=John; email=***;`
   c) `name=John; email=john@example.com;`
   d) `name=***; email=***;`

8. What is the format string used in the `RedactingFormatter` class?
   a) `[HOLBERTON] %(name)s %(levelname)s %(message)s`
   b) `[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s`
   c) `[HOLBERTON] %(levelname)s %(message)s`
   d) `[HOLBERTON] %(asctime)-15s %(name)s: %(message)s`

9. In the `main` function, what is the purpose of `cursor.fetchall()`?
   a) To execute a SQL query
   b) To retrieve all rows from the query result
   c) To close the database cursor
   d) To commit the database transaction

10. Why is it important to use environment variables for database credentials?
    a) To improve database performance
    b) To keep credentials secure and out of source code
    c) To make credentials easier to access
    d) To enable faster database connections

## Answers

1. b) Regular expressions
2. b) RedactingFormatter
3. c) To filter values in log records
4. b) StreamHandler
5. c) PERSONAL_DATA_DB_PORT
6. c) mysql-connector-python
7. a) `name=***; email=john@example.com;`
8. b) `[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s`
9. b) To retrieve all rows from the query result
10. b) To keep credentials secure and out of source code

# Encrypting Passwords and Checking Validity

## Introduction
Ensuring the security of user passwords is crucial in any application. Storing passwords in plain text is highly insecure. Instead, passwords should be hashed and salted before storage. This guide will cover how to securely hash passwords using the bcrypt package and how to validate passwords against their hashes.

## 5. Encrypting Passwords

### Function: `hash_password`
This function takes a plain text password, hashes it using bcrypt, and returns the hashed password.

#### Implementation:
1. **Import the bcrypt package**: This package provides a robust hashing mechanism.
2. **Generate a salt**: Salting adds an extra layer of security.
3. **Hash the password**: Combine the password with the salt and hash it.

```python
import bcrypt

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
```

### Example Usage
```python
plain_password = "my_secure_password"
hashed_password = hash_password(plain_password)
print(hashed_password)
```

## 6. Check Valid Password

### Function: `is_valid`
This function checks whether a provided plain text password matches a previously hashed password.

#### Implementation:
1. **Import the bcrypt package**: Ensure bcrypt is available for use.
2. **Check the password**: Use bcrypt to verify if the plain text password matches the hashed password.

```python
def is_valid(hashed_password: bytes, password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)
```

### Example Usage
```python
plain_password = "my_secure_password"
hashed_password = hash_password(plain_password)

# Valid password check
print(is_valid(hashed_password, plain_password))  # Output: True

# Invalid password check
print(is_valid(hashed_password, "wrong_password"))  # Output: False
```

## Real-World Application
In real-world projects, ensuring password security is a critical component of user authentication systems. Properly hashed and salted passwords protect against various attacks, such as brute force attacks and rainbow table attacks.

### Example Application in a Web Application
Consider a web application that requires user authentication. When a user registers, their password is hashed using the `hash_password` function and stored in the database. When the user attempts to log in, the provided password is checked against the stored hash using the `is_valid` function.

## Chapter End Questions

1. What is the primary purpose of hashing passwords before storing them?
   a) To reduce storage space
   b) To ensure password security
   c) To make the passwords readable
   d) To speed up the login process

2. Which package is used in the provided code to hash passwords?
   a) hashlib
   b) cryptography
   c) bcrypt
   d) secure

3. What is the purpose of salting a password before hashing?
   a) To make the password longer
   b) To enhance security by adding randomness
   c) To convert the password to bytes
   d) To make the password case-insensitive

4. In the `hash_password` function, what does the `gensalt` function do?
   a) Hashes the password
   b) Generates a random salt
   c) Encrypts the password
   d) Converts the password to a string

5. What type does the `hash_password` function return?
   a) str
   b) int
   c) bytes
   d) bool

6. In the `is_valid` function, which method is used to check if the password matches the hashed password?
   a) `bcrypt.compare`
   b) `bcrypt.verify`
   c) `bcrypt.check`
   d) `bcrypt.checkpw`

7. What is the return type of the `is_valid` function?
   a) str
   b) int
   c) bytes
   d) bool

8. Why is it important not to store passwords in plain text?
   a) To save storage space
   b) To protect user privacy and security
   c) To make the database queries faster
   d) To ensure passwords are unique

9. Which of the following is a benefit of using bcrypt for hashing passwords?
   a) It's faster than other hashing algorithms
   b) It provides automatic salting and multiple rounds of hashing
   c) It stores passwords in plain text
   d) It converts passwords to uppercase

10. What is the correct way to encode a plain text password before hashing with bcrypt?
    a) `password.encode('utf-8')`
    b) `str(password)`
    c) `password.upper()`
    d) `password.lower()`

## Answers

1. b) To ensure password security
2. c) bcrypt
3. b) To enhance security by adding randomness
4. b) Generates a random salt
5. c) bytes
6. d) bcrypt.checkpw
7. d) bool
8. b) To protect user privacy and security
9. b) It provides automatic salting and multiple rounds of hashing
10. a) password.encode('utf-8')

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
