## 1. **JavaScript Classes:**

### Defining a Class `Rectangle`:
To define a class `Rectangle` in JavaScript using the class notation, we follow this syntax:

```javascript
class Rectangle {
  // Class methods and properties will go here
}
```

### Constructor with Instance Attributes Initialization:
To define a constructor for the `Rectangle` class that initializes instance attributes `width` and `height`, we use the `constructor` keyword:

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
}
```

### Handling Invalid Inputs in Constructor:
To handle cases where width or height is 0 or not a positive integer in the `Rectangle` class constructor, we can add logic within the constructor:

```javascript
class Rectangle {
  constructor(width, height) {
    if (width <= 0 || height <= 0 || !Number.isInteger(width) || !Number.isInteger(height)) {
      throw new Error('Width and height must be positive integers');
    }
    this.width = width;
    this.height = height;
  }
}
```

### Adding `print()` Instance Method:
To add an instance method `print()` to the `Rectangle` class that prints the rectangle using the character 'X', we define the method within the class:

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  
  print() {
    let row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
```

### Adding `rotate()` and `double()` Instance Methods:
To add instance methods `rotate()` and `double()` to the `Rectangle` class, we follow the same pattern as adding the `print()` method:

```javascript
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  
  print() {
    let row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
  
  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }
  
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}
```

### Real-World Application:
These concepts are crucial when developing applications that deal with geometric shapes. For example, in a graphics editor software, you might use classes like `Rectangle` to represent shapes on the canvas. The ability to define classes with constructors and instance methods allows you to create and manipulate these shapes dynamically, providing essential functionality like printing, rotating, and scaling.

## 2. **Inheritance and Extension:**

### Extending the `Rectangle` Class to Create a `Square` Class:
To define a class `Square` in JavaScript that extends the `Rectangle` class and initializes the instance attribute `size`, we use the `extends` keyword:

```javascript
class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call superclass constructor with size for both width and height
    this.size = size; // Initialize the size attribute
  }
}
```

### Adding an Instance Method `charPrint(c)` to the `Square` Class:
To add an instance method `charPrint(c)` to the `Square` class as described, we simply define the method within the `Square` class:

```javascript
class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.size = size;
  }
  
  charPrint(c = 'X') {
    let row = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
}
```

### Real-World Application:
In a real-world scenario, inheritance and extension are essential when building complex software systems. For instance, in a game development project, you might have a base class representing a generic game character, with subclasses for specific types of characters like warriors, mages, and archers. Each subclass inherits common properties and behaviors from the base class while adding its own unique features. In this case, the `Square` class extending the `Rectangle` class demonstrates how a specialized shape can inherit properties and methods from a more general shape class, while also adding its own functionality. This inheritance and extension mechanism promotes code reusability and maintainability, making it easier to manage and update the codebase as the project evolves.

## 3. **JavaScript Functions:**

### Implementing `nbOccurences(list, searchElement)` Function:
To implement a JavaScript function called `nbOccurences(list, searchElement)` that counts the occurrences of `searchElement` in `list`, we use a loop to iterate through the list and count occurrences:

```javascript
function nbOccurences(list, searchElement) {
  let count = 0;
  for (let element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
}
```

### Implementing `esrever(list)` Function:
To implement a JavaScript function called `esrever(list)` that reverses the given list without using the built-in `reverse()` method, we can swap elements from the start and end of the list until we reach the middle:

```javascript
function esrever(list) {
  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    let temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
  return list;
}
```

### Implementing `logMe(item)` Function:
To implement a JavaScript function called `logMe(item)` to keep track of and print the number of arguments already processed, we can use a closure to maintain a counter:

```javascript
function logMe() {
  let count = 1;
  return function(item) {
    console.log(`Argument ${count}: ${item}`);
    count++;
  };
}

// Example usage:
const logger = logMe();
logger('apple'); // Output: Argument 1: apple
logger('banana'); // Output: Argument 2: banana
logger('orange'); // Output: Argument 3: orange
```

### Real-World Application:
These functions are fundamental building blocks used in various programming tasks and projects. For example, the `nbOccurences()` function can be used in data analysis applications to count occurrences of specific elements in datasets. The `esrever()` function can be handy in scenarios where reversing a list is needed, such as reversing the order of items in a shopping cart. The `logMe()` function can be useful for debugging purposes, allowing developers to track the flow of arguments passed to a function and identify potential issues in the code. These functions demonstrate the importance of understanding basic programming concepts and how they can be applied to solve real-world problems efficiently.

## 4. **Functional Programming:**

### Implementing `converter(base)` Function:
To implement a JavaScript function called `converter(base)` that returns another function capable of converting a number from base 10 to the specified base, we can utilize closures to remember the specified base and perform the conversion:

```javascript
function converter(base) {
  return function(number) {
    return number.toString(base);
  };
}

// Example usage:
const convertToBinary = converter(2);
console.log(convertToBinary(10)); // Output: "1010"

const convertToHexadecimal = converter(16);
console.log(convertToHexadecimal(255)); // Output: "ff"
```

### Real-World Application:
This approach to functional programming allows for the creation of reusable functions tailored to specific needs. In real-world projects, such as web development, you might encounter scenarios where data needs to be converted from one format to another. For instance, when building an e-commerce platform, you might need to convert prices from one currency to another based on user preferences. By using a function like `converter(base)`, you can easily create conversion functions for various bases, providing flexibility and efficiency in your code. This functional programming technique promotes code modularity and reusability, making it easier to maintain and scale projects as requirements evolve.

## 5. **Array Manipulation and Iteration:**

### Using the `map` Function to Perform Element-wise Multiplication:
The `map` function in JavaScript is used to apply a function to each element of an array and return a new array with the results. To create a new array where each element is equal to the value of the corresponding element in the initial list multiplied by its index, we can use the `map` function along with the index:

```javascript
const initialList = [1, 2, 3, 4, 5];
const multipliedList = initialList.map((element, index) => element * index);

console.log(multipliedList); // Output: [0, 2, 6, 12, 20]
```

### Iterating Over a Dictionary to Create a New Dictionary Based on Occurrences:
To iterate over an initial dictionary and create a new dictionary where keys represent the number of occurrences and values represent the list of user ids with that number of occurrences, we can use a combination of `for...of` loop and object manipulation:

```javascript
const initialDictionary = {
  'user1': 3,
  'user2': 5,
  'user3': 3,
  'user4': 7
};

const newDictionary = {};
for (const [userId, occurrences] of Object.entries(initialDictionary)) {
  if (!newDictionary[occurrences]) {
    newDictionary[occurrences] = [];
  }
  newDictionary[occurrences].push(userId);
}

console.log(newDictionary);
// Output: {
//   '3': ['user1', 'user3'],
//   '5': ['user2'],
//   '7': ['user4']
// }
```

### Real-World Application:
These array manipulation and iteration techniques are commonly used in various programming tasks and projects. For example, in a web application, you might need to manipulate and transform data retrieved from a database or an API before displaying it to the user. The ability to use the `map` function for element-wise operations on arrays allows for efficient data processing and transformation. Similarly, when dealing with user data or logs, iterating over dictionaries to analyze occurrences and patterns is essential for understanding user behavior or system performance. These techniques demonstrate the importance of understanding array manipulation and iteration in solving real-world problems efficiently.

© [2024] [Paschal Ugwu]
