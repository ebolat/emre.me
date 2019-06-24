---
title: "Linked Lists"
header:
  image: https://cdn.emre.me/2019-06-13-linked-list-header-image.jpg
  caption: "Photo credit: [**Pexels**](https://www.pexels.com/photo/blue-carriage-clouds-daylight-358167/)"
categories:
  - data-structures
tags:
  - basics
  - python
  - linked-list
  - data-structures
toc: true
toc_sticky: true
---

Linked Lists are among the most common data structures used in [computer science](https://emre.me/categories/#computer-science). 

In arrays, the data is stored at contiguous memory locations but linked lists are different, they do not store data at contiguous memory locations. For each linked list node, it stores the value of the item and the reference (pointer) to the next item.

## Singly Linked Lists ##

![Singly Linked List](https://cdn.emre.me/2019-06-13-linked-list-singly.png){: .align-center}

Linked lists are dynamic data structures which means memory allocation is dynamic, reserved memory for linked list can increase or decrease at runtime and no memory is allocated in advance. Whenever a new memory space is needed for adding a new node to a linked list, the memory needed for the new node is created at runtime.

This dynamic memory allocation structure is also make easy updates possible. *Removing* and *inserting* nodes are **fast** operations in linked lists.

However, this kind of flexibility comes together with some trade-offs. Since each linked list node has to store the reference to the next node, some extra memory is required. Also, unlike arrays, where you can directly access an item with its index number, you cannot access a linked list item directly since only information you have is the first item in the linked list and references following to this first item. That is why, worst-case access time is **O(n)**.

## Doubly Linked Lists ##

[Doubly Linked Lists](#doubly-linked-lists) are actually an extension to [Singly Linked Lists](#singly-linked-lists) with some advantages. Unlike singly linked lists, doubly linked lists can be searched and traversed from both directions because each node in a doubly linked list contains both next node link and previous node link which we can call *next and *prev*.

![Doubly Linked List](https://cdn.emre.me/2019-06-13-linked-list-doubly.png){: .align-center}

Also, basic operations like insertion or deletion are easier to implement in doubly linked lists because extra traverse operations to the previous node to store its value is unnecessary since referance to previous node is already stored in the node itself. Only drawbacks we can list are you need more memory space to store previous node reference for each node and these adds a few more steps to implementation.

### Creating a Node ###

First of all, we need to define a **Node** class. I want to implement a Singly Linked List therefore, our node class will consists of two variables **val** for storing the *value* and **next** for storing the *reference to the next node*.

```python
class Node:
    def __init__(self, data):
        """
        a node in a singly linked list.
        """
        self.val = data
        self.next = None
```

Value (`val`) of the item will be set to the value passed by the constructor and the initial value of the `next` node reference will be `None` initially.

### Creating an Empty Singly Linked List ###

Lets create a singly linked list together. To be able to have a flexible implementation, I want to have `head`, `tail` and `size` attributes in my singly linked list.

```python
class LinkedList:
    def __init__(self):
        # create a new singly linked list
        # takes O(1) time
        self.head = None
        self.tail = None
        self.size = 0
```

Our empty linked list is ready. To initialize it, we need to call it like: `LinkedList()`.

### Insert a New Node at the Beginning ###

We will add a `prepend()` method to our existing singly linked list implementation which takes `data` as a parameter and adds a new node at the beginning of the linked list with this `data`.

```python
def prepend(self, data):
    # insert a new node at the beginning of the linked list
    # takes O(1) time
    if self.head is None:
        self.head = Node(data)
        self.tail = self.head
    else:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    self.size += 1
```

If our linked list is empty, `self.head` will be `None` and in this case, we are creating a new node and assign it to `self.head`. Since there is only one node in the linked list, both `head` and `tail` are equal to this node.

If there are already some nodes in the linked list and we are just adding one more at the beginning of it, then we need to create a new node. `next` attribute of this new node should refer to current `self.head`. Also new `self.head` will be this new node and old head became the second node in the linked list.

### Insert a New Node at the End ###

We need to implement an `append()` method to our existing singly linked list implementation which takes `data` as a parameter and adds a new node at the end of the linked list with this new `data`.

```python
def append(self, data):
    # inserts a new node at the end of the linked list
    # takes O(1) time
    if self.head is None:
        self.head = Node(data)
        self.tail = self.head
    else:
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
    self.size += 1
```

If our linked list is empty, `self.head` will be `None` and in this case, we are creating a new node and assign it to `self.head`. Since there is only one node in the linked list, both `head` and `tail` are equal to this node.

If there are already some nodes in the linked list and we are just adding one more at the end of it, then we need to create a new node and set this new node as `tail`.

### Accessing a Node ###

To be able to access a specific node, you need to implement a `get()` method which will get `index` parameter.

```python
def get(self, index):
    # get the value of index-th node in the linked list
    # return None if node not found
    # takes O(n) time
    if index < 0 or self.head is None or index >= self.size:
        return None
    if self.head is None:
        return None

    current = self.head
    for i in range(index):
        current = current.next
    return current.val
```

You have to visit each node one-by-one until you reach the target `index` value. This visiting process makes our time complexity **O(n)**.

### Insert a New Node at the Index ###

If we want to add our newly created node to an index, we need to create a new method `add_at_index()` which takes `index` and `data` parameters.

![Singly Linked List Insert at Index](https://cdn.emre.me/2019-06-13-linked-list-insert-at-index.png){: .align-center}

```python
def add_at_index(self, index, data):
    # insert a new node at the index-th node of the linked list
    # takes O(n) time
    if index < 0 or index > self.size:
        return print(f"index {index} is out of boundaries")
    elif index == self.size:
        self.append(data)
    else:
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
    self.size += 1
```

To be able to insert a new node to an index, first you need to go to target place by visiting each node one-by-one. Then, updating `next` parameter of previous node and newly created node will be necessary.

### Delete a Node at the Index ###
Just like [Insert a New Node at the Index](#insert-a-new-node-at-the-index), to be able to delete *index-th* node, first you need to visit each node one-by-one until you reach the target node.

```python
def delete_at_index(self, index):
    # delete the index-th node of the linked list
    # takes O(n) time
    if index < 0 or index >= self.size:
        return print(f"index {index} is out of boundaries")
    elif index == 0:
        self.head = self.head.next
        if not self.head:
            self.tail = None
    else:
        current = self.head
        for i in range(index - 1):
            current = current.next
        if current.next.next is None:
            current.next = None
            self.tail = current
        else:
            current.next = current.next.next
    self.size -= 1
```

After reaching to target, all you need to do is breaking the linked list links by setting the taret node to its next node.

## Summary ##

This post was all about Linked Lists and its implementation in [Python 3](https://docs.python.org/3/whatsnew/3.7.html).

Linked Lists are one of the most common data structures in Computer Science and has some great advantages with **O(1)** `prepend()` / `append()` (to the beginning and end of the list). But directly accessing a node `get()` or deleting a node `delete-at-index()` is taking **O(n)** time.