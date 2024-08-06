## Prime Numbers

### Understanding Prime Numbers

Prime numbers are natural numbers greater than 1 that have no divisors other than 1 and themselves. This means a prime number $\( p \)$ can only be evenly divided by 1 and $\( p \)$.

**Examples:**
- 2 (divisors: 1, 2)
- 3 (divisors: 1, 3)
- 5 (divisors: 1, 5)
- 7 (divisors: 1, 7)

### Non-Prime (Composite) Numbers

Numbers greater than 1 that are not prime are called composite numbers. They have divisors other than 1 and themselves.

**Examples:**
- 4 (divisors: 1, 2, 4)
- 6 (divisors: 1, 2, 3, 6)
- 8 (divisors: 1, 2, 4, 8)
- 9 (divisors: 1, 3, 9)

### Efficient Algorithms for Identifying Prime Numbers

To find prime numbers efficiently, we can use various algorithms. Here are two commonly used methods:

#### 1. Trial Division

Trial division tests if a number $\( n \)$ is prime by dividing it by all numbers less than $\( n \)$. If $\( n \)$ is divisible by any of these numbers, it's not prime.

**Steps:**
1. Start with a number $\( n \)$.
2. Check divisibility from 2 to $\( \sqrt{n} \)$.
3. If $\( n \)$ is divisible by any of these numbers, it's not prime.

**Example in Python:**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testing the function
print(is_prime(11))  # True
print(is_prime(15))  # False
```

#### 2. Sieve of Eratosthenes

The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified integer $\( n \)$.

**Steps:**
1. Create a list of integers from 2 to $\( n \)$.
2. Start with the first prime number (2).
3. Mark all multiples of this prime number as non-prime.
4. Move to the next number and repeat step 3 until you have processed numbers up to $\( \sqrt{n} \)$.

**Example in Python:**
```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p**2 <= n):
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Testing the function
print(sieve_of_eratosthenes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Application in the Ambrosial App

In the Ambrosial app, suppose we want to add a feature that allows users to generate a list of prime numbers up to a given number. This can be useful for learning purposes or for fun challenges among users.

**Implementation:**

1. **User Interface:**
   Add a form where users can input a number $\( n \)$.

2. **Backend Processing:**
   Use the `sieve_of_eratosthenes` function to generate the list of prime numbers up to $\( n \)$.

3. **Display Results:**
   Show the generated list to the user on the results page.

**Example Code Snippet:**
```python
from flask import Flask, request, render_template

app = Flask(__name__)

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p**2 <= n):
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

@app.route('/generate_primes', methods=['GET', 'POST'])
def generate_primes():
    if request.method == 'POST':
        n = int(request.form['number'])
        prime_numbers = sieve_of_eratosthenes(n)
        return render_template('primes.html', primes=prime_numbers)
    return render_template('generate_primes.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### End of Chapter MCQ

1. What is a prime number?
   - A) A number divisible by 1 and itself
   - B) A number divisible by 2
   - C) A number divisible by 3
   - D) A number divisible by 5

2. Which of the following is a prime number?
   - A) 4
   - B) 6
   - C) 8
   - D) 7

3. What is the first step in the trial division method to check if a number $\( n \)$ is prime?
   - A) Divide $\( n \)$ by all numbers less than $\( n \)$
   - B) Divide $\( n \)$ by 2
   - C) Check divisibility from 2 to $\( \sqrt{n} \)$
   - D) Check divisibility from 2 to $\( n \)$

4. In the Sieve of Eratosthenes algorithm, what is the initial value of $\( p \)$?
   - A) 1
   - B) 2
   - C) 3
   - D) 4

5. Which algorithm is more efficient for finding all prime numbers up to a large number $\( n \)$?
   - A) Trial Division
   - B) Sieve of Eratosthenes
   - C) Bubble Sort
   - D) Binary Search

6. In the Sieve of Eratosthenes, what do we do after marking the multiples of the current prime number?
   - A) Stop the algorithm
   - B) Move to the next prime number
   - C) Restart the algorithm
   - D) Mark the number itself as non-prime

7. What is the purpose of `int(n**0.5) + 1` in the trial division method?
   - A) To include all numbers up to $\( n \)$
   - B) To reduce the number of checks needed
   - C) To increase the number of checks needed
   - D) To simplify the code

8. How do you initiate the Sieve of Eratosthenes?
   - A) Start marking multiples of 1
   - B) Start with a list of True values for all numbers from 2 to $\( n \)$
   - C) Start marking multiples of $\( n \)$
   - D) Start with a list of False values for all numbers from 2 to $\( n \)$

9. What does the function `sieve_of_eratosthenes(n)` return?
   - A) A list of non-prime numbers up to $\( n \)$
   - B) A list of numbers divisible by 2 up to $\( n \)$
   - C) A list of prime numbers up to $\( n \)$
   - D) A list of numbers greater than $\( n \)$

10. In the Ambrosial app, what is the purpose of adding a feature to generate prime numbers?
    - A) For data storage
    - B) For user learning and engagement
    - C) For improving app performance
    - D) For database management

### Answers

1. A
2. D
3. C
4. B
5. B
6. B
7. B
8. B
9. C
10. B

## Sieve of Eratosthenes

### Understanding the Sieve of Eratosthenes

The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a specified integer $\( n \)$. It is highly efficient and works by iteratively marking the multiples of each prime number starting from 2.

### How the Algorithm Works

1. **Initialization:**
   - Create a list of boolean values, `primes`, indexed from 0 to $\( n \)$, initially all set to `True`. A value in `primes[i]` will be `True` if $\( i \)$ is a prime number.
   - Set `primes[0]` and `primes[1]` to `False` because 0 and 1 are not prime numbers.

2. **Marking Multiples:**
   - Start with the first prime number, $\( p = 2 \)$.
   - Mark all multiples of $\( p \)$ (i.e., $\( 2p, 3p, 4p, \ldots \)$) as `False` since they are not prime.
   - Find the next number in the list that is `True` and repeat the process.
   - Continue this process until $\( p^2 \)$ is greater than $\( n \)$.

3. **Collecting Primes:**
   - The numbers which remain `True` in the `primes` list are the prime numbers up to $\( n \)$.

### Example in Python
Here is a Python implementation of the Sieve of Eratosthenes:

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Testing the function
print(sieve_of_eratosthenes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Application in the Ambrosial App

In the Ambrosial app, a feature to generate prime numbers up to a given number can be added. This feature can enhance user engagement by providing educational content and interesting challenges.

**Steps to Implement:**

1. **User Interface:**
   - Add a form on the frontend where users can input a number $\( n \)$.

2. **Backend Processing:**
   - Use the `sieve_of_eratosthenes` function to compute prime numbers up to $\( n \)$.

3. **Displaying Results:**
   - Show the list of prime numbers on the results page.

### Flask Implementation Example

Here’s how this can be integrated into the Flask-based Ambrosial app:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

@app.route('/generate_primes', methods=['GET', 'POST'])
def generate_primes():
    if request.method == 'POST':
        n = int(request.form['number'])
        prime_numbers = sieve_of_eratosthenes(n)
        return render_template('primes.html', primes=prime_numbers)
    return render_template('generate_primes.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### End of Chapter MCQ

1. What is the first step in the Sieve of Eratosthenes algorithm?
   - A) Mark all even numbers as non-prime
   - B) Create a list of boolean values initialized to `True`
   - C) Start with the number 1
   - D) Mark all multiples of 5

2. In the Sieve of Eratosthenes, which numbers are initially set to `False` in the `primes` list?
   - A) 0 and 1
   - B) 1 and 2
   - C) 2 and 3
   - D) 3 and 4

3. What is the significance of $\( p^2 \)$ in the Sieve of Eratosthenes algorithm?
   - A) It is the smallest number to start marking multiples
   - B) It is the highest number to check for primality
   - C) It is the threshold beyond which marking multiples is unnecessary
   - D) It is the last number to be checked

4. How are non-prime numbers marked in the Sieve of Eratosthenes?
   - A) By setting their value to `True`
   - B) By setting their value to `False`
   - C) By skipping them
   - D) By deleting them from the list

5. What is the time complexity of the Sieve of Eratosthenes algorithm?
   - A) $\( O(n) \)$
   - B) $\( O(\sqrt{n}) \)$
   - C) $\( O(n \log \log n) \)$
   - D) $\( O(n^2) \)$

6. Which of the following is a prime number identified by the Sieve of Eratosthenes up to 30?
   - A) 9
   - B) 15
   - C) 23
   - D) 28

7. How does the Sieve of Eratosthenes improve efficiency over trial division?
   - A) By only checking even numbers
   - B) By marking multiples of each prime starting from $\( p^2 \)$
   - C) By using recursion
   - D) By using logarithmic checks

8. What is the main purpose of the boolean list in the Sieve of Eratosthenes?
   - A) To store the prime numbers directly
   - B) To mark whether numbers are prime or not
   - C) To count the number of primes
   - D) To sort the numbers

9. In the Ambrosial app, what input is required from the user to generate a list of prime numbers?
   - A) A range of numbers
   - B) A single integer $\( n \)$
   - C) A list of numbers
   - D) A string input

10. Why is the Sieve of Eratosthenes suitable for generating prime numbers in a web application?
    - A) It uses minimal memory
    - B) It is simple to implement
    - C) It is highly efficient for large ranges
    - D) It requires user interaction

### Answers

1. B
2. A
3. C
4. B
5. C
6. C
7. B
8. B
9. B
10. C

## Game Theory

### Basic Principles of Competitive Games

Game theory studies strategic interactions where players make decisions to maximize their outcomes. In competitive games, players often take turns, and each player's decision can affect the outcomes for all players.

**Key Concepts:**
1. **Players:** Individuals or entities making decisions in the game.
2. **Strategies:** Plans or actions taken by players to achieve their objectives.
3. **Payoffs:** Outcomes or rewards received by players based on the combination of strategies chosen.
4. **Games:** Scenarios or environments in which players interact.

### Optimal Play

Optimal play involves making the best possible moves to maximize a player's advantage or minimize losses, considering the strategies of other players. It often leads to a situation where no player can improve their outcome by changing their strategy unilaterally (Nash Equilibrium).

**Examples:**
- In chess, optimal play involves making moves that maximize the player's chances of winning or drawing while minimizing the opponent's chances of winning.
- In tic-tac-toe, optimal play ensures that a player either wins or ties the game.

### Understanding Win Conditions and Strategies

**Win Conditions:** 
These are specific conditions or states of the game that result in a player winning.

**Strategies Leading to a Win:**
Strategies that increase the likelihood of meeting the win conditions. This can involve offensive tactics (aggressively pursuing win conditions) or defensive tactics (preventing the opponent from achieving their win conditions).

### Example: Tic-Tac-Toe

**Win Conditions:**
- A player wins by placing three of their marks in a row, column, or diagonal.

**Strategies:**
- **Offensive Strategy:** Focus on creating opportunities to place three marks in a row.
- **Defensive Strategy:** Block the opponent's attempts to place three marks in a row.

**Optimal Play:**
- Always take the center if available.
- If the center is taken, take a corner.
- Block the opponent from completing three in a row.

### Example in Python: Tic-Tac-Toe

```python
# Tic-Tac-Toe game implementation
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, mark):
    # Check rows, columns, and diagonals
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [mark, mark, mark] in win_cond

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {players[turn]}, enter the row (0-2): "))
        col = int(input(f"Player {players[turn]}, enter the column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = players[turn]
            if check_win(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                return
            turn = (turn + 1) % 2
        else:
            print("Cell already taken, try again.")

    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()
```

### Application in the Ambrosial App

In the Ambrosial app, consider integrating a feature where users can participate in recipe competitions. Users can submit their recipes, and others can vote on them. The competition can have win conditions, such as the highest votes, and users can strategize to promote their recipes.

**Steps to Implement:**

1. **User Interface:**
   - Add a section for recipe competitions where users can submit their recipes.
   - Add voting functionality where users can vote on their favorite recipes.

2. **Backend Processing:**
   - Implement logic to track recipe submissions and votes.
   - Determine the winner based on the highest votes.

3. **Displaying Results:**
   - Show the winning recipes and the number of votes they received.

### End of Chapter MCQ

1. What is a player in game theory?
   - A) A person watching the game
   - B) An individual or entity making decisions in the game
   - C) A piece used in the game
   - D) A random number generator

2. What is a strategy in game theory?
   - A) A random action taken by a player
   - B) A plan or action taken by a player to achieve their objectives
   - C) A rule of the game
   - D) A type of game

3. What is the Nash Equilibrium?
   - A) A state where one player can improve their outcome
   - B) A state where no player can improve their outcome by changing their strategy unilaterally
   - C) A random state of the game
   - D) A winning strategy

4. In tic-tac-toe, what is an optimal first move?
   - A) The center
   - B) A corner
   - C) The edge
   - D) Any empty cell

5. What is a win condition in a game?
   - A) A condition where the game ends
   - B) A condition where a player wins the game
   - C) A condition where a player loses the game
   - D) A condition where the game draws

6. What should a player do if the center cell is taken in tic-tac-toe?
   - A) Take any cell
   - B) Take a corner cell
   - C) Take an edge cell
   - D) Skip their turn

7. What is the main goal of a defensive strategy in a game?
   - A) To score the most points
   - B) To block the opponent's win conditions
   - C) To make random moves
   - D) To speed up the game

8. In a competitive game, how do players' decisions affect the outcome?
   - A) They do not affect the outcome
   - B) They affect only their own outcome
   - C) They affect the outcome for all players
   - D) They affect only the opponent's outcome

9. What is the primary goal of optimal play?
   - A) To make the most moves
   - B) To maximize the player's advantage or minimize losses
   - C) To confuse the opponent
   - D) To end the game quickly

10. How can users participate in recipe competitions in the Ambrosial app?
    - A) By submitting recipes and voting on their favorites
    - B) By watching videos
    - C) By playing games
    - D) By writing reviews

### Answers

1. B
2. B
3. B
4. A
5. B
6. B
7. B
8. C
9. B
10. A

## Dynamic Programming and Memoization

### Introduction to Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful when the problem can be divided into overlapping subproblems that can be solved independently.

**Key Concepts:**
1. **Overlapping Subproblems:** Problems that can be broken down into smaller, reusable subproblems.
2. **Optimal Substructure:** The optimal solution of the problem can be constructed from optimal solutions of its subproblems.

### Memoization

Memoization is an optimization technique used to speed up dynamic programming. It involves storing the results of expensive function calls and reusing those results when the same inputs occur again.

**Key Concepts:**
1. **Cache:** A storage structure (like a dictionary) that saves the results of subproblems.
2. **Recursive Solution:** A solution that breaks the problem into smaller parts and solves each part recursively, storing results in the cache.

### Example: Fibonacci Sequence

The Fibonacci sequence is a classic example where dynamic programming and memoization can be applied.

**Recursive Solution Without Memoization:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Testing the function
print(fibonacci(10))  # Output: 55
```

This approach is inefficient for large $\( n \)$ because it recalculates the same values multiple times.

**Optimized Solution With Memoization:**

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Testing the function
print(fibonacci_memo(10))  # Output: 55
```

By using a memoization technique, we store previously computed values and avoid redundant calculations, making the algorithm more efficient.

### Application in the Ambrosial App

Consider a feature in the Ambrosial app where users can participate in recipe challenges that involve multiple rounds. Each round requires optimizing ingredient combinations to achieve the best recipe score.

**Steps to Implement:**

1. **User Interface:**
   - Add a form where users can input ingredients and their quantities.
   - Add a button to calculate the optimal combination for maximum recipe score.

2. **Backend Processing:**
   - Use dynamic programming and memoization to calculate the best ingredient combinations efficiently.

3. **Displaying Results:**
   - Show the optimal combination and the recipe score on the results page.

### Example: Recipe Score Optimization

```python
def max_recipe_score(ingredients, max_quantity, memo={}):
    if max_quantity in memo:
        return memo[max_quantity]
    if max_quantity == 0 or not ingredients:
        return 0
    
    ingredient = ingredients[0]
    include = (ingredient['score'] + max_recipe_score(ingredients, max_quantity - ingredient['quantity'], memo)
               if ingredient['quantity'] <= max_quantity else 0)
    exclude = max_recipe_score(ingredients[1:], max_quantity, memo)
    
    memo[max_quantity] = max(include, exclude)
    return memo[max_quantity]

# Example ingredients and their scores
ingredients = [
    {'name': 'flour', 'quantity': 2, 'score': 3},
    {'name': 'sugar', 'quantity': 1, 'score': 2},
    {'name': 'butter', 'quantity': 3, 'score': 4}
]

# Testing the function
max_quantity = 5
print(max_recipe_score(ingredients, max_quantity))  # Output: 6
```

### End of Chapter MCQ

1. What is the main goal of dynamic programming?
   - A) To solve problems using brute force
   - B) To solve complex problems by breaking them into simpler subproblems
   - C) To store all possible solutions
   - D) To generate random solutions

2. What is memoization?
   - A) A technique to speed up computation by storing previous results
   - B) A way to generate new problems
   - C) A method to avoid recursion
   - D) A technique to reduce memory usage

3. Which data structure is commonly used for memoization?
   - A) List
   - B) Set
   - C) Dictionary
   - D) Tuple

4. In the Fibonacci sequence example, what is stored in the memo dictionary?
   - A) The input value
   - B) The result of the Fibonacci function for each input
   - C) The sum of all Fibonacci numbers
   - D) The difference between Fibonacci numbers

5. What is the time complexity of the optimized Fibonacci function using memoization?
   - A) $\(O(n^2)\)$
   - B) $\(O(n \log n)\)$
   - C) $\(O(n)\)$
   - D) $\(O(\log n)\)$

6. In the recipe score optimization example, what does the function `max_recipe_score` calculate?
   - A) The minimum recipe score
   - B) The total number of ingredients
   - C) The maximum recipe score based on given ingredients and quantities
   - D) The average recipe score

7. How does dynamic programming improve efficiency in solving problems?
   - A) By generating random solutions
   - B) By solving each subproblem multiple times
   - C) By storing solutions to subproblems and reusing them
   - D) By using more memory

8. What is an overlapping subproblem?
   - A) A problem that cannot be solved
   - B) A problem that appears multiple times within a larger problem
   - C) A problem that does not have a solution
   - D) A unique problem

9. What is the optimal substructure property in dynamic programming?
   - A) The optimal solution can be constructed from optimal solutions of its subproblems
   - B) The optimal solution is unique
   - C) The optimal solution cannot be broken down into smaller problems
   - D) The optimal solution is always the smallest

10. In the Ambrosial app, how can dynamic programming be used to enhance recipe challenges?
    - A) By storing recipes
    - B) By calculating the optimal combination of ingredients for maximum score efficiently
    - C) By generating random ingredients
    - D) By sorting recipes alphabetically

### Answers

1. B
2. A
3. C
4. B
5. C
6. C
7. C
8. B
9. A
10. B

## Python Programming

### Loops and Conditional Statements

Loops and conditional statements are fundamental constructs in Python programming. They are essential for implementing game logic and algorithms.

#### Loops

Loops allow you to execute a block of code multiple times. Python provides two main types of loops: `for` loops and `while` loops.

**For Loops:**
A `for` loop iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.

```python
# Example: Iterating over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

**While Loops:**
A `while` loop executes a block of code as long as a specified condition is `True`.

```python
# Example: Using a while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

#### Conditional Statements

Conditional statements allow you to execute different blocks of code based on certain conditions. The main conditional statements in Python are `if`, `elif`, and `else`.

```python
# Example: Using conditional statements
number = 10
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
```

### Arrays and Lists

Arrays and lists are used to store collections of items. In Python, lists are more commonly used and provide flexibility and ease of use.

**Lists:**
A list is a collection of items that can be of different types. Lists are mutable, meaning their elements can be changed.

```python
# Example: Creating and modifying a list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

### Implementing Game Logic and Algorithms

By combining loops, conditional statements, and lists, you can implement complex game logic and algorithms. Let's consider an example where we use these constructs to implement a simple number guessing game.

### Example: Number Guessing Game

```python
import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    guess = None

    while guess != target_number:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")

# Run the game
number_guessing_game()
```

### Application in the Ambrosial App

In the Ambrosial app, you might need to manage lists of ingredients or implement game logic for recipe challenges. Here's an example of how you can use loops, conditional statements, and lists to handle user input and track the status of a recipe competition.

**Example: Managing Recipe Submissions**

```python
# List to store submitted recipes
recipes = []

def submit_recipe():
    recipe_name = input("Enter the name of your recipe: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    recipes.append({
        "name": recipe_name,
        "ingredients": ingredients
    })

def display_recipes():
    for recipe in recipes:
        print(f"Recipe: {recipe['name']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f" - {ingredient}")

def recipe_competition():
    while True:
        print("1. Submit a recipe")
        print("2. Display all recipes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            submit_recipe()
        elif choice == "2":
            display_recipes()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the recipe competition
recipe_competition()
```

### End of Chapter MCQ

1. What does a `for` loop do in Python?
   - A) Executes a block of code once
   - B) Executes a block of code a specific number of times
   - C) Executes a block of code while a condition is true
   - D) Executes a block of code until an error occurs

2. What is a list in Python?
   - A) A collection of immutable items
   - B) A collection of items that can be changed
   - C) A type of loop
   - D) A conditional statement

3. Which of the following is true about `while` loops?
   - A) They execute a block of code a fixed number of times
   - B) They execute a block of code as long as a condition is true
   - C) They are used to iterate over a sequence
   - D) They cannot be nested

4. What does the `elif` statement do?
   - A) It is used to end a loop
   - B) It checks an additional condition if the previous `if` statement is false
   - C) It always executes if the `if` statement is false
   - D) It is used to initialize a loop

5. How do you add an item to a list in Python?
   - A) `list.add(item)`
   - B) `list.append(item)`
   - C) `list.insert(item)`
   - D) `list.push(item)`

6. What will the following code print?
   ```python
   numbers = [1, 2, 3]
   for number in numbers:
       print(number)
   ```
   - A) 123
   - B) 1 2 3
   - C) [1, 2, 3]
   - D) Error

7. What does the `break` statement do in a loop?
   - A) It continues to the next iteration
   - B) It exits the loop immediately
   - C) It skips the current iteration
   - D) It does nothing

8. What will the following code output if the input is 50?
   ```python
   target_number = 50
   guess = int(input("Guess a number: "))
   if guess < target_number:
       print("Too low!")
   elif guess > target_number:
       print("Too high!")
   else:
       print("Correct!")
   ```
   - A) Too low!
   - B) Too high!
   - C) Correct!
   - D) Error

9. Which method removes the last item from a list in Python?
   - A) `remove()`
   - B) `pop()`
   - C) `delete()`
   - D) `discard()`

10. How do you iterate over a dictionary to print its keys and values?
    - A) `for key, value in dictionary.items():`
    - B) `for key, value in dictionary.keys():`
    - C) `for key, value in dictionary.values():`
    - D) `for key, value in dictionary.entries():`

### Answers

1. B
2. B
3. B
4. B
5. B
6. B
7. B
8. C
9. B
10. A
