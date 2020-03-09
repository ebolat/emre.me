---
title: "Coding Patterns: Fast & Slow Pointers"
header:
  image: https://cdn.emre.me/2019-10-23-fast-slow-pointers-header-image.jpg
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/) and [Two Pointers](https://emre.me/coding-patterns/two-pointers/) patterns and today, we will introduce [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/) pattern (a.k.a. [Floyd's Tortoise and Hare Algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)) which is very useful when dealing with cyclic [Linked Lists](https://emre.me/data-structures/linked-lists/) or [Arrays](https://emre.me/data-structures/lists/).

By moving at different speeds, the algorithm proves that the two pointers are going to meet eventually. The *fast* pointer should catch the *slow* pointer once both the pointers are in a **cyclic loop**.

## Problem: Linked List Cycle ##
{% capture notice %}
[**LeetCode 141 - Linked List Cycle** [*easy*]](https://leetcode.com/problems/linked-list-cycle/)

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is **-1**, then there is no cycle in the linked list.

**Example 1:**

```python
Input: head = [3, 2, 0, -4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![Circular Linked List - Test 1](https://cdn.emre.me/2019-10-23-circularlinkedlist-test1.png){: .align-center}

**Example 2:**

```python
Input: head = [1, 2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![Circular Linked List - Test 2](https://cdn.emre.me/2019-10-23-circularlinkedlist-test2.png){: .align-center}

**Example 3:**

```python
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![Circular Linked List - Test 3](https://cdn.emre.me/2019-10-23-circularlinkedlist-test3.png){: .align-center}

**Follow up:**

Can you solve it using **O(1)** (i.e. constant) memory?
{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Fast & Slow Pointers Solution ###

If you need to refresh your knowledge in [Linked Lists](https://emre.me/data-structures/linked-lists/), I would suggest to do so before jumping into the solution.

Imagine two racers running in a **circular** racing track. If one racer is *faster* than the other, the *faster* racer is bound to catch up and cross the *slower* racer from behind. In each iteration, **Tortoise** :turtle: (*slow* pointer) moves *one* step and the **Hare** :rabbit2: (*fast* pointer) moves *two* steps.

* If the [Linked Lists](https://emre.me/data-structures/linked-lists/) does not have a cycle in it, **Hare** :rabbit2: will reach the end of the [Linked Lists](https://emre.me/data-structures/linked-lists/) before the **Tortoise** :turtle: and this will reveal that there is **no** cycle in the [Linked Lists](https://emre.me/data-structures/linked-lists/).
* The **Tortoise** :turtle: will never be catch up the **Hare** :rabbit2: if there is **no** cycle in the [Linked Lists](https://emre.me/data-structures/linked-lists/).

If at any stage the **Tortoise** :turtle: (*slow* pointer) meet with the **Hare** :rabbit2: (*fast* pointer), we can conclude that the [Linked Lists](https://emre.me/data-structures/linked-lists/) is **cyclic**. Here is the proof:

* If the **Hare** :rabbit2: (*fast* pointer) is *one step behind* the **Tortoise** :turtle: (*slow* pointer): The **fast** pointer moves *two steps* and the **slow** pointer moves *one step*, and **they both meet**.
* If the **Hare** :rabbit2: (*fast* pointer) is *two steps behind* the **Tortoise** :turtle: (*slow* pointer): The **fast** pointer moves *two steps* and the **slow** pointer moves *one step*. After the moves, the **fast** pointer will be *one step behind* the **slow** pointer, which reduces this scenario to the first scenario. This means that the two pointers *will meet in the next iteration*.

![The Tortoise and the Hare](https://cdn.emre.me/2019-10-23-tortoise-and-hare.gif){: .align-center}

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True  # found the cycle
        return False
```
**Time Complexity**: **O(N)** where **`N`** is the number of *nodes* in the [Linked Lists](https://emre.me/data-structures/linked-lists/).

**Space Complexity**: **O(1)**, algorithm runs in constant space.

## Problem: Linked List Cycle II ##
{% capture notice %}
[**LeetCode 142 - Linked List Cycle II** [*medium*]](https://leetcode.com/problems/linked-list-cycle-ii/)

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is **-1**, then there is no cycle in the linked list.

Note: Do not modify the linked list.

**Example 1:**

```python
Input: head = [3, 2, 0, -4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![Circular Linked List - Test 1](https://cdn.emre.me/2019-10-23-circularlinkedlist-test1.png){: .align-center}

**Example 2:**

```python
Input: head = [1, 2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![Circular Linked List - Test 2](https://cdn.emre.me/2019-10-23-circularlinkedlist-test2.png){: .align-center}

**Example 3:**

```python
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

![Circular Linked List - Test 3](https://cdn.emre.me/2019-10-23-circularlinkedlist-test3.png){: .align-center}

**Follow up:**

Can you solve it without using extra space?
{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Fast & Slow Pointers Solution ###

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                current = head
                while current is not slow:
                    current = current.next
                    slow = slow.next
                return slow
        return None
```
**Time Complexity**: **O(N)** where **`N`** is the number of *nodes* in the [Linked Lists](https://emre.me/data-structures/linked-lists/).

**Space Complexity**: **O(1)**, algorithm runs in constant space.

As you can see, only difference between two problems is the part:

```python
if slow == fast:
    current = head
    while current is not slow:
        current = current.next
        slow = slow.next
    return slow
```

Let's try to understand it with a diagram:

![Calculate Entry Point](https://cdn.emre.me/2019-10-23-fast-slow-pointers-cyclic-entry-point.png){: .align-center}

When the **Hare** :rabbit2: (*fast* pointer) and the **Tortoise** :turtle: (*slow* pointer) meet at point **-4**, the length they have run are `A+2B+C` (for **Hare**) and `A+B` (for **Tortoise**).

Since the *fast* pointer is **2 times** *faster* than the *slow* pointer, `A+2B+C == 2(A+B)`, then we get `A==C`.

So, when another pointer (`current`) run from `head` to **2** (distance `A`), at the same time, previous `slow` pointer will run from **-4** to **2** (distance `C`), so they meet at the pointer **2** together, which is **the point where cycle begins** as problem asked.

## How to identify? ##

This approach is quite useful when dealing with **cyclic** [Linked Lists](https://emre.me/data-structures/linked-lists/) or [Arrays](https://emre.me/data-structures/lists/).

When the problem involves something related to **cyclic** data structures, you should think about [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/) pattern.

## Similar LeetCode Problems ##
* [LeetCode 202 - Happy Number [*easy*]](https://leetcode.com/problems/happy-number/)
* [LeetCode 876 - Middle of the Linked List [*easy*]](https://leetcode.com/problems/middle-of-the-linked-list/)