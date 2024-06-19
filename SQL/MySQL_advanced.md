# Creating Tables with Constraints in SQL

### Introduction

In SQL, tables are created to store data in an organized manner. Constraints are rules applied to the columns in a table to enforce data integrity and accuracy. They ensure that the data adheres to specific standards, which helps maintain the quality and reliability of the database.

### Key Concepts

#### 1. **Constraints in SQL**

Constraints are rules applied to table columns to control the type of data that can be inserted. The main types of constraints include:

- **NOT NULL:** Ensures that a column cannot have a `NULL` value.
- **UNIQUE:** Ensures all values in a column are different.
- **PRIMARY KEY:** Uniquely identifies each record in a table.
- **FOREIGN KEY:** Ensures the value in one column matches a value in another table’s column.
- **CHECK:** Ensures the value in a column meets a specific condition.
- **DEFAULT:** Sets a default value for a column when no value is specified.

### Creating Tables with Constraints

#### **Syntax Overview**

The general syntax for creating a table with constraints is:

```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ...
);
```

#### **Example**

Let's create a `students` table with some constraints:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    enrollment_year INT CHECK (enrollment_year >= 2000),
    major_id INT,
    FOREIGN KEY (major_id) REFERENCES majors(major_id)
);
```

- **`student_id INT PRIMARY KEY`**: The `student_id` column is the primary key, ensuring each student has a unique identifier.
- **`first_name VARCHAR(50) NOT NULL`**: The `first_name` column must contain a value (cannot be NULL).
- **`email VARCHAR(100) UNIQUE`**: The `email` column must have unique values, ensuring no two students can have the same email address.
- **`enrollment_year INT CHECK (enrollment_year >= 2000)`**: The `enrollment_year` must be 2000 or later.
- **`FOREIGN KEY (major_id) REFERENCES majors(major_id)`**: The `major_id` column must match a valid `major_id` in the `majors` table, ensuring referential integrity.

### Real-World Application

Imagine a library system where you need to keep track of books and their loans. You could create two tables, `books` and `loans`, and apply constraints to manage the relationships and data integrity.

**`books` Table:**

```sql
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100),
    published_year INT CHECK (published_year > 0),
    genre VARCHAR(50)
);
```

**`loans` Table:**

```sql
CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
```

- **`book_id`** in the `loans` table must refer to a valid `book_id` in the `books` table, ensuring that every loan is for an existing book.

### Example SQL Statements

**Adding a new student:**

```sql
INSERT INTO students (student_id, first_name, last_name, email, date_of_birth, enrollment_year, major_id)
VALUES (1, 'Alice', 'Smith', 'alice.smith@example.com', '2005-04-23', 2022, 1);
```

**Adding a new book:**

```sql
INSERT INTO books (book_id, title, author, published_year, genre)
VALUES (1, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction');
```

**Loaning a book:**

```sql
INSERT INTO loans (loan_id, book_id, member_id, loan_date, return_date)
VALUES (1, 1, 101, '2024-06-01', '2024-06-15');
```

### Multiple Choice Questions

1. **Which constraint ensures that a column must have unique values?**
    - A) NOT NULL
    - B) UNIQUE
    - C) PRIMARY KEY
    - D) FOREIGN KEY

2. **What does the PRIMARY KEY constraint do?**
    - A) Allows duplicate values in a column
    - B) Ensures the column has unique values and no NULLs
    - C) Links two tables together
    - D) Checks the value against a specific condition

3. **Which of the following is used to link a column to another table’s column?**
    - A) PRIMARY KEY
    - B) FOREIGN KEY
    - C) UNIQUE
    - D) DEFAULT

4. **What constraint would you use to ensure a column cannot have a NULL value?**
    - A) NOT NULL
    - B) CHECK
    - C) UNIQUE
    - D) DEFAULT

5. **In the context of constraints, what does the CHECK constraint do?**
    - A) Ensures all values in a column are different
    - B) Ensures the value meets a specific condition
    - C) Sets a default value for a column
    - D) Ensures the value is not NULL

6. **Which constraint would you use to set a default value for a column?**
    - A) NOT NULL
    - B) DEFAULT
    - C) UNIQUE
    - D) CHECK

7. **Which SQL statement is used to create a table with constraints?**
    - A) INSERT INTO
    - B) CREATE TABLE
    - C) ALTER TABLE
    - D) UPDATE

8. **If a column `salary` should be greater than 0, which constraint should be used?**
    - A) PRIMARY KEY
    - B) NOT NULL
    - C) CHECK
    - D) DEFAULT

9. **Which constraint helps maintain referential integrity between tables?**
    - A) NOT NULL
    - B) CHECK
    - C) FOREIGN KEY
    - D) UNIQUE

10. **In which part of the CREATE TABLE statement do you specify constraints?**
    - A) After the table name
    - B) After each column definition
    - C) At the end of the statement
    - D) After the PRIMARY KEY definition

### Answers

1. B) UNIQUE
2. B) Ensures the column has unique values and no NULLs
3. B) FOREIGN KEY
4. A) NOT NULL
5. B) Ensures the value meets a specific condition
6. B) DEFAULT
7. B) CREATE TABLE
8. C) CHECK
9. C) FOREIGN KEY
10. B) After each column definition

# Optimizing Queries by Adding Indexes

### Introduction

Indexes in SQL are powerful tools for speeding up query performance. They function like an index in a book, allowing the database to quickly locate specific data without scanning the entire table. Understanding how to create and use indexes effectively can significantly enhance the efficiency of database operations.

### Key Concepts

#### 1. **What is an Index?**

An index is a database object that improves the speed of data retrieval operations on a table. It is created on one or more columns of a table and provides a fast lookup mechanism. While indexes speed up read operations, they can slow down write operations (INSERT, UPDATE, DELETE) because the index must also be updated.

#### 2. **Types of Indexes**

- **Single-Column Index:** Created on a single column of a table.
- **Composite Index:** Created on two or more columns of a table.
- **Unique Index:** Ensures all values in the index are distinct.
- **Full-Text Index:** Allows for efficient searching of text columns.
- **Clustered Index:** Determines the physical order of data in a table (each table can have only one clustered index).
- **Non-Clustered Index:** A separate structure from the data rows that points to the location of the data.

### Creating Indexes

#### **Syntax Overview**

To create an index, use the `CREATE INDEX` statement:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

#### **Example**

Let’s create a table `employees` and add indexes:

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    department_id INT
);
```

Create an index on the `last_name` column:

```sql
CREATE INDEX idx_last_name
ON employees (last_name);
```

This index will make searches based on `last_name` faster.

Create a composite index on `department_id` and `last_name`:

```sql
CREATE INDEX idx_department_last_name
ON employees (department_id, last_name);
```

This index is useful for queries that filter by `department_id` and `last_name`.

### Optimizing Queries with Indexes

#### **Using Indexes in Queries**

Indexes can speed up various types of queries, especially those involving `SELECT` statements with `WHERE` clauses, `ORDER BY`, `JOIN`, and `GROUP BY`. Here’s how indexes can optimize different operations:

- **Searching:** Quickly find rows matching specific criteria.
  
  ```sql
  SELECT * FROM employees WHERE last_name = 'Smith';
  ```

- **Sorting:** Efficiently retrieve data in a sorted order.
  
  ```sql
  SELECT * FROM employees ORDER BY last_name;
  ```

- **Joining Tables:** Speed up joins between large tables.
  
  ```sql
  SELECT e.first_name, e.last_name, d.department_name
  FROM employees e
  JOIN departments d ON e.department_id = d.department_id;
  ```

- **Grouping:** Improve performance of aggregate functions.

  ```sql
  SELECT department_id, COUNT(*)
  FROM employees
  GROUP BY department_id;
  ```

#### **Practical Example**

Consider a web application with a `products` table:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT
);
```

To speed up searches by `category`, create an index:

```sql
CREATE INDEX idx_category
ON products (category);
```

For an online store that frequently checks stock status, an index on `stock_quantity` can help:

```sql
CREATE INDEX idx_stock_quantity
ON products (stock_quantity);
```

### Best Practices for Using Indexes

- **Selective Columns:** Use indexes on columns frequently used in `WHERE`, `JOIN`, or `ORDER BY` clauses.
- **Composite Index Order:** Place the most selective column first (the column that reduces the search space the most).
- **Avoid Over-Indexing:** Too many indexes can slow down write operations and consume more storage.
- **Monitor Performance:** Regularly check query performance and adjust indexes as needed.

### Example SQL Statements

**Querying with an index:**

```sql
SELECT * FROM employees WHERE department_id = 3;
```

With an index on `department_id`, this query runs faster because the database uses the index to locate rows.

**Sorting with an index:**

```sql
SELECT * FROM products ORDER BY price;
```

If there’s an index on `price`, sorting is more efficient.

**Joining with an index:**

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```

Indexes on `department_id` in both tables speed up the join operation.

### Multiple Choice Questions

1. **What is the primary purpose of an index in SQL?**
    - A) Increase storage size
    - B) Speed up data retrieval
    - C) Decrease query complexity
    - D) Slow down write operations

2. **Which index type allows a column to have only unique values?**
    - A) Composite Index
    - B) Full-Text Index
    - C) Unique Index
    - D) Clustered Index

3. **How many clustered indexes can a table have?**
    - A) 0
    - B) 1
    - C) 2
    - D) Unlimited

4. **Which SQL statement creates an index?**
    - A) CREATE TABLE
    - B) CREATE INDEX
    - C) CREATE VIEW
    - D) CREATE SEQUENCE

5. **Which of the following best describes a composite index?**
    - A) An index on a single column
    - B) An index that ensures unique values
    - C) An index on multiple columns
    - D) An index used for full-text search

6. **Which operation is most likely to benefit from an index?**
    - A) INSERT
    - B) DELETE
    - C) SELECT with WHERE clause
    - D) UPDATE

7. **What is a potential downside of having too many indexes?**
    - A) Increased query performance
    - B) Reduced storage requirements
    - C) Slower write operations
    - D) Easier data retrieval

8. **Which clause in a SELECT statement is often sped up by an index?**
    - A) FROM
    - B) WHERE
    - C) INSERT INTO
    - D) VALUES

9. **What should be considered when creating a composite index?**
    - A) The order of columns in the index
    - B) The data type of the columns
    - C) Only the first column's selectivity
    - D) Avoiding all SELECT queries

10. **What is a non-clustered index?**
    - A) An index that determines the physical order of data
    - B) An index separate from the data rows, pointing to data locations
    - C) An index on full-text columns
    - D) An index that automatically updates with every change

### Answers

1. B) Speed up data retrieval
2. C) Unique Index
3. B) 1
4. B) CREATE INDEX
5. C) An index on multiple columns
6. C) SELECT with WHERE clause
7. C) Slower write operations
8. B) WHERE
9. A) The order of columns in the index
10. B) An index separate from the data rows, pointing to data locations

# Stored Procedures and Functions in MySQL

### Introduction

Stored procedures and functions are powerful tools in MySQL that allow you to store complex queries and operations on the database server. They encapsulate SQL code that can be executed repeatedly without needing to rewrite the code each time. This can simplify application logic and improve performance.

### Key Concepts

#### 1. **Stored Procedures**

A stored procedure is a set of SQL statements that you can save and reuse. It allows you to encapsulate logic that might involve multiple operations, such as inserting, updating, or deleting records, and even control structures like loops and conditionals.

**Advantages:**
- **Modularity:** Encapsulates complex logic into manageable chunks.
- **Performance:** Reduces network traffic since multiple SQL statements are executed on the server side.
- **Reusability:** Can be called multiple times from various parts of an application.

#### 2. **Functions**

A function is similar to a stored procedure but is used to return a single value. Functions can be used in SQL statements like `SELECT` or `WHERE`, and they help in performing calculations or operations that return a result.

**Differences from Stored Procedures:**
- Functions return a single value, whereas procedures do not necessarily return a value.
- Functions can be used directly in SQL queries, procedures are invoked using the `CALL` statement.

### Implementing Stored Procedures

#### **Syntax Overview**

The basic syntax for creating a stored procedure is:

```sql
CREATE PROCEDURE procedure_name (IN parameter_name datatype, OUT parameter_name datatype, ...)
BEGIN
    -- SQL statements
END;
```

- `IN` parameters: Accept input values.
- `OUT` parameters: Return values.
- `INOUT` parameters: Accept input and return values.

#### **Example**

Let's create a stored procedure to add a new employee:

```sql
DELIMITER //
CREATE PROCEDURE AddEmployee(IN first_name VARCHAR(50), IN last_name VARCHAR(50), IN email VARCHAR(100))
BEGIN
    INSERT INTO employees (first_name, last_name, email)
    VALUES (first_name, last_name, email);
END //
DELIMITER ;
```

- **`DELIMITER //`** changes the default delimiter to `//` so that the procedure can contain `;`.
- **`DELIMITER ;`** resets the delimiter back to `;`.

To call this procedure:

```sql
CALL AddEmployee('John', 'Doe', 'john.doe@example.com');
```

### Implementing Functions

#### **Syntax Overview**

The basic syntax for creating a function is:

```sql
CREATE FUNCTION function_name (parameter_name datatype, ...)
RETURNS datatype
BEGIN
    -- SQL statements
    RETURN value;
END;
```

- `RETURNS datatype`: Specifies the type of the value returned by the function.

#### **Example**

Let's create a function to calculate the total price of products in stock:

```sql
CREATE FUNCTION CalculateTotalStockValue()
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total DECIMAL(10, 2);
    SELECT SUM(price * stock_quantity) INTO total FROM products;
    RETURN total;
END;
```

To use this function:

```sql
SELECT CalculateTotalStockValue();
```

### Real-World Application

#### **Stored Procedure Example**

Consider a retail system where you need to update inventory after a sale. A stored procedure can handle this:

```sql
DELIMITER //
CREATE PROCEDURE UpdateInventory(IN product_id INT, IN quantity_sold INT)
BEGIN
    UPDATE products
    SET stock_quantity = stock_quantity - quantity_sold
    WHERE product_id = product_id;
END //
DELIMITER ;
```

Call this procedure after a sale:

```sql
CALL UpdateInventory(1, 3);
```

#### **Function Example**

In an analytics application, you might need to calculate the average order value. A function can help:

```sql
CREATE FUNCTION AverageOrderValue()
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE average DECIMAL(10, 2);
    SELECT AVG(total_amount) INTO average FROM orders;
    RETURN average;
END;
```

Use this function to get the average order value:

```sql
SELECT AverageOrderValue();
```

### Error Handling

You can handle errors in stored procedures using the `DECLARE` handler statement:

```sql
DELIMITER //
CREATE PROCEDURE SafeUpdateInventory(IN product_id INT, IN quantity_sold INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Error handling code
        ROLLBACK;
    END;
    START TRANSACTION;
    UPDATE products
    SET stock_quantity = stock_quantity - quantity_sold
    WHERE product_id = product_id;
    COMMIT;
END //
DELIMITER ;
```

### Example SQL Statements

**Create a procedure to delete an employee:**

```sql
DELIMITER //
CREATE PROCEDURE DeleteEmployee(IN employee_id INT)
BEGIN
    DELETE FROM employees WHERE employee_id = employee_id;
END //
DELIMITER ;
```

**Call the procedure:**

```sql
CALL DeleteEmployee(101);
```

**Create a function to calculate discount price:**

```sql
CREATE FUNCTION CalculateDiscountPrice(price DECIMAL(10, 2), discount_rate DECIMAL(5, 2))
RETURNS DECIMAL(10, 2)
BEGIN
    RETURN price - (price * discount_rate / 100);
END;
```

**Use the function in a query:**

```sql
SELECT product_name, CalculateDiscountPrice(price, 10) AS discounted_price
FROM products;
```

### Multiple Choice Questions

1. **What is the primary purpose of a stored procedure in MySQL?**
    - A) Return a single value
    - B) Encapsulate and execute multiple SQL statements
    - C) Enforce foreign key constraints
    - D) Define table structures

2. **Which keyword is used to call a stored procedure?**
    - A) RUN
    - B) EXECUTE
    - C) CALL
    - D) PERFORM

3. **What is a key difference between a function and a stored procedure?**
    - A) Functions cannot return values
    - B) Stored procedures cannot be reused
    - C) Functions return a single value, procedures may not
    - D) Stored procedures can be used in `SELECT` statements

4. **What keyword specifies the data type of the value returned by a function?**
    - A) RETURNS
    - B) RETURN
    - C) OUTPUT
    - D) RESULT

5. **Which statement correctly defines an `IN` parameter for a stored procedure?**
    - A) `IN parameter_name datatype`
    - B) `OUT parameter_name datatype`
    - C) `PARAM parameter_name datatype`
    - D) `INPUT parameter_name datatype`

6. **How do you declare an `OUT` parameter in a stored procedure?**
    - A) `INOUT parameter_name datatype`
    - B) `OUT parameter_name datatype`
    - C) `OUTPUT parameter_name datatype`
    - D) `EXTERNAL parameter_name datatype`

7. **What is the correct syntax to create a function that returns a `VARCHAR` value?**
    - A) `CREATE FUNCTION function_name() RETURNS VARCHAR`
    - B) `CREATE FUNCTION function_name() RETURNS STRING`
    - C) `CREATE FUNCTION function_name() RETURNS CHAR`
    - D) `CREATE FUNCTION function_name() RETURNS TEXT`

8. **In which type of SQL statement can a function be used?**
    - A) `SELECT`
    - B) `DELETE`
    - C) `INSERT`
    - D) All of the above

9. **What keyword is used to start a block of SQL statements in a stored procedure?**
    - A) `START`
    - B) `BEGIN`
    - C) `OPEN`
    - D) `LAUNCH`

10. **How do you change the default delimiter in MySQL to write a stored procedure?**
    - A) `CHANGE DELIMITER`
    - B) `SET DELIMITER`
    - C) `ALTER DELIMITER`
    - D) `DELIMITER`

### Answers

1. B) Encapsulate and execute multiple SQL statements
2. C) CALL
3. C) Functions return a single value, procedures may not
4. A) RETURNS
5. A) IN parameter_name datatype
6. B) OUT parameter_name datatype
7. A) CREATE FUNCTION function_name() RETURNS VARCHAR
8. D) All of the above
9. B) BEGIN
10. D) DELIMITER

# Views in MySQL

### Introduction

Views in MySQL are virtual tables based on the result-set of a `SELECT` query. They do not store data physically but present it from one or more tables. Views simplify complex queries, enhance security by restricting access to certain data, and can represent complex joins or calculations as simple tables.

### Key Concepts

#### 1. **What is a View?**

A view is a saved query that you can treat as a table. It is a way to present data in a specific format without altering the actual tables. Think of a view as a window through which you can see specific data from one or more tables.

**Advantages:**
- **Simplification:** Simplifies complex queries by breaking them down into manageable parts.
- **Security:** Limits access to sensitive data by exposing only certain fields to the user.
- **Data Abstraction:** Provides a level of abstraction that hides the complexity of underlying table structures.

#### 2. **Creating a View**

To create a view, use the `CREATE VIEW` statement followed by the view name and the `SELECT` query that defines it.

**Syntax Overview:**

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Example

Consider a table `employees`:

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);
```

To create a view showing only employee names and departments:

```sql
CREATE VIEW employee_view AS
SELECT first_name, last_name, department
FROM employees;
```

This view `employee_view` can be queried like a table:

```sql
SELECT * FROM employee_view;
```

### Working with Views

#### **Querying a View**

You use the same `SELECT` statements on views as you would on tables:

```sql
SELECT * FROM employee_view WHERE department = 'HR';
```

#### **Updating Data Through Views**

Views can be updatable if they meet certain conditions, such as not containing aggregate functions or joins. If the view is updatable, you can perform `INSERT`, `UPDATE`, and `DELETE` operations on it, and these operations will affect the underlying table.

Example of an updatable view:

```sql
CREATE VIEW salary_view AS
SELECT employee_id, salary
FROM employees;
```

Update the salary of an employee through the view:

```sql
UPDATE salary_view
SET salary = 70000
WHERE employee_id = 1;
```

#### **Dropping a View**

To remove a view, use the `DROP VIEW` statement:

```sql
DROP VIEW employee_view;
```

This will delete the view but not the underlying table.

### Real-World Application

#### **Simplifying Complex Queries**

Imagine a database for a school management system with several tables (`students`, `courses`, `enrollments`). You need to frequently get a list of students and their enrolled courses. Instead of writing complex joins every time, you create a view:

```sql
CREATE VIEW student_courses AS
SELECT s.student_id, s.first_name, s.last_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;
```

Query this view to get student course information easily:

```sql
SELECT * FROM student_courses;
```

#### **Enhancing Security**

If a company wants to allow access only to a subset of employee data (like just the name and department, but not the salary), a view can be created:

```sql
CREATE VIEW public_employee_info AS
SELECT first_name, last_name, department
FROM employees;
```

Then, permissions can be set on this view to restrict access.

### Example SQL Statements

**Create a view to show high-salary employees:**

```sql
CREATE VIEW high_salary_employees AS
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 50000;
```

**Query this view:**

```sql
SELECT * FROM high_salary_employees;
```

**Create a view with a calculated column:**

```sql
CREATE VIEW employee_summary AS
SELECT first_name, last_name, salary, salary * 12 AS annual_salary
FROM employees;
```

**Use this view:**

```sql
SELECT * FROM employee_summary;
```

### Best Practices

- **Naming Conventions:** Use clear and descriptive names for views.
- **Performance:** Be aware that complex views might degrade performance if they encapsulate very complex queries.
- **Security:** Use views to expose only the necessary data to users, enhancing security.

### Multiple Choice Questions

1. **What is a view in MySQL?**
    - A) A physical table that stores data
    - B) A virtual table based on the result-set of a `SELECT` query
    - C) A function that returns a single value
    - D) A temporary table that holds data for a session

2. **How do you create a view in MySQL?**
    - A) `CREATE TABLE`
    - B) `CREATE INDEX`
    - C) `CREATE VIEW`
    - D) `CREATE FUNCTION`

3. **Which SQL statement is used to delete a view?**
    - A) `DELETE VIEW`
    - B) `REMOVE VIEW`
    - C) `DROP VIEW`
    - D) `ALTER VIEW`

4. **Which of the following can be a part of a view definition?**
    - A) `INSERT`
    - B) `UPDATE`
    - C) `SELECT`
    - D) `DELETE`

5. **What happens when you query a view?**
    - A) Data is stored permanently in the view
    - B) The query on the view is run against the underlying tables
    - C) A new table is created
    - D) The view must be rebuilt every time

6. **Can you perform `INSERT` operations on a view?**
    - A) Yes, always
    - B) No, never
    - C) Yes, if the view is updatable
    - D) Only on specific days

7. **Which of the following is a benefit of using views?**
    - A) They always improve performance
    - B) They store additional data
    - C) They simplify complex queries
    - D) They remove the need for primary keys

8. **How can views enhance security?**
    - A) By storing all data in a separate table
    - B) By allowing access only to specific parts of the data
    - C) By encrypting the data
    - D) By running faster queries

9. **What is an updatable view?**
    - A) A view that can be altered after creation
    - B) A view that supports `INSERT`, `UPDATE`, and `DELETE` operations
    - C) A view that automatically updates its data
    - D) A view that combines data from multiple databases

10. **What is a potential downside of using views?**
    - A) They can simplify complex queries
    - B) They might degrade performance for complex queries
    - C) They provide an additional layer of security
    - D) They can return data from multiple tables

### Answers

1. B) A virtual table based on the result-set of a `SELECT` query
2. C) CREATE VIEW
3. C) DROP VIEW
4. C) SELECT
5. B) The query on the view is run against the underlying tables
6. C) Yes, if the view is updatable
7. C) They simplify complex queries
8. B) By allowing access only to specific parts of the data
9. B) A view that supports `INSERT`, `UPDATE`, and `DELETE` operations
10. B) They might degrade performance for complex queries

# Triggers in MySQL

### Introduction

Triggers in MySQL are special types of stored procedures that automatically execute or fire when certain events occur on a table. Triggers can be used to enforce business rules, validate data, update or modify data in other tables, and perform various auditing and logging tasks.

### Key Concepts

#### 1. **What is a Trigger?**

A trigger is a database object that is activated when a specified event happens for a table. The event can be an `INSERT`, `UPDATE`, or `DELETE` operation. Triggers can help automate processes and enforce constraints by running predefined SQL code when changes occur in the database.

**Advantages:**
- **Automation:** Automatically execute code in response to table changes.
- **Consistency:** Ensure that changes adhere to business rules and maintain data integrity.
- **Auditing:** Track changes in data and user activities.

#### 2. **Types of Triggers**

Triggers are defined based on timing and the type of event that activates them:

- **Timing:**
  - **BEFORE:** Executes before the triggering event.
  - **AFTER:** Executes after the triggering event.
- **Event:**
  - **INSERT:** Fires when a new row is inserted.
  - **UPDATE:** Fires when a row is updated.
  - **DELETE:** Fires when a row is deleted.

### Implementing Triggers

#### **Syntax Overview**

The basic syntax for creating a trigger is:

```sql
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
BEGIN
    -- SQL statements
END;
```

- `trigger_name`: Name of the trigger.
- `{BEFORE | AFTER}`: Specifies whether the trigger fires before or after the event.
- `{INSERT | UPDATE | DELETE}`: Specifies the event that activates the trigger.
- `ON table_name`: Specifies the table on which the trigger acts.
- `FOR EACH ROW`: Indicates the trigger executes once for each row affected by the triggering event.
- `BEGIN ... END`: Block containing the SQL statements to execute.

#### **Example**

Consider a table `orders` that records customer orders:

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2)
);
```

To create a trigger that automatically sets the `order_date` to the current date if not provided:

```sql
CREATE TRIGGER set_order_date
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_date IS NULL THEN
        SET NEW.order_date = CURDATE();
    END IF;
END;
```

- **`NEW`**: Refers to the new row being inserted.

### Working with Triggers

#### **Example of AFTER INSERT Trigger**

To log order creation in a separate table `order_log`:

```sql
CREATE TABLE order_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER log_order_creation
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_log (order_id)
    VALUES (NEW.order_id);
END;
```

#### **Example of BEFORE UPDATE Trigger**

To validate that the `amount` field is positive before updating an order:

```sql
CREATE TRIGGER validate_order_amount
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.amount <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Order amount must be positive';
    END IF;
END;
```

#### **Example of AFTER DELETE Trigger**

To archive deleted orders into an `archived_orders` table:

```sql
CREATE TABLE archived_orders AS SELECT * FROM orders WHERE 1=0; -- Creates an empty table with the same structure

CREATE TRIGGER archive_deleted_order
AFTER DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO archived_orders (order_id, customer_id, order_date, amount)
    VALUES (OLD.order_id, OLD.customer_id, OLD.order_date, OLD.amount);
END;
```

- **`OLD`**: Refers to the row that is being deleted or updated.

### Real-World Application

#### **Data Auditing**

In a banking system, it's crucial to track changes to the `accounts` table. Create a trigger to log changes:

```sql
CREATE TABLE account_changes (
    change_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    old_balance DECIMAL(10, 2),
    new_balance DECIMAL(10, 2),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER audit_account_changes
AFTER UPDATE ON accounts
FOR EACH ROW
BEGIN
    INSERT INTO account_changes (account_id, old_balance, new_balance)
    VALUES (OLD.account_id, OLD.balance, NEW.balance);
END;
```

#### **Enforcing Business Rules**

For an inventory management system, ensure the quantity of products never goes negative:

```sql
CREATE TRIGGER check_quantity
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    IF NEW.quantity < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Quantity cannot be negative';
    END IF;
END;
```

### Example SQL Statements

**Create a BEFORE INSERT trigger to set a default value:**

```sql
CREATE TRIGGER set_default_amount
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.amount IS NULL THEN
        SET NEW.amount = 0.00;
    END IF;
END;
```

**Create an AFTER DELETE trigger to log deletions:**

```sql
CREATE TRIGGER log_order_deletion
AFTER DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_log (order_id, log_date)
    VALUES (OLD.order_id, NOW());
END;
```

**Create a BEFORE UPDATE trigger to enforce data validation:**

```sql
CREATE TRIGGER validate_customer_id
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.customer_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer ID cannot be null';
    END IF;
END;
```

### Best Practices

- **Use Descriptive Names:** Name triggers clearly to indicate their purpose.
- **Limit Complexity:** Keep trigger logic simple to avoid performance issues and maintain readability.
- **Avoid Recursive Triggers:** Ensure that triggers do not call other triggers unnecessarily, leading to infinite loops.
- **Test Thoroughly:** Ensure triggers work as expected under various scenarios.

### Multiple Choice Questions

1. **What is a trigger in MySQL?**
    - A) A stored procedure that runs at a scheduled time
    - B) A set of rules to validate data
    - C) A database object that automatically executes in response to certain events on a table
    - D) A type of index to speed up queries

2. **Which of the following events can activate a trigger?**
    - A) `SELECT`
    - B) `INSERT`
    - C) `CREATE`
    - D) `ALTER`

3. **How do you specify when a trigger should execute relative to an event?**
    - A) `WHEN`
    - B) `WHERE`
    - C) `BEFORE` or `AFTER`
    - D) `TIMING`

4. **What does the `FOR EACH ROW` clause in a trigger definition mean?**
    - A) The trigger applies to every row in the table
    - B) The trigger will execute once for each row affected by the event
    - C) The trigger affects only the new rows
    - D) The trigger affects only the old rows

5. **How can you refer to the row that will be inserted in a `BEFORE INSERT` trigger?**
    - A) `OLD`
    - B) `NEW`
    - C) `INSERTED`
    - D) `CURRENT`

6. **What keyword is used to generate a custom error message in a trigger?**
    - A) `THROW`
    - B) `SIGNAL`
    - C) `RAISE`
    - D) `ERROR`

7. **Can a trigger call other triggers?**
    - A) Yes, but it should be avoided due to potential infinite loops
    - B) No, triggers are isolated
    - C) Yes, with no limitations
    - D) Only with special permissions

8. **Which statement correctly creates a trigger to update a log table after deleting a record?**
    - A) `CREATE TRIGGER update_log AFTER DELETE ON table_name FOR EACH ROW ...`
    - B) `CREATE TRIGGER update_log BEFORE DELETE ON table_name FOR EACH ROW ...`
    - C) `CREATE TRIGGER update_log AFTER INSERT ON table_name FOR EACH ROW ...`
    - D) `CREATE TRIGGER update_log BEFORE INSERT ON table_name FOR EACH ROW ...`

9. **What is the purpose of the `BEGIN ... END` block in a trigger?**
    - A) To mark the end of the trigger definition
    - B) To indicate the start and end of the SQL statements executed by the trigger
    - C) To set the scope of the trigger
    - D) To loop through each row in the table

10. **Which of the following is not a type of trigger in MySQL?**
    - A) `BEFORE INSERT`
    - B) `AFTER UPDATE`
    - C) `AFTER SELECT`
    - D) `BEFORE DELETE`

### Answers

1. C) A database object that automatically executes in response to certain events on a table
2. B) INSERT
3. C) BEFORE or AFTER
4. B) The trigger will execute once for each row affected by the event
5. B) NEW
6. B) SIGNAL
7. A) Yes, but it should be avoided due to potential infinite loops
8. A) CREATE TRIGGER update_log AFTER DELETE ON table_name FOR EACH ROW ...
9. B) To indicate the start and end of the SQL statements executed by the trigger
10. C) AFTER SELECT
