---
title: "Coding Patterns: Modified Binary Search"
header:
  image: https://cdn.emre.me/2019-11-20-modified-binary-search-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/4rDCa5hBlCs)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/) and [Subsets](https://emre.me/coding-patterns/subsets/) patterns and today, we will introduce [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/) pattern which is very useful to solve the problems whenever we are given a sorted [Array](https://emre.me/data-structures/lists/) or [Linked List](https://emre.me/data-structures/linked-lists/) or Matrix, and we are asked to find a certain element.

This pattern describes an efficient way to handle all problems involving [Binary Search](https://emre.me/data-structures/binary-search-trees/).

## Problem: Binary Search ##
{% capture notice %}
[**LeetCode 704 - Binary Search** [*easy*]](https://leetcode.com/problems/binary-search/)

Given a sorted (in ascending order) integer array `nums` of **n** elements and a `target` value, write a function to search `target` in `nums`. If `target` exists, then return its index, otherwise return **-1**.

**Example 1:**

**Input:** `nums` = [-1, 0, 3, 5, 9, 12], `target` = 9

**Output:** 4

**Explanation:** 9 exists in `nums` and its index is 4

**Example 2:**

**Input:** `nums` = [-1, 0, 3, 5, 9, 12], `target` = 2

**Output:** -1

**Explanation:** 2 does not exist in nums so return -1
 
**Note:**

You may assume that all elements in `nums` are unique.

**n** will be in the range [1, 10000].

The value of each element in `nums` will be in the range [-9999, 9999].

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Binary Search Solution ###

**1-** Let's assume that `start` is the first element and `end` is the last element in `nums`.

```python
start = 0
end = len(nums) - 1
```

**2-** We need to find middle value, `mid`. An easy way to do it in [Python](https://www.python.org/) is

```python
mid = (start + end) // 2
```

For [Java](https://www.java.com/) and [C++](https://isocpp.org/), this equation will work for most cases, but when `start` or `end` is *large*, this equation will give us the wrong result due to *integer overflow*. To solve this problem, we will do our calculation a bit differently;

```java
int mid = start + (end - start) / 2;
```

**3-** Next, we will see if the `target` value is equal to the number at `mid` value. If it is equal we return `mid` as the required index.

**4-** If `target` is not equal to number at index `mid`, there are two possibilities that we need to check:


- If `target < nums[mid]`, then we can conclude that `target` will be **smaller** than all the numbers after index `mid` as the array is sorted in the ascending order. We can reduce our search to `end = mid - 1`.


- If `target > nums[mid]`, then we can conclude that `target` will be **greater** than all numbers before index `mid` as the array is sorted in the ascending order. We can reduce our search to `start = mid + 1`.

![Binary Search](https://cdn.emre.me/2019-08-08-binary-search.png){: .align-center}

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
```

**Time Complexity**: **O(log N)** where **N** is the total elements in the given array.

**Space Complexity**: **O(1)**

## How to identify? ##

This approach is quite useful to solve the problems whenever we are given a sorted [Array](https://emre.me/data-structures/lists/) or [Linked List](https://emre.me/data-structures/linked-lists/) or Matrix, and we are asked to find a certain element.

This pattern describes an efficient way to handle all problems involving [Binary Search](https://emre.me/data-structures/binary-search-trees/).

## Similar LeetCode Problems ##
* [LeetCode 744 - Find Smallest Letter Greater Than Target [*easy*]](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)