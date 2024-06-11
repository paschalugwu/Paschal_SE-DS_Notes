#  JavaScript Array Methods, Typed Arrays, and Advanced Data Structures

## Introduction

In modern JavaScript development, efficient data manipulation and understanding of advanced data structures are crucial. This guide covers three essential topics:

1. **Using map, filter, and reduce on arrays**: Learn how to transform, filter, and reduce arrays effectively, enhancing your data processing capabilities.
2. **Typed arrays**: Understand how to handle binary data with typed arrays, which provide a way to work with raw binary data directly.
3. **The Set, Map, and Weak data structures**: Discover how to use Sets and Maps for unique collections and key-value pairs, along with their weak counterparts for efficient memory management.

By mastering these concepts, you'll be well-equipped to handle complex data operations in real-world JavaScript applications.

## Using `map`, `filter`, and `reduce` on Arrays

### Introduction

JavaScript provides powerful methods for manipulating arrays. Three of the most commonly used methods are `map`, `filter`, and `reduce`. These methods allow you to transform, filter, and reduce arrays in a very concise and readable way.

### `map` Method

The `map` method creates a new array by applying a function to each element of the original array. It doesn't change the original array.

#### Syntax
```javascript
let newArray = array.map(callback);
```
- `callback` is a function that will be called for every element of the array.
- `array` is the original array.

#### Example
Suppose we have an array of numbers and we want to create a new array with each number doubled.
```javascript
let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map(num => num * 2);

console.log(doubled); // [2, 4, 6, 8, 10]
```

### `filter` Method

The `filter` method creates a new array with all elements that pass a test implemented by the provided function. It doesn't change the original array.

#### Syntax
```javascript
let newArray = array.filter(callback);
```
- `callback` is a function that will be called for every element of the array.
- `array` is the original array.

#### Example
Suppose we have an array of numbers and we want to create a new array with only the even numbers.
```javascript
let numbers = [1, 2, 3, 4, 5];
let evens = numbers.filter(num => num % 2 === 0);

console.log(evens); // [2, 4]
```

### `reduce` Method

The `reduce` method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value. It doesn't change the original array.

#### Syntax
```javascript
let result = array.reduce(callback, initialValue);
```
- `callback` is a function that will be called for every element of the array.
- `initialValue` is the initial value for the accumulator.
- `array` is the original array.

#### Example
Suppose we have an array of numbers and we want to calculate the sum of all the numbers.
```javascript
let numbers = [1, 2, 3, 4, 5];
let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

console.log(sum); // 15
```

### Real-World Application

These methods are often used in data processing and manipulation tasks. For example, in a web application, you might have an array of user objects, and you want to create a new array with only the users from a certain location, or you want to calculate the average age of users.

#### Example Project

Suppose we have an array of students, and we want to perform several operations:
1. Get an array of student names.
2. Get an array of students who scored more than 70.
3. Calculate the average score of all students.

```javascript
let students = [
  { name: 'Alice', score: 85 },
  { name: 'Bob', score: 92 },
  { name: 'Charlie', score: 65 },
  { name: 'Dave', score: 78 },
  { name: 'Eve', score: 55 }
];

// 1. Get an array of student names
let names = students.map(student => student.name);
console.log(names); // ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

// 2. Get an array of students who scored more than 70
let passed = students.filter(student => student.score > 70);
console.log(passed); 
// [{ name: 'Alice', score: 85 }, { name: 'Bob', score: 92 }, { name: 'Dave', score: 78 }]

// 3. Calculate the average score of all students
let totalScore = students.reduce((acc, student) => acc + student.score, 0);
let averageScore = totalScore / students.length;
console.log(averageScore); // 75
```

### End of Chapter MCQs

1. What does the `map` method do?
    - A) Modifies each element of the original array.
    - B) Creates a new array with the results of calling a provided function on every element in the array.
    - C) Filters elements from the original array.
    - D) Reduces the array to a single value.

2. Which method would you use to create a new array with elements that pass a certain test?
    - A) `map`
    - B) `filter`
    - C) `reduce`
    - D) `forEach`

3. What is the purpose of the `reduce` method?
    - A) To filter elements from an array.
    - B) To transform each element in an array.
    - C) To reduce an array to a single value.
    - D) To iterate over each element in an array.

4. What does the `callback` function in the `map` method receive as its first argument?
    - A) The index of the current element.
    - B) The current element.
    - C) The entire array.
    - D) The initial value.

5. Which method would you use to sum all numbers in an array?
    - A) `map`
    - B) `filter`
    - C) `reduce`
    - D) `forEach`

6. If `students` is an array of student objects, how would you get an array of student names?
    - A) `students.map(student => student.name)`
    - B) `students.filter(student => student.name)`
    - C) `students.reduce((acc, student) => acc + student.name, [])`
    - D) `students.forEach(student => student.name)`

7. What does `filter` return if no elements match the test condition?
    - A) `null`
    - B) `undefined`
    - C) An empty array
    - D) The original array

8. In the `reduce` method, what is the second argument typically used for?
    - A) The current element.
    - B) The initial value for the accumulator.
    - C) The index of the current element.
    - D) The entire array.

9. How can you find all even numbers in an array?
    - A) `array.map(num => num % 2 === 0)`
    - B) `array.filter(num => num % 2 === 0)`
    - C) `array.reduce((acc, num) => acc + (num % 2 === 0), [])`
    - D) `array.forEach(num => num % 2 === 0)`

10. Which method allows chaining to apply multiple array transformations sequentially?
    - A) `map`
    - B) `filter`
    - C) `reduce`
    - D) All of the above

### Answers to MCQs

1. B
2. B
3. C
4. B
5. C
6. A
7. C
8. B
9. B
10. D

## Typed Arrays in JavaScript

### Introduction

JavaScript Typed Arrays provide a way to handle binary data directly. This is particularly useful when dealing with raw binary data, such as that coming from network protocols, binary file formats, or WebGL. Typed Arrays allow you to work with arrays of binary data with a specific data type and size.

![JavaSript Array Methods](https://github.com/paschalugwu/My_SE-Guidebook/raw/main/JavaScript/Images/373b3bfc-47b8-45a9-8848-178e11217099.jfif)

### Basic Concepts

#### ArrayBuffer
An `ArrayBuffer` is a generic, fixed-length binary data buffer. It is an object used to represent a generic, fixed-length raw binary data buffer. The `ArrayBuffer` object cannot be directly manipulated but can be accessed through a `TypedArray` or `DataView`.

#### TypedArray
A `TypedArray` is an array-like view of an underlying binary data buffer. There are several types of typed arrays, each handling different types of binary data:

- `Int8Array`
- `Uint8Array`
- `Uint8ClampedArray`
- `Int16Array`
- `Uint16Array`
- `Int32Array`
- `Uint32Array`
- `Float32Array`
- `Float64Array`

#### Creating Typed Arrays

1. **From an existing `ArrayBuffer`:**
   ```javascript
   let buffer = new ArrayBuffer(16);
   let int32View = new Int32Array(buffer);
   console.log(int32View); // Int32Array(4) [0, 0, 0, 0]
   ```

2. **From an array or array-like object:**
   ```javascript
   let typedArray = new Uint8Array([1, 2, 3, 4]);
   console.log(typedArray); // Uint8Array(4) [1, 2, 3, 4]
   ```

3. **With a specified length:**
   ```javascript
   let typedArray = new Float32Array(4);
   console.log(typedArray); // Float32Array(4) [0, 0, 0, 0]
   ```

### Example Usage

#### Reading and Writing Binary Data

Suppose you are working with a binary file format that stores 16-bit integers. You can read this data into a `Uint16Array`.

```javascript
let buffer = new ArrayBuffer(8);
let uint16View = new Uint16Array(buffer);
uint16View[0] = 42;
uint16View[1] = 84;

console.log(uint16View); // Uint16Array(4) [42, 84, 0, 0]
```

#### Interacting with Web APIs

Typed Arrays are often used with Web APIs. For example, the Web Audio API and WebGL API both use Typed Arrays to handle audio and graphics data.

```javascript
let audioBuffer = new Float32Array(1024);
// Fill the buffer with audio data, manipulate it, or pass it to an audio API
```

### Real-World Applications

1. **Image Processing:**
   Typed Arrays can be used to manipulate pixel data directly, making it easier to apply filters and transformations to images.
   
   ```javascript
   let imageData = new Uint8ClampedArray([255, 0, 0, 255, 0, 255, 0, 255]);
   // This represents two pixels: red (255, 0, 0, 255) and green (0, 255, 0, 255)
   ```

2. **Network Protocols:**
   Handling binary protocols over WebSockets or other network APIs can be streamlined with Typed Arrays.

   ```javascript
   let buffer = new ArrayBuffer(8);
   let dataView = new DataView(buffer);
   dataView.setUint32(0, 25, true);
   dataView.setUint32(4, 50, true);
   ```

3. **3D Graphics:**
   WebGL uses Typed Arrays to manage vertex buffers and other graphical data.

   ```javascript
   let vertices = new Float32Array([
     -1.0, -1.0, 0.0,
      1.0, -1.0, 0.0,
      1.0,  1.0, 0.0,
     -1.0,  1.0, 0.0
   ]);
   ```

### End of Chapter MCQs

1. What is an `ArrayBuffer`?
   - A) An array of integers
   - B) A fixed-length binary data buffer
   - C) A variable-length binary data buffer
   - D) A JSON object

2. Which TypedArray would you use to store an array of 8-bit unsigned integers?
   - A) `Int8Array`
   - B) `Uint8Array`
   - C) `Int16Array`
   - D) `Float32Array`

3. How do you create a `TypedArray` from an existing `ArrayBuffer`?
   - A) `new Uint8Array(16)`
   - B) `new Uint8Array(buffer)`
   - C) `new ArrayBuffer(16)`
   - D) `new ArrayBuffer(buffer)`

4. Which of the following is NOT a type of TypedArray in JavaScript?
   - A) `Uint8Array`
   - B) `Uint8ClampedArray`
   - C) `Uint24Array`
   - D) `Float64Array`

5. How would you initialize a `Float32Array` with a length of 4?
   - A) `new Float32Array([4])`
   - B) `new Float32Array(4)`
   - C) `new Float32Array(buffer, 4)`
   - D) `new ArrayBuffer(4)`

6. How do you set the value at the first position of a `Uint16Array` to 42?
   - A) `typedArray[0] = 42`
   - B) `typedArray.set(42, 0)`
   - C) `typedArray.add(0, 42)`
   - D) `typedArray.push(42)`

7. What does the following code output?
   ```javascript
   let buffer = new ArrayBuffer(4);
   let view = new Uint8Array(buffer);
   view[0] = 1;
   console.log(view);
   ```
   - A) `Uint8Array(4) [1, 0, 0, 0]`
   - B) `Uint8Array(4) [0, 0, 0, 1]`
   - C) `Uint8Array(4) [1, 1, 1, 1]`
   - D) `Uint8Array(4) [1, 0]`

8. How would you create a `Uint8ClampedArray` from an array `[255, -1, 300]`?
   - A) `new Uint8ClampedArray(buffer)`
   - B) `new Uint8ClampedArray([255, -1, 300])`
   - C) `Uint8ClampedArray.of(255, -1, 300)`
   - D) `Uint8ClampedArray.from([255, -1, 300])`

9. Which of the following is true about `Uint8ClampedArray`?
   - A) It allows negative values.
   - B) It clamps values to the range 0-255.
   - C) It allows floating point values.
   - D) It automatically sorts the values.

10. What is the main purpose of using Typed Arrays in WebGL?
    - A) To handle audio data
    - B) To manipulate HTML elements
    - C) To manage vertex buffers and graphical data
    - D) To fetch data from a server

### Answers to MCQs

1. B
2. B
3. B
4. C
5. B
6. A
7. A
8. B
9. B
10. C

## The Set, Map, and Weak Data Structures in JavaScript

### Introduction

JavaScript provides several built-in data structures to manage collections of data efficiently. These include `Set`, `Map`, `WeakSet`, and `WeakMap`. Each of these data structures serves different purposes and has unique characteristics that make them suitable for specific use cases.

### Set

A `Set` is a collection of unique values. This means that it cannot contain duplicate values.

#### Creating a Set

```javascript
let mySet = new Set();
mySet.add(1);
mySet.add(5);
mySet.add(1); // This will not be added as 1 is already in the set
console.log(mySet); // Set { 1, 5 }
```

#### Methods and Properties

- `add(value)`: Adds a new value to the Set.
- `delete(value)`: Removes the specified value from the Set.
- `has(value)`: Returns true if the value exists in the Set.
- `clear()`: Removes all elements from the Set.
- `size`: Returns the number of elements in the Set.

```javascript
mySet.has(1); // true
mySet.size; // 2
mySet.delete(5);
console.log(mySet); // Set { 1 }
```

#### Iterating Over a Set

```javascript
mySet.add(5);
for (let item of mySet) {
  console.log(item); // 1, 5
}
```

### Map

A `Map` is a collection of key-value pairs. Keys can be of any type, including objects, while in traditional objects, keys are usually strings or symbols.

#### Creating a Map

```javascript
let myMap = new Map();
myMap.set('key1', 'value1');
myMap.set('key2', 'value2');
console.log(myMap); // Map { 'key1' => 'value1', 'key2' => 'value2' }
```

#### Methods and Properties

- `set(key, value)`: Adds or updates an element with a specified key and value.
- `get(key)`: Returns the value associated with the key.
- `has(key)`: Returns true if the key exists in the Map.
- `delete(key)`: Removes the specified key-value pair.
- `clear()`: Removes all elements from the Map.
- `size`: Returns the number of key-value pairs in the Map.

```javascript
myMap.get('key1'); // 'value1'
myMap.size; // 2
myMap.delete('key2');
console.log(myMap); // Map { 'key1' => 'value1' }
```

#### Iterating Over a Map

```javascript
myMap.set('key2', 'value2');
for (let [key, value] of myMap) {
  console.log(key, value); // 'key1' 'value1', 'key2' 'value2'
}
```

### WeakSet

A `WeakSet` is a collection of objects only. It does not prevent its items from being garbage-collected. If there are no other references to an object stored in the `WeakSet`, the object can be garbage-collected.

#### Creating a WeakSet

```javascript
let weakSet = new WeakSet();
let obj1 = {a: 1};
let obj2 = {b: 2};
weakSet.add(obj1);
weakSet.add(obj2);
console.log(weakSet.has(obj1)); // true
```

#### Methods

- `add(value)`: Adds a new object to the WeakSet.
- `delete(value)`: Removes the specified object.
- `has(value)`: Returns true if the object exists in the WeakSet.

```javascript
weakSet.delete(obj2);
console.log(weakSet.has(obj2)); // false
```

### WeakMap

A `WeakMap` is a collection of key-value pairs where the keys are objects only, and the values can be arbitrary values. Similar to `WeakSet`, `WeakMap` keys are not prevented from garbage collection if there are no other references to the object.

#### Creating a WeakMap

```javascript
let weakMap = new WeakMap();
let obj1 = {};
let obj2 = {};
weakMap.set(obj1, 'value1');
weakMap.set(obj2, 'value2');
console.log(weakMap.get(obj1)); // 'value1'
```

#### Methods

- `set(key, value)`: Adds or updates an element with a specified object key and value.
- `get(key)`: Returns the value associated with the key.
- `has(key)`: Returns true if the key exists in the WeakMap.
- `delete(key)`: Removes the specified key-value pair.

```javascript
weakMap.delete(obj2);
console.log(weakMap.has(obj2)); // false
```

### Real-World Applications

1. **Set**: Removing duplicates from an array.

   ```javascript
   let numbers = [1, 2, 2, 3, 4, 4];
   let uniqueNumbers = new Set(numbers);
   console.log([...uniqueNumbers]); // [1, 2, 3, 4]
   ```

2. **Map**: Storing configuration settings with complex keys.

   ```javascript
   let config = new Map();
   config.set('fontSize', '16px');
   config.set('theme', 'dark');
   ```

3. **WeakSet**: Tracking objects without preventing garbage collection.

   ```javascript
   let visitedNodes = new WeakSet();
   let node = document.getElementById('node');
   visitedNodes.add(node);
   ```

4. **WeakMap**: Storing metadata related to objects without interfering with garbage collection.

   ```javascript
   let metaData = new WeakMap();
   let element = document.getElementById('element');
   metaData.set(element, { id: 1 });
   ```

### End of Chapter MCQs

1. What does a `Set` store?
   - A) Key-value pairs
   - B) Unique values
   - C) Both key-value pairs and unique values
   - D) Only numbers

2. How do you add a value to a `Set`?
   - A) `set.add(value)`
   - B) `set.push(value)`
   - C) `set.append(value)`
   - D) `set.insert(value)`

3. Which method would you use to check if a key exists in a `Map`?
   - A) `hasKey()`
   - B) `contains()`
   - C) `exists()`
   - D) `has()`

4. What type of keys can a `WeakMap` have?
   - A) Strings
   - B) Numbers
   - C) Objects
   - D) Booleans

5. How would you iterate over all entries in a `Map`?
   - A) `for (let entry of map.entries())`
   - B) `for (let entry of map)`
   - C) `map.each(entry => {})`
   - D) `map.loop(entry => {})`

6. What will `mySet.add(1).add(1).size` return?
   - A) `1`
   - B) `2`
   - C) `0`
   - D) `undefined`

7. Which of the following statements is true about `WeakSet`?
   - A) It can store any type of data.
   - B) It prevents garbage collection of its objects.
   - C) It only stores objects.
   - D) It maintains the insertion order of its elements.

8. How do you remove all elements from a `Set`?
   - A) `set.clearAll()`
   - B) `set.empty()`
   - C) `set.clear()`
   - D) `set.removeAll()`

9. What will `myMap.set('a', 1).set('b', 2).size` return?
   - A) `1`
   - B) `2`
   - C) `3`
   - D) `undefined`

10. What does `weakMap.has(obj)` do?
    - A) Checks if `obj` is a value in the WeakMap
    - B) Checks if `obj` is a key in the WeakMap
    - C) Checks if `obj` is an entry in the WeakMap
    - D) Checks if `obj` is a WeakMap

### Answers to MCQs

1. B
2. A
3. D
4. C
5. A
6. A
7. C
8. C
9. B
10. B

## Conclusion

Mastering the use of `map`, `filter`, and `reduce` methods on arrays, along with understanding typed arrays and advanced data structures like `Set`, `Map`, `WeakSet`, and `WeakMap`, empowers you to write more efficient and robust JavaScript code. These tools are fundamental for handling data effectively and are integral to many real-world applications. With this knowledge, you are well-prepared to tackle various data manipulation tasks and optimize your code for better performance and maintainability.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
