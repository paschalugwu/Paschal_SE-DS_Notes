# Comprehensive Exploration of Binary Trees: From Fundamentals to Advanced Topics and Big O Analysis.

Binary trees are foundational data structures that play a crucial role in computer science and software engineering. Their hierarchical nature enables efficient storage and retrieval of information, making them a fundamental concept in algorithmic design. This note delves into the diverse aspects of binary trees, covering everything from basic concepts to advanced topics and concluding with a critical analysis of their time complexities.

## Binary Trees - Understanding Fundamental Concepts

### 1. What is a Binary Tree?

A **binary tree** is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. The topmost node in a binary tree is called the root, and nodes with no children are called leaves. The structure resembles an inverted tree, with the root at the top and branches extending downward.

Here's a simple representation of a binary tree:

```c
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

In this example, each node contains an integer value and pointers to its left and right children.

### 2. Difference between Binary Tree and Binary Search Tree (BST)

While a binary tree allows any values in its nodes, a **Binary Search Tree (BST)** imposes a specific order. In a BST, for every node:
- All nodes in its left subtree have values less than the node's value.
- All nodes in its right subtree have values greater than the node's value.

This ordering property facilitates efficient search operations. Here's a simplified example:

```c
struct BSTNode {
    int data;
    struct BSTNode* left;
    struct BSTNode* right;
};
```

### 3. Time Complexity Gain Compared to Linked Lists

In terms of time complexity, binary trees offer advantages over linked lists, particularly in search, insert, and delete operations.

- **Search Operation:**
  - In a binary search tree, searching for a value is more efficient compared to a linked list.
  - The order of elements allows for a binary search, reducing the time complexity to O(log n) on average, where n is the number of elements.

- **Insert and Delete Operations:**
  - Similarly, the ordered structure of binary search trees streamlines insert and delete operations.
  - On average, these operations also have a time complexity of O(log n).

In contrast, linked lists, which require linear traversal, have a time complexity of O(n) for these operations.

## Binary Trees - Understanding Binary Tree Properties

### 1. Depth, Height, and Size of a Binary Tree

- **Depth:**
  - The depth of a node in a binary tree is the length of the path from the root to that node. The depth of the root is 0.
  
- **Height:**
  - The height of a node in a binary tree is the length of the longest path from that node to a leaf. The height of the tree is the height of the root.
  
- **Size:**
  - The size of a binary tree is the total number of nodes in the tree.

These properties help us analyze and understand the structure of a binary tree.

### 2. Types of Binary Trees

- **Full Binary Tree:**
  - In a full binary tree, every node has either 0 or 2 children. No node has only one child.
  
- **Perfect Binary Tree:**
  - A perfect binary tree is both full and all its leaf nodes are at the same level.
  
- **Balanced Binary Tree:**
  - A balanced binary tree is a tree in which the depth of the left and right subtrees of any node differs by no more than one.

### 3. Measuring Height, Depth, and Size

- **Height:**
  - The height of a binary tree can be calculated recursively. The height of a node is the maximum height of its left and right subtrees, plus one.
  
  ```c
  int calculateHeight(struct Node* root) {
      if (root == NULL) {
          return -1;  // Height of an empty tree is -1
      }
      int leftHeight = calculateHeight(root->left);
      int rightHeight = calculateHeight(root->right);
      return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
  }
  ```

- **Depth:**
  - The depth of a node is its distance from the root. It is calculated by tracing the path from the root to the node.

- **Size:**
  - The size of a binary tree is the sum of the sizes of its left and right subtrees, plus one for the current node.
  
  ```c
  int calculateSize(struct Node* root) {
      if (root == NULL) {
          return 0;  // Size of an empty tree is 0
      }
      return 1 + calculateSize(root->left) + calculateSize(root->right);
  }
  ```

## Binary Trees - Understanding Traversal Methods

### 1. Different Traversal Methods

Traversing a binary tree involves systematically visiting all nodes in a specific order. There are three main traversal methods:

- **Pre-order Traversal:**
  - In pre-order traversal, you visit the root node first, followed by the left subtree, and then the right subtree.
  
  ```c
  void preOrderTraversal(struct Node* root) {
      if (root != NULL) {
          printf("%d ", root->data);
          preOrderTraversal(root->left);
          preOrderTraversal(root->right);
      }
  }
  ```

- **In-order Traversal:**
  - In in-order traversal, you visit the left subtree first, followed by the root node, and then the right subtree. In the case of binary search trees, this results in visiting nodes in ascending order.
  
  ```c
  void inOrderTraversal(struct Node* root) {
      if (root != NULL) {
          inOrderTraversal(root->left);
          printf("%d ", root->data);
          inOrderTraversal(root->right);
      }
  }
  ```

- **Post-order Traversal:**
  - In post-order traversal, you visit the left subtree first, then the right subtree, and finally the root node.
  
  ```c
  void postOrderTraversal(struct Node* root) {
      if (root != NULL) {
          postOrderTraversal(root->left);
          postOrderTraversal(root->right);
          printf("%d ", root->data);
      }
  }
  ```

### 2. Applying Traversal Methods

These traversal methods find applications in various scenarios, such as:

- **Searching for a Specific Node:**
  - By traversing a binary tree using these methods, you can efficiently search for a specific node.

- **Printing Nodes in a Specific Order:**
  - If you want to print the nodes of a binary tree in a specific order, these traversal methods provide the necessary sequence.

- **Calculating Expression Results:**
  - In mathematical expressions represented as binary trees, traversal methods are useful for calculating the result using different orders of operations.

## Binary Trees - Node Operations

### 1. Creating a New Binary Tree Node

To create a new binary tree node, you need a structure representing a node and a function to allocate memory for the new node and initialize its values.

```c
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode != NULL) {
        newNode->data = value;
        newNode->left = NULL;
        newNode->right = NULL;
    }
    return newNode;
}
```

This function takes a value, allocates memory for a new node, sets its data, left, and right pointers, and returns the newly created node.

### 2. Inserting a New Node

Inserting a new node involves linking it to the tree appropriately based on its value.

```c
void insertNode(struct Node* parent, int value, char position) {
    if (parent == NULL) {
        printf("Cannot insert into a NULL parent.\n");
        return;
    }

    struct Node* newNode = createNode(value);

    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    if (position == 'L') {
        parent->left = newNode;
    } else if (position == 'R') {
        parent->right = newNode;
    } else {
        printf("Invalid position. Use 'L' for left child or 'R' for right child.\n");
        free(newNode);  // Free memory in case of an error
    }
}
```

This function inserts a new node with a specified value as the left or right child of a given parent node.

### 3. Deleting an Entire Binary Tree

To free the memory allocated for a binary tree, you can perform a post-order traversal and free each node.

```c
void deleteTree(struct Node* root) {
    if (root != NULL) {
        deleteTree(root->left);
        deleteTree(root->right);
        free(root);
    }
}
```

This recursive function deletes the entire binary tree by traversing it post-order and freeing each node.

### 4. Determining Node Type

You can determine if a given node is a leaf or a root by checking its children.

```c
int isLeaf(struct Node* node) {
    return (node != NULL && node->left == NULL && node->right == NULL);
}

int isRoot(struct Node* node) {
    return (node != NULL && node->left == NULL && node->right == NULL);
}
```

These functions return true if the given node is a leaf or a root, respectively.

## Binary Trees - Exploring Advanced Topics

### 1. Measuring the Balance Factor

The balance factor of a binary tree is the difference between the height of the left subtree and the height of the right subtree for each node. A balanced tree has a balance factor of -1, 0, or 1. You can calculate it using the height function discussed earlier.

```c
int balanceFactor(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return calculateHeight(node->left) - calculateHeight(node->right);
}
```

### 2. Definitions of Full and Perfect Binary Trees

- **Full Binary Tree:**
  - A full binary tree is a binary tree in which every node has either 0 or 2 children. No node has only one child.

- **Perfect Binary Tree:**
  - A perfect binary tree is both full and all its leaf nodes are at the same level. It has 2^(h+1) - 1 nodes (where 'h' is the height).

### 3. Finding the Lowest Common Ancestor

The lowest common ancestor (LCA) of two nodes in a binary tree is the shared ancestor farthest from the root. It can be found by traversing the tree and keeping track of the path to each node.

```c
struct Node* findLowestCommonAncestor(struct Node* root, int value1, int value2) {
    if (root == NULL || root->data == value1 || root->data == value2) {
        return root;
    }

    struct Node* leftLCA = findLowestCommonAncestor(root->left, value1, value2);
    struct Node* rightLCA = findLowestCommonAncestor(root->right, value1, value2);

    if (leftLCA != NULL && rightLCA != NULL) {
        return root;  // Current root is the LCA
    }

    return (leftLCA != NULL) ? leftLCA : rightLCA;
}
```

### 4. Implementing Level-Order Traversal

Level-order traversal involves visiting nodes level by level, from left to right. It uses a queue to keep track of the nodes at each level.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct QueueNode {
    struct Node* data;
    struct QueueNode* next;
};

struct Queue {
    struct QueueNode* front;
    struct QueueNode* rear;
};

void enqueue(struct Queue* queue, struct Node* data) {
    struct QueueNode* newNode = (struct QueueNode*)malloc(sizeof(struct QueueNode));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }
    newNode->data = data;
    newNode->next = NULL;

    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
        return;
    }

    queue->rear->next = newNode;
    queue->rear = newNode;
}

struct Node* dequeue(struct Queue* queue) {
    if (queue->front == NULL) {
        return NULL;
    }

    struct QueueNode* temp = queue->front;
    struct Node* data = temp->data;

    queue->front = queue->front->next;
    free(temp);

    if (queue->front == NULL) {
        queue->rear = NULL;
    }

    return data;
}

void levelOrderTraversal(struct Node* root) {
    if (root == NULL) {
        return;
    }

    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    if (queue == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }
    queue->front = queue->rear = NULL;

    enqueue(queue, root);

    while (queue->front != NULL) {
        struct Node* current = dequeue(queue);
        printf("%d ", current->data);

        if (current->left != NULL) {
            enqueue(queue, current->left);
        }

        if (current->right != NULL) {
            enqueue(queue, current->right);
        }
    }

    free(queue);
}
```

## Binary Trees - Understanding Binary Search Trees (BST)

### 1. Validating a Binary Search Tree (BST)

To validate whether a binary tree is a Binary Search Tree (BST), you need to check that the left subtree of a node contains only values less than the node, and the right subtree contains only values greater than the node. This property should hold for all nodes in the tree.

```c
int isBST(struct Node* root, int min, int max) {
    if (root == NULL) {
        return 1;  // An empty tree is a BST
    }

    if (root->data < min || root->data > max) {
        return 0;  // Node value violates the BST property
    }

    return isBST(root->left, min, root->data - 1) && isBST(root->right, root->data + 1, max);
}
```

This recursive function checks if the binary tree is a BST within the specified range for each node.

### 2. Inserting into a Binary Search Tree (BST)

Inserting a value into a BST involves finding the appropriate position for the value based on the BST property.

```c
struct Node* insertBST(struct Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }

    if (value < root->data) {
        root->left = insertBST(root->left, value);
    } else if (value > root->data) {
        root->right = insertBST(root->right, value);
    }

    return root;
}
```

This recursive function inserts a new value while maintaining the BST properties.

### 3. Building a Binary Search Tree (BST) from an Array

To build a BST from an array, you can insert each element into the tree.

```c
struct Node* buildBSTFromArray(int arr[], int start, int end) {
    if (start > end) {
        return NULL;
    }

    int mid = (start + end) / 2;
    struct Node* root = createNode(arr[mid]);

    root->left = buildBSTFromArray(arr, start, mid - 1);
    root->right = buildBSTFromArray(arr, mid + 1, end);

    return root;
}
```

This function builds a balanced BST from a sorted array by recursively selecting the middle element as the root.

### 4. Searching in a Binary Search Tree (BST)

Searching in a BST involves comparing the target value with the current node and deciding whether to continue the search in the left or right subtree.

```c
struct Node* searchBST(struct Node* root, int value) {
    if (root == NULL || root->data == value) {
        return root;
    }

    if (value < root->data) {
        return searchBST(root->left, value);
    } else {
        return searchBST(root->right, value);
    }
}
```

This function returns the node with the target value or NULL if the value is not present in the BST.

## Binary Trees - Understanding AVL Trees

### 1. Checking Validity of an AVL Tree

An AVL Tree is a self-balancing binary search tree where the balance factor of every node is between -1, 0, or 1. You can validate if a binary tree is a valid AVL Tree by ensuring that it satisfies the AVL balance property.

```c
int isAVL(struct Node* root) {
    if (root == NULL) {
        return 1;  // An empty tree is an AVL Tree
    }

    int leftHeight = calculateHeight(root->left);
    int rightHeight = calculateHeight(root->right);

    if (abs(leftHeight - rightHeight) > 1) {
        return 0;  // AVL balance property violated
    }

    return isAVL(root->left) && isAVL(root->right);
}
```

This function recursively checks the AVL balance property for each node.

### 2. Inserting into an AVL Tree

To insert a value into an AVL Tree while maintaining its balance, you need to perform standard BST insertion and then update the height and balance factors.

```c
int max(int a, int b) {
    return (a > b) ? a : b;
}

int height(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return 1 + max(height(node->left), height(node->right));
}

int getBalance(struct Node* node) {
    if (node == NULL) {
        return 0;
    }
    return height(node->left) - height(node->right);
}

struct Node* rotateRight(struct Node* y) {
    struct Node* x = y->left;
    struct Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    return x;
}

struct Node* rotateLeft(struct Node* x) {
    struct Node* y = x->right;
    struct Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    return y;
}

struct Node* insertAVL(struct Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }

    if (value < root->data) {
        root->left = insertAVL(root->left, value);
    } else if (value > root->data) {
        root->right = insertAVL(root->right, value);
    } else {
        return root;  // Duplicate values are not allowed in AVL Trees
    }

    // Update height of the current node
    root->height = 1 + max(height(root->left), height(root->right));

    // Get the balance factor and perform rotations if needed
    int balance = getBalance(root);

    // Left-Left Case
    if (balance > 1 && value < root->left->data) {
        return rotateRight(root);
    }

    // Right-Right Case
    if (balance < -1 && value > root->right->data) {
        return rotateLeft(root);
    }

    // Left-Right Case
    if (balance > 1 && value > root->left->data) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    // Right-Left Case
    if (balance < -1 && value < root->right->data) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}
```

### 3. Building an AVL Tree from an Array

Building an AVL tree from an array involves first sorting the array and then creating an AVL tree using the sorted values.

```c
struct Node* buildAVLFromArray(int arr[], int start, int end) {
    if (start > end) {
        return NULL;
    }

    int mid = (start + end) / 2;
    struct Node* root = createNode(arr[mid]);

    root->left = buildAVLFromArray(arr, start, mid - 1);
    root->right = buildAVLFromArray(arr, mid + 1, end);

    return root;
}
```

### 4. Removing a Node from an AVL Tree

Removing a node from an AVL tree while maintaining balance requires standard BST deletion and additional rotations if necessary.

```c
struct Node* deleteNode(struct Node* root, int value) {
    // Standard BST delete
    if (root == NULL) {
        return root;
    }

    if (value < root->data) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->data) {
        root->right = deleteNode(root->right, value);
    } else {
        // Node with only one child or no child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }

        // Node with two children, get the inorder successor
        struct Node* temp = minValueNode(root->right);

        // Copy the inorder successor's data to this node
        root->data = temp->data;

        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->data);
    }

    // If the tree had only one node, return
    if (root == NULL) {
        return root;
    }

    // Update height of the current node
    root->height = 1 + max(height(root->left), height(root->right));

    // Get the balance factor and perform rotations if needed
    int balance = getBalance(root);

    // Left-Left Case
    if (balance > 1 && getBalance(root->left) >= 0) {
        return rotateRight(root);
    }

    // Left-Right Case
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    // Right-Right Case
    if (balance < -1 && getBalance(root->right) <= 0) {
        return rotateLeft(root);
    }

    // Right-Left Case
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}
```

## Binary Trees - Exploring Heap Operations

### 1. Building AVL Tree from a Sorted Array Without Rotations

To efficiently build an AVL tree from a sorted array without using rotations, you can recursively build a balanced BST and then update the height of each node.

```c
struct Node* buildAVLFromArrayWithoutRotations(int arr[], int start, int end) {
    if (start > end) {
        return NULL;
    }

    int mid = (start + end) / 2;
    struct Node* root = createNode(arr[mid]);

    root->left = buildAVLFromArrayWithoutRotations(arr, start, mid - 1);
    root->right = buildAVLFromArrayWithoutRotations(arr, mid + 1, end);

    // Update height of the current node
    root->height = 1 + max(height(root->left), height(root->right));

    return root;
}
```

This function builds a balanced AVL tree from a sorted array without explicitly using rotations.

### 2. Validating a Max Binary Heap

A Max Binary Heap is a binary tree where the value of each node is greater than or equal to the values of its children. You can validate if a binary tree is a valid Max Binary Heap by checking this property.

```c
int isMaxHeap(struct Node* root) {
    if (root == NULL) {
        return 1;  // An empty tree is a Max Binary Heap
    }

    if (root->left != NULL && root->left->data > root->data) {
        return 0;  // Left child violates the Max Heap property
    }

    if (root->right != NULL && root->right->data > root->data) {
        return 0;  // Right child violates the Max Heap property
    }

    return isMaxHeap(root->left) && isMaxHeap(root->right);
}
```

This function recursively checks the Max Heap property for each node.

### 3. Inserting into a Max Binary Heap

Inserting a value into a Max Binary Heap involves adding the value at the bottom level and then swapping it with its parent until the Max Heap property is restored.

```c
struct Node* insertMaxHeap(struct Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }

    if (isFull(root)) {
        printf("Heap is full. Cannot insert.\n");
        return root;
    }

    if (root->left == NULL) {
        root->left = insertMaxHeap(root->left, value);
    } else if (root->right == NULL) {
        root->right = insertMaxHeap(root->right, value);
    } else {
        if (height(root->left) <= height(root->right)) {
            root->left = insertMaxHeap(root->left, value);
        } else {
            root->right = insertMaxHeap(root->right, value);
        }
    }

    // Swap with parent if necessary
    if (root->left != NULL && root->left->data > root->data) {
        swap(&(root->data), &(root->left->data));
    }

    if (root->right != NULL && root->right->data > root->data) {
        swap(&(root->data), &(root->right->data));
    }

    return root;
}
```

This function inserts a value into a Max Binary Heap while maintaining the Max Heap property.

### 4. Converting Binary Max Heap to Sorted Array

Converting a Binary Max Heap into a sorted array involves repeatedly extracting the maximum element (root) and swapping it with the last element until the heap is empty.

```c
void heapSort(struct Node* root, int sortedArray[], int* index) {
    if (root == NULL) {
        return;
    }

    heapSort(root->left, sortedArray, index);
    sortedArray[(*index)++] = root->data;
    heapSort(root->right, sortedArray, index);
}
```

This function performs a heap sort by converting a Max Binary Heap into a sorted array in descending order.

## Binary Trees - Understanding Big O Analysis

### Time Complexities of Operations on Binary Trees

1. **Binary Tree:**
   - **Search (in worst case):** O(n)
   - **Insertion (at a given position):** O(1) - assuming you have a pointer/reference to the parent node.
   - **Deletion (of a given node):** O(1) - assuming you have a pointer/reference to the node.

2. **Binary Search Tree (BST):**
   - **Search (average and worst case):** O(log n) - balanced tree.
   - **Insertion (average and worst case):** O(log n) - balanced tree.
   - **Deletion (average and worst case):** O(log n) - balanced tree.

3. **AVL Tree:**
   - **Search (average and worst case):** O(log n) - AVL trees are balanced.
   - **Insertion (average and worst case):** O(log n) - AVL trees are balanced.
   - **Deletion (average and worst case):** O(log n) - AVL trees are balanced.

4. **Max Binary Heap:**
   - **Search (in worst case):** O(n) - No specific order in Max Heap.
   - **Insertion (at the last position):** O(log n) - to maintain the heap property.
   - **Deletion (of the maximum element):** O(log n) - to maintain the heap property.

### Explanation:

- **Binary Tree:**
  - Searching requires traversing the entire tree in the worst case, making it O(n).
  - Insertion and deletion depend on having a reference to the position, so they can be O(1).

- **Binary Search Tree (BST):**
  - Searching, insertion, and deletion are O(log n) on average and in the worst case for a balanced tree.

- **AVL Tree:**
  - AVL trees are self-balancing, ensuring that search, insertion, and deletion operations remain O(log n).

- **Max Binary Heap:**
  - Searching in a Max Heap is O(n) in the worst case, as there is no inherent order.
  - Insertion and deletion involve maintaining the heap property, resulting in O(log n) complexity.

## Applications

Understanding binary trees is essential for solving a variety of computational problems. They find applications in databases, file systems, expression parsing, and more. Moreover, specialized types like Binary Search Trees (BST), AVL Trees, and Max Binary Heaps serve specific purposes in optimizing search, retrieval, and sorting operations. Proficiency in working with binary trees is invaluable for any programmer seeking to design efficient algorithms and data structures.

## Conclusion

In conclusion, this note has provided a comprehensive exploration of binary trees, ranging from fundamental concepts to advanced topics and performance analysis. By understanding the properties, traversal methods, node operations, and specialized tree types like BST, AVL, and Max Binary Heap, you gain a robust foundation for solving real-world problems efficiently. The note culminates in a discussion on the average time complexities of key operations across different tree types, empowering you to make informed choices when selecting the right structure for your applications. Mastery of these concepts is not only essential for academic excellence but is also a critical skill for any software engineer navigating the complexities of algorithmic design.

© [2024] [Paschal Ugwu]
