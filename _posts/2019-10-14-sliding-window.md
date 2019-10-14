---
title: "Coding Patterns: Sliding Window"
header:
  image: https://cdn.emre.me/2019-10-14-sliding-window-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/tGm0O_ePW6w)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

First, we will introduce [Sliding Window](https://emre.me/coding-patterns/sliding-window/) pattern which is very useful to solve problems in which you are asked to find the *longest/shortest string*, *subarray*, or a *desired value* which you need to calculate from subarrays.

## Problem: Maximum Average Subarray ##

{% capture notice--primary %}
**LeetCode 643 - Maximum Average Subarray I** ([link](https://leetcode.com/problems/maximum-average-subarray-i/))

Given an array consisting of **`n`** integers, find the *contiguous subarray* of given length **`k`** that has the maximum average value. And you need to output the *maximum average value*.

**Example:**

**Input:** [1, 12, -5, -6, 50, 3], k = 4

**Output:** 12.75

**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

{% endcapture %}

<div class="notice--primary">
  {{ notice--primary | markdownify }}
</div>

### Brute Force Solution ###

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = 0.0

        for i in range(len(nums) - k + 1):
            _sum = 0.0  # find sum of next k elements

            for j in range(i, i + k):
                _sum += nums[j]

            average = _sum / k  # calculate the average of selected k elements
            max_average = max(max_average, average)  # update max_average

            if len(nums) == 1:  # if there is only 1 element in nums
                return average

        return max_average
```

**Time Complexity**: **O(N*k)** where **`N`** is the number of elements in the input array. 

This solution exceeds the time limit defined by [Leetcode](https://leetcode.com/) and is **not accepted**.

If we check our example array again: `[1, 12, -5, -6, 50, 3]` for `k = 4`, there are 3 *overlapping* elements between subarrays `[1, 12, -5, -6]` and `[12, -5, -6, 50]`. Can we somehow reuse the `_sum` we have calculated for the *overlapping* elements to make our solution more efficient?

### Sliding Window Solution ###

![Sliding Window](https://cdn.emre.me/2019-10-14-sliding-window.png){: .align-center}

To be able to reuse the `_sum` from the previous *subarray*, we will **subtract** the element *going out* of the window and *add* the element now being **included** in the sliding window.

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = []
        _sum, start = 0, 0
        for end in range(len(nums)):
            _sum += nums[end]  # add the next element

            if end >= k - 1:
                average.append(_sum / k)  # calculate the average
                _sum -= nums[start]  # subtract the element going out
                start += 1  # slide the window

        return max(average)
```

**Time Complexity**: **O(N)** where **`N`** is the number of elements in the input array.

## How to identify? ##
So we want to be able to identify the problems that [sliding window](https://emre.me/coding-patterns/sliding-window/) pattern works.

* The problem involves a data structure that is ordered and iterable like *arrays*, *strings*, etc.
* The problem is asking to find a subrange in an *array*/*string*, contiguous *longest*, *shortest*, *average* or *target* value.
* There is an apparent *naive* or [brute force](#brute-force-solution) solution that runs in **O(N<sup>2</sup>)**, **O(2<sup>N</sup>)** or some other large time complexity.

The amazing thing about [sliding window](https://emre.me/coding-patterns/sliding-window/) problems is that most of the time they can be solved in **O(N)** time and **O(1)** space complexity.

## Similar LeetCode Problems ##

A list of similar problems is going to be updated...