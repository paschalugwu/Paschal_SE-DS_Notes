# C (Search Algorithms) - What is a search algorithm

A search algorithm is a method or procedure used to locate a specific item or value within a collection of data. In simpler terms, it's like looking for a needle in a haystack, where the needle is the item you're searching for, and the haystack is the data set.

## Understanding Search Algorithms

Search algorithms are fundamental in computer science and are used in various applications such as web search engines, database systems, and artificial intelligence. They help in efficiently finding information from vast amounts of data.

### Types of Search Algorithms

There are different types of search algorithms, each with its own approach and efficiency. Some common ones include:

1. **Linear Search (Sequential Search):** This is the simplest search algorithm where each element in the data set is checked until the target element is found or the entire list is traversed. It's like reading a book page by page until you find the information you're looking for.

2. **Binary Search:** This algorithm works on sorted arrays and divides the search interval in half each time. It's like searching for a word in a dictionary by flipping pages halfway through until you find the word you're looking for.

3. **Hash Table:** Hashing is a technique used to map keys to values, making it efficient for retrieval. It's like having a table of contents in a book where you can quickly find the page number corresponding to a specific chapter.

4. **Depth-First Search (DFS) and Breadth-First Search (BFS):** These are graph traversal algorithms used to visit all the vertices of a graph. DFS explores as far as possible along each branch before backtracking, while BFS explores all neighbor vertices at the current depth before moving to the next depth level.

### Example: Linear Search

Let's take a look at how a linear search algorithm works in C:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i; // Return the index where the key is found
        }
    }
    return -1; // Return -1 if the key is not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 23;
    int result = linearSearch(arr, n, key);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

In this example, we have an array `arr` containing some elements. We want to search for a specific element (`key`) within the array using the linear search algorithm. If the element is found, its index is returned; otherwise, `-1` is returned.

## Real-World Applications

Understanding search algorithms is crucial for developing efficient search functionalities in various software applications. For example:

- **Web Search Engines:** Google, Bing, and other search engines use complex search algorithms to quickly retrieve relevant web pages based on user queries.

- **Database Systems:** Search algorithms are used in database systems to efficiently retrieve records matching certain criteria.

- **Navigation Systems:** GPS and mapping applications use search algorithms to find the shortest or fastest route between two locations.

- **Recommendation Systems:** E-commerce platforms and streaming services use search algorithms to recommend products or content based on user preferences.

By mastering search algorithms, software engineers can develop faster and more efficient solutions for a wide range of real-world problems.

# C (Search Algorithms) - What is a linear search

A linear search is a simple search algorithm that sequentially checks each element in a list or array until a match is found or the entire list has been traversed. It's like looking for a specific item by checking each item in a list one by one.

## Understanding Linear Search

Linear search is straightforward to understand and implement, making it suitable for small lists or unsorted data. However, its time complexity is O(n), where n is the number of elements in the list. This means that as the size of the list grows, the time taken for searching also increases linearly.

### Example: Linear Search in C

Let's see how a linear search algorithm can be implemented in C:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i; // Return the index where the key is found
        }
    }
    return -1; // Return -1 if the key is not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 23;
    int result = linearSearch(arr, n, key);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

In this example, we have an array `arr` containing some elements. We want to search for a specific element (`key`) within the array using the linear search algorithm. If the element is found, its index is returned; otherwise, `-1` is returned.

## Real-World Applications

Although linear search is not the most efficient search algorithm, it still finds applications in various real-world scenarios:

- **Searching Unsorted Lists:** When dealing with small lists or data that is not sorted, linear search provides a simple solution to find specific elements.

- **Data Validation:** Linear search can be used to check if a particular value exists in a dataset, aiding in data validation processes.

- **User Interfaces:** In user interfaces, linear search may be used to find items in dropdown menus or lists.

While linear search may not be suitable for large datasets or time-critical applications, understanding its principles is essential for building a strong foundation in algorithmic problem-solving.

# C (Search Algorithms) - What is a binary search

Binary search is an efficient search algorithm used to find a specific target value within a sorted array or list. It works by repeatedly dividing the search interval in half until the target value is found or the interval becomes empty. It's like searching for a word in a dictionary by repeatedly dividing the pages in half.

## Understanding Binary Search

Binary search is much faster than linear search for large datasets because it eliminates half of the remaining elements at each step. Its time complexity is O(log n), where n is the number of elements in the array. This makes it particularly useful for searching in sorted arrays or lists.

### Example: Binary Search in C

Let's see how binary search can be implemented in C:

```c
#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            return mid; // Return the index where the key is found
        }
        if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Return -1 if the key is not found
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 23;
    int result = binarySearch(arr, 0, n - 1, key);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

In this example, we have a sorted array `arr` containing some elements. We want to search for a specific element (`key`) within the array using the binary search algorithm. If the element is found, its index is returned; otherwise, `-1` is returned.

## Real-World Applications

Binary search finds applications in various real-world scenarios, especially where quick retrieval of information is crucial:

- **Searching in Databases:** Binary search is used in database systems to quickly retrieve records based on indexed values.

- **Finding Elements in Sorted Lists:** It's commonly used in sorted lists or arrays to locate specific elements efficiently.

- **Searching in File Systems:** Binary search can be employed in file systems to locate files or directories based on their names or attributes.

- **Network Routing:** Binary search algorithms are used in network routing protocols to efficiently find routes between nodes.

By understanding binary search, software engineers can develop faster and more efficient solutions for searching and retrieval tasks in various applications.

# C (Search Algorithms) - What is the best search algorithm to use depending on your needs

Choosing the best search algorithm depends on various factors such as the size of the dataset, whether the data is sorted, and the time complexity requirements of the application. Different search algorithms have different strengths and weaknesses, so it's essential to select the most appropriate one based on the specific requirements of the problem at hand.

## Factors to Consider

### Size of Dataset
- **Linear Search:** Suitable for small datasets or unsorted data.
- **Binary Search:** Ideal for large sorted datasets due to its efficient O(log n) time complexity.

### Data Structure
- **Arrays:** Binary search is suitable for sorted arrays due to its ability to divide the search space efficiently.
- **Linked Lists:** Linear search is typically used since binary search cannot be directly applied to linked lists.

### Time Complexity Requirements
- If time efficiency is crucial and the data is sorted, binary search is usually preferred.
- If the dataset is small or the data is unsorted, linear search may suffice.

## Choosing the Right Algorithm

### Linear Search
- Use when the dataset is small or unsorted.
- Suitable for scenarios where simplicity is more important than efficiency.
- Can be applied to both arrays and linked lists.

### Binary Search
- Use when the dataset is large and sorted.
- Provides significantly faster search times compared to linear search for large datasets.
- Requires the data to be sorted beforehand.
- Ideal for applications where time efficiency is critical, such as database systems and search engines.

## Example: Choosing Between Linear Search and Binary Search

Let's consider a scenario where you need to search for a word in a dictionary:

- **If the dictionary is not sorted:** Linear search (sequential search) would be appropriate. You would start from the beginning and check each page until you find the word.
  
- **If the dictionary is sorted:** Binary search would be more efficient. You would open the dictionary in the middle and decide whether to continue searching in the first half or the second half based on the alphabetical order of the words.

## Real-World Applications

- **Linear Search:** Used in simple search functionalities in applications with small datasets or unsorted data.
  
- **Binary Search:** Applied in various real-world scenarios such as database systems, sorting algorithms, and search engines to efficiently retrieve information from large sorted datasets.

By understanding the strengths and weaknesses of different search algorithms, software engineers can make informed decisions when choosing the most appropriate algorithm for a particular task, leading to optimized performance and resource utilization in real-world projects.

# **C (Search Algorithms) - Linear search**

Linear search is a simple search algorithm that sequentially checks each element in a list until the target element is found or the end of the list is reached. It's often compared to how we might search for an item in a list manually, checking each item until we find the desired one.

Here's how to implement linear search in C:

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * linear_search - Searches for a value in an array of integers using linear search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of value if found, otherwise -1
 */
int linear_search(int *array, size_t size, int value)
{
    size_t i;

    if (array == NULL)
        return -1;

    for (i = 0; i < size; i++)
    {
        printf("Value checked array[%lu] = [%d]\n", i, array[i]);
        if (array[i] == value)
            return i;
    }

    return -1; // Value not found
}

int main(void)
{
    int array[] = {10, 1, 42, 3, 4, 42, 6, 7, -1, 9};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 3, linear_search(array, size, 3));
    printf("Found %d at index: %d\n\n", 42, linear_search(array, size, 42));
    printf("Found %d at index: %d\n", 999, linear_search(array, size, 999));
    return EXIT_SUCCESS;
}
```

In the `linear_search` function:
- We iterate through the array using a loop, checking each element.
- For each element, we print the value being checked.
- If the value is found, we return the index of that value.
- If the value is not found after checking all elements, we return -1.

This algorithm has a time complexity of O(n), where n is the number of elements in the array, as it may need to check every element in the worst-case scenario.

Real-world application: Linear search can be used when the data is unsorted or when we need to search through a small number of elements. For example, in a to-do list app, linear search can be used to find specific tasks by their titles.

# **C (Search Algorithms) - Binary search**

Binary search is a highly efficient search algorithm used to find a specific target value within a sorted array of elements. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty.

Here's how to implement binary search in C:

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * binary_search - Searches for a value in a sorted array of integers using binary search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of value if found, otherwise -1
 */
int binary_search(int *array, size_t size, int value)
{
    size_t left = 0;
    size_t right = size - 1;
    size_t mid;

    if (array == NULL)
        return -1;

    while (left <= right)
    {
        size_t i;

        printf("Searching in array: ");
        for (i = left; i < right; i++)
            printf("%d, ", array[i]);
        printf("%d\n", array[right]);

        mid = (left + right) / 2;

        if (array[mid] == value)
            return mid;
        else if (array[mid] < value)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1; // Value not found
}

int main(void)
{
    int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 2, binary_search(array, size, 2));
    printf("Found %d at index: %d\n\n", 5, binary_search(array, size, 5));
    printf("Found %d at index: %d\n", 999, binary_search(array, size, 999));
    return EXIT_SUCCESS;
}
```

In the `binary_search` function:
- We initialize two pointers, `left` and `right`, to mark the current search interval.
- We repeatedly divide the interval in half until the target value is found or the interval is empty.
- At each step, we print the current search interval.
- If the target value is found, we return its index.
- If the target value is not found, we update the search interval based on whether the target value is less than or greater than the midpoint.

This algorithm has a time complexity of O(log n), where n is the number of elements in the array, as the size of the search interval is halved in each step.

Real-world application: Binary search is commonly used in scenarios where quick retrieval of data is crucial, such as searching in databases, looking up items in sorted lists or arrays, and in various searching algorithms used in computer science. For example, in a phone book, binary search can be used to quickly find a person's name by searching through the sorted list of names.

# **C (Search Algorithms) - Big O #0**

In a linear search algorithm, the time complexity (worst case) can be determined by analyzing how the number of comparisons grows with the size of the input array.

For a linear search in an array of size n:
- In the worst-case scenario, where the target element is either not present in the array or is located at the last position, the algorithm needs to iterate through all n elements of the array before determining that the target element is not present.
- Therefore, the number of comparisons required is directly proportional to the size of the array, n.

As a result, the time complexity (worst case) of a linear search in an array of size n is **O(n)**.

This means that as the size of the array increases, the time taken by the linear search algorithm grows linearly. In other words, if the size of the array doubles, the time taken by the algorithm also doubles.

Real-world application: Understanding the time complexity of algorithms like linear search is crucial for optimizing the performance of software systems. In scenarios where data sets are large, knowing that a linear search has O(n) time complexity can help developers decide whether alternative algorithms with better time complexities, such as binary search (O(log n)), should be used for better performance.

# **C (Search Algorithms) - Big O #1**

Space complexity refers to the amount of memory space required by an algorithm to execute with respect to the input size. For an iterative linear search algorithm in an array of size n, the space complexity is constant, denoted as **O(1)**.

Here's why the space complexity is O(1) for an iterative linear search algorithm:
- The algorithm uses a fixed amount of memory regardless of the size of the input array.
- In an iterative linear search, only a few variables are used to keep track of the current index, the target value, and the size of the array. These variables occupy constant space, irrespective of the size of the input array.
- As the size of the input array increases, the memory space required by the algorithm remains the same.

Therefore, the space complexity of an iterative linear search algorithm in an array of size n is O(1), indicating constant space usage.

Real-world application: Constant space complexity is desirable in many real-world applications, especially in embedded systems, mobile applications, and systems with limited memory resources. Understanding the space complexity of algorithms helps developers make informed decisions about memory usage and optimize their code for better performance.

# **C (Search Algorithms) - Big O #2**

The time complexity (worst case) of a binary search algorithm in an array of size n can be determined by analyzing how the size of the input affects the number of operations performed by the algorithm.

For a binary search in an array of size n:
- At each step of the binary search, the algorithm divides the search interval in half, effectively reducing the search space by half.
- This process continues until the target element is found or the search interval becomes empty.
- Therefore, the number of operations performed by the binary search algorithm grows logarithmically with the size of the input array.

As a result, the time complexity (worst case) of a binary search in an array of size n is **O(log n)**.

This means that as the size of the array increases, the time taken by the binary search algorithm grows logarithmically. In other words, even if the size of the array doubles, the time taken by the algorithm increases only by a logarithmic factor.

Real-world application: Binary search is widely used in various applications where quick retrieval of data is required, such as searching in sorted arrays, databases, and searching algorithms. For example, binary search is used by search engines to efficiently locate relevant information from vast amounts of data. Understanding the time complexity of binary search helps developers design efficient algorithms for searching and retrieving data.

# **C (Search Algorithms) - Big O #3**

The space complexity (worst case) of a binary search algorithm in an array of size n refers to the amount of memory space required by the algorithm to execute with respect to the input size.

For a binary search in an array of size n:
- The space complexity is determined by the recursive implementation of the binary search algorithm.
- In each recursive call, the algorithm requires additional space on the call stack to store information about the current state of the search.
- The number of recursive calls made by the binary search algorithm depends on the height of the binary search tree formed during the search process.
- In the worst case scenario, where the binary search tree is unbalanced and resembles a linked list, the height of the binary search tree is equal to the number of elements in the array, n.

As a result, the space complexity (worst case) of a binary search in an array of size n is **O(n)**.

This means that in the worst case scenario, where the binary search tree is unbalanced, the space taken by the algorithm on the call stack grows linearly with the size of the input array.

Real-world application: While the worst-case space complexity of a binary search algorithm is O(n), in practice, binary search is often implemented iteratively to avoid excessive space usage. Iterative binary search implementations typically have a space complexity of O(1), making them more efficient in terms of memory usage. Understanding the space complexity of algorithms helps developers make informed decisions about memory usage and optimize their code for better performance.

# **C (Search Algorithms) - Big O #4**

The given function `allocate_map` is responsible for dynamically allocating memory for a two-dimensional array (matrix) of size `n` rows and `m` columns. Let's analyze its space complexity:

- The function allocates memory for an array of `n` integer pointers using `malloc(sizeof(int *) * n)`. This operation requires `n * sizeof(int *)` bytes of memory.
- For each row, the function allocates memory for an array of `m` integers using `malloc(sizeof(int) * m)`. This operation is repeated `n` times, resulting in `n * sizeof(int) * m` bytes of memory.
- Therefore, the total memory allocated by the function is the sum of memory required for the integer pointers array and the memory required for all the row arrays.
- The total space complexity of the function can be expressed as O(n + n * m), which simplifies to O(n * m).

The space complexity of the `allocate_map` function is **O(n * m)**, where `n` is the number of rows and `m` is the number of columns in the two-dimensional array.

Real-world application: This function can be applied in real-world projects that involve dynamic memory allocation for matrices, such as image processing algorithms, graph traversal algorithms, and simulations. For example, in a game development project, this function can be used to allocate memory for a game map represented as a grid of tiles or cells. Understanding the space complexity of memory allocation functions helps developers manage memory efficiently and avoid memory-related issues such as memory leaks and heap fragmentation.

# **C (Search Algorithms) - Jump search**

Jump search is a searching algorithm used on sorted arrays. It works by jumping ahead by fixed steps to find the right range and then performing a linear search within that range.

Here's how to implement jump search in C:

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/**
 * jump_search - Searches for a value in a sorted array of integers using jump search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of value if found, otherwise -1
 */
int jump_search(int *array, size_t size, int value)
{
    size_t jump = sqrt(size);
    size_t left = 0;
    size_t right = jump;

    if (array == NULL)
        return -1;

    printf("Value checked array[%lu] = [%d]\n", left, array[left]);
    while (right < size && array[right] < value)
    {
        printf("Value checked array[%lu] = [%d]\n", right, array[right]);
        left = right;
        right += jump;
    }

    printf("Value found between indexes [%lu] and [%lu]\n", left, right);
    for (size_t i = left; i <= right && i < size; i++)
    {
        printf("Value checked array[%lu] = [%d]\n", i, array[i]);
        if (array[i] == value)
            return i;
    }

    return -1; // Value not found
}

int main(void)
{
    int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 6, jump_search(array, size, 6));
    printf("Found %d at index: %d\n\n", 1, jump_search(array, size, 1));
    printf("Found %d at index: %d\n", 999, jump_search(array, size, 999));
    return EXIT_SUCCESS;
}
```

In the `jump_search` function:
- We determine the jump step by taking the square root of the size of the array.
- We then iterate through the array in jumps until we find a range where the target value might be located.
- Once we find the range, we perform a linear search within that range to find the target value.
- We print out the values being checked at each step for clarity.

This algorithm has a time complexity of O(√n) for the jump step plus O(√n) for the linear search within the range, which simplifies to O(√n) in total.

Real-world application: Jump search is beneficial when dealing with large sorted arrays, especially when random access to elements is expensive. It's commonly used in scenarios where sequential access to elements is faster than random access, such as in file systems and databases. For example, in a large database, jump search can be used to quickly locate records based on their keys.

# **C (Search Algorithms) - Big O #5**

The time complexity of a jump search in an array of size n, using a step size of sqrt(n), depends on the number of comparisons required to find the target element.

In jump search:
- We start by jumping ahead by fixed steps until we find a range where the target element might be located.
- Once we find the range, we perform a linear search within that range to find the target element.

Let's analyze the time complexity:
- The number of jumps required to cover the entire array is sqrt(n), where n is the size of the array.
- In the worst-case scenario, the target element is located in the last block that we jump to, or it's not present in the array at all.
- After jumping to the appropriate block, we perform a linear search within that block, which requires at most sqrt(n) comparisons.
- Therefore, the total number of comparisons required is at most 2 * sqrt(n) in the worst case.

As a result, the time complexity (average case) of a jump search in an array of size n, using a step size of sqrt(n), is **O(sqrt(n))**.

Real-world application: Understanding the time complexity of algorithms like jump search is crucial for optimizing search operations in real-world projects, especially when dealing with large datasets. For example, in a web search engine, jump search can be used to quickly locate relevant web pages based on search queries. By knowing the time complexity of jump search, developers can make informed decisions about which search algorithm to use based on the characteristics of their data and performance requirements.

# **C (Search Algorithms) - Interpolation search**

Interpolation search is an algorithm used for searching a value in a sorted array of integers. It improves upon binary search by using a probe position formula to determine where to look for the target value.

Here's how to implement interpolation search in C:

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * interpolation_search - Searches for a value in a sorted array of integers using interpolation search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of value if found, otherwise -1
 */
int interpolation_search(int *array, size_t size, int value)
{
    size_t low = 0;
    size_t high = size - 1;
    size_t pos;

    if (array == NULL || size == 0)
        return -1;

    while (low <= high && value >= array[low] && value <= array[high])
    {
        pos = low + (((double)(high - low) / (array[high] - array[low])) * (value - array[low]));
        printf("Value checked array[%lu] = [%d]\n", pos, array[pos]);

        if (array[pos] == value)
            return pos;
        else if (array[pos] < value)
            low = pos + 1;
        else
            high = pos - 1;
    }

    printf("Value checked array[%lu] is out of range\n", pos);
    return -1; // Value not found
}

int main(void)
{
    int array[] = {0, 0, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8, 9, 9};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 3, interpolation_search(array, size, 3));
    printf("Found %d at index: %d\n\n", 7, interpolation_search(array, size, 7));
    printf("Found %d at index: %d\n", 999, interpolation_search(array, size, 999));
    return EXIT_SUCCESS;
}
```

In the `interpolation_search` function:
- We start with a range from `low` to `high` indices of the array.
- We calculate the probe position using the interpolation formula: `pos = low + (((double)(high - low) / (array[high] - array[low])) * (value - array[low]))`.
- We compare the value at the probe position with the target value and adjust the range accordingly.
- We continue this process until we find the target value or determine that it's not present in the array.

This algorithm has an average time complexity of O(log log n), making it more efficient than binary search for uniformly distributed datasets.

Real-world application: Interpolation search can be applied in real-world projects where search performance is critical, such as database systems and scientific applications. For example, in a database system, interpolation search can be used to quickly locate records based on their keys, improving the efficiency of database queries. Understanding interpolation search helps developers optimize search operations and improve the performance of their applications.

# **C (Search Algorithms) - Exponential search**

Exponential search is an algorithm used for searching a value in a sorted array of integers. It works by searching for a range where the target value might be located and then using binary search within that range to find the exact position of the value.

Here's how to implement exponential search in C:

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * exponential_search - Searches for a value in a sorted array of integers using exponential search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of value if found, otherwise -1
 */
int exponential_search(int *array, size_t size, int value)
{
    if (array == NULL || size == 0)
        return -1;

    // If the first element is the target value
    if (array[0] == value)
        return 0;

    // Find range to perform binary search
    size_t bound = 1;
    while (bound < size && array[bound] <= value)
    {
        printf("Value checked array[%lu] = [%d]\n", bound, array[bound]);
        bound *= 2;
    }

    // Perform binary search within the range
    size_t low = bound / 2;
    size_t high = (bound < size) ? bound : size - 1;

    printf("Value found between indexes [%lu] and [%lu]\n", low, high);
    printf("Searching in array:");
    for (size_t i = low; i <= high; i++)
    {
        printf(" %d", array[i]);
        if (i < high)
            printf(",");
    }
    printf("\n");

    // Binary search
    while (low <= high)
    {
        size_t mid = low + (high - low) / 2;
        printf("Searching in array:");
        for (size_t i = low; i <= high; i++)
        {
            printf(" %d", array[i]);
            if (i < high)
                printf(",");
        }
        printf("\n");

        if (array[mid] == value)
            return mid;
        else if (array[mid] < value)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1; // Value not found
}

int main(void)
{
    int array[] = {0, 1, 2, 3, 4, 7, 12, 15, 18, 19, 23, 54, 61, 62, 76, 99};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 62, exponential_search(array, size, 62));
    printf("Found %d at index: %d\n\n", 3, exponential_search(array, size, 3));
    printf("Found %d at index: %d\n", 999, exponential_search(array, size, 999));
    return EXIT_SUCCESS;
}
```

In the `exponential_search` function:
- We start with a range from index 1 and keep doubling it until we find a range where the target value might be located.
- We then perform binary search within this range to find the exact position of the target value.

This algorithm has a time complexity of O(log n), making it efficient for searching in large datasets.

Real-world application: Exponential search can be applied in real-world projects where search performance is crucial, such as search engines, file systems, and databases. For example, in a search engine, exponential search can be used to quickly locate relevant documents based on search queries, improving the efficiency of search operations. Understanding exponential search helps developers optimize search algorithms and enhance the performance of their applications.

# **C (Search Algorithms) - Advanced binary search**

The advanced binary search algorithm is an enhanced version of the basic binary search. It aims to return the index of the first occurrence of a target value in a sorted array, even if that value appears multiple times in the array.

Here's how to implement the advanced binary search algorithm in C:

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * advanced_binary_recursive - Recursive helper function for advanced binary search
 * @array: Pointer to the first element of the array to search in
 * @low: Index of the first element in the current range
 * @high: Index of the last element in the current range
 * @value: Value to search for
 *
 * Return: Index of the first occurrence of value if found, otherwise -1
 */
int advanced_binary_recursive(int *array, size_t low, size_t high, int value)
{
    if (low > high)
        return -1;

    size_t mid = low + (high - low) / 2;

    printf("Searching in array:");
    for (size_t i = low; i <= high; i++)
    {
        printf(" %d", array[i]);
        if (i < high)
            printf(",");
    }
    printf("\n");

    if (array[mid] == value)
    {
        if (mid == 0 || array[mid - 1] != value)
            return mid;
        else
            return advanced_binary_recursive(array, low, mid, value);
    }
    else if (array[mid] < value)
        return advanced_binary_recursive(array, mid + 1, high, value);
    else
        return advanced_binary_recursive(array, low, mid - 1, value);
}

/**
 * advanced_binary - Searches for a value in a sorted array of integers using advanced binary search
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index of the first occurrence of value if found, otherwise -1
 */
int advanced_binary(int *array, size_t size, int value)
{
    if (array == NULL || size == 0)
        return -1;

    return advanced_binary_recursive(array, 0, size - 1, value);
}

int main(void)
{
    int array[] = {0, 1, 2, 5, 5, 6, 6, 7, 8, 9};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Found %d at index: %d\n\n", 8, advanced_binary(array, size, 8));
    printf("Found %d at index: %d\n\n", 5, advanced_binary(array, size, 5));
    printf("Found %d at index: %d\n", 999, advanced_binary(array, size, 999));
    return EXIT_SUCCESS;
}
```

In this implementation:
- We use a recursive approach to perform the binary search.
- We check if the mid element is the target value and if it's the first occurrence by comparing it with the previous element.
- If the mid element is not the first occurrence, we recursively search the left subarray to find the first occurrence.

This algorithm has a time complexity of O(log n), making it efficient for searching in large datasets.

Real-world application: Advanced binary search can be used in various applications where it's essential to find the first occurrence of a value in a sorted dataset, such as searching for specific items in a database or retrieving relevant information from a sorted list. Understanding advanced binary search helps developers optimize search algorithms and improve the efficiency of their applications.

# **C (Search Algorithms) - Jump search in a singly linked list**

Jump search in a singly linked list is a search algorithm used to find a specific value in a sorted list efficiently. It combines linear search and jump search techniques.

First, let's define the data structure for a singly linked list node in the `search_algos.h` header file:

```c
/**
 * struct listint_s - singly linked list
 *
 * @n: Integer
 * @index: Index of the node in the list
 * @next: Pointer to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    size_t index;
    struct listint_s *next;
} listint_t;
```

Now, let's implement the `jump_list` function:

```c
#include <stdio.h>
#include <math.h>
#include "search_algos.h"

/**
 * jump_list - Searches for a value in a sorted list of integers using Jump search
 * @list: Pointer to the head of the list to search in
 * @size: Number of nodes in list
 * @value: Value to search for
 *
 * Return: Pointer to the first node where value is located, or NULL if not found
 */
listint_t *jump_list(listint_t *list, size_t size, int value)
{
    if (list == NULL || size == 0)
        return NULL;

    size_t jump = sqrt(size); // Jump step

    listint_t *current = list;
    listint_t *prev = NULL;

    // Jump to the right block
    while (current->next != NULL && current->n < value)
    {
        prev = current;
        for (size_t i = 0; current->next != NULL && i < jump; i++)
            current = current->next;
        printf("Value checked at index [%lu] = [%d]\n", current->index, current->n);
    }

    printf("Value found between indexes [%lu] and [%lu]\n", prev->index, current->index);

    // Perform linear search in the block
    while (prev != NULL && prev->n < value)
    {
        printf("Value checked at index [%lu] = [%d]\n", prev->index, prev->n);
        if (prev->n == value)
            return prev;
        prev = prev->next;
    }

    return NULL; // Value not found
}
```

In the `jump_list` function:
- We determine the jump step using the square root of the size of the list.
- We jump through the list until we find the right block where the value might be located.
- We then perform a linear search within that block to find the exact position of the value.

Real-world application: Jump search in a singly linked list can be used in scenarios where memory efficiency is crucial, such as searching in large datasets stored in a singly linked list format. For example, in a file system, jump search can be employed to efficiently locate files or directories within a directory structure, enhancing the performance of file search operations. Understanding jump search helps developers optimize search algorithms and improve the efficiency of their applications.

# **C (Search Algorithms) - Linear search in a skip list**

In skip lists, an additional "express lane" is added to optimize the time complexity of search operations. This express lane enables faster traversal through the list by skipping a certain number of elements.

Let's define the data structure for a skip list node in the `search_algos.h` header file:

```c
/**
 * struct skiplist_s - Singly linked list with an express lane
 *
 * @n: Integer
 * @index: Index of the node in the list
 * @next: Pointer to the next node
 * @express: Pointer to the next node in the express lane
 *
 * Description: singly linked list node structure with an express lane
 */
typedef struct skiplist_s
{
    int n;
    size_t index;
    struct skiplist_s *next;
    struct skiplist_s *express;
} skiplist_t;
```

Now, let's implement the `linear_skip` function:

```c
#include <stdio.h>
#include "search_algos.h"

/**
 * linear_skip - Searches for a value in a sorted skip list of integers
 * @list: Pointer to the head of the skip list to search in
 * @value: Value to search for
 *
 * Return: Pointer to the first node where value is located, or NULL if not found
 */
skiplist_t *linear_skip(skiplist_t *list, int value)
{
    if (list == NULL)
        return NULL;

    skiplist_t *current = list;
    skiplist_t *express = NULL;

    while (current->next != NULL && current->n < value)
    {
        express = current->express;
        printf("Value checked at index [%lu] = [%d]\n", current->index, current->n);

        if (express == NULL || express->n >= value)
            break;

        current = express;
    }

    printf("Value found between indexes [%lu] and [%lu]\n", current->index, express->index);

    while (current != NULL && current->n < value)
    {
        printf("Value checked at index [%lu] = [%d]\n", current->index, current->n);

        if (current->n == value)
            return current;

        current = current->next;
    }

    return NULL; // Value not found
}
```

In the `linear_skip` function:
- We traverse the list using the express lane until we find a segment where the value might be located.
- Then, we perform linear search within that segment to find the exact position of the value.

Real-world application: Linear search in a skip list can be applied in scenarios where fast search operations are required on large datasets, such as database management systems. Skip lists are efficient data structures for maintaining sorted lists, and linear search in skip lists can enhance search performance compared to traditional singly linked lists. Understanding skip lists and their search algorithms is essential for designing efficient data structures and algorithms in various software applications.

# **C (Search Algorithms) - Big O #6**
The time complexity of a jump search in a singly linked list of size $$n$$, using a step size of $$m$$, can be analyzed as follows:

1. **Finding the block:** Since the jump search algorithm divides the list into blocks of size $$m$$, finding the block where the target element may reside takes $$O(\sqrt{n})$$ time.

2. **Linear search within the block:** Once the block is found, a linear search within that block is performed. In the worst case, this linear search takes $$O(m)$$ time because the block size is $$m$$.

Combining both steps, the time complexity of jump search in a singly linked list with a step size of $$m$$ is $$O(\sqrt{n})$$ in the average case.

This time complexity is derived from the fact that the jump search algorithm reduces the search space by a factor of $$m$$ with each iteration, resulting in a sublinear time complexity.

Real-world application: Understanding the time complexity of algorithms, such as jump search in a singly linked list, is crucial for designing efficient search algorithms in various applications. For example, in large-scale data systems where search performance is critical, employing algorithms with sublinear time complexity can significantly improve search efficiency and overall system performance.

# **C (Search Algorithms) - Big O #7**

The time complexity of a jump search in a skip list of size $$n$$, with an express lane using a step size of $$m$$, can be analyzed as follows:

1. **Finding the block:** Since the jump search algorithm in a skip list also divides the list into blocks of size $$m$$, finding the block where the target element may reside takes $$O(\sqrt{n})$$ time.

2. **Linear search within the block:** Once the block is found, a linear search within that block is performed. In the worst case, this linear search takes $$O(m)$$ time because the block size is $$m$$.

Combining both steps, the time complexity of jump search in a skip list with an express lane using a step size of $$m$$ is $$O(\sqrt{n})$$ in the average case.

This time complexity is derived from the fact that the express lane in the skip list allows for faster traversal through the list, reducing the search space by a factor of $$m$$ with each iteration.

Real-world application: Skip lists are commonly used in data structures where efficient searching, insertion, and deletion operations are required, such as in databases and key-value stores. Understanding the time complexity of operations in skip lists, including jump search, is crucial for designing and optimizing data structures in real-world applications.

© [2024] [Paschal Ugwu]

***AI Use Disclosure:*** *I utilized ChatGPT to assist in the generation and refinement of technical content for this note.*
