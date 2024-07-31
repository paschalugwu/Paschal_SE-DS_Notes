## 2D Arrays (Matrices)

A 2D array, also known as a matrix, is a collection of elements arranged in rows and columns. Think of it as a table where data is stored in a grid format.

### Accessing Elements in a 2D Array

To access elements in a 2D array, you need to know the row and column indices. The first index represents the row, and the second index represents the column. In most programming languages, indices start from 0.

**Example in Python:**
```python
# Define a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access the element in the second row and third column
element = matrix[1][2]  # This will give us 6
print(element)  # Output: 6
```

### Iterating Over Elements in a 2D Array

You can iterate over the elements of a 2D array using nested loops. The outer loop iterates over the rows, while the inner loop iterates over the columns within each row.

**Example in Python:**
```python
# Define a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over each element in the 2D array
for row in matrix:
    for element in row:
        print(element)
```

### Navigating Through Adjacent Cells

In a 2D array, each cell can have up to four adjacent cells: left, right, top, and bottom. To navigate through these adjacent cells, you need to manipulate the indices accordingly.

**Example in Python:**
```python
# Define a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define the position of the cell we are interested in
row = 1
col = 1

# Accessing adjacent cells
left = matrix[row][col - 1] if col > 0 else None
right = matrix[row][col + 1] if col < len(matrix[0]) - 1 else None
top = matrix[row - 1][col] if row > 0 else None
bottom = matrix[row + 1][col] if row < len(matrix) - 1 else None

print("Left:", left)      # Output: 4
print("Right:", right)    # Output: 6
print("Top:", top)        # Output: 2
print("Bottom:", bottom)  # Output: 8
```

### Real-World Application

Imagine you are developing a game where you need to check if a player can move to an adjacent cell on a game board. You would use the concept of navigating through adjacent cells to determine the valid moves.

### End of Chapter MCQ

1. What is the value of `matrix[2][1]` in the following 2D array?
   ```python
   matrix = [
       [5, 3, 1],
       [2, 9, 7],
       [8, 6, 4]
   ]
   ```
   a) 5  
   b) 9  
   c) 6  
   d) 4  

2. Which of the following code snippets correctly iterates over all elements in a 2D array?
   a)
   ```python
   for row in matrix:
       print(row)
   ```
   b)
   ```python
   for row in matrix:
       for element in row:
           print(element)
   ```
   c)
   ```python
   for col in matrix:
       for element in col:
           print(element)
   ```
   d)
   ```python
   for element in matrix:
       print(element)
   ```

3. How would you access the top adjacent cell of `matrix[1][1]` if `matrix` is a 3x3 matrix?
   a) `matrix[0][1]`  
   b) `matrix[1][0]`  
   c) `matrix[1][2]`  
   d) `matrix[2][1]`  

4. What does the following code snippet print?
   ```python
   matrix = [
       [10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]
   ]
   print(matrix[2][0])
   ```
   a) 10  
   b) 40  
   c) 70  
   d) 90  

5. Which of the following is NOT a valid way to access an element in a 2D array?
   a) `matrix[0][0]`  
   b) `matrix[1, 1]`  
   c) `matrix[2][2]`  
   d) `matrix[1][2]`  

6. If `matrix` is defined as `matrix = [[1, 2], [3, 4]]`, what will `matrix[1][1]` return?
   a) 1  
   b) 2  
   c) 3  
   d) 4  

7. In a 2D array, how can you find the number of rows?
   a) `len(matrix)`  
   b) `len(matrix[0])`  
   c) `matrix.length`  
   d) `matrix[0].length`  

8. What is the correct way to print all elements in the second row of a 2D array named `matrix`?
   a) `print(matrix[1])`  
   b) `print(matrix[0])`  
   c) `print(matrix[2])`  
   d) `print(matrix[1][0:])`  

9. How do you access the bottom adjacent cell of `matrix[1][1]` in a 3x3 matrix?
   a) `matrix[2][1]`  
   b) `matrix[1][2]`  
   c) `matrix[0][1]`  
   d) `matrix[1][0]`  

10. Given the following 2D array, which statement is true?
    ```python
    matrix = [
        [3, 5, 7],
        [1, 4, 9],
        [8, 6, 2]
    ]
    ```
    a) `matrix[1][2]` is 4  
    b) `matrix[2][1]` is 6  
    c) `matrix[0][0]` is 5  
    d) `matrix[1][0]` is 9  

### Answers

1. c) 6
2. b) `for row in matrix: for element in row: print(element)`
3. a) `matrix[0][1]`
4. c) 70
5. b) `matrix[1, 1]`
6. d) 4
7. a) `len(matrix)`
8. a) `print(matrix[1])`
9. a) `matrix[2][1]`
10. b) `matrix[2][1]` is 6

## Conditional Logic: Applying Conditions to Determine Whether a Cell Contributes to the Perimeter of the Island

Conditional logic is essential in programming for making decisions based on specific conditions. In this context, we will learn how to use conditional logic to determine whether a cell in a 2D array contributes to the perimeter of an island.

### Understanding the Problem

Imagine you have a 2D grid representing a map where `1` represents land and `0` represents water. An island is a group of `1`s (land) connected horizontally or vertically. The perimeter of the island is the total length of the edges that are adjacent to water or the edges of the grid.

### Applying Conditional Logic

To determine if a cell contributes to the perimeter of the island, we need to check its adjacent cells. If an adjacent cell is water or it’s on the boundary of the grid, then that part of the cell's edge contributes to the perimeter.

**Example in Python:**
```python
def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter

# Example grid
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

### Explanation

1. **Check Top**: If the cell is in the first row (`row == 0`) or the cell above it is water (`grid[row-1][col] == 0`), add to the perimeter.
2. **Check Bottom**: If the cell is in the last row (`row == rows-1`) or the cell below it is water (`grid[row+1][col] == 0`), add to the perimeter.
3. **Check Left**: If the cell is in the first column (`col == 0`) or the cell to the left is water (`grid[row][col-1] == 0`), add to the perimeter.
4. **Check Right**: If the cell is in the last column (`col == cols-1`) or the cell to the right is water (`grid[row][col+1] == 0`), add to the perimeter.

### Real-World Application

This logic can be applied in geographic information systems (GIS) to calculate the boundaries of landmasses, design game maps where players can build on islands, or even in robotics for pathfinding on different terrains.

### End of Chapter MCQ

1. What does `if row == 0 or grid[row-1][col] == 0:` check?
   a) If the cell is in the last row or the cell below it is water  
   b) If the cell is in the first row or the cell above it is water  
   c) If the cell is in the first column or the cell to the left is water  
   d) If the cell is in the last column or the cell to the right is water  

2. What is the perimeter of the island in the following grid?
   ```python
   grid = [
       [1, 1],
       [1, 1]
   ]
   ```
   a) 4  
   b) 6  
   c) 8  
   d) 10  

3. In the context of the provided example, what does `cols` represent?
   a) The number of rows in the grid  
   b) The number of columns in the grid  
   c) The number of islands in the grid  
   d) The number of water cells in the grid  

4. Which condition checks if a cell is on the boundary of the grid on the right side?
   a) `if col == 0 or grid[row][col-1] == 0:`  
   b) `if col == cols-1 or grid[row][col+1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if row == rows-1 or grid[row+1][col] == 0:`  

5. How many times will the inner loop run for a 3x3 grid?
   a) 3  
   b) 6  
   c) 9  
   d) 12  

6. What value will be added to the perimeter if `grid[2][1]` is `1` and `grid[1][1]` is `0`?
   a) 0  
   b) 1  
   c) 2  
   d) 3  

7. Which part of the code checks if a cell is contributing to the perimeter on the left?
   a) `if col == 0 or grid[row][col-1] == 0:`  
   b) `if col == cols-1 or grid[row][col+1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if row == rows-1 or grid[row+1][col] == 0:`  

8. If `grid` is `[[1, 0], [0, 1]]`, what is the perimeter?
   a) 2  
   b) 4  
   c) 6  
   d) 8  

9. What does the `perimeter` variable store?
   a) The number of land cells  
   b) The total number of cells in the grid  
   c) The length of the edges of land cells adjacent to water or the grid boundary  
   d) The number of water cells  

10. How is the perimeter calculated in the provided example?
    a) By adding the number of land cells  
    b) By adding the length of the edges of each cell in the grid  
    c) By adding the length of the edges of land cells adjacent to water or the grid boundary  
    d) By subtracting the number of water cells from the total number of cells  

### Answers

1. b) If the cell is in the first row or the cell above it is water
2. c) 8
3. b) The number of columns in the grid
4. b) `if col == cols-1 or grid[row][col+1] == 0:`
5. c) 9
6. b) 1
7. a) `if col == 0 or grid[row][col-1] == 0:`
8. d) 8
9. c) The length of the edges of land cells adjacent to water or the grid boundary
10. c) By adding the length of the edges of land cells adjacent to water or the grid boundary

## Counting Techniques: Developing a Method to Count the Edges that Contribute to the Island’s Perimeter

In this section, we will learn how to develop a method to count the edges that contribute to the perimeter of an island in a 2D grid. This involves using counting techniques and conditional logic to identify and count the relevant edges.

### Understanding the Problem

We have a 2D grid where `1` represents land and `0` represents water. An island is formed by connected `1`s (land cells). Our goal is to calculate the perimeter of the island by counting the edges of the land cells that are adjacent to water or are on the boundary of the grid.

### Method to Count the Edges

To count the edges that contribute to the island’s perimeter, we need to check each land cell (`1`) and its adjacent cells (top, bottom, left, and right). If an adjacent cell is water (`0`) or if the land cell is on the boundary of the grid, then that edge contributes to the perimeter.

**Example in Python:**
```python
def count_island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter

# Example grid
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(count_island_perimeter(grid))  # Output: 16
```

### Explanation

1. **Check Top**: If the cell is in the first row (`row == 0`) or the cell above it is water (`grid[row-1][col] == 0`), add to the perimeter.
2. **Check Bottom**: If the cell is in the last row (`row == rows-1`) or the cell below it is water (`grid[row+1][col] == 0`), add to the perimeter.
3. **Check Left**: If the cell is in the first column (`col == 0`) or the cell to the left is water (`grid[row][col-1] == 0`), add to the perimeter.
4. **Check Right**: If the cell is in the last column (`col == cols-1`) or the cell to the right is water (`grid[row][col+1] == 0`), add to the perimeter.

### Real-World Application

This technique can be applied in various real-world scenarios such as geographic information systems (GIS) for calculating the perimeter of landmasses, game development for defining the boundaries of terrains, and robotics for pathfinding on different surfaces.

### End of Chapter MCQ

1. In the method to count the edges, what does `if row == 0 or grid[row-1][col] == 0:` check?
   a) If the cell is in the last row or the cell below it is water  
   b) If the cell is in the first row or the cell above it is water  
   c) If the cell is in the first column or the cell to the left is water  
   d) If the cell is in the last column or the cell to the right is water  

2. What is the perimeter of the island in the following grid?
   ```python
   grid = [
       [1, 1],
       [1, 1]
   ]
   ```
   a) 4  
   b) 6  
   c) 8  
   d) 10  

3. How many edges contribute to the perimeter for the cell at `grid[1][1]` if `grid` is as follows?
   ```python
   grid = [
       [0, 1, 0],
       [1, 1, 1],
       [0, 1, 0]
   ]
   ```
   a) 0  
   b) 1  
   c) 2  
   d) 4  

4. Which condition checks if a cell is on the boundary of the grid on the left side?
   a) `if col == 0 or grid[row][col-1] == 0:`  
   b) `if col == cols-1 or grid[row][col+1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if row == rows-1 or grid[row+1][col] == 0:`  

5. What value will be added to the perimeter if `grid[2][1]` is `1` and `grid[1][1]` is `0`?
   a) 0  
   b) 1  
   c) 2  
   d) 3  

6. How is the perimeter of an island calculated in the provided method?
   a) By adding the number of land cells  
   b) By adding the length of the edges of each cell in the grid  
   c) By adding the length of the edges of land cells adjacent to water or the grid boundary  
   d) By subtracting the number of water cells from the total number of cells  

7. Which part of the code checks if a cell is contributing to the perimeter on the right?
   a) `if col == 0 or grid[row][col-1] == 0:`  
   b) `if col == cols-1 or grid[row][col+1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if row == rows-1 or grid[row+1][col] == 0:`  

8. If `grid` is `[[1, 0], [0, 1]]`, what is the perimeter?
   a) 2  
   b) 4  
   c) 6  
   d) 8  

9. What does the `perimeter` variable store?
   a) The number of land cells  
   b) The total number of cells in the grid  
   c) The length of the edges of land cells adjacent to water or the grid boundary  
   d) The number of water cells  

10. How many edges contribute to the perimeter for the cell at `grid[0][0]` if `grid` is `[[1, 1], [1, 1]]`?
    a) 0  
    b) 1  
    c) 2  
    d) 3  

### Answers

1. b) If the cell is in the first row or the cell above it is water
2. c) 8
3. c) 2
4. a) `if col == 0 or grid[row][col-1] == 0:`
5. b) 1
6. c) By adding the length of the edges of land cells adjacent to water or the grid boundary
7. b) `if col == cols-1 or grid[row][col+1] == 0:`
8. d) 8
9. c) The length of the edges of land cells adjacent to water or the grid boundary
10. d) 3

## Problem-Solving Strategies: Breaking Down the Problem into Smaller Tasks

Effective problem-solving involves breaking down a complex problem into manageable tasks. In this context, we will break down the problem of calculating the perimeter of an island in a 2D grid into smaller, manageable tasks.

### Understanding the Problem

We have a 2D grid where `1` represents land and `0` represents water. Our goal is to calculate the perimeter of the island formed by connected land cells. We will break this problem down into smaller tasks: identifying land cells and calculating their contribution to the perimeter.

### Breaking Down the Problem

1. **Identify Land Cells**: Traverse the grid to find all the land cells (`1`).
2. **Calculate Contribution to Perimeter**: For each land cell, determine its contribution to the perimeter by checking its adjacent cells (top, bottom, left, and right).

**Example in Python:**
```python
def calculate_island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Identify land cell
                # Check top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter

# Example grid
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(calculate_island_perimeter(grid))  # Output: 16
```

### Explanation

1. **Identify Land Cells**: We use nested loops to traverse each cell in the grid. If a cell contains `1`, it is identified as a land cell.
2. **Calculate Contribution to Perimeter**: For each land cell, we check its adjacent cells:
    - **Check Top**: If the cell is in the first row (`row == 0`) or the cell above it is water (`grid[row-1][col] == 0`), add to the perimeter.
    - **Check Bottom**: If the cell is in the last row (`row == rows-1`) or the cell below it is water (`grid[row+1][col] == 0`), add to the perimeter.
    - **Check Left**: If the cell is in the first column (`col == 0`) or the cell to the left is water (`grid[row][col-1] == 0`), add to the perimeter.
    - **Check Right**: If the cell is in the last column (`col == cols-1`) or the cell to the right is water (`grid[row][col+1] == 0`), add to the perimeter.

### Real-World Application

Breaking down problems into smaller tasks is a critical skill in software engineering. This approach can be applied to various scenarios such as:
- **Geographic Information Systems (GIS)**: Calculating the boundaries of landmasses.
- **Game Development**: Defining the boundaries of terrains or game maps.
- **Robotics**: Pathfinding and obstacle detection on different surfaces.

### End of Chapter MCQ

1. What is the first step in breaking down the problem of calculating the island perimeter?
   a) Calculate the total number of cells  
   b) Identify water cells  
   c) Identify land cells  
   d) Count the total number of rows and columns  

2. What does the condition `if grid[row][col] == 1:` check?
   a) If the cell is water  
   b) If the cell is land  
   c) If the cell is on the boundary of the grid  
   d) If the cell is adjacent to water  

3. How do we determine if a land cell contributes to the perimeter on the top side?
   a) `if row == rows-1 or grid[row+1][col] == 0:`  
   b) `if col == 0 or grid[row][col-1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if col == cols-1 or grid[row][col+1] == 0:`  

4. What is the perimeter of the island in the following grid?
   ```python
   grid = [
       [1, 1],
       [1, 1]
   ]
   ```
   a) 4  
   b) 6  
   c) 8  
   d) 10  

5. Which part of the code checks if a cell is contributing to the perimeter on the left?
   a) `if col == 0 or grid[row][col-1] == 0:`  
   b) `if col == cols-1 or grid[row][col+1] == 0:`  
   c) `if row == 0 or grid[row-1][col] == 0:`  
   d) `if row == rows-1 or grid[row+1][col] == 0:`  

6. If `grid` is `[[1, 0], [0, 1]]`, what is the perimeter?
   a) 2  
   b) 4  
   c) 6  
   d) 8  

7. How many edges contribute to the perimeter for the cell at `grid[2][1]` if `grid` is as follows?
   ```python
   grid = [
       [0, 1, 0],
       [1, 1, 1],
       [0, 1, 0]
   ]
   ```
   a) 0  
   b) 1  
   c) 2  
   d) 4  

8. What does the `perimeter` variable store?
   a) The number of land cells  
   b) The total number of cells in the grid  
   c) The length of the edges of land cells adjacent to water or the grid boundary  
   d) The number of water cells  

9. How is the perimeter of an island calculated in the provided method?
    a) By adding the number of land cells  
    b) By adding the length of the edges of each cell in the grid  
    c) By adding the length of the edges of land cells adjacent to water or the grid boundary  
    d) By subtracting the number of water cells from the total number of cells  

10. What value will be added to the perimeter if `grid[2][1]` is `1` and `grid[1][1]` is `0`?
    a) 0  
    b) 1  
    c) 2  
    d) 3  

### Answers

1. c) Identify land cells
2. b) If the cell is land
3. c) `if row == 0 or grid[row-1][col] == 0:`
4. c) 8
5. a) `if col == 0 or grid[row][col-1] == 0:`
6. d) 8
7. c) 2
8. c) The length of the edges of land cells adjacent to water or the grid boundary
9. c) By adding the length of the edges of land cells adjacent to water or the grid boundary
10. b) 1

## Python Programming: Nested Loops and Conditional Statements

In this section, we will learn how to use nested loops for iterating over grid cells and conditional statements to check the status of adjacent cells. These techniques are essential for solving problems related to 2D arrays, such as calculating the perimeter of an island in a grid.

### Nested Loops for Iterating Over Grid Cells

Nested loops allow us to iterate over each cell in a 2D grid. The outer loop iterates through the rows, and the inner loop iterates through the columns of each row.

**Example:**
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        print(grid[row][col], end=" ")
    print()
```

### Conditional Statements to Check the Status of Adjacent Cells

Conditional statements allow us to check the status of adjacent cells (top, bottom, left, right) and make decisions based on their values. This is useful for determining if a cell contributes to the perimeter of an island.

**Example:**
```python
def calculate_island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Check top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter

# Example grid
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(calculate_island_perimeter(grid))  # Output: 16
```

### Explanation

1. **Nested Loops**: The outer loop iterates through each row, and the inner loop iterates through each column within that row. This allows us to access each cell in the grid.
2. **Conditional Statements**: 
    - **Top Check**: If the cell is in the first row (`row == 0`) or the cell above it is water (`grid[row-1][col] == 0`), increment the perimeter.
    - **Bottom Check**: If the cell is in the last row (`row == rows-1`) or the cell below it is water (`grid[row+1][col] == 0`), increment the perimeter.
    - **Left Check**: If the cell is in the first column (`col == 0`) or the cell to the left is water (`grid[row][col-1] == 0`), increment the perimeter.
    - **Right Check**: If the cell is in the last column (`col == cols-1`) or the cell to the right is water (`grid[row][col+1] == 0`), increment the perimeter.

### Real-World Application

These techniques are widely used in various fields such as:
- **Image Processing**: Iterating over pixels in an image to apply filters or detect edges.
- **Game Development**: Checking the status of cells in a game board or map for pathfinding and collision detection.
- **Robotics**: Navigating a grid-based environment by checking the status of adjacent cells to avoid obstacles.

### End of Chapter MCQ

1. What is the purpose of nested loops in the context of a 2D grid?
   a) To iterate over each element in a 1D array  
   b) To iterate over each cell in a 2D grid  
   c) To find the maximum value in the grid  
   d) To sort the elements of the grid  

2. What does the inner loop in nested loops typically iterate over?
   a) Rows of the grid  
   b) Columns of the grid  
   c) Diagonals of the grid  
   d) All elements of the grid simultaneously  

3. What does the condition `if row == 0 or grid[row-1][col] == 0:` check?
   a) If the cell is in the last row or the cell below it is water  
   b) If the cell is in the first row or the cell above it is water  
   c) If the cell is in the first column or the cell to the left is water  
   d) If the cell is in the last column or the cell to the right is water  

4. How many times will the inner loop execute if the grid has 3 rows and 4 columns?
   a) 3  
   b) 4  
   c) 7  
   d) 12  

5. What value will be added to the perimeter if `grid[1][1]` is `1` and `grid[1][2]` is `0`?
   a) 0  
   b) 1  
   c) 2  
   d) 3  

6. Which conditional check verifies if a cell is contributing to the perimeter on the right side?
   a) `if row == 0 or grid[row-1][col] == 0:`  
   b) `if col == 0 or grid[row][col-1] == 0:`  
   c) `if row == rows-1 or grid[row+1][col] == 0:`  
   d) `if col == cols-1 or grid[row][col+1] == 0:`  

7. How can you identify a land cell in a grid?
   a) `if grid[row][col] == 0:`  
   b) `if grid[row][col] == 1:`  
   c) `if grid[row][col] == 2:`  
   d) `if grid[row][col] == -1:`  

8. If `grid` is `[[1, 1], [1, 0]]`, what is the perimeter?
   a) 4  
   b) 6  
   c) 8  
   d) 10  

9. What does the `perimeter` variable store?
   a) The number of land cells  
   b) The total number of cells in the grid  
   c) The length of the edges of land cells adjacent to water or the grid boundary  
   d) The number of water cells  

10. How is the perimeter of an island calculated in the provided method?
    a) By adding the number of land cells  
    b) By adding the length of the edges of each cell in the grid  
    c) By adding the length of the edges of land cells adjacent to water or the grid boundary  
    d) By subtracting the number of water cells from the total number of cells  

### Answers

1. b) To iterate over each cell in a 2D grid
2. b) Columns of the grid
3. b) If the cell is in the first row or the cell above it is water
4. d) 12
5. b) 1
6. d) `if col == cols-1 or grid[row][col+1] == 0:`
7. b) `if grid[row][col] == 1:`
8. b) 6
9. c) The length of the edges of land cells adjacent to water or the grid boundary
10. c) By adding the length of the edges of land cells adjacent to water or the grid boundary
