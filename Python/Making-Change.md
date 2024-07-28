## Greedy Algorithms

### Understanding Greedy Algorithms

Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. The idea is to make the locally optimal choice at each step with the hope of finding a global optimum. 

#### Example: The Coin Change Problem

Imagine you are a cashier, and you need to provide change for a certain amount of money using the fewest number of coins possible. The denominations of the coins available are 1, 5, 10, and 25 cents. A greedy algorithm for this problem would involve always giving out the highest denomination coin possible.

**Steps to solve the coin change problem using a greedy algorithm:**

1. Start with the total amount of change needed.
2. Choose the largest coin denomination that is less than or equal to the remaining amount.
3. Subtract the value of the chosen coin from the remaining amount.
4. Repeat steps 2 and 3 until no more change is needed.

**Example Code in Python:**

```python
def coin_change_greedy(amount, coins):
    result = []
    coins.sort(reverse=True)  # Sort coins in descending order
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Example usage
amount = 87
coins = [1, 5, 10, 25]
change = coin_change_greedy(amount, coins)
print(f"Change for {amount} cents: {change}")
```

Output:
```
Change for 87 cents: [25, 25, 25, 10, 1, 1]
```

### Recognizing Limitations

While greedy algorithms are efficient and easy to implement, they do not always provide the optimal solution. 

#### Limitation Example: The Fractional Knapsack Problem

In the fractional knapsack problem, you have a knapsack that can hold a maximum weight, and you need to fill it with items to maximize the total value. Each item can be broken into smaller parts.

**Greedy Approach:**

1. Calculate the value-to-weight ratio for each item.
2. Sort items by this ratio in descending order.
3. Start adding items to the knapsack from the top of the sorted list until you cannot add the next item completely.
4. If an item cannot be added completely, add the fractional part of it.

**Example Code in Python:**

```python
def fractional_knapsack(weight, items):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    for w, v in items:
        if weight >= w:
            weight -= w
            total_value += v
        else:
            total_value += v * (weight / w)
            break
    return total_value

# Example usage
weight = 50
items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
max_value = fractional_knapsack(weight, items)
print(f"Maximum value in the knapsack: {max_value}")
```

Output:
```
Maximum value in the knapsack: 240.0
```

### Real-World Application

Greedy algorithms are used in many real-world applications, such as:

1. **Huffman Coding:** Used for data compression.
2. **Prim's and Kruskal's Algorithms:** Used to find the minimum spanning tree in a graph.
3. **Dijkstra's Algorithm:** Used for finding the shortest path in a graph.

### End of Chapter Multiple-Choice Questions

1. What is the main idea behind greedy algorithms?
   a) Always choosing the smallest possible option.
   b) Always choosing the option that seems best at the moment.
   c) Always choosing the option with the least computational complexity.
   d) Always choosing the option that minimizes memory usage.

2. In the coin change problem, if you need to make change for 63 cents using denominations of 1, 5, 10, and 25 cents, what coins will a greedy algorithm choose?
   a) [25, 25, 10, 1, 1, 1]
   b) [10, 10, 10, 10, 10, 10, 3]
   c) [25, 25, 5, 5, 1, 1, 1]
   d) [20, 20, 20, 3]

3. What is a key characteristic of problems suited for greedy algorithms?
   a) They can be divided into overlapping subproblems.
   b) They can be divided into non-overlapping subproblems.
   c) They have no optimal solution.
   d) They can be solved in parallel.

4. Why might a greedy algorithm not always provide the optimal solution?
   a) It ignores the global context.
   b) It uses too much memory.
   c) It takes too long to execute.
   d) It requires complex data structures.

5. Which of the following problems is typically solved using a greedy algorithm?
   a) Merge Sort
   b) Longest Common Subsequence
   c) Huffman Coding
   d) Binary Search

6. In the fractional knapsack problem, what determines the order in which items are added to the knapsack?
   a) Their weight
   b) Their value
   c) Their size
   d) Their value-to-weight ratio

7. What is the time complexity of a greedy algorithm for the coin change problem?
   a) O(n^2)
   b) O(n log n)
   c) O(n)
   d) O(1)

8. Which of the following is NOT a step in a typical greedy algorithm?
   a) Make a choice
   b) Prove the choice leads to an optimal solution
   c) Solve the subproblem arising after the choice is made
   d) Combine solutions to subproblems

9. For which type of problems are greedy algorithms guaranteed to find an optimal solution?
   a) Problems with overlapping subproblems
   b) Problems with an optimal substructure
   c) Problems with local maxima
   d) Problems that are computationally expensive

10. In the context of Dijkstra's algorithm, which of the following is NOT true?
    a) It is a type of greedy algorithm.
    b) It finds the shortest path in a weighted graph.
    c) It works with negative weight edges.
    d) It uses a priority queue for efficient implementation.

### Answers

1. b) Always choosing the option that seems best at the moment.
2. c) [25, 25, 5, 5, 1, 1, 1]
3. b) They can be divided into non-overlapping subproblems.
4. a) It ignores the global context.
5. c) Huffman Coding
6. d) Their value-to-weight ratio
7. c) O(n)
8. b) Prove the choice leads to an optimal solution
9. b) Problems with an optimal substructure
10. c) It works with negative weight edges.

## Dynamic Programming

### Basic Principles of Dynamic Programming

Dynamic Programming (DP) is a method used to solve complex problems by breaking them down into simpler subproblems. It is particularly effective for optimization problems where the problem can be divided into overlapping subproblems that are solved independently.

#### Key Concepts:
1. **Overlapping Subproblems**: These are smaller parts of the problem that are reused multiple times. Instead of recomputing their solutions, dynamic programming saves their results to avoid redundant work.
2. **Optimal Substructure**: This means that the optimal solution of the problem can be constructed from the optimal solutions of its subproblems.

### Example: The Coin Change Problem

The coin change problem involves finding the minimum number of coins required to make a certain amount of change. Given coin denominations and a target amount, dynamic programming can be used to solve this problem efficiently.

**Steps to solve the coin change problem using dynamic programming:**

1. Create an array `dp` where `dp[i]` will store the minimum number of coins required for amount `i`.
2. Initialize `dp[0]` to 0 because no coins are needed to make zero amount.
3. For each coin, update the `dp` array for all amounts that can be reached using this coin.
4. The final answer will be in `dp[amount]`.

**Example Code in Python:**

```python
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins to make {amount} cents: {coin_change_dp(coins, amount)}")
```

Output:
```
Minimum coins to make 11 cents: 3
```

### Overlapping Subproblems and Optimal Substructure

In the context of the coin change problem:
- **Overlapping Subproblems**: To find the minimum number of coins for amount `i`, we use the results of amounts less than `i` that have already been computed.
- **Optimal Substructure**: The optimal solution for the amount `i` is built from the optimal solutions of smaller amounts.

### Real-World Application

Dynamic programming is widely used in various real-world applications, such as:
1. **Fibonacci Sequence Calculation**: Storing previously computed values to avoid redundant calculations.
2. **Knapsack Problem**: Determining the maximum value that can be achieved with a given weight limit.
3. **Pathfinding Algorithms**: Finding the shortest path in graphs, such as in GPS navigation systems.

### End of Chapter Multiple-Choice Questions

1. What is the main principle behind dynamic programming?
   a) Breaking a problem into non-overlapping subproblems
   b) Breaking a problem into overlapping subproblems and solving them independently
   c) Always choosing the option that seems best at the moment
   d) None of the above

2. In the coin change problem using dynamic programming, what does `dp[i]` represent?
   a) The number of coins available
   b) The minimum number of coins required to make the amount `i`
   c) The total value of coins used so far
   d) The largest coin denomination used

3. What is the time complexity of the dynamic programming solution for the coin change problem?
   a) O(n^2)
   b) O(n log n)
   c) O(amount * number of coins)
   d) O(1)

4. Which of the following best describes the optimal substructure property?
   a) The problem can be broken down into non-overlapping subproblems
   b) The optimal solution to the problem can be constructed from optimal solutions of its subproblems
   c) The problem can be solved in a greedy manner
   d) None of the above

5. Which real-world problem is commonly solved using dynamic programming?
   a) Sorting an array
   b) Searching in a binary search tree
   c) Calculating the shortest path in a graph
   d) Binary search

6. In dynamic programming, how are overlapping subproblems handled?
   a) By recomputing the solutions every time
   b) By storing and reusing previously computed solutions
   c) By ignoring them
   d) By using a stack to manage them

7. What does the term "memoization" refer to in dynamic programming?
   a) Storing results of subproblems to avoid redundant calculations
   b) Ignoring subproblems that overlap
   c) Using a greedy approach to solve problems
   d) Combining solutions of subproblems

8. Which of the following problems does NOT typically use dynamic programming?
   a) Longest Common Subsequence
   b) Coin Change
   c) Binary Search
   d) Fibonacci Sequence

9. What is the initial value of `dp[0]` in the coin change problem using dynamic programming?
   a) `float('inf')`
   b) 0
   c) 1
   d) -1

10. Which of the following best describes the approach of dynamic programming?
    a) Top-down
    b) Bottom-up
    c) Both top-down and bottom-up
    d) Neither top-down nor bottom-up

### Answers

1. b) Breaking a problem into overlapping subproblems and solving them independently
2. b) The minimum number of coins required to make the amount `i`
3. c) O(amount * number of coins)
4. b) The optimal solution to the problem can be constructed from optimal solutions of its subproblems
5. c) Calculating the shortest path in a graph
6. b) By storing and reusing previously computed solutions
7. a) Storing results of subproblems to avoid redundant calculations
8. c) Binary Search
9. b) 0
10. c) Both top-down and bottom-up

## Algorithmic Complexity

### Analyzing the Time and Space Complexity of Algorithms

Algorithmic complexity is a way to describe the efficiency of an algorithm, mainly focusing on how the running time and space requirements grow as the input size increases.

#### Time Complexity

Time complexity measures the amount of time an algorithm takes to complete as a function of the input size. It is often expressed using Big O notation, which describes the upper bound of the algorithm's running time.

**Common Time Complexities:**

1. **O(1) - Constant Time**: The running time does not change with the input size.
   ```python
   def constant_time_example(n):
       return n + 1
   ```

2. **O(log n) - Logarithmic Time**: The running time increases logarithmically with the input size.
   ```python
   def logarithmic_time_example(n):
       count = 0
       while n > 1:
           n = n // 2
           count += 1
       return count
   ```

3. **O(n) - Linear Time**: The running time increases linearly with the input size.
   ```python
   def linear_time_example(arr):
       total = 0
       for num in arr:
           total += num
       return total
   ```

4. **O(n^2) - Quadratic Time**: The running time increases quadratically with the input size.
   ```python
   def quadratic_time_example(arr):
       count = 0
       for i in range(len(arr)):
           for j in range(len(arr)):
               count += 1
       return count
   ```

5. **O(2^n) - Exponential Time**: The running time doubles with each additional element in the input.
   ```python
   def exponential_time_example(n):
       if n == 0:
           return 1
       else:
           return exponential_time_example(n-1) + exponential_time_example(n-1)
   ```

#### Space Complexity

Space complexity measures the amount of memory an algorithm uses as a function of the input size. Like time complexity, it is also expressed using Big O notation.

**Common Space Complexities:**

1. **O(1) - Constant Space**: The space required does not change with the input size.
   ```python
   def constant_space_example(n):
       result = n + 1
       return result
   ```

2. **O(n) - Linear Space**: The space required grows linearly with the input size.
   ```python
   def linear_space_example(n):
       arr = [0] * n
       return arr
   ```

### Striving for Solutions with Lower Complexity

When designing algorithms, it is crucial to strive for solutions with lower time and space complexity to ensure they meet runtime constraints, especially for large input sizes. Optimizing algorithms to reduce complexity can significantly improve performance.

### Real-World Application

Optimizing algorithmic complexity is essential in various real-world applications, such as:

1. **Web Search Engines**: Efficient algorithms ensure quick retrieval of search results from vast databases.
2. **Social Media Platforms**: Algorithms must handle millions of users and their interactions in real time.
3. **Financial Systems**: Algorithms process numerous transactions quickly and accurately.

### End of Chapter Multiple-Choice Questions

1. What does O(n) represent in time complexity?
   a) The running time is constant.
   b) The running time grows linearly with the input size.
   c) The running time grows quadratically with the input size.
   d) The running time doubles with each additional element.

2. Which of the following time complexities is the most efficient?
   a) O(n^2)
   b) O(n log n)
   c) O(2^n)
   d) O(n!)

3. What does O(1) represent in space complexity?
   a) The space required grows linearly with the input size.
   b) The space required grows quadratically with the input size.
   c) The space required is constant.
   d) The space required doubles with each additional element.

4. What is the time complexity of a binary search algorithm?
   a) O(1)
   b) O(n)
   c) O(log n)
   d) O(n^2)

5. What is the space complexity of a recursive algorithm that uses no additional data structures?
   a) O(1)
   b) O(n)
   c) O(n^2)
   d) O(log n)

6. Which of the following is an example of an algorithm with O(n^2) time complexity?
   a) Binary Search
   b) Merge Sort
   c) Bubble Sort
   d) Linear Search

7. What does Big O notation describe?
   a) The exact running time of an algorithm
   b) The exact space required by an algorithm
   c) The upper bound of the running time or space requirements of an algorithm
   d) The average case performance of an algorithm

8. Which of the following algorithms has a logarithmic time complexity?
   a) Linear Search
   b) Binary Search
   c) Bubble Sort
   d) Insertion Sort

9. What is the time complexity of the following code snippet?
   ```python
   def example(arr):
       for i in range(len(arr)):
           print(arr[i])
   ```
   a) O(1)
   b) O(log n)
   c) O(n)
   d) O(n^2)

10. Which of the following statements is true about space complexity?
    a) It only considers the input size.
    b) It measures the amount of memory used by an algorithm.
    c) It is always more important than time complexity.
    d) It describes the average memory usage of an algorithm.

### Answers

1. b) The running time grows linearly with the input size.
2. b) O(n log n)
3. c) The space required is constant.
4. c) O(log n)
5. b) O(n)
6. c) Bubble Sort
7. c) The upper bound of the running time or space requirements of an algorithm
8. b) Binary Search
9. c) O(n)
10. b) It measures the amount of memory used by an algorithm.

## Problem-Solving Strategies

### Breaking Down the Problem into Smaller, Manageable Sub-Problems

When faced with a complex problem, it is often useful to break it down into smaller, more manageable sub-problems. This approach helps in understanding the problem better and finding a solution more effectively.

#### Steps to Break Down a Problem:

1. **Understand the Problem**: Make sure you have a clear understanding of the problem statement and requirements.
2. **Identify Sub-Problems**: Divide the main problem into smaller sub-problems that are easier to solve.
3. **Solve Sub-Problems**: Address each sub-problem individually.
4. **Combine Solutions**: Integrate the solutions of the sub-problems to solve the original problem.

**Example: Sum of an Array**

To find the sum of elements in an array, we can break it down into the sum of two halves.

**Example Code in Python:**

```python
def sum_array(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_sum = sum_array(arr[:mid])
        right_sum = sum_array(arr[mid:])
        return left_sum + right_sum

# Example usage
arr = [1, 2, 3, 4, 5]
print(f"Sum of array: {sum_array(arr)}")
```

Output:
```
Sum of array: 15
```

### Iterative vs Recursive Approaches to Dynamic Programming

Dynamic programming can be implemented using either iterative (bottom-up) or recursive (top-down) approaches.

#### Iterative Approach

The iterative approach solves the sub-problems starting from the smallest ones and uses their solutions to build up the solutions to larger sub-problems.

**Example: Fibonacci Sequence**

```python
def fibonacci_iterative(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Example usage
print(f"10th Fibonacci number (iterative): {fibonacci_iterative(10)}")
```

Output:
```
10th Fibonacci number (iterative): 55
```

#### Recursive Approach

The recursive approach involves solving the problem by solving the same problem on smaller instances and combining the results.

**Example: Fibonacci Sequence with Memoization**

```python
def fibonacci_recursive(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

# Example usage
print(f"10th Fibonacci number (recursive): {fibonacci_recursive(10)}")
```

Output:
```
10th Fibonacci number (recursive): 55
```

### Real-World Application

Breaking down problems and using dynamic programming is essential in various real-world applications, such as:

1. **Route Optimization**: Finding the shortest path in navigation systems.
2. **Resource Allocation**: Allocating resources efficiently in project management.
3. **Game Development**: Implementing algorithms to compute possible moves and outcomes.

### End of Chapter Multiple-Choice Questions

1. What is the first step in breaking down a problem into smaller sub-problems?
   a) Solve the sub-problems
   b) Understand the problem
   c) Combine solutions
   d) Identify sub-problems

2. Which approach solves the smallest sub-problems first?
   a) Recursive
   b) Iterative
   c) Both
   d) Neither

3. What is the main advantage of breaking down a problem into sub-problems?
   a) It makes the problem more complex
   b) It simplifies the problem
   c) It increases the time complexity
   d) It increases the space complexity

4. In the iterative approach to dynamic programming, what is the sequence of solving sub-problems?
   a) From largest to smallest
   b) Randomly
   c) From smallest to largest
   d) Simultaneously

5. Which of the following is a characteristic of the recursive approach to dynamic programming?
   a) Uses loops to solve sub-problems
   b) Solves sub-problems iteratively
   c) Uses function calls to solve sub-problems
   d) None of the above

6. What is memoization in the context of recursive dynamic programming?
   a) Ignoring already solved sub-problems
   b) Recomputing the solutions of sub-problems
   c) Storing solutions of sub-problems to avoid redundant calculations
   d) Using a stack to manage sub-problems

7. Which problem-solving strategy is demonstrated in the sum of array example?
   a) Combining solutions of sub-problems
   b) Ignoring sub-problems
   c) Breaking down the problem into smaller sub-problems
   d) None of the above

8. Which of the following is an example of a problem that can be solved using dynamic programming?
   a) Binary Search
   b) Merge Sort
   c) Fibonacci Sequence
   d) Quick Sort

9. What is the time complexity of the iterative approach to compute the nth Fibonacci number?
   a) O(1)
   b) O(log n)
   c) O(n)
   d) O(n^2)

10. In the context of problem-solving, what does combining solutions mean?
    a) Solving sub-problems independently
    b) Integrating solutions of sub-problems to solve the original problem
    c) Ignoring the original problem
    d) None of the above

### Answers

1. b) Understand the problem
2. b) Iterative
3. b) It simplifies the problem
4. c) From smallest to largest
5. c) Uses function calls to solve sub-problems
6. c) Storing solutions of sub-problems to avoid redundant calculations
7. c) Breaking down the problem into smaller sub-problems
8. c) Fibonacci Sequence
9. c) O(n)
10. b) Integrating solutions of sub-problems to solve the original problem

## Python Programming

### Manipulating Lists and Using List Comprehensions

Lists are one of the most versatile data structures in Python. They allow for storing sequences of elements, which can be manipulated in various ways. List comprehensions offer a concise way to create and modify lists.

#### Basic List Operations

1. **Creating a List**:
   ```python
   fruits = ["apple", "banana", "cherry"]
   ```

2. **Accessing Elements**:
   ```python
   first_fruit = fruits[0]  # "apple"
   ```

3. **Modifying Elements**:
   ```python
   fruits[1] = "blueberry"  # ["apple", "blueberry", "cherry"]
   ```

4. **Adding Elements**:
   ```python
   fruits.append("date")  # ["apple", "blueberry", "cherry", "date"]
   ```

5. **Removing Elements**:
   ```python
   fruits.remove("blueberry")  # ["apple", "cherry", "date"]
   ```

#### List Comprehensions

List comprehensions provide a more readable and concise way to create lists. They can replace the need for loops to generate list elements.

**Syntax**:
```python
new_list = [expression for item in iterable if condition]
```

**Examples**:

1. **Creating a List of Squares**:
   ```python
   squares = [x**2 for x in range(10)]
   ```

2. **Filtering Even Numbers**:
   ```python
   evens = [x for x in range(10) if x % 2 == 0]
   ```

3. **Using Conditions in List Comprehensions**:
   ```python
   fruits = ["apple", "banana", "cherry", "date"]
   fruit_lengths = [len(fruit) for fruit in fruits if len(fruit) > 5]
   ```

### Implementing Functions with Efficient Looping and Conditional Statements

Functions in Python allow for modular and reusable code. Using efficient looping and conditional statements within functions can optimize performance and readability.

#### Defining Functions

1. **Basic Function**:
   ```python
   def greet(name):
       return f"Hello, {name}!"
   ```

2. **Function with Default Arguments**:
   ```python
   def greet(name="Guest"):
       return f"Hello, {name}!"
   ```

#### Looping in Functions

Efficient looping ensures that your functions run optimally, especially with large datasets.

1. **For Loop**:
   ```python
   def sum_numbers(numbers):
       total = 0
       for num in numbers:
           total += num
       return total
   ```

2. **While Loop**:
   ```python
   def count_down(n):
       while n > 0:
           print(n)
           n -= 1
   ```

#### Conditional Statements

Conditional statements help in making decisions within functions.

1. **If-Else**:
   ```python
   def check_even(number):
       if number % 2 == 0:
           return "Even"
       else:
           return "Odd"
   ```

2. **Elif**:
   ```python
   def grade(score):
       if score >= 90:
           return "A"
       elif score >= 80:
           return "B"
       elif score >= 70:
           return "C"
       elif score >= 60:
           return "D"
       else:
           return "F"
   ```

### Real-World Application

Manipulating lists and using efficient looping and conditional statements are essential in various real-world applications, such as:

1. **Data Processing**: Cleaning and transforming datasets for analysis.
2. **Web Development**: Handling user inputs and dynamic content generation.
3. **Automation**: Writing scripts to automate repetitive tasks.

### End of Chapter Multiple-Choice Questions

1. What is the output of the following list comprehension?
   ```python
   [x*2 for x in range(3)]
   ```
   a) [0, 1, 2]
   b) [0, 2, 4]
   c) [2, 4, 6]
   d) [1, 2, 3]

2. How do you access the third element of a list named `my_list`?
   a) `my_list[2]`
   b) `my_list[3]`
   c) `my_list[1]`
   d) `my_list[-3]`

3. What does the `append` method do to a list?
   a) Removes an element
   b) Sorts the list
   c) Adds an element to the end
   d) Reverses the list

4. What is the purpose of a list comprehension?
   a) To create and manipulate dictionaries
   b) To create new lists based on existing lists
   c) To handle exceptions in lists
   d) To sort lists efficiently

5. Which of the following functions correctly sums all elements of a list `numbers`?
   a) 
   ```python
   def sum_list(numbers):
       total = 0
       for num in numbers:
           total += num
       return total
   ```
   b) 
   ```python
   def sum_list(numbers):
       total = 0
       while numbers:
           total += numbers
       return total
   ```
   c) 
   ```python
   def sum_list(numbers):
       total = sum(numbers)
       return total
   ```
   d) Both a and c

6. What does the following function return when called with `check_even(4)`?
   ```python
   def check_even(number):
       if number % 2 == 0:
           return "Even"
       else:
           return "Odd"
   ```
   a) "Odd"
   b) "Even"
   c) None
   d) Error

7. Which of the following is a correct way to create a list of even numbers from 0 to 9 using list comprehension?
   a) 
   ```python
   evens = [x for x in range(10) if x % 2 == 0]
   ```
   b) 
   ```python
   evens = [x for x in range(10) if x % 2 != 0]
   ```
   c) 
   ```python
   evens = [x*2 for x in range(5)]
   ```
   d) Both a and c

8. How do you remove an element from a list in Python?
   a) `list.add(element)`
   b) `list.pop(element)`
   c) `list.remove(element)`
   d) `list.delete(element)`

9. Which of the following is the correct syntax to define a function in Python?
   a) 
   ```python
   function my_func():
       pass
   ```
   b) 
   ```python
   def my_func:
       pass
   ```
   c) 
   ```python
   def my_func():
       pass
   ```
   d) 
   ```python
   my_func() def:
       pass
   ```

10. What will the following code print?
    ```python
    def greet(name="Guest"):
        return f"Hello, {name}!"
    
    print(greet())
    ```
    a) `Hello,`
    b) `Hello, Guest!`
    c) `Hello, None!`
    d) Error

### Answers

1. b) [0, 2, 4]
2. a) `my_list[2]`
3. c) Adds an element to the end
4. b) To create new lists based on existing lists
5. d) Both a and c
6. b) "Even"
7. d) Both a and c
8. c) `list.remove(element)`
9. c) 
   ```python
   def my_func():
       pass
   ```
10. b) `Hello, Guest!`
