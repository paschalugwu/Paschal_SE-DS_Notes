# Matrix Representation in Python

## Understanding 2D Matrices Using Lists of Lists in Python

In Python, a 2D matrix is commonly represented as a list of lists. Each element of the main list is another list that represents a row in the matrix.

### Creating a 2D Matrix

A 2D matrix can be created manually by defining a list of lists. Here's an example of a 3x3 matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

In this example, `matrix` is a list containing three lists. Each of these lists contains three elements, making it a 3x3 matrix.

### Accessing Elements in a 2D Matrix

You can access elements in a 2D matrix using two indices: one for the row and one for the column. The first index refers to the row number and the second index refers to the column number. Both indices start from 0.

For example, to access the element in the second row and third column (which is `6`), you would do the following:

```python
element = matrix[1][2]
print(element)  # Output: 6
```

### Modifying Elements in a 2D Matrix

You can modify elements in a 2D matrix in a similar way to accessing them. Specify the row and column indices of the element you want to change, and then assign a new value to it.

For example, to change the element in the first row and second column to `10`, you would do:

```python
matrix[0][1] = 10
print(matrix)  # Output: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]
```

## Real-World Applications

### Example 1: Image Representation

A common real-world application of 2D matrices is in image representation. In a grayscale image, each pixel's brightness can be represented as an integer. The entire image can be represented as a 2D matrix where each element is the brightness value of a pixel.

```python
image = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]
]
```

### Example 2: Game Boards

Another application is representing game boards, such as a chessboard or tic-tac-toe grid. Each cell of the board can be represented by an element in the matrix.

```python
tic_tac_toe = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]
```

## End-of-Chapter Multiple Choice Questions

1. What is a 2D matrix in Python?
    - a) A list of tuples
    - b) A list of dictionaries
    - c) A list of lists
    - d) A list of sets

2. How do you access the element in the first row and third column of a matrix?
    - a) matrix[1][3]
    - b) matrix[0][2]
    - c) matrix[2][0]
    - d) matrix[3][1]

3. How do you modify the element in the second row and second column to `15`?
    - a) matrix[1][1] = 15
    - b) matrix[2][2] = 15
    - c) matrix[1][2] = 15
    - d) matrix[0][1] = 15

4. Which of the following can be represented by a 2D matrix?
    - a) An image
    - b) A game board
    - c) Both a and b
    - d) None of the above

5. What will `print(matrix[2][2])` output if the matrix is `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`?
    - a) 5
    - b) 6
    - c) 9
    - d) 3

6. How do you create a 2x2 matrix with all elements set to `0`?
    - a) matrix = [[0, 0], [0, 0]]
    - b) matrix = [[0, 0, 0], [0, 0, 0]]
    - c) matrix = [(0, 0), (0, 0)]
    - d) matrix = [0, 0, 0, 0]

7. How do you represent the brightness values of a grayscale image using a 2D matrix?
    - a) Using a list of strings
    - b) Using a list of integers
    - c) Using a list of lists of integers
    - d) Using a list of tuples of integers

8. In a tic-tac-toe grid represented as a 2D matrix, what would the element in the second row and first column be for the matrix `[['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]`?
    - a) 'X'
    - b) 'O'
    - c) ' '
    - d) None

9. What is the main advantage of using a 2D matrix to represent data?
    - a) It saves memory
    - b) It is faster
    - c) It organizes data in a grid-like structure
    - d) It is more readable

10. How do you print the entire second row of a matrix?
    - a) print(matrix[2])
    - b) print(matrix[1])
    - c) print(matrix[0])
    - d) print(matrix[3])

## Answers

1. c) A list of lists
2. b) matrix[0][2]
3. a) matrix[1][1] = 15
4. c) Both a and b
5. c) 9
6. a) matrix = [[0, 0], [0, 0]]
7. c) Using a list of lists of integers
8. b) 'O'
9. c) It organizes data in a grid-like structure
10. b) print(matrix[1])

# In-place Operations

## Performing Operations on Data Without Creating a Copy

In-place operations are techniques where changes are made directly to the data structure, without creating a new copy. This is useful for saving memory and improving performance, especially when working with large datasets.

### Example: In-place Addition

Consider a list where we want to add a constant value to each element. An in-place operation would modify the original list directly.

```python
numbers = [1, 2, 3, 4, 5]

# Add 10 to each element in place
for i in range(len(numbers)):
    numbers[i] += 10

print(numbers)  # Output: [11, 12, 13, 14, 15]
```

In this example, `numbers` is modified directly, and no new list is created.

### Example: In-place Matrix Transposition

Transposing a matrix means swapping its rows and columns. Here's how to do this in place for a square matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix in place
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

In this example, each element `matrix[i][j]` is swapped with `matrix[j][i]`, transposing the matrix without creating a new one.

## Importance of Minimizing Space Complexity

Minimizing space complexity means using as little additional memory as possible. This is important for efficiency, especially with large datasets or limited memory environments.

### Example: Sorting in Place

Sorting a list can be done in place, using algorithms like QuickSort or Bubble Sort. Here's an example using Python's built-in sort method, which sorts the list in place:

```python
numbers = [5, 3, 8, 6, 2]

# Sort the list in place
numbers.sort()

print(numbers)  # Output: [2, 3, 5, 6, 8]
```

In this example, `numbers` is sorted directly, and no additional list is created.

### Real-World Application: Image Processing

In image processing, applying filters or transformations to an image can be done in place to save memory. For instance, converting an image to grayscale can be performed directly on the pixel array.

```python
# Example pixel data for a 2x2 image (R, G, B)
image = [
    [(255, 0, 0), (0, 255, 0)],
    [(0, 0, 255), (255, 255, 0)]
]

# Convert to grayscale in place
for i in range(len(image)):
    for j in range(len(image[i])):
        r, g, b = image[i][j]
        # Calculate the grayscale value
        gray = int(0.3 * r + 0.59 * g + 0.11 * b)
        # Update the pixel with the grayscale value
        image[i][j] = (gray, gray, gray)

print(image)  # Output: [[(76, 76, 76), (149, 149, 149)], [(29, 29, 29), (225, 225, 225)]]
```

## End-of-Chapter Multiple Choice Questions

1. What is an in-place operation?
    - a) An operation that creates a new copy of the data structure
    - b) An operation that modifies the data structure directly
    - c) An operation that deletes the data structure
    - d) An operation that sorts the data structure

2. How do you add 10 to each element of a list `numbers` in place?
    - a) `new_numbers = [x + 10 for x in numbers]`
    - b) `numbers = [x + 10 for x in numbers]`
    - c) `for i in range(len(numbers)): numbers[i] += 10`
    - d) `numbers = numbers + 10`

3. Which of the following is an example of in-place matrix transposition?
    - a) Creating a new transposed matrix
    - b) Swapping elements directly within the same matrix
    - c) Deleting the original matrix
    - d) Multiplying each element by its index

4. Why is minimizing space complexity important?
    - a) To make the code look cleaner
    - b) To reduce memory usage
    - c) To increase the number of operations
    - d) To make the program run slower

5. How do you sort a list `numbers` in place?
    - a) `sorted_numbers = sorted(numbers)`
    - b) `numbers = sorted(numbers)`
    - c) `numbers.sort()`
    - d) `numbers = numbers.sort()`

6. What does the following code do?
    ```python
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    ```
    - a) Sorts the matrix
    - b) Transposes the matrix in place
    - c) Reverses the matrix
    - d) Deletes the matrix

7. In image processing, why would you convert an image to grayscale in place?
    - a) To increase the file size
    - b) To save memory
    - c) To make the image colorful
    - d) To create a new image

8. Which of the following is NOT an in-place operation?
    - a) `numbers.sort()`
    - b) `numbers.append(10)`
    - c) `numbers = [x * 2 for x in numbers]`
    - d) `numbers.extend([10, 20])`

9. What is the main advantage of in-place operations for large datasets?
    - a) They are easier to write
    - b) They use less memory
    - c) They always run faster
    - d) They create multiple copies of the data

10. How do you modify an element at index `2` in a list `numbers` to `20` in place?
    - a) `numbers[2] = 20`
    - b) `numbers = [20 if i == 2 else x for i, x in enumerate(numbers)]`
    - c) `numbers.insert(2, 20)`
    - d) `numbers.remove(2)`

## Answers

1. b) An operation that modifies the data structure directly
2. c) for i in range(len(numbers)): numbers[i] += 10
3. b) Swapping elements directly within the same matrix
4. b) To reduce memory usage
5. c) numbers.sort()
6. b) Transposes the matrix in place
7. b) To save memory
8. c) numbers = [x * 2 for x in numbers]
9. b) They use less memory
10. a) numbers[2] = 20

# Matrix Transposition

## Understanding the Concept of Transposing a Matrix

Matrix transposition involves swapping the rows and columns of a matrix. For a given matrix \( A \), the transpose of \( A \), denoted as \( A^T \), is formed by turning the rows of \( A \) into columns and the columns into rows.

### Example of Transposing a Matrix

Consider a matrix \( A \):

\[ 
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
\]

The transpose of \( A \), \( A^T \), is:

\[ 
A^T = \begin{pmatrix}
1 & 4 & 7 \\
2 & 5 & 8 \\
3 & 6 & 9
\end{pmatrix}
\]

### Implementing Matrix Transposition in Python

To transpose a matrix in Python, you can use a nested loop to swap the elements.

```python
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose(matrix)
print(transposed_matrix)
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

In this example, the function `transpose` swaps the elements \( matrix[i][j] \) with \( matrix[j][i] \) to transpose the matrix.

## Implementing Matrix Transposition as a Step in the Rotation Process

Matrix transposition is often a step in more complex matrix operations, such as rotating a matrix. To rotate a matrix by 90 degrees clockwise, you can first transpose the matrix and then reverse each row.

### Rotating a Matrix by 90 Degrees Clockwise

1. Transpose the matrix.
2. Reverse each row of the transposed matrix.

```python
def rotate_90_clockwise(matrix):
    # Transpose the matrix
    transpose(matrix)
    
    # Reverse each row
    for row in matrix:
        row.reverse()
    
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_90_clockwise(matrix)
print(rotated_matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

In this example, the function `rotate_90_clockwise` first transposes the matrix and then reverses each row to achieve a 90-degree rotation.

## End-of-Chapter Multiple Choice Questions

1. What is the transpose of the matrix \( \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix} \)?
    - a) \( \begin{pmatrix}1 & 3 \\ 2 & 4 \end{pmatrix} \)
    - b) \( \begin{pmatrix}4 & 3 \\ 2 & 1 \end{pmatrix} \)
    - c) \( \begin{pmatrix}1 & 2 \\ 3 & 4 \end{pmatrix} \)
    - d) \( \begin{pmatrix}2 & 1 \\ 4 & 3 \end{pmatrix} \)

2. What does transposing a matrix involve?
    - a) Multiplying each element by -1
    - b) Swapping rows with columns
    - c) Reversing the order of elements
    - d) Doubling the size of the matrix

3. In Python, which operation correctly swaps the elements \( matrix[i][j] \) and \( matrix[j][i] \)?
    - a) `matrix[i][j] = matrix[j][i]`
    - b) `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`
    - c) `matrix[i][j] = matrix[i][j]`
    - d) `matrix[j][i] = matrix[i][j]`

4. What is the first step to rotate a matrix by 90 degrees clockwise?
    - a) Reverse each row
    - b) Reverse each column
    - c) Transpose the matrix
    - d) Add 90 to each element

5. After transposing the matrix \( \begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \), what is the next step to rotate it by 90 degrees clockwise?
    - a) Reverse each row
    - b) Reverse each column
    - c) Transpose it again
    - d) Rotate it by another 90 degrees

6. Which function correctly transposes a matrix in place?
    - a) 
    ```python
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - b) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - c) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - d) 
    ```python
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```

7. What is the result of reversing the rows of the transposed matrix \( \begin{pmatrix}1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix} \)?
    - a) \( \begin{pmatrix}7 & 4 & 1 \\ 8 & 5 & 2 \\ 9 & 6 & 3 \end{pmatrix} \)
    - b) \( \begin{pmatrix}3 & 6 & 9 \\ 2 & 5 & 8 \\ 1 & 4 & 7 \end{pmatrix} \)
    - c) \( \begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \)
    - d) \( \begin{pmatrix}9 & 8 & 7 \\ 6 & 5 & 4 \\ 3 & 2 & 1 \end{pmatrix} \)

8. Which of the following best describes the process of matrix transposition?
    - a) Multiplying all elements by 2
    - b) Swapping each element with its diagonal counterpart
    - c) Reversing the order of all elements
    - d) Doubling the size of the matrix

9. What is the primary purpose of transposing a matrix before other operations, such as rotation?
    - a) To make the matrix smaller
    - b) To simplify further operations
    - c) To change the data type of the elements
    - d) To sort the matrix

10. How do you reverse a row in Python?
    - a) `row.sort()`
    - b) `row = row[::-1]`
    - c) `row.reverse()`
    - d) `row = reversed(row)`

## Answers

1. a) \( \begin{pmatrix}1 & 3 \\ 2 & 4 \end{pmatrix} \)
2. b) Swapping rows with columns
3. b) `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`
4. c) Transpose the matrix
5. a) Reverse each row
6. c) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
7. a) \( \begin{pmatrix}7 & 4 & 1 \\ 8 & 5 & 2 \\ 9 & 6 & 3 \end{pmatrix} \)
8. b) Swapping each element with its diagonal counterpart
9. b) To simplify further operations
10. c) `row.reverse()`

# Reversing Rows in a Matrix

## Manipulating Rows of a Matrix by Reversing Their Order

Reversing the rows of a matrix is a common operation in various matrix manipulations, including rotating the matrix. This process involves taking each row in the matrix and reversing the order of its elements.

### Example of Reversing Rows

Consider a matrix \( A \):

\[ 
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
\]

Reversing each row of \( A \) gives:

\[ 
A' = \begin{pmatrix}
3 & 2 & 1 \\
6 & 5 & 4 \\
9 & 8 & 7
\end{pmatrix}
\]

### Implementing Row Reversal in Python

To reverse the rows of a matrix in Python, you can use a loop to iterate through each row and apply the `reverse()` method.

```python
def reverse_rows(matrix):
    for row in matrix:
        row.reverse()
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_rows(matrix)
print(reversed_matrix)
# Output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
```

In this example, the function `reverse_rows` iterates through each row of the matrix and reverses it in place.

## Applying Row Reversal in Real-World Projects

Reversing rows can be a step in more complex matrix operations, such as rotating a matrix by 90 degrees. This is often used in image processing, game development, and data transformations.

### Rotating a Matrix by 90 Degrees Clockwise

To rotate a matrix by 90 degrees clockwise, you need to:

1. Transpose the matrix.
2. Reverse each row of the transposed matrix.

Here’s how to perform this operation in Python:

```python
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def rotate_90_clockwise(matrix):
    transpose(matrix)
    reverse_rows(matrix)
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_90_clockwise(matrix)
print(rotated_matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

In this example, the function `rotate_90_clockwise` first transposes the matrix and then reverses each row to achieve the rotation.

## End-of-Chapter Multiple Choice Questions

1. What is the result of reversing the row \([1, 2, 3]\)?
    - a) \([1, 2, 3]\)
    - b) \([3, 2, 1]\)
    - c) \([2, 3, 1]\)
    - d) \([1, 3, 2]\)

2. Which method is used to reverse a list in Python?
    - a) `list.reverse()`
    - b) `list.sort()`
    - c) `list.append()`
    - d) `list.remove()`

3. What is the output of reversing the rows of the matrix \(\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}\)?
    - a) \(\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}\)
    - b) \(\begin{pmatrix}2 & 1 \\ 4 & 3\end{pmatrix}\)
    - c) \(\begin{pmatrix}4 & 3 \\ 2 & 1\end{pmatrix}\)
    - d) \(\begin{pmatrix}3 & 4 \\ 1 & 2\end{pmatrix}\)

4. Which of the following is a correct way to reverse rows in a matrix in Python?
    - a) 
    ```python
    def reverse_rows(matrix):
        matrix.reverse()
        return matrix
    ```
    - b) 
    ```python
    def reverse_rows(matrix):
        for row in matrix:
            row.reverse()
        return matrix
    ```
    - c) 
    ```python
    def reverse_rows(matrix):
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix
    ```
    - d) 
    ```python
    def reverse_rows(matrix):
        for i in range(len(matrix)):
            matrix[i] = matrix[::-1]
        return matrix
    ```

5. What is the first step in rotating a matrix by 90 degrees clockwise?
    - a) Reverse each row
    - b) Transpose the matrix
    - c) Add 90 to each element
    - d) Reverse each column

6. After reversing the rows of the transposed matrix \(\begin{pmatrix}1 & 4 \\ 2 & 5\end{pmatrix}\), what is the result?
    - a) \(\begin{pmatrix}4 & 1 \\ 5 & 2\end{pmatrix}\)
    - b) \(\begin{pmatrix}1 & 2 \\ 4 & 5\end{pmatrix}\)
    - c) \(\begin{pmatrix}5 & 2 \\ 4 & 1\end{pmatrix}\)
    - d) \(\begin{pmatrix}2 & 5 \\ 1 & 4\end{pmatrix}\)

7. Why would you reverse the rows of a matrix in an image processing application?
    - a) To change the color of the image
    - b) To rotate the image
    - c) To increase the size of the image
    - d) To add noise to the image

8. What is the result of reversing the rows of the matrix \(\begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{pmatrix}\)?
    - a) \(\begin{pmatrix}3 & 2 & 1 \\ 6 & 5 & 4 \\ 9 & 8 & 7\end{pmatrix}\)
    - b) \(\begin{pmatrix}1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9\end{pmatrix}\)
    - c) \(\begin{pmatrix}7 & 8 & 9 \\ 4 & 5 & 6 \\ 1 & 2 & 3\end{pmatrix}\)
    - d) \(\begin{pmatrix}9 & 8 & 7 \\ 6 & 5 & 4 \\ 3 & 2 & 1\end{pmatrix}\)

9. How do you reverse a row in Python?
    - a) `row.sort()`
    - b) `row = row[::-1]`
    - c) `row.reverse()`
    - d) `row = reversed(row)`

10. Which of the following operations can be part of the process to rotate a matrix by 90 degrees clockwise?
    - a) Transpose the matrix and then reverse each row
    - b) Reverse each row and then transpose the matrix
    - c) Reverse each column and then transpose the matrix
    - d) Transpose the matrix and then reverse each column

## Answers

1. b) \([3, 2, 1]\)
2. a) `list.reverse()`
3. b) \(\begin{pmatrix}2 & 1 \\ 4 & 3\end{pmatrix}\)
4. b) 
    ```python
    def reverse_rows(matrix):
        for row in matrix:
            row.reverse()
        return matrix
    ```
5. b) Transpose the matrix
6. a) \(\begin{pmatrix}4 & 1 \\ 5 & 2\end{pmatrix}\)
7. b) To rotate the image
8. a) \(\begin{pmatrix}3 & 2 & 1 \\ 6 & 5 & 4 \\ 9 & 8 & 7\end{pmatrix}\)
9. c) `row.reverse()`
10. a) Transpose the matrix and then reverse each row

# Nested Loops

## Using Nested Loops to Iterate Through 2D Data Structures Like Matrices

A matrix is a two-dimensional data structure that can be represented as a list of lists in Python. To manipulate or traverse a matrix, nested loops are commonly used. A nested loop is a loop inside another loop.

### Example of Using Nested Loops to Traverse a Matrix

Consider a matrix:

\[ 
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
\]

To print each element of this matrix, you can use nested loops:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
```

Output:
```
1 2 3 
4 5 6 
7 8 9 
```

In this example, the outer loop iterates through each row, and the inner loop iterates through each element in the current row.

## Modifying Elements Within Nested Loops to Achieve the Desired Rotation

Nested loops are useful for modifying elements within a matrix. To demonstrate this, let's look at rotating a matrix by 90 degrees clockwise.

### Rotating a Matrix by 90 Degrees Clockwise

To rotate a matrix by 90 degrees clockwise, you need to:

1. Transpose the matrix.
2. Reverse each row of the transposed matrix.

#### Step 1: Transposing the Matrix

To transpose a matrix, you swap the elements at positions [i][j] and [j][i].

```python
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
```

#### Step 2: Reversing Each Row

To reverse each row, you use a loop to iterate through each row and reverse it.

```python
def reverse_rows(matrix):
    for row in matrix:
        row.reverse()
    return matrix
```

#### Combining Both Steps

You can combine both steps into a single function to rotate the matrix.

```python
def rotate_90_clockwise(matrix):
    transpose(matrix)
    reverse_rows(matrix)
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_90_clockwise(matrix)
print(rotated_matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

In this example, the function `rotate_90_clockwise` first transposes the matrix and then reverses each row to achieve the rotation.

## End-of-Chapter Multiple Choice Questions

1. What is the output of the following code snippet?
    ```python
    matrix = [
        [1, 2],
        [3, 4]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    ```
    - a) `1 2 3 4`
    - b) `1 3 2 4`
    - c) `1 2\n3 4`
    - d) `1 3\n2 4`

2. Which of the following is the correct way to transpose a matrix?
    - a) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - b) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - c) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
    - d) 
    ```python
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```

3. What is the purpose of using nested loops in matrix operations?
    - a) To multiply matrices
    - b) To iterate through and manipulate 2D data structures
    - c) To sort the elements of the matrix
    - d) To add new rows to the matrix

4. How do you reverse a row in Python?
    - a) `row.sort()`
    - b) `row = row[::-1]`
    - c) `row.reverse()`
    - d) `row = reversed(row)`

5. What is the first step in rotating a matrix by 90 degrees clockwise?
    - a) Reverse each row
    - b) Transpose the matrix
    - c) Add 90 to each element
    - d) Reverse each column

6. In the function `rotate_90_clockwise`, what does the line `transpose(matrix)` do?
    - a) Rotates the matrix by 90 degrees
    - b) Swaps the rows and columns of the matrix
    - c) Reverses each row of the matrix
    - d) Multiplies each element by 2

7. What is the output of the following code snippet?
    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(matrix)
    reverse_rows(matrix)
    print(matrix)
    ```
    - a) `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`
    - b) `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
    - c) `[[3, 2, 1], [6, 5, 4], [9, 8, 7]]`
    - d) `[[1, 4, 7], [2, 5, 8], [3, 6, 9]]`

8. What is the result of the following nested loops?
    ```python
    matrix = [
        [1, 2],
        [3, 4]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

    print(matrix)
    ```
    - a) `[[2, 3], [4, 5]]`
    - b) `[[1, 2], [3, 4]]`
    - c) `[[2, 3], [3, 4]]`
    - d) `[[1, 2], [4, 5]]`

9. Which of the following operations can be part of the process to rotate a matrix by 90 degrees clockwise?
    - a) Transpose the matrix and then reverse each row
    - b) Reverse each row and then transpose the matrix
    - c) Reverse each column and then transpose the matrix
    - d) Transpose the matrix and then reverse each column

10. What is the correct output of the nested loops for the matrix \(\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}\) if we add 1 to each element?
    ```python
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    ```
    - a) \(\begin{pmatrix}2 & 3 \\ 4 & 5\end{pmatrix}\)
    - b) \(\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}\)
    - c) \(\begin{pmatrix}0 & 1 \\ 2 & 3\end{pmatrix}\)
    - d) \(\begin{pmatrix}3 & 4 \\ 5 & 6\end{pmatrix}\)

## Answers

1. c) `1 2\n3 4`
2. c) 
    ```python
    def transpose(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    ```
3. b) To iterate through and manipulate 2D data structures
4. c) `row.reverse()`
5. b) Transpose the matrix
6. b) Swaps the rows and columns of the matrix
7. a) `[[7, 4, 1], [8, 5, 2],

 [9, 6, 3]]`
8. a) `[[2, 3], [4, 5]]`
9. a) Transpose the matrix and then reverse each row
10. a) \(\begin{pmatrix}2 & 3 \\ 4 & 5\end{pmatrix}\)

# Rotate 2D Matrix

## Objective

Given an n x n 2D matrix, rotate it 90 degrees clockwise. The rotation must be done in-place, meaning the matrix itself should be modified without using extra space for another matrix.

## Prototype
```python
def rotate_2d_matrix(matrix):
    # Implement rotation logic here
    pass
```

## Steps to Rotate a 2D Matrix 90 Degrees Clockwise

To rotate a 2D matrix by 90 degrees clockwise, you can follow these steps:
1. **Transpose the Matrix**: Swap elements at positions [i][j] and [j][i].
2. **Reverse Each Row**: Reverse the elements of each row to complete the 90-degree rotation.

### Step 1: Transpose the Matrix
Transposing a matrix means converting its rows into columns and vice versa.

Example:
\[ 
\text{Original Matrix} = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
\]

\[ 
\text{Transposed Matrix} = \begin{pmatrix}
1 & 4 & 7 \\
2 & 5 & 8 \\
3 & 6 & 9
\end{pmatrix}
\]

### Step 2: Reverse Each Row
After transposing the matrix, reverse each row to achieve the 90-degree rotation.

Example:
\[ 
\text{Transposed Matrix} = \begin{pmatrix}
1 & 4 & 7 \\
2 & 5 & 8 \\
3 & 6 & 9
\end{pmatrix}
\]

\[ 
\text{Rotated Matrix} = \begin{pmatrix}
7 & 4 & 1 \\
8 & 5 & 2 \\
9 & 6 & 3
\end{pmatrix}
\]

### Implementation in Python

Here's how you can implement these steps in Python:

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
    # Output should be: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

### Explanation

- **Transposing the Matrix**:
  - The outer loop iterates through each row `i`.
  - The inner loop iterates through each column `j` starting from `i + 1` to avoid swapping back.
  - `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]` swaps the elements at positions [i][j] and [j][i].

- **Reversing Each Row**:
  - `matrix[i].reverse()` reverses the elements in each row `i`.

## Application in Real-World Projects

Matrix rotation is useful in various applications, such as image processing, computer graphics, and game development. For example, rotating a 2D image matrix by 90 degrees clockwise can be done using the same method, where each pixel is represented as an element in the matrix.

## End-of-Chapter Multiple Choice Questions

1. What does the `rotate_2d_matrix` function do?
   - a) Rotates a 2D matrix by 180 degrees.
   - b) Rotates a 2D matrix by 90 degrees clockwise.
   - c) Rotates a 2D matrix by 90 degrees counterclockwise.
   - d) Flips the matrix upside down.

2. What is the first step in rotating a matrix by 90 degrees clockwise?
   - a) Reverse each row.
   - b) Transpose the matrix.
   - c) Reverse each column.
   - d) Rotate each element.

3. What is the purpose of the transpose operation in matrix rotation?
   - a) To flip the matrix horizontally.
   - b) To convert rows into columns and vice versa.
   - c) To reverse the order of elements in each row.
   - d) To shift elements diagonally.

4. How do you reverse a row in Python?
   - a) `row.sort()`
   - b) `row = row[::-1]`
   - c) `row.reverse()`
   - d) `row = reversed(row)`

5. What does the following code do?
   ```python
   for i in range(len(matrix)):
       for j in range(i + 1, len(matrix)):
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   ```
   - a) It reverses each row in the matrix.
   - b) It transposes the matrix.
   - c) It rotates the matrix by 90 degrees clockwise.
   - d) It shifts elements to the right.

6. After transposing the matrix, what is the next step to complete the 90-degree rotation?
   - a) Reverse each column.
   - b) Transpose the matrix again.
   - c) Reverse each row.
   - d) Add 90 to each element.

7. What will be the output of the following code?
   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]

   rotate_2d_matrix(matrix)
   print(matrix)
   ```
   - a) `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
   - b) `[[9, 6, 3], [8, 5, 2], [7, 4, 1]]`
   - c) `[[3, 6, 9], [2, 5, 8], [1, 4, 7]]`
   - d) `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

8. What does `matrix[i].reverse()` do in the context of matrix rotation?
   - a) It transposes the matrix.
   - b) It rotates the matrix by 180 degrees.
   - c) It reverses the elements of row `i`.
   - d) It shifts elements to the left.

9. Which of the following best describes the in-place modification requirement?
   - a) The function should return a new matrix.
   - b) The function should not return anything and modify the matrix directly.
   - c) The function should create a copy of the matrix.
   - d) The function should only modify specific rows.

10. Why is it important to use in-place modification for this task?
    - a) To minimize space complexity.
    - b) To make the function faster.
    - c) To make the code easier to read.
    - d) To avoid errors.

## Answers

1. b) Rotates a 2D matrix by 90 degrees clockwise.
2. b) Transpose the matrix.
3. b) To convert rows into columns and vice versa.
4. c) `row.reverse()`
5. b) It transposes the matrix.
6. c) Reverse each row.
7. d) `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`
8. c) It reverses the elements of row `i`.
9. b) The function should not return anything and modify the matrix directly.
10. a) To minimize space complexity.
