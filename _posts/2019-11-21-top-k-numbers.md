---
title: "Coding Patterns: Top K Numbers"
header:
  image: https://cdn.emre.me/2019-11-21-top-k-numbers-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/52p1K0d0euM)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/) and [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/) patterns and today, we will introduce [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers) pattern which is very useful to solve the problems that asks us to find the *top* / *smallest* / *frequent* **K** elements among a given set.

We are going to use [Heap](https://emre.me/data-structures/heaps/) data structure to keep track of **K** elements.

## Problem: Binary Search ##
{% capture notice %}
[**LeetCode 215 - Kth Largest Element in an Array** [*medium*]](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Find the **k**th largest element in an unsorted array. Note that it is the **k**th largest element in the sorted order, not the **k**th distinct element.

**Example 1:**

**Input:** [3, 2, 1, 5, 6, 4] and k = 2

**Output:** 5


**Example 2:**

**Input:** [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4

**Output:** 4

**Note:**

You may assume **k** is always valid, 1 ≤ **k** ≤ array's length.

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Top K Numbers Solution ###

The best data structure to keep track of top **K** elements is [Heap](https://emre.me/data-structures/heaps/).

If we iterate through the array one element at a time and keep **k**th largest element in a [heap](https://emre.me/data-structures/heaps/) such that each time we find a *larger* number than the *smallest* number in the [heap](https://emre.me/data-structures/heaps/), we do two things:


1. Take out the **smallest** number from the heap
2. Insert the **larger** number into the heap

This will ensure that we always have top **k** largest numbers in the [heap](https://emre.me/data-structures/heaps/). We will use a [min-heap](https://emre.me/data-structures/heaps/#min_heapify-and-build_min_heap) for this; 

```python
from heapq import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for i in range(k):
            heappush(min_heap, nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
            
        return min_heap[0]
```

**Time Complexity**: **O(N log K)**.

**Space Complexity**: **O(K)**

## How to identify? ##
If the problem asking us to find the *top* / *smallest* / *frequent* **K** elements among a given set, we need to think about [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers) pattern.

While solving the problems, we are going to use [Heap](https://emre.me/data-structures/heaps/) data structure to keep track of **K** elements.

## Similar LeetCode Problems ##
* [LeetCode 973 - K Closest Points to Origin [*medium*]](https://leetcode.com/problems/k-closest-points-to-origin/)