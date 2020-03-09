---
title: "Coding Patterns: Bitwise XOR"
header:
  image: https://cdn.emre.me/2019-12-11-bitwise-xor-header-image.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/illustrations/binary-code-binary-binary-system-475664/)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/), [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers), [K-way Merge](https://emre.me/coding-patterns/k-way-merge), [0/1 Knapsack](https://emre.me/coding-patterns/knapsack) and [Topological Sort](https://emre.me/coding-patterns/topological-sort) patterns and today, we will introduce [Bitwise XOR](https://emre.me/coding-patterns/bitwise-xor) pattern which is very surprising to know the approaches that the **XOR operator (^)** enables us to solve certain problems.

If you are not familiar with **binary computation** and **bit manipulation**, I *strongly* recommend to read these *two* posts first:

1. [Binary Computation and Bitwise Operators](https://emre.me/computer-science/binary-computation-and-bitwise-operators/)
2. [Bit Manipulation Tricks](https://emre.me/computer-science/bit-manipulation-tricks/)

## Problem: Single Number ##
{% capture notice %}
[**LeetCode 136 - Single Number** [*easy*]](https://leetcode.com/problems/single-number/)

Given a non-empty array of integers, every element appears **twice** except for *one*. Find that *single one*.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**

```python
Input: [2, 2, 1]
Output: 1
```

**Example 2:**

```python
Input: [4, 1, 2, 1, 2]
Output: 4
```

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Bitwise XOR Solution ###

Recall the following two [properties of XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator):

1. It returns **0** if we take **XOR** of *two same numbers*.
2. It returns the *same number* if we **XOR** with **0**.

So we can **XOR** all the numbers in the input; duplicate numbers will *zero* out each other and we will be left with the single number.

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            num ^= i
        return num
```

**Time Complexity**: **O(N)** where **N** is the total number of elements in the input array.

**Space Complexity**: **O(1)**

## Problem: Single Number III ##
{% capture notice %}
[**LeetCode 260 - Single Number III** [*medium*]](https://leetcode.com/problems/single-number-iii/)

Given an array of numbers **nums**, in which exactly **two** elements appear *only once* and all the other elements appear *exactly twice*. Find the two elements that appear *only once*.

**Example:**

```python
Input:  [1, 2, 1, 3, 2, 5]
Output: [3, 5]
```

**Note:**

- The order of the result is not important. So in the above example, **[5, 3]** is also correct.
- Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Bitwise XOR Solution ###

Let's say `num1` and `num2` are the two single numbers. If we do [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) of all elements of the given array, we will be left with [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) of `num1` and `num2` as all other numbers will cancel each other because all of them appeared *twice*.

> Since we now have [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) of `num1` and `num2`, how can we find these two single numbers?

As we know that `num1` and `num2` are **two different numbers**, therefore, *they should have at least one bit different between them*! 

If a bit in `n1xn2` is **1**, this means that `num1` and `num2` have different bits in that place. We can take any bit which is **1** in `n1xn2` and partition all numbers in the given array into two groups based on that bit. 

One group will have all those numbers with that bit set to **0** and the other with the bit set to **1**. This will ensure that `num1` will be in one group and `num2` will be in the other. 

We can take [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) of all numbers in each group separately to get `num1` and `num2`, as all other numbers in each group will cancel each other.

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # XOR of all numbers in the given list
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num

        # rightmost bit which is 1
        rightmost_bit = 1
        while rightmost_bit & n1xn2 == 0:
            rightmost_bit = rightmost_bit << 1

        num1, num2 = 0, 0
        
        for num in nums:
            if num & rightmost_bit != 0:  # the bit is set
                num1 ^= num
            else:  # the bit is not set
                num2 ^= num

        return [num1, num2]
```

**Time Complexity**: **O(N)** where **N** is the total number of elements in the input array.

**Space Complexity**: **O(1)**

## How to identify? ##
Knowing [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) properties well opens some surprising doors in your problem solving skills. To be able to identify [XOR](https://emre.me/computer-science/binary-computation-and-bitwise-operators/#xor-operator) related problems are mostly coming from previous experiences. But if you need to eliminate the same numbers from an integer array, using [Bit Manipulation Tricks](https://emre.me/computer-science/bit-manipulation-tricks/) is extremely helpful.

## Similar LeetCode Problems ##
* [LeetCode 137 - Single Number II [*medium*]](https://leetcode.com/problems/single-number-ii/)