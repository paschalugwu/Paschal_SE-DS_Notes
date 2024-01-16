# SQL Fundamentals

In the ever-evolving landscape of software engineering, the management and manipulation of data form the backbone of dynamic and responsive applications. As developers, understanding the fundamentals of databases and their query language is paramount. This comprehensive note aims to demystify essential concepts, ranging from the fundamental definition of databases to the intricate operations within a relational database using SQL, with a focus on the MySQL database management system. We will explore the creation and alteration of tables, the art of querying and manipulating data, and the powerful features of subqueries and MySQL functions. By the end of this note, you will have a solid grasp of these foundational elements, paving the way for your journey into the realm of database-driven applications.

# SQL Fundamentals: Understanding Databases

## 1. What's a Database?

### Definition:
A **database** is a structured collection of data organized in a way that a computer program can quickly select and retrieve specific pieces of data. It is like an electronic filing system that allows for efficient storage, retrieval, and manipulation of information.

### Components of a Database:

#### 1. **Tables:**
   - In a database, data is organized into tables, which are similar to spreadsheets. Each table contains rows and columns where each row represents a record, and each column represents a field.

   ```sql
   -- Example of creating a 'users' table
   CREATE TABLE users (
       user_id INT PRIMARY KEY,
       username VARCHAR(50),
       email VARCHAR(100)
   );
   ```

#### 2. **Rows and Records:**
   - Rows, also known as records, are individual entries in a table. They contain data corresponding to each field in the table.

   ```sql
   -- Example of inserting data into the 'users' table
   INSERT INTO users (user_id, username, email)
   VALUES (1, 'JohnDoe', 'john.doe@example.com');
   ```

#### 3. **Columns and Fields:**
   - Columns, also known as fields, define the type of data that can be stored in a table. They represent specific attributes of the data.

   ```sql
   -- Example of querying specific columns from the 'users' table
   SELECT username, email FROM users WHERE user_id = 1;
   ```

### Real-World Application:
Understanding databases is crucial in software engineering. Consider a scenario where you are developing a social media application. The user data, such as usernames and emails, would be stored in a database. When a user logs in, the application queries the database to verify their credentials and retrieve their information.

By grasping the concept of databases, you can efficiently design, manage, and interact with data in various real-world projects, making your software more robust and responsive.

# SQL Fundamentals: Understanding Relational Databases

## 2. What's a Relational Database?

### Definition:
A **relational database** is a type of database that organizes data into tables, and the relationships among these tables are defined. It follows the principles of the relational model, where data is stored in a structured manner, allowing for easy retrieval and manipulation.

### Key Concepts of Relational Databases:

#### 1. **Tables and Relationships:**
   - In a relational database, data is stored in multiple tables, each representing a specific entity or concept. The relationships between tables are established using keys.

   ```sql
   -- Example of creating two related tables: 'orders' and 'products'
   CREATE TABLE products (
       product_id INT PRIMARY KEY,
       product_name VARCHAR(100),
       price DECIMAL(10, 2)
   );

   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       product_id INT,
       quantity INT,
       FOREIGN KEY (product_id) REFERENCES products(product_id)
   );
   ```

#### 2. **Primary and Foreign Keys:**
   - A **primary key** uniquely identifies each record in a table. It is used to establish relationships with other tables. A **foreign key** is a field in a table that refers to the primary key in another table.

   ```sql
   -- Example of using primary and foreign keys in the 'orders' table
   INSERT INTO orders (order_id, product_id, quantity)
   VALUES (1, 101, 3);

   -- Retrieving order details along with product information
   SELECT orders.order_id, products.product_name, orders.quantity
   FROM orders
   JOIN products ON orders.product_id = products.product_id
   WHERE orders.order_id = 1;
   ```

#### 3. **Normalization:**
   - Normalization is the process of organizing data to reduce redundancy and improve data integrity. It involves breaking down large tables into smaller, related tables.

   ```sql
   -- Example of normalizing data by creating a 'customers' table
   CREATE TABLE customers (
       customer_id INT PRIMARY KEY,
       customer_name VARCHAR(100),
       email VARCHAR(100)
   );

   -- Adjusting the 'orders' table to reference 'customers' using foreign key
   ALTER TABLE orders
   ADD COLUMN customer_id INT,
   ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
   ```

### Real-World Application:
Relational databases are widely used in applications where data integrity and structure are critical. In an e-commerce platform, for instance, you might have tables for products, orders, and customers. The relationships between these tables allow for efficient retrieval of information, such as getting all products in an order or finding details about a specific customer's orders.

Understanding relational databases is essential for designing robust and scalable systems, ensuring data consistency and providing a foundation for complex data queries in real-world projects.

# SQL Fundamentals: Understanding SQL

## 3. What does SQL stand for?

### Definition:
**SQL** stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases. SQL provides a standardized way to interact with databases, allowing users to perform various operations such as querying data, inserting new records, updating existing records, and deleting records.

### Key Concepts of SQL:

#### 1. **SELECT Statement:**
   - The `SELECT` statement is used to retrieve data from one or more tables. It allows you to specify the columns you want to retrieve and apply conditions to filter the results.

   ```sql
   -- Example of a simple SELECT statement
   SELECT column1, column2
   FROM table_name
   WHERE condition;
   ```

#### 2. **INSERT Statement:**
   - The `INSERT` statement is used to add new records to a table. It specifies the table and the values to be inserted into each column.

   ```sql
   -- Example of an INSERT statement
   INSERT INTO table_name (column1, column2)
   VALUES (value1, value2);
   ```

#### 3. **UPDATE Statement:**
   - The `UPDATE` statement is used to modify existing records in a table. It identifies the table, sets the new values, and applies a condition to determine which records to update.

   ```sql
   -- Example of an UPDATE statement
   UPDATE table_name
   SET column1 = value1, column2 = value2
   WHERE condition;
   ```

#### 4. **DELETE Statement:**
   - The `DELETE` statement is used to remove records from a table based on a specified condition.

   ```sql
   -- Example of a DELETE statement
   DELETE FROM table_name
   WHERE condition;
   ```

### Real-World Application:
SQL is a fundamental tool for interacting with databases in various real-world projects. Consider a scenario where you are developing a blog platform. SQL queries would be used to retrieve blog posts, insert new posts, update existing posts, and delete outdated posts.

In an e-commerce system, SQL would be employed to manage product information, track orders, and handle customer data. The ability to use SQL effectively is crucial for software developers to build applications that can store, retrieve, and manipulate data efficiently.

# SQL Fundamentals: Understanding MySQL

## 4. What's MySQL?

### Definition:
**MySQL** is a popular open-source relational database management system (RDBMS) that uses SQL as its query language. It is widely used for building and managing databases in various applications due to its reliability, scalability, and ease of use. MySQL is particularly favored for web development and is a core component of the LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack.

### Key Features of MySQL:

#### 1. **Data Types:**
   - MySQL supports various data types to store different kinds of information, such as integers, decimals, strings, and dates.

   ```sql
   -- Example of defining data types in a table
   CREATE TABLE students (
       student_id INT PRIMARY KEY,
       student_name VARCHAR(50),
       age INT,
       enrollment_date DATE
   );
   ```

#### 2. **Indexing:**
   - Indexes in MySQL improve the speed of data retrieval operations on a database table. They are created on one or more columns of a table.

   ```sql
   -- Example of creating an index on the 'student_name' column
   CREATE INDEX idx_student_name ON students (student_name);
   ```

#### 3. **Joins:**
   - MySQL supports different types of joins to combine rows from two or more tables based on a related column.

   ```sql
   -- Example of using INNER JOIN to retrieve data from two related tables
   SELECT orders.order_id, customers.customer_name
   FROM orders
   INNER JOIN customers ON orders.customer_id = customers.customer_id;
   ```

#### 4. **Stored Procedures:**
   - Stored procedures in MySQL allow you to execute a set of SQL statements and encapsulate complex logic that can be reused.

   ```sql
   -- Example of creating a stored procedure to get student information by ID
   DELIMITER //
   CREATE PROCEDURE GetStudentByID (IN studentID INT)
   BEGIN
       SELECT * FROM students WHERE student_id = studentID;
   END //
   DELIMITER ;
   ```

### Real-World Application:
MySQL is widely used in various real-world projects. For instance, in a content management system (CMS) where you have user data, blog posts, and comments, MySQL can be employed to store and manage this information efficiently. The ability to use MySQL allows developers to create dynamic and data-driven websites, ensuring seamless interactions between the application and the database.

# SQL Fundamentals: Creating a Database in MySQL

## 5. How to Create a Database in MySQL?

### Creating a Database:
To create a new database in MySQL, you can use the `CREATE DATABASE` statement.

```sql
-- Example of creating a database named 'school'
CREATE DATABASE school;
```

### Selecting a Database:
Once a database is created, you can use the `USE` statement to switch to that database and perform operations within it.

```sql
-- Example of selecting the 'school' database
USE school;
```

### Creating Tables in the Database:
Tables are used to organize and store data within a database. You can create tables with the `CREATE TABLE` statement.

```sql
-- Example of creating a 'students' table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);
```

### Real-World Application:
Imagine you're developing a school management system. The database 'school' could contain tables like 'students,' 'teachers,' and 'courses.' Creating a database allows you to organize information efficiently. The 'students' table, for instance, stores data about students, such as their ID, name, age, and grade. Each table represents a different aspect of the school system, allowing for a well-structured and organized database.

By understanding how to create databases and tables, you gain the foundation to build and manage data in real-world projects, ensuring information is stored in an organized and accessible manner.

# SQL Fundamentals: Understanding DDL and DML

## 6. What does DDL and DML stand for?

### DDL: Data Definition Language

**Definition:**
**DDL** stands for Data Definition Language. It comprises SQL commands that define, alter, or drop database objects such as tables and indexes. DDL is responsible for the structure and schema of the database.

**Key Commands:**
1. **CREATE:** Used to create database objects like tables.
   ```sql
   -- Example of creating a 'students' table
   CREATE TABLE students (
       student_id INT PRIMARY KEY,
       student_name VARCHAR(50),
       age INT,
       grade CHAR(1)
   );
   ```

2. **ALTER:** Modifies the structure of an existing database object.
   ```sql
   -- Example of adding a new column 'address' to the 'students' table
   ALTER TABLE students
   ADD COLUMN address VARCHAR(100);
   ```

3. **DROP:** Deletes a database object.
   ```sql
   -- Example of dropping the 'students' table
   DROP TABLE students;
   ```

### DML: Data Manipulation Language

**Definition:**
**DML** stands for Data Manipulation Language. It includes SQL commands that manipulate data stored in the database. DML is concerned with the content of the database.

**Key Commands:**
1. **INSERT:** Adds new records to a table.
   ```sql
   -- Example of inserting a new student record
   INSERT INTO students (student_id, student_name, age, grade, address)
   VALUES (1, 'John Doe', 16, 'A', '123 Main St');
   ```

2. **UPDATE:** Modifies existing records in a table.
   ```sql
   -- Example of updating the age of a student
   UPDATE students
   SET age = 17
   WHERE student_id = 1;
   ```

3. **DELETE:** Removes records from a table.
   ```sql
   -- Example of deleting a student record
   DELETE FROM students
   WHERE student_id = 1;
   ```

### Real-World Application:
In a real-world scenario, consider an online bookstore database. Using DDL, you could define the structure of the database by creating tables for books, customers, and orders. With DML, you would insert new books into the 'books' table, update customer information, and delete outdated records. DDL and DML work together to ensure the database is well-structured and contains relevant data for efficient operations.

# SQL Fundamentals: Creating and Altering Tables

## 7. How to CREATE or ALTER a Table?

### Creating a Table with `CREATE TABLE`:

The `CREATE TABLE` statement is used to define a new table, specifying its columns along with their data types and constraints.

```sql
-- Example of creating a 'students' table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);
```

In this example:
- `student_id` is an integer column and the primary key.
- `student_name` is a variable character column (string) with a maximum length of 50 characters.
- `age` is an integer column.
- `grade` is a character column with a maximum length of 1.

### Altering a Table with `ALTER TABLE`:

The `ALTER TABLE` statement is used to modify an existing table structure. Common modifications include adding or dropping columns.

#### Adding a Column:
```sql
-- Example of adding a new column 'address' to the 'students' table
ALTER TABLE students
ADD COLUMN address VARCHAR(100);
```

#### Dropping a Column:
```sql
-- Example of dropping the 'address' column from the 'students' table
ALTER TABLE students
DROP COLUMN address;
```

### Real-World Application:

Imagine you are developing a database for a library. Initially, you create a 'books' table with columns like `book_id`, `title`, `author`, and `published_year`. Later, you realize you need to store information about the book's genre. You can use `ALTER TABLE` to add a new column:

```sql
-- Adding a new column 'genre' to the 'books' table
ALTER TABLE books
ADD COLUMN genre VARCHAR(50);
```

This flexibility in altering tables allows you to adapt the database structure as project requirements evolve. Understanding how to create and alter tables is essential for building and maintaining databases in real-world projects.

# SQL Fundamentals: Selecting Data from a Table

## 8. How to SELECT Data from a Table?

### Retrieving Data with `SELECT`:

The `SELECT` statement is used to query and retrieve data from one or more tables. It allows you to specify the columns you want to retrieve, apply conditions to filter the results, and even join multiple tables.

#### Basic `SELECT` Syntax:
```sql
-- Example of selecting all columns from the 'students' table
SELECT * FROM students;
```

#### Selecting Specific Columns:
```sql
-- Example of selecting specific columns from the 'students' table
SELECT student_id, student_name, age
FROM students;
```

### Filtering Data with `WHERE` Clause:

The `WHERE` clause is used to filter the results based on a specified condition.

```sql
-- Example of selecting students older than 18
SELECT student_id, student_name, age
FROM students
WHERE age > 18;
```

### Joining Tables with `JOIN`:

When data is spread across multiple tables, the `JOIN` clause is used to combine rows from two or more tables based on a related column.

```sql
-- Example of joining the 'students' and 'grades' tables
SELECT students.student_id, students.student_name, grades.grade_value
FROM students
JOIN grades ON students.student_id = grades.student_id;
```

### Real-World Application:

Consider a scenario where you are developing a customer management system for an online store. The database has two tables: 'customers' and 'orders.' You can use `SELECT` to retrieve information about customers who made a purchase:

```sql
-- Example of selecting customer and order information
SELECT customers.customer_id, customers.customer_name, orders.order_id, orders.total_amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

Understanding how to use `SELECT` allows you to retrieve specific information, apply conditions to filter data, and combine data from different tables in real-world projects. This is crucial for building applications that can display relevant information to users based on their queries.

# SQL Fundamentals: Inserting, Updating, and Deleting Data

## 9. How to INSERT, UPDATE, or DELETE Data?

### Inserting Data with `INSERT INTO`:

The `INSERT INTO` statement is used to add new records to a table.

#### Basic `INSERT` Syntax:
```sql
-- Example of inserting a new student into the 'students' table
INSERT INTO students (student_id, student_name, age)
VALUES (1, 'John Doe', 16);
```

### Updating Data with `UPDATE`:

The `UPDATE` statement is used to modify existing records in a table.

#### Basic `UPDATE` Syntax:
```sql
-- Example of updating the age of a student in the 'students' table
UPDATE students
SET age = 17
WHERE student_id = 1;
```

### Deleting Data with `DELETE FROM`:

The `DELETE FROM` statement is used to remove records from a table.

#### Basic `DELETE` Syntax:
```sql
-- Example of deleting a student from the 'students' table
DELETE FROM students
WHERE student_id = 1;
```

### Real-World Application:

Imagine you're developing a task management system. Users can add new tasks, update task details, and mark tasks as completed. SQL statements for these operations might look like:

#### Inserting a New Task:
```sql
-- Example of inserting a new task into the 'tasks' table
INSERT INTO tasks (task_id, task_description, due_date, completed)
VALUES (1, 'Write SQL Notes', '2024-01-31', 0);
```

#### Updating Task Details:
```sql
-- Example of updating the due date of a task in the 'tasks' table
UPDATE tasks
SET due_date = '2024-02-15'
WHERE task_id = 1;
```

#### Deleting a Completed Task:
```sql
-- Example of deleting a completed task from the 'tasks' table
DELETE FROM tasks
WHERE task_id = 1 AND completed = 1;
```

Understanding how to insert, update, and delete data is essential for maintaining the integrity and relevance of information in real-world projects. These operations ensure that your database remains up-to-date and reflects the current state of your application.

# SQL Fundamentals: Understanding Subqueries

## 10. What are Subqueries?

### Definition:
A **subquery** (or nested query) is a query nested within another query. It is used to retrieve data that will be used in the main query as a condition or to perform further operations. Subqueries are enclosed in parentheses and can be placed in various parts of a SQL statement.

### Types of Subqueries:

#### 1. **Single-Row Subquery:**
   - A subquery that returns only one row and one column. It can be used in conditions where a single value is expected.

   ```sql
   -- Example of a single-row subquery in a SELECT statement
   SELECT student_name
   FROM students
   WHERE student_id = (SELECT MAX(student_id) FROM students);
   ```

#### 2. **Multiple-Row Subquery:**
   - A subquery that returns multiple rows but only one column. It can be used with operators such as `IN` or `EXISTS`.

   ```sql
   -- Example of a multiple-row subquery with the IN operator
   SELECT student_name
   FROM students
   WHERE grade IN (SELECT grade FROM grades WHERE passing_score = 'A');
   ```

#### 3. **Multiple-Column Subquery:**
   - A subquery that returns multiple rows and columns. It can be used with comparison operators in conditions.

   ```sql
   -- Example of a multiple-column subquery in a WHERE clause
   SELECT student_name
   FROM students
   WHERE (age, grade) = (SELECT MAX(age), 'A' FROM students);
   ```

### Real-World Application:

Consider a scenario where you are developing an online store database. You want to find customers who have made the most recent purchases. You can use a subquery to identify the maximum order date and then retrieve customers who placed orders on that date.

```sql
-- Example of a subquery to find customers with the most recent purchases
SELECT customer_id, customer_name
FROM customers
WHERE order_date = (SELECT MAX(order_date) FROM orders);
```

Subqueries provide a powerful way to perform complex queries and obtain specific information by leveraging the results of inner queries within the main query. Understanding subqueries is crucial for advanced data retrieval and analysis in real-world projects.

# SQL Fundamentals: Using MySQL Functions

## 11. How to Use MySQL Functions?

### Introduction to Functions:

In MySQL, functions are predefined operations that can be performed on data. These functions can manipulate, analyze, or format data to meet specific requirements. Let's explore some commonly used MySQL functions.

### 1. String Functions:

#### `CONCAT()` - Concatenate Strings:
Concatenates two or more strings together.

```sql
-- Example: Concatenating first and last names
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;
```

#### `UPPER()` and `LOWER()` - Convert Case:
Converts a string to uppercase or lowercase.

```sql
-- Example: Converting product names to uppercase
SELECT UPPER(product_name) AS product_name_upper
FROM products;
```

### 2. Numeric Functions:

#### `ROUND()` - Round a Number:
Rounds a numeric value to a specified number of decimal places.

```sql
-- Example: Rounding average ratings to two decimal places
SELECT ROUND(AVG(rating), 2) AS average_rating
FROM reviews;
```

#### `ABS()` - Absolute Value:
Returns the absolute value of a numeric expression.

```sql
-- Example: Calculating the absolute difference between two values
SELECT ABS(column1 - column2) AS absolute_difference
FROM table_name;
```

### 3. Date and Time Functions:

#### `NOW()` - Current Date and Time:
Returns the current date and time.

```sql
-- Example: Retrieving orders placed today
SELECT order_id, order_date
FROM orders
WHERE DATE(order_date) = CURDATE();
```

#### `DATEDIFF()` - Date Difference:
Calculates the difference between two dates.

```sql
-- Example: Calculating the number of days between order and delivery dates
SELECT order_id, DATEDIFF(delivery_date, order_date) AS days_to_delivery
FROM orders;
```

### Real-World Application:

Imagine you are working on an e-commerce platform. You might use string functions to format product names, numeric functions to calculate average ratings, and date functions to track order-related metrics. These functions enhance the ability to analyze and present data in meaningful ways within real-world projects.

Understanding how to use MySQL functions is crucial for manipulating and transforming data effectively, providing valuable insights in various applications.

© [2024] [Paschal Ugwu]
