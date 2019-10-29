---
title: "Coding Patterns: Merge Intervals"
header:
  image: https://cdn.emre.me/2019-10-27-merge-intervals-header-image.jpg
  caption: "Photo credit: [**Pexels**](https://www.pexels.com/photo/multi-colored-building-2443590/)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/) and [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/) patterns and today, we will introduce [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/) pattern which is very useful to solve the problems involve intervals, overlapping items that need to be merged etc.

## Problem: Merge Intervals ##
{% capture notice %}
[**LeetCode 56 - Merge Intervals** [*medium*]](https://leetcode.com/problems/merge-intervals/)

Given a collection of intervals, merge all *overlapping* intervals.

**Example 1:**

**Input:** [[1,3],[2,6],[8,10],[15,18]]

**Output:** [[1,6],[8,10],[15,18]]

**Explanation:** Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

**Example 2:**

**Input:** [[1,4],[4,5]]

**Output:** [[1,5]]

**Explanation:** Intervals [1,4] and [4,5] are considered overlapping.
{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Merge Intervals Solution ###

Given two intervals **A** and **B**, there will be **six** different ways the two intervals can relate to each other:

![Merge Intervals](https://cdn.emre.me/2019-10-27-merge-intervals.png){: .align-center}

If `a.start <= b.start`, only **1**, **2** and **3** are possible from the above scenarios.

Our goal is to merge the intervals whenever they overlap. For the *two* overlapping scenarios **2** and **3**, this is how we will merge them:

![Merging Example](https://cdn.emre.me/2019-10-27-merging-example.png){: .align-center}

We are going to merge them into a new interval **`c`** such that;

```python
c.start = a.start
c.end = max(a.end, b.end)
```
Here is what our code will look like:

```python
class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:  # overlapping intervals
                end = max(interval[1], end)
            else:  # non-overlapping interval, add the previous interval and reset
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
            
        merged.append([start, end])  # add the last interval
        return merged
```
## How to identify? ##

This approach is quite useful when dealing with *intervals*, *overlapping items* or *merging intervals*.

When the problem involves these clue words, you should think about [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/) pattern.

## Similar LeetCode Problems ##
* [LeetCode 57 - Insert Interval [*hard*]](https://leetcode.com/problems/insert-interval/)
* [LeetCode 986 - Interval List Intersections [*medium*]](https://leetcode.com/problems/interval-list-intersections/)



