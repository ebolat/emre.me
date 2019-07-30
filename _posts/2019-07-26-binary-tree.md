---
title: "Binary Tree"
header:
  image: https://cdn.emre.me/2019-07-26-binary-tree-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/b9drVB7xIOI)"
categories:
  - data-structures
tags:
  - basics
  - python
  - binary-tree
  - data-structures
toc: true
toc_sticky: true
---

Binary Tree is a classical data structure in [Computer Science](https://en.wikipedia.org/wiki/Computer_science). It is a non-linear [data structure](https://emre.me/categories/#data-structures) and formally a binary tree is either *empty* or a *root* node with a left binary tree and a right binary tree.

The left binary tree is sometimes referred to as *the left subtree* of the root and the right binary tree is referred to as *the right subtree* of the root.

Binary trees most commonly occur in the context of Binary Search Trees (BST), where keys are stored in a sorted fashion but in this article we will only focus on Binary Trees. Binary Search Trees (BST) will be explained deeply in another article.

![Binary Tree](https://cdn.emre.me/2019-07-26-binary-tree.png){: .align-center}

In this graphical representation of Binary Tree, Node **A** is the *root* and Node **B** and **I** are the left and right children of root **A**.

The *depth* of a node **n** is the number of nodes on the search path from the root to **n**, not including **n** itself. The *height* of a binary tree is the maximum depth of any node in that tree. A *level* of a tree is all nodes at the same depth.

## Implementation of Binary Tree ##

Just like we did in [Linked List](https://emre.me/data-structures/linked-lists/), we need to start the implementation by defining a root *Node* and its left and right children.

```python
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data
```

Notice that constructor function expects some kind of data to store in the root. If we want to expand our tree beyond the root node, we will need funcions to insert new data to *left* and *right* nodes.

### insert_left function ###

Let's implement `insert_left()` function together.
We must consider two possibilities to be able to implement this function. First case is a node with no existing left child and the second case is node with an existing left child.

```python
def insert_left(self, value):
    if self.left is None:
        self.left = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left = self.left
        self.left = new_node
```

When there is no left child, all we need to do is simply create a left child with creating a new node. In the second case, where there is already an existing left child, we are inserting as new node and pushing existing child node one level down in the tree.

### insert_right function ###

Implementation of `insert_right()` function is symmetric with the implementation of `insert_left()` function.

```python
def insert_right(self, value):
    if self.right is None:
        self.right = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left = self.left
        self.left = new_node
```

There will be either no right child or there will be an existing right child which will be pushed down one level with the addition of new right child.

## Implementation Summary ##

let's summarize what we implemented so far by adding getter and setter functions to call existing nodes.

```python
class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_value(self, value):
        self.root = value

    def get_root_value(self):
        return self.root
```

### Example ###

![Binary Tree](https://cdn.emre.me/2019-07-26-binary-tree-abcdef.png){: .align-center}

To test our code, we can try to implement this tree.

So;
- node **a** is our *root* node.
- node **b** is the *left* child of node **a**
- node **c** is the *right* child of node **a**
- node **d** is the *right* child of node **b**
- node **e** is the *left* child of node **c**
- node **f** is the *right* child of node **c**

if we want to implement this structure in our code, it will look like this;

```python
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f
```

## Summary ##

Binary Tree is a fundamental data structure in computer science and this article is just scratching the surface. I will continue writing more about trees in new articles about searching (Depth-First Search - DFS, Breadth-First Search - BFS), Binary Search Trees (BST), balanced trees, AVL trees, tree treversal etc.

## References ##

1. Wikipedia, *[Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)* 