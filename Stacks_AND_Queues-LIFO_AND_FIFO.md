# Exploring Stacks, Queues, and Proper Usage of Global Variables in C Programming

## Introduction: 
Welcome to this comprehensive guide on stacks, queues, and the strategic usage of global variables in C programming. This note aims to provide a well-rounded understanding of these fundamental concepts, catering to programmers of all levels, including those with experience in the field. We will explore the basics as well as delve into advanced implementations and practical applications. By the end of this guide, you will have a solid grasp of LIFO and FIFO, advanced techniques for implementing stacks and queues, and a strategic approach to utilizing global variables. Let's embark on this journey of expanding our knowledge!  

## 1. What do LIFO and FIFO mean?

LIFO and FIFO are terms used in computer science and programming to describe different ways of organizing and manipulating data. Let's understand each concept in a more relatable way:

1. LIFO (Last-In, First-Out):
LIFO stands for "Last-In, First-Out." Imagine you have a stack of plates. When you wash a plate, you place it on top of the stack. Now, when you need to use a plate, you take the one from the top. The last plate you put on the stack is the first one you can take off. This is how LIFO works.

In programming, a stack is a common data structure that follows the LIFO principle. It's like a stack of plates, where the last plate you put on top is the first one you can take off. Similarly, in a stack, the last item you add is the first one you can remove.

Here's an example in C programming to implement a stack using an array:

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void push(Stack* stack, int item) {
    if (stack->top == MAX_SIZE - 1) {
        printf("Stack overflow!\n");
        return;
    }
    stack->top++;
    stack->data[stack->top] = item;
}

int pop(Stack* stack) {
    if (stack->top == -1) {
        printf("Stack underflow!\n");
        return -1; // or any appropriate error value
    }
    int item = stack->data[stack->top];
    stack->top--;
    return item;
}
```

This code defines a stack data structure in C programming. The stack is implemented using an array called  `data`  and a variable called  `top`  that keeps track of the index of the top element in the stack. The maximum size of the stack is defined as  `MAX_SIZE` , which is set to 100.

The  `push`  function is used to add an item to the stack. It takes a pointer to a  `Stack`  structure and an item as parameters. First, it checks if the stack is already full by comparing the  `top`  value to  `MAX_SIZE - 1` . If the stack is full, it prints an error message indicating a "stack overflow" and returns. Otherwise, it increments the  `top`  value and assigns the item to the  `data`  array at the updated  `top`  index.

The  `pop`  function is used to remove and return the topmost item from the stack. It also takes a pointer to a  `Stack`  structure as a parameter. First, it checks if the stack is empty by comparing the  `top`  value to -1. If the stack is empty, it prints an error message indicating a "stack underflow" and returns an appropriate error value (e.g., -1). Otherwise, it retrieves the item from the  `data`  array at the current  `top`  index, decrements the  `top`  value, and returns the item.

Overall, this code provides a basic implementation of a stack data structure with functions to push items onto the stack and pop items from the stack, while also handling overflow and underflow conditions.

2. FIFO (First-In, First-Out):
FIFO stands for "First-In, First-Out." Imagine you're waiting in a queue at a movie theater. The person who arrives first gets to enter the theater first. Similarly, in a queue, the first item that is added is the first one to be removed.

In programming, a queue is a common data structure that follows the FIFO principle. It's like a queue of people waiting in line, where the person who arrives first is the first one to leave. In a queue, new items are added at one end, and the items are removed from the other end.

Here's an example in C programming to implement a queue using an array:

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} Queue;

void enqueue(Queue* queue, int item) {
    if (queue->rear == MAX_SIZE - 1) {
        printf("Queue overflow!\n");
        return;
    }
    queue->rear++;
    queue->data[queue->rear] = item;
}

int dequeue(Queue* queue) {
    if (queue->front > queue->rear) {
        printf("Queue underflow!\n");
        return -1; // or any appropriate error value
    }
    int item = queue->data[queue->front];
    queue->front++;
    return item;
}
```

This code defines a queue data structure in C programming. The queue is implemented using an array called  `data`  and two variables called  `front`  and  `rear`  to keep track of the indices of the front and rear elements of the queue, respectively. The maximum size of the queue is defined as  `MAX_SIZE` , which is set to 100.

The  `enqueue`  function is used to add an item to the queue. It takes a pointer to a  `Queue`  structure and an item as parameters. First, it checks if the rear index is equal to  `MAX_SIZE - 1` , indicating that the queue is already full. If the queue is full, it prints an error message indicating a "queue overflow" and returns. Otherwise, it increments the rear index and assigns the item to the  `data`  array at the updated rear index.

The  `dequeue`  function is used to remove and return the frontmost item from the queue. It also takes a pointer to a  `Queue`  structure as a parameter. First, it checks if the front index is greater than the rear index, indicating that the queue is empty. If the queue is empty, it prints an error message indicating a "queue underflow" and returns an appropriate error value (e.g., -1). Otherwise, it retrieves the item from the  `data`  array at the current front index, increments the front index, and returns the item.

In summary, this code provides a basic implementation of a queue data structure with functions to enqueue items into the queue and dequeue items from the queue, while also handling overflow and underflow conditions.

## 2. What is a stack, and when to use it?

Imagine you have a stack of plates in front of you, where you can only access the topmost plate. A stack in computer science works in a similar way. It's like a vertical arrangement of objects, where you can add or remove items from the top only. This is called a stack because it follows the Last-In, First-Out (LIFO) principle.

A stack is a collection of elements with two main operations: push and pop. When you push an item onto the stack, it goes on top of the existing items. When you pop an item from the stack, you remove the topmost item. This way, the last item you added is the first one to be removed.

In programming, stacks are incredibly useful in different situations. Let's explore some relatable examples:

1. Function call stack: Imagine you have a set of functions calling each other, like a chain of actions. When a function is called, it gets added to the stack, just like adding a plate to the top of the stack. When a function finishes executing, it gets removed from the stack, allowing the program to go back to the previous function. It's like a stack of function calls!

2. Expression evaluation: Have you ever solved a mathematical expression with parentheses? You start by evaluating the innermost parentheses first, right? Stacks can help with that. Think of a stack as a tool to keep track of the operations and numbers in an expression. When you encounter an opening parenthesis, you push it onto the stack. As you solve the inner expression, the results are pushed onto the stack. When you encounter a closing parenthesis, you pop the elements from the stack and perform the corresponding operation. This way, the stack helps maintain the correct order of operations.

3. Undo/Redo functionality: Imagine you are using a drawing application and want to undo or redo your actions. A stack can come to the rescue! Every action you perform, like drawing a line or adding a shape, gets pushed onto the stack. If you want to undo, you pop the last action from the stack and revert it. If you want to redo, you push the previously undone action back onto the stack. It's like stacking your actions, allowing you to go back and forth in your drawing history.

4. Backtracking algorithms: Let's say you are exploring a maze or solving a puzzle. Backtracking algorithms like depth-first search (DFS) use stacks to keep track of different paths. As you explore one path, the states or positions you encounter are pushed onto the stack. If you reach a dead-end, you backtrack by popping from the stack and trying a different path. This way, the stack helps you remember the different options you have explored.

Here's an example of implementing a stack using an array in C:

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void push(Stack* stack, int item) {
    if (stack->top == MAX_SIZE - 1) {
        printf("Stack overflow!\n");
        return;
    }
    stack->top++;
    stack->data[stack->top] = item;
}

int pop(Stack* stack) {
    if (stack->top == -1) {
        printf("Stack underflow!\n");
        return -1; // or any appropriate error value
    }
    int item = stack->data[stack->top];
    stack->top--;
    return item;
}
```

This code defines a stack data structure in the C programming language. The stack is implemented using an array called  `data`  and a variable called  `top`  that keeps track of the index of the top element in the stack. The maximum size of the stack is defined as  `MAX_SIZE` , which is set to 100.

The  `push`  function is used to add an item to the stack. It takes a pointer to a  `Stack`  structure and an item as parameters. First, it checks if the stack is already full by comparing the  `top`  value to  `MAX_SIZE - 1` . If the stack is full, it prints an error message indicating a "stack overflow" and returns. Otherwise, it increments the  `top`  value and assigns the item to the  `data`  array at the updated  `top`  index.

The  `pop`  function is used to remove and return the topmost item from the stack. It also takes a pointer to a  `Stack`  structure as a parameter. First, it checks if the stack is empty by comparing the  `top`  value to -1. If the stack is empty, it prints an error message indicating a "stack underflow" and returns an appropriate error value (e.g., -1). Otherwise, it retrieves the item from the  `data`  array at the current  `top`  index, decrements the  `top`  value, and returns the item.

Overall, this code provides a basic implementation of a stack data structure with functions to push items onto the stack and pop items from the stack, while also handling overflow and underflow conditions.

## 3. What is a queue, and when to use it?

Imagine you are waiting in line at a popular ice cream shop. You see people joining the line, and the person who arrived first gets their ice cream first. A queue in computer science works in a similar way. It's like a line of people waiting for something, where the person who arrived first gets served first. This is called a queue because it follows the First-In, First-Out (FIFO) principle.

A queue is a collection of elements with two main operations: enqueue and dequeue. Enqueue means adding an item to the end of the queue, and dequeue means removing an item from the front of the queue. Just like people join the line at the end and leave from the front, elements are added to the rear and removed from the front of a queue.

In terms of memory organization, a queue can be implemented using an array or a linked list. Think of the queue as a line of people waiting for something exciting. Each person has a unique number, and the front and rear of the queue keep track of the positions.

Here are some real-life scenarios where queues are commonly used:

1. Process scheduling: Imagine an operating system managing different processes. The processes join a queue based on when they arrive, and they are executed in the order they joined the queue. It's like people waiting for their turn to use a computer.

2. Print spooling: When multiple users send print requests to a printer, a queue is used to manage the order in which the documents are printed. The documents are added to the queue based on their arrival time, and they are printed one by one as they reach the front of the queue. It's like a line of documents waiting to be printed.

3. Breadth-first search (BFS): In graph traversal algorithms like BFS, a queue is used to explore neighboring vertices level by level. It's like exploring a network of interconnected rooms, where you visit the neighboring rooms before moving on to the next level. The queue helps in maintaining the order of exploration.

4. Message passing between threads: Imagine different threads or processes in a program communicating with each other. A queue is used to pass messages between them. One thread adds a message to the queue, and another thread takes messages from the front of the queue and processes them. It's like passing notes between friends using a queue.

Here's an example of implementing a queue using an array in C:

```c
#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} Queue;

void enqueue(Queue* queue, int item) {
    if (queue->rear == MAX_SIZE - 1) {
        printf("Queue overflow!\n");
        return;
    }
    queue->rear++;
    queue->data[queue->rear] = item;
}

int dequeue(Queue* queue) {
    if (queue->front > queue->rear) {
        printf("Queue underflow!\n");
        return -1; // or any appropriate error value
    }
    int item = queue->data[queue->front];
    queue->front++;
    return item;
}
```

This code defines a queue data structure in C programming. The queue is implemented using an array called  `data`  and two variables called  `front`  and  `rear`  to keep track of the indices of the front and rear elements of the queue, respectively. The maximum size of the queue is defined as  `MAX_SIZE` , which is set to 100.

The  `enqueue`  function is used to add an item to the queue. It takes a pointer to a  `Queue`  structure and an item as parameters. First, it checks if the rear index is equal to  `MAX_SIZE - 1` , indicating that the queue is already full. If the queue is full, it prints an error message indicating a "queue overflow" and returns. Otherwise, it increments the rear index and assigns the item to the  `data`  array at the updated rear index.

The  `dequeue`  function is used to remove and return the frontmost item from the queue. It also takes a pointer to a  `Queue`  structure as a parameter. First, it checks if the front index is greater than the rear index, indicating that the queue is empty. If the queue is empty, it prints an error message indicating a "queue underflow" and returns an appropriate error value (e.g., -1). Otherwise, it retrieves the item from the  `data`  array at the current front index, increments the front index, and returns the item.

In summary, this code provides a basic implementation of a queue data structure with functions to enqueue items into the queue and dequeue items from the queue, while also handling overflow and underflow conditions.

## 4. What are the common implementations of stacks and queues?

Let's explore the common ways to implement stacks and queues in a way that's easy to understand.

- Common implementations of stacks:
   a. Array-based implementation: Imagine you have a stack of books on a table. Each book represents an element in the stack, and the top book represents the most recently added element. In an array-based implementation, the stack is like a fixed-size shelf where you can only add or remove books from the top. The size of the array determines the maximum number of books you can have on the shelf. When you add a book, you place it on top of the stack, and when you remove a book, you take it from the top. However, if you try to add more books than the shelf can hold, it will overflow, and if you try to remove a book from an empty shelf, it will underflow.

   b. Linked list-based implementation: Imagine you have a stack of plates, and each plate represents an element in the stack. The top plate represents the most recently added element. In a linked list-based implementation, the stack is like a stack of plates where you can add or remove plates from the top. Each plate has a reference to the plate below it, forming a chain. When you add a plate, you place it on top of the stack, and when you remove a plate, you take it from the top. This implementation allows for a dynamic number of elements, and you can add or remove plates without worrying about the size of the stack.

- Common implementations of queues:
   a. Array-based implementation: Imagine you are waiting in line at a movie theater. Each person in the line represents an element in the queue. In an array-based implementation, the queue is like a fixed-size line where people join at the rear and leave from the front. When a new person arrives, they join the line at the rear, and when it's their turn, they leave from the front. However, if the line becomes full and you try to add more people, it will overflow, and if you try to remove a person from an empty line, it will underflow.

   b. Linked list-based implementation: Imagine you are waiting in line at a theme park, and each person represents an element in the queue. In a linked list-based implementation, the queue is like a line of people where they join at the rear and leave from the front. Each person has a reference to the person behind them, forming a chain. When a new person arrives, they join the line at the rear, and when it's their turn, they leave from the front. This implementation allows for a dynamic number of elements, and you can add or remove people without worrying about the size of the queue.

## 5. What are the most common use cases of stacks and queues?

Let's explore some real-life scenarios where stacks and queues are commonly used.

- Most common use cases of stacks:
   a. Function call stack: Imagine you have a set of instructions to follow, and each instruction calls another set of instructions. The function call stack is like a stack of instruction sets. When you start executing a new set of instructions, you push it onto the stack. As you complete each set of instructions, you pop it from the stack and continue with the previous set. This helps in keeping track of where you are in the instructions and allows you to return to the previous set once you finish the current one.

   b. Expression evaluation: Imagine you have a complex mathematical expression to solve, like (2 + 3) * 4. To evaluate this expression correctly, you need to follow the order of operations and keep track of the numbers and operators. A stack can help with that. It's like having a stack of numbers and operators. As you encounter numbers and operators in the expression, you push them onto the stack. When you reach an operator with higher precedence, you pop the necessary elements from the stack, perform the operation, and push the result back onto the stack. This way, the stack helps maintain the correct order of operations.

   c. Undo/Redo functionality: Imagine you are working on a digital drawing application, and you want to undo or redo your actions. The undo/redo functionality is like a stack of actions. Each action you perform, like drawing a line or adding a shape, gets pushed onto the stack. If you want to undo, you pop the last action from the stack and revert it. If you want to redo, you push the previously undone action back onto the stack. This way, the stack helps you keep track of your actions and allows you to go back and forth in your drawing history.

   d. Backtracking algorithms: Imagine you are exploring a maze or solving a puzzle. Backtracking algorithms, like depth-first search (DFS), use a stack to keep track of different paths. As you explore one path, you push the states or positions you encounter onto the stack. If you reach a dead-end, you backtrack by popping from the stack and trying a different path. This way, the stack helps you remember the different options you have explored and allows you to backtrack when needed.

- Most common use cases of queues:
   a. Process scheduling: Imagine you have multiple processes or tasks waiting to be executed on your computer. The process scheduling is like a queue of tasks. Each task joins the queue based on when it arrives, and they are executed in the order they joined the queue. It's like people waiting in line to use a computer, and the next person in line gets their turn to use the computer.

   b. Print spooling: Imagine you are in a school computer lab, and multiple students send print requests to a printer. The print spooling is like a queue of print jobs. Each print job joins the queue based on when it was requested, and they are printed in the order they joined the queue. It's like a line of documents waiting to be printed, and the printer processes them one by one.

   c. Breadth-first search (BFS): Imagine you have a network of interconnected rooms, and you want to explore it systematically. Breadth-first search (BFS) is like exploring the rooms level by level. You start at one room, visit all its neighboring rooms, and then move on to the next level of neighboring rooms. A queue can help with that. As you visit a room, you enqueue its neighboring rooms, and you dequeue rooms from the front of the queue to explore them. This way, the queue helps you maintain the order of exploration.

   d. Message passing between threads: Imagine you have multiple threads or processes in a program, and they need to communicate with each other. Message passing is like passing notes between friends using a queue. One thread enqueues a message, and another thread dequeues and processes it. This allows for orderly communication and synchronization between different parts of the program.

## 6. What is the proper way to use global variables?

When it comes to using global variables in C programming, there are some guidelines that ensure their proper usage. Let's explore these guidelines in a way that's easy to understand:

a. Limit their usage: Global variables should be used sparingly and only when necessary. It's like having a special tool that you use only when other options are not available. Instead of relying on global variables, it's generally recommended to use local variables within functions or pass variables as parameters. This helps keep your code organized and prevents unexpected behavior.

b. Declare them at the top: When you use global variables, it's important to declare them at the top of the file, outside of any function. Think of it as placing important information at the beginning of a book. This makes it easier for you and other programmers to locate and understand the global variables used within the program.

c. Initialize them explicitly: Global variables should be explicitly initialized when declared. It's like setting the stage before starting a play. By initializing global variables, you prevent any unexpected behavior that may occur due to uninitialized variables. This ensures that your program starts with the desired initial values.

d. Avoid excessive dependencies: Global variables can introduce dependencies, making your code harder to understand and maintain. It's like having too many strings attached. Try to minimize the dependencies on global variables by encapsulating related functionality within functions or structures. This way, you can keep your code modular and easier to manage.

e. Use proper naming conventions: Give meaningful and descriptive names to global variables. It's like labeling items in your room, so you can easily find what you need. Meaningful names enhance code readability and understanding. You can also use prefixes or other naming conventions to indicate that a variable is global. This way, you and other programmers can quickly identify global variables in your code.

f. Consider using constants instead: If a variable does not need to be modified, consider using constants instead of global variables. Constants are like fixed values that cannot be changed. They provide better clarity and prevent unintended modifications. This is especially useful when you have values that should remain constant throughout your program.

g. Document their purpose: It is crucial to document the purpose and usage of global variables, especially if they are shared across multiple files or modules. It's like writing a note to yourself or others, explaining why a certain item is important. Documentation helps other programmers understand and use the global variables correctly. It's also a good practice to include comments in your code to provide additional explanations when necessary.

By following these guidelines, you can ensure the proper usage of global variables in your C programs. Remember, global variables should be used thoughtfully and with caution, keeping in mind the impact they may have on the overall structure and maintainability of your code.

## Conclusion:
In conclusion, this comprehensive guide has covered the essentials of stacks, queues, and the strategic usage of global variables in C programming. While the concepts discussed may be familiar to experienced programmers, it is always beneficial to revisit and reinforce our understanding. We have explored both the foundational aspects and advanced implementations, ensuring a balanced approach to cater to programmers of varying expertise. Remember to adapt these concepts to suit the specific requirements of your projects, and continue to stay curious and open to new insights. With your experience and this enhanced understanding, you are well-equipped to tackle programming challenges with confidence. Happy coding!


© [2023] [Paschal Ugwu]
