### Basic Types in TypeScript JavaScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore the basic types in TypeScript JavaScript and how they can be applied in real-world projects.

### Basic Types

TypeScript supports several basic types that can be used to define the data type of a variable. These types include:

- **Number**: This type is used to define a numeric value. It can be a whole number or a decimal number.

```typescript
let age: number = 25;
```

- **String**: This type is used to define a sequence of characters. It can be a single character or a sequence of multiple characters.

```typescript
let name: string = "John";
```

- **Boolean**: This type is used to define a logical value that can be either true or false.

```typescript
let isAdmin: boolean = true;
```

- **Array**: This type is used to define a collection of values of the same type. It can be a collection of numbers, strings, or any other type.

```typescript
let numbers: number[] = [1, 2, 3];
```

- **Object**: This type is used to define a collection of key-value pairs. It can be a collection of any type.

```typescript
let person: { name: string, age: number } = { name: "John", age: 25 };
```

### Type Inference

TypeScript can automatically infer the type of a variable based on the value assigned to it. This is known as type inference.

```typescript
let age = 25;
```

In this example, TypeScript will automatically infer the type of `age` as `number`.

### Type Annotations

Type annotations are used to explicitly specify the type of a variable. This is useful when you want to ensure that a variable has a specific type.

```typescript
let age: number = 25;
```

In this example, the type of `age` is explicitly specified as `number`.

### Real-World Applications

Basic types in TypeScript JavaScript are used extensively in real-world projects. For example, in a user authentication system, you might use a `boolean` type to store whether a user is an administrator or not.

```typescript
let isAdmin: boolean = true;
```

### MCQs

1. What is the basic type used to define a numeric value in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: Number

2. What is the basic type used to define a sequence of characters in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: String

3. What is the basic type used to define a logical value that can be either true or false in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: Boolean

4. What is the basic type used to define a collection of values of the same type in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: Array

5. What is the basic type used to define a collection of key-value pairs in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Object

Answer: Object

6. What is type inference in TypeScript JavaScript?
   - The process of explicitly specifying the type of a variable
   - The process of automatically inferring the type of a variable based on the value assigned to it
   - The process of defining a variable without specifying its type
   - The process of defining a variable with a specific type

Answer: The process of automatically inferring the type of a variable based on the value assigned to it

7. What are type annotations in TypeScript JavaScript?
   - The process of explicitly specifying the type of a variable
   - The process of automatically inferring the type of a variable based on the value assigned to it
   - The process of defining a variable without specifying its type
   - The process of defining a variable with a specific type

Answer: The process of explicitly specifying the type of a variable

8. What is the basic type used to define a whole number in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: Number

9. What is the basic type used to define a sequence of multiple characters in TypeScript JavaScript?
   - Number
   - String
   - Boolean
   - Array

Answer: String

10. What is the basic type used to define a logical value that can be either true or false in TypeScript JavaScript?
    - Number
    - String
    - Boolean
    - Array

Answer: Boolean

### Interfaces, Classes, and Functions in TypeScript JavaScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore interfaces, classes, and functions in TypeScript JavaScript and how they can be applied in real-world projects.

### Interfaces

Interfaces are used to define the structure of an object. They are used to ensure that an object has specific properties and methods.

```typescript
interface Person {
  name: string;
  age: number;
}

let person: Person = {
  name: "John",
  age: 25
};
```

### Classes

Classes are used to define the structure and behavior of an object. They are used to create objects that have specific properties and methods.

```typescript
class Person {
  private name: string;
  private age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  public sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

let person = new Person("John", 25);
person.sayHello();
```

### Functions

Functions are used to define a block of code that can be executed multiple times. They are used to perform specific tasks.

```typescript
function add(a: number, b: number): number {
  return a + b;
}

let result = add(5, 3);
console.log(result);
```

### Real-World Applications

Interfaces, classes, and functions in TypeScript JavaScript are used extensively in real-world projects. For example, in a user authentication system, you might use a class to define a user and its properties and methods.

```typescript
class User {
  private username: string;
  private password: string;

  constructor(username: string, password: string) {
    this.username = username;
    this.password = password;
  }

  public login() {
    // Login logic
  }
}

let user = new User("john", "password123");
user.login();
```

### MCQs

1. What is the purpose of an interface in TypeScript JavaScript?
   - To define the structure of an object
   - To define the behavior of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure of an object

2. What is the purpose of a class in TypeScript JavaScript?
   - To define the structure and behavior of an object
   - To define the structure of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

3. What is the purpose of a function in TypeScript JavaScript?
   - To define a block of code that can be executed multiple times
   - To define the structure of an object
   - To define the behavior of an object
   - To define a collection of values of the same type

Answer: To define a block of code that can be executed multiple times

4. What is the purpose of type annotations in TypeScript JavaScript?
   - To define the structure of an object
   - To define the behavior of an object
   - To define a block of code that can be executed multiple times
   - To define the type of a variable

Answer: To define the type of a variable

5. What is the purpose of type inference in TypeScript JavaScript?
   - The process of explicitly specifying the type of a variable
   - The process of automatically inferring the type of a variable based on the value assigned to it
   - The process of defining a variable without specifying its type
   - The process of defining a variable with a specific type

Answer: The process of automatically inferring the type of a variable based on the value assigned to it

6. What is the purpose of a constructor in a class in TypeScript JavaScript?
   - To define the structure and behavior of an object
   - To define the structure of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

7. What is the purpose of a method in a class in TypeScript JavaScript?
   - To define the structure and behavior of an object
   - To define the structure of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

8. What is the purpose of a property in a class in TypeScript JavaScript?
   - To define the structure and behavior of an object
   - To define the structure of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

9. What is the purpose of a function in a class in TypeScript JavaScript?
   - To define the structure and behavior of an object
   - To define the structure of an object
   - To define a block of code that can be executed multiple times
   - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

10. What is the purpose of a class in TypeScript JavaScript?
    - To define the structure and behavior of an object
    - To define the structure of an object
    - To define a block of code that can be executed multiple times
    - To define a collection of values of the same type

Answer: To define the structure and behavior of an object

### Working with the DOM and TypeScript

The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the structure of a document as a tree of nodes, each of which represents an element, attribute, or piece of text. TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore how to work with the DOM and TypeScript.

### Accessing the DOM

To access the DOM, you can use the `document` object, which is the root of the DOM tree. You can access elements by their ID, class, or tag name.

```typescript
// Accessing an element by ID
let element = document.getElementById('myId');

// Accessing elements by class
let elements = document.getElementsByClassName('myClass');

// Accessing elements by tag name
let elements = document.getElementsByTagName('div');
```

### Manipulating the DOM

You can manipulate the DOM by adding, removing, or modifying elements.

```typescript
// Adding an element
let newElement = document.createElement('div');
newElement.textContent = 'New Element';
document.body.appendChild(newElement);

// Removing an element
let elementToRemove = document.getElementById('myId');
document.body.removeChild(elementToRemove);

// Modifying an element
let element = document.getElementById('myId');
element.textContent = 'Modified Element';
```

### TypeScript and the DOM

TypeScript can be used to add type safety to your DOM manipulation code. You can define the type of an element or a collection of elements.

```typescript
// Defining the type of an element
let element: HTMLDivElement = document.getElementById('myId');

// Defining the type of a collection of elements
let elements: HTMLCollectionOf<HTMLDivElement> = document.getElementsByClassName('myClass');
```

### Real-World Applications

Working with the DOM and TypeScript is used extensively in real-world projects. For example, in a web application, you might use TypeScript to define the structure and behavior of a user interface component.

```typescript
// Defining a user interface component
interface UIComponent {
  element: HTMLDivElement;
  init(): void;
}

class Button implements UIComponent {
  element: HTMLDivElement;

  constructor() {
    this.element = document.createElement('button');
    this.element.textContent = 'Click Me';
  }

  init(): void {
    document.body.appendChild(this.element);
  }
}

let button = new Button();
button.init();
```

### MCQs

1. What is the purpose of the `document` object in TypeScript?
   - To access the DOM
   - To manipulate the DOM
   - To define the structure of a document
   - To define the behavior of a document

Answer: To access the DOM

2. How do you access an element by ID in TypeScript?
   - Using `document.getElementById('myId')`
   - Using `document.getElementById('myId', 'myClass')`
   - Using `document.getElementById('myId', 'myTag')`
   - Using `document.getElementById('myId', 'myId')`

Answer: Using `document.getElementById('myId')`

3. How do you access elements by class in TypeScript?
   - Using `document.getElementsByClassName('myClass')`
   - Using `document.getElementById('myClass')`
   - Using `document.getElementsByTagName('myClass')`
   - Using `document.getElementById('myClass', 'myTag')`

Answer: Using `document.getElementsByClassName('myClass')`

4. How do you access elements by tag name in TypeScript?
   - Using `document.getElementsByTagName('div')`
   - Using `document.getElementById('div')`
   - Using `document.getElementsByClassName('div')`
   - Using `document.getElementById('div', 'myTag')`

Answer: Using `document.getElementsByTagName('div')`

5. What is the purpose of type annotations in TypeScript when working with the DOM?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To define the type of a variable

Answer: To add type safety to your DOM manipulation code

6. What is the purpose of the `appendChild` method in TypeScript?
   - To add an element to the DOM
   - To remove an element from the DOM
   - To modify an element in the DOM
   - To define the structure of a document

Answer: To add an element to the DOM

7. What is the purpose of the `removeChild` method in TypeScript?
   - To add an element to the DOM
   - To remove an element from the DOM
   - To modify an element in the DOM
   - To define the structure of a document

Answer: To remove an element from the DOM

8. What is the purpose of the `textContent` property in TypeScript?
   - To set the text content of an element
   - To get the text content of an element
   - To set the HTML content of an element
   - To get the HTML content of an element

Answer: To set the text content of an element

9. What is the purpose of the `innerHTML` property in TypeScript?
   - To set the HTML content of an element
   - To get the HTML content of an element
   - To set the text content of an element
   - To get the text content of an element

Answer: To set the HTML content of an element

10. What is the purpose of the `addEventListener` method in TypeScript?
    - To add an event listener to an element
    - To remove an event listener from an element
    - To modify an event listener on an element
    - To define the structure of a document

Answer: To add an event listener to an element

### Generic Types in TypeScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore generic types in TypeScript and how they can be applied in real-world projects.

### What are Generic Types?

Generic types are a feature in TypeScript that allows you to create reusable functions and classes that can work with different data types. They are defined using type parameters, which are placeholders for the actual types that will be used when the function or class is called.

### Example of Generic Types

Here is an example of a generic function that can work with different data types:

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let result1 = identity<string>('Hello');
let result2 = identity<number>(42);
```

In this example, the `identity` function is defined with a type parameter `T`. This means that the function can work with any data type. When the function is called with a string argument, the type of `arg` is inferred as `string`. Similarly, when the function is called with a number argument, the type of `arg` is inferred as `number`.

### Real-World Applications

Generic types are used extensively in real-world projects. For example, in a web application, you might use a generic type to define a reusable function for validating user input.

```typescript
function validateInput<T>(input: T): boolean {
  // Validation logic
  return true;
}

let isValidString = validateInput<string>('Hello');
let isValidNumber = validateInput<number>(42);
```

### MCQs

1. What is the purpose of generic types in TypeScript?
   - To create reusable functions and classes that can work with different data types
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

2. How do you define a generic type in TypeScript?
   - Using the `interface` keyword
   - Using the `class` keyword
   - Using the `function` keyword with type parameters
   - Using the `type` keyword

Answer: Using the `function` keyword with type parameters

3. What is the purpose of type parameters in generic types?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To create reusable functions and classes that can work with different data types

Answer: To create reusable functions and classes that can work with different data types

4. How do you use a generic type in a function?
   - By defining the type of the function's return value
   - By defining the type of the function's parameters
   - By using the `as` keyword to cast the function's return value
   - By using the `as` keyword to cast the function's parameters

Answer: By defining the type of the function's parameters

5. What is the purpose of the `identity` function in TypeScript?
   - To create a reusable function that can work with different data types
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code

Answer: To create a reusable function that can work with different data types

6. How do you use a generic type in a class?
   - By defining the type of the class's properties
   - By defining the type of the class's methods
   - By using the `as` keyword to cast the class's properties
   - By using the `as` keyword to cast the class's methods

Answer: By defining the type of the class's properties

7. What is the purpose of the `validateInput` function in TypeScript?
   - To create a reusable function that can work with different data types
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code

Answer: To create a reusable function that can work with different data types

8. How do you use a generic type in a type alias?
   - By defining the type of the type alias
   - By using the `as` keyword to cast the type alias
   - By using the `type` keyword to define the type alias
   - By using the `interface` keyword to define the type alias

Answer: By defining the type of the type alias

9. What is the purpose of the `type` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To create reusable functions and classes that can work with different data types

Answer: To create reusable functions and classes that can work with different data types

10. How do you use a generic type in a type guard?
    - By defining the type of the type guard
    - By using the `as` keyword to cast the type guard
    - By using the `type` keyword to define the type guard
    - By using the `interface` keyword to define the type guard

Answer: By defining the type of the type guard

### Using Namespaces in TypeScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore how to use namespaces in TypeScript and how they can be applied in real-world projects.

### What are Namespaces?

Namespaces are a way to organize and structure your code in TypeScript. They are used to group related functions, classes, and variables together, making it easier to manage and maintain your codebase.

### Example of Namespaces

Here is an example of how to use namespaces in TypeScript:

```typescript
// Define a namespace
namespace MyNamespace {
  export function greet(name: string) {
    console.log(`Hello, ${name}`);
  }
}

// Use the namespace
MyNamespace.greet('John');
```

In this example, we define a namespace called `MyNamespace` and export a function `greet` that takes a name as a parameter. We then use the namespace to call the `greet` function.

### Real-World Applications

Namespaces are used extensively in real-world projects. For example, in a web application, you might use a namespace to define a reusable module for handling user authentication.

```typescript
// Define a namespace
namespace Auth {
  export function login(username: string, password: string) {
    // Login logic
  }
  export function logout() {
    // Logout logic
  }
}

// Use the namespace
Auth.login('john', 'password123');
Auth.logout();
```

### MCQs

1. What is the purpose of namespaces in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To organize and structure your code
   - To add type safety to your DOM manipulation code

Answer: To organize and structure your code

2. How do you define a namespace in TypeScript?
   - Using the `interface` keyword
   - Using the `class` keyword
   - Using the `function` keyword with type parameters
   - Using the `namespace` keyword

Answer: Using the `namespace` keyword

3. What is the purpose of the `export` keyword in namespaces?
   - To define the structure of a document
   - To define the behavior of a document
   - To make functions and classes available outside the namespace
   - To add type safety to your DOM manipulation code

Answer: To make functions and classes available outside the namespace

4. How do you use a namespace in a function?
   - By defining the type of the function's return value
   - By defining the type of the function's parameters
   - By using the `as` keyword to cast the function's return value
   - By using the `as` keyword to cast the function's parameters

Answer: By defining the type of the function's parameters

5. What is the purpose of the `namespace` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To organize and structure your code
   - To add type safety to your DOM manipulation code

Answer: To organize and structure your code

6. How do you use a namespace in a class?
   - By defining the type of the class's properties
   - By defining the type of the class's methods
   - By using the `as` keyword to cast the class's properties
   - By using the `as` keyword to cast the class's methods

Answer: By defining the type of the class's properties

7. What is the purpose of the `Auth` namespace in the example?
   - To define the structure of a document
   - To define the behavior of a document
   - To organize and structure your code
   - To add type safety to your DOM manipulation code

Answer: To organize and structure your code

8. How do you use a namespace in a type alias?
   - By defining the type of the type alias
   - By using the `as` keyword to cast the type alias
   - By using the `type` keyword to define the type alias
   - By using the `interface` keyword to define the type alias

Answer: By defining the type of the type alias

9. What is the purpose of the `type` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To create reusable functions and classes that can work with different data types

Answer: To create reusable functions and classes that can work with different data types

10. How do you use a namespace in a type guard?
    - By defining the type of the type guard
    - By using the `as` keyword to cast the type guard
    - By using the `type` keyword to define the type guard
    - By using the `interface` keyword to define the type guard

Answer: By defining the type of the type guard

### Merging Declarations in TypeScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore how to merge declarations in TypeScript and how they can be applied in real-world projects.

### What are Merged Declarations?

Merged declarations are a way to combine multiple declarations into a single declaration. This is useful when you have multiple declarations that have the same name but different types.

### Example of Merged Declarations

Here is an example of how to merge declarations in TypeScript:

```typescript
// Declare a variable
let x: number = 5;

// Merge the declaration
x = 'hello';
```

In this example, we declare a variable `x` with the type `number` and assign it the value `5`. Then, we merge the declaration by assigning a new value `'hello'` to `x`. This is allowed because TypeScript is able to infer the type of `x` as `string` based on the new value.

### Real-World Applications

Merging declarations is used extensively in real-world projects. For example, in a web application, you might use merged declarations to handle different types of user input.

```typescript
// Declare a function
function greet(name: string) {
  console.log(`Hello, ${name}`);
}

// Merge the declaration
greet('John');
greet(42);
```

In this example, we declare a function `greet` that takes a `string` as a parameter. Then, we merge the declaration by calling the function with different types of arguments. This is allowed because TypeScript is able to infer the type of the arguments based on the context.

### MCQs

1. What is the purpose of merged declarations in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To combine multiple declarations into a single declaration
   - To add type safety to your DOM manipulation code

Answer: To combine multiple declarations into a single declaration

2. How do you merge declarations in TypeScript?
   - Using the `interface` keyword
   - Using the `class` keyword
   - Using the `function` keyword with type parameters
   - Using the `namespace` keyword

Answer: Using the `namespace` keyword

3. What is the purpose of the `namespace` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To organize and structure your code
   - To add type safety to your DOM manipulation code

Answer: To organize and structure your code

4. How do you use merged declarations in a function?
   - By defining the type of the function's return value
   - By defining the type of the function's parameters
   - By using the `as` keyword to cast the function's return value
   - By using the `as` keyword to cast the function's parameters

Answer: By defining the type of the function's parameters

5. What is the purpose of the `interface` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

6. How do you use merged declarations in a class?
   - By defining the type of the class's properties
   - By defining the type of the class's methods
   - By using the `as` keyword to cast the class's properties
   - By using the `as` keyword to cast the class's methods

Answer: By defining the type of the class's properties

7. What is the purpose of the `class` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

8. How do you use merged declarations in a type alias?
   - By defining the type of the type alias
   - By using the `as` keyword to cast the type alias
   - By using the `type` keyword to define the type alias
   - By using the `interface` keyword to define the type alias

Answer: By defining the type of the type alias

9. What is the purpose of the `type` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To create reusable functions and classes that can work with different data types

Answer: To create reusable functions and classes that can work with different data types

10. How do you use merged declarations in a type guard?
    - By defining the type of the type guard
    - By using the `as` keyword to cast the type guard
    - By using the `type` keyword to define the type guard
    - By using the `interface` keyword to define the type guard

Answer: By defining the type of the type guard

### Using an Ambient Namespace to Import an External Library

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore how to use an ambient namespace to import an external library in TypeScript and how it can be applied in real-world projects.

### What is an Ambient Namespace?

An ambient namespace is a way to import an external library in TypeScript. It allows you to use the library's functions and classes in your code without having to manually import them.

### Example of Using an Ambient Namespace

Here is an example of how to use an ambient namespace to import an external library in TypeScript:

```typescript
// Import the external library
import 'external-library';

// Use the library
console.log('Hello, World!');
```

In this example, we import the external library using the `import` statement. Then, we use the library's functions and classes in our code.

### Real-World Applications

Using an ambient namespace to import an external library is used extensively in real-world projects. For example, in a web application, you might use an ambient namespace to import a library for handling user authentication.

```typescript
// Import the external library
import 'auth-library';

// Use the library
auth.login('john', 'password123');
```

In this example, we import the external library using the `import` statement. Then, we use the library's functions and classes in our code.

### MCQs

1. What is the purpose of an ambient namespace in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To import an external library
   - To add type safety to your DOM manipulation code

Answer: To import an external library

2. How do you use an ambient namespace in TypeScript?
   - Using the `interface` keyword
   - Using the `class` keyword
   - Using the `function` keyword with type parameters
   - Using the `namespace` keyword

Answer: Using the `namespace` keyword

3. What is the purpose of the `namespace` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To organize and structure your code
   - To add type safety to your DOM manipulation code

Answer: To organize and structure your code

4. How do you use an ambient namespace in a function?
   - By defining the type of the function's return value
   - By defining the type of the function's parameters
   - By using the `as` keyword to cast the function's return value
   - By using the `as` keyword to cast the function's parameters

Answer: By defining the type of the function's parameters

5. What is the purpose of the `interface` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

6. How do you use an ambient namespace in a class?
   - By defining the type of the class's properties
   - By defining the type of the class's methods
   - By using the `as` keyword to cast the class's properties
   - By using the `as` keyword to cast the class's methods

Answer: By defining the type of the class's properties

7. What is the purpose of the `class` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

8. How do you use an ambient namespace in a type alias?
   - By defining the type of the type alias
   - By using the `as` keyword to cast the type alias
   - By using the `type` keyword to define the type alias
   - By using the `interface` keyword to define the type alias

Answer: By defining the type of the type alias

9. What is the purpose of the `type` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To add type safety to your DOM manipulation code
   - To create reusable functions and classes that can work with different data types

Answer: To create reusable functions and classes that can work with different data types

10. How do you use an ambient namespace in a type guard?
    - By defining the type of the type guard
    - By using the `as` keyword to cast the type guard
    - By using the `type` keyword to define the type guard
    - By using the `interface` keyword to define the type guard

Answer: By defining the type of the type guard

### Basic Nominal Typing with TypeScript

TypeScript is a statically typed version of JavaScript that adds optional static typing and other features to improve the development experience. In this note, we will explore basic nominal typing with TypeScript and how it can be applied in real-world projects.

### What is Nominal Typing?

Nominal typing is a way to define the structure and behavior of a type in TypeScript. It is based on the concept of nominalism, which states that a type is defined by its name rather than its properties.

### Example of Nominal Typing

Here is an example of basic nominal typing with TypeScript:

```typescript
// Define a type
type Person = {
  name: string;
  age: number;
};

// Create an object of type Person
let person: Person = {
  name: 'John',
  age: 25
};
```

In this example, we define a type `Person` with two properties: `name` and `age`. We then create an object `person` of type `Person` and assign it the values `'John'` and `25` for `name` and `age`, respectively.

### Real-World Applications

Nominal typing is used extensively in real-world projects. For example, in a web application, you might use nominal typing to define the structure and behavior of a user object.

```typescript
// Define a type
type User = {
  username: string;
  password: string;
};

// Create an object of type User
let user: User = {
  username: 'john',
  password: 'password123'
};
```

In this example, we define a type `User` with two properties: `username` and `password`. We then create an object `user` of type `User` and assign it the values `'john'` and `'password123'` for `username` and `password`, respectively.

### MCQs

1. What is nominal typing in TypeScript?
   - A way to define the structure and behavior of a type
   - A way to define the structure of a document
   - A way to define the behavior of a document
   - A way to add type safety to your DOM manipulation code

Answer: A way to define the structure and behavior of a type

2. How do you define a type in TypeScript?
   - Using the `interface` keyword
   - Using the `class` keyword
   - Using the `function` keyword with type parameters
   - Using the `type` keyword

Answer: Using the `type` keyword

3. What is the purpose of the `type` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

4. How do you use a type in TypeScript?
   - By defining the type of a variable
   - By defining the type of a function
   - By using the `as` keyword to cast a type
   - By using the `interface` keyword to define a type

Answer: By defining the type of a variable

5. What is the purpose of the `interface` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

6. How do you use an interface in TypeScript?
   - By defining the type of a variable
   - By defining the type of a function
   - By using the `as` keyword to cast an interface
   - By using the `interface` keyword to define an interface

Answer: By defining the type of a variable

7. What is the purpose of the `class` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

8. How do you use a class in TypeScript?
   - By defining the type of a variable
   - By defining the type of a function
   - By using the `as` keyword to cast a class
   - By using the `class` keyword to define a class

Answer: By defining the type of a variable

9. What is the purpose of the `function` keyword in TypeScript?
   - To define the structure of a document
   - To define the behavior of a document
   - To create reusable functions and classes that can work with different data types
   - To add type safety to your DOM manipulation code

Answer: To create reusable functions and classes that can work with different data types

10. How do you use a function in TypeScript?
    - By defining the type of a variable
    - By defining the type of a function
    - By using the `as` keyword to cast a function
    - By using the `function` keyword to define a function

Answer: By defining the type of a variable
