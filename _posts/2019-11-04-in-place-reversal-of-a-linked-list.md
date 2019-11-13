---
title: "Coding Patterns: In-place Reversal of a Linked List"
header:
  image: https://cdn.emre.me/2019-11-04-in-place-reversal-of-a-linked-list-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/PDxYfXVlK2M)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/) and [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/) patterns and today, we will introduce [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/) pattern which is very useful to solve the problems involving reversal of a Linked List with the constraint that we need to do it **in-place** *without* using extra memory.

## Problem: Reverse Linked List ##
{% capture notice %}
[**LeetCode 206 - Reverse Linked List** [*easy*]](https://leetcode.com/problems/reverse-linked-list/)

Reverse a singly linked list.

**Example:**

**Input:** 1->2->3->4->5->NULL

**Output:** 5->4->3->2->1->NULL

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### In-Place Reversal Solution ###

We are going to reverse one node at a time. We will start with a variable `current` which will initially point to the `head` of the Linked List and a variable `previous` which will point to the *previous node* that we have processed; initially `previous` will point to `null`.

We will reverse the `current` node by pointing it to the `previous` before moving on to the next node. Also, we will update the `previous` to always point to the previous node that we have processed.

![In-Place Reversal of a Linked List](https://cdn.emre.me/2019-11-04-in-place-reversal.gif){: .align-center}

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        previous, current, next = None, head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current  # point previous to the current node
            current = next  # move on
        return previous
```
**Time Complexity**: **O(N)** where **`N`** is the number of *nodes* in the [Linked Lists](https://emre.me/data-structures/linked-lists/).

**Space Complexity**: **O(1)**, algorithm runs in constant space.

## How to identify? ##

This approach is quite useful when dealing with reversal of [Linked Lists](https://emre.me/data-structures/linked-lists/) when there is a constraint to do it *without* using extra memory.

When the problem gives this constraint and [Linked Lists](https://emre.me/data-structures/linked-lists/) data structure, you should think about [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/) pattern.

## Similar LeetCode Problems ##
* [LeetCode 92 - Reverse Linked List II [*medium*]](https://leetcode.com/problems/reverse-linked-list-ii/)

