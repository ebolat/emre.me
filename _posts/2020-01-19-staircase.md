---
title: "Coding Patterns: Staircase (DP)"
header:
  image: https://cdn.emre.me/2020-01-19-staircase-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/3OKYUJV7YTA)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
  - dynamic-programming
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/), [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers), [K-way Merge](https://emre.me/coding-patterns/k-way-merge), [0/1 Knapsack](https://emre.me/coding-patterns/knapsack), [Topological Sort](https://emre.me/coding-patterns/topological-sort) and [Bitwise XOR](https://emre.me/coding-patterns/bitwise-xor) patterns and today, we will introduce [Staircase](https://emre.me/coding-patterns/staircase) pattern which is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving minimum / maximum steps, jumps, stairs, fibonacci numbers etc. to reach a target.

If you need to refresh your knowledge of [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/), you may want to check the [Fibonacci Number Problem](https://emre.me/algorithms/dynamic-programming/#memoization) before diving into more advanced problems.

## Problem: Climbing Stairs ##
{% capture notice %}
[**LeetCode 70 - Climbing Stairs** [*easy*]](https://leetcode.com/problems/climbing-stairs/)

You are climbing a stair case. It takes **n** steps to reach to the top.
Each time you can either climb **1** or **2** steps. In how many *distinct* ways can you climb to the top?

**Note:**

Given n will be a positive integer.

**Example 1:**

**Input:** 2

**Output:** 2

**Explanation:** There are two ways to climb to the top.

* **1** step + **1** step
* **2** steps

**Example 2:**

**Input:** 3

**Output:** 3

**Explanation:** There are three ways to climb to the top.

* **1** step + **1** step + **1** step
* **1** step + **2** steps
* **2** steps + **1** step

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Brute Force Solution ###

At every step, we have two options: either climb **1** step or **2** steps.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # we don't take any steps, so there is only 1 way
        if n == 0:
            return 0
        # we can take one step to reach the end, and this is the only way
        if n == 1:
            return 1
        # we can take one step twice or take two steps to reach the end
        if n == 2:
            return 2

        # if we take one step, we are left with "n - 1" steps
        take1step = self.climbStairs(n - 1)
        # if we take two steps, we are left with "n - 2" steps
        take2steps = self.climbStairs(n - 2)

        return take1step + take2steps
```

**Time Complexity**: **O(2<sup>N</sup>)** because we are making **2** recursive calls in the same function.

**Space Complexity**: **O(N)** which is used to store the recursion stack.

But can we do better? To be able to understand this, lets visualize the recursion stack.

![Climbing Stairs](https://cdn.emre.me/2020-01-19-staircase.png)

We can clearly see from colors that there are lots of *overlapping sub-problems* that we don't need to calculate them again and again.

### Top-down Dynamic Programming with Memoization ###

We can use an array to store already solved sub-problems.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        return self.climbStairs_recursive(dp, n)
    
    def climbStairs_recursive(self, dp, n):
        # we don't take any steps, so there is only 1 way
        if n == 0:
            return 0
        # we can take one step to reach the end, and this is the only way
        if n == 1:
            return 1
        # we can take one step twice or take two steps to reach the end
        if n == 2:
            return 2
        
        if dp[n] == 0:
            # if we take one step, we are left with "n - 1" steps
            take1step = self.climbStairs_recursive(dp, n - 1)
            # if we take two steps, we are left with "n - 2" steps
            take2steps = self.climbStairs_recursive(dp, n - 2)
            
            dp[n] = take1step + take2steps
            
        return dp[n]
```

**Time Complexity**: **O(N)** because [memoization](https://emre.me/algorithms/dynamic-programming/#memoization) array `dp[n+1]` stores the results of **all** *sub-problems*. We can conclude that we will not have more than `n + 1` *sub-problems*.

**Space Complexity**: **O(N)** which is used to store the recursion stack.

### Bottom-up Dynamic Programming with Tabulation ###

Let's try to populate our `dp[]` array in a bottom-up fashion. As we see from the recursion stack visualization, each `climbStairs(n)` call is the sum of the **two** previous calls.

We can use this fact while populating our `dp[]` array.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
```
**Time Complexity**: **O(N)**

**Space Complexity**: **O(N)** which is used to store the recursion stack.

### Memory Optimization ###

As we can see from the visualization of the recursive stack and other solutions, to be able to calculate the **n**, you need the value of last two combinations: **n-1** and **n-2**.

These two values are enough and we don't need to store all other past combinations.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1  # how many step possibilities there are with 1 stairs
        second = 2  # how many step possibilities there are with 2 stairs
        third = 0

        for _ in range(2, n):
            third = first + second
            first = second  # walk up first to second
            second = third  # walk up second to third
        return third
```

OR more shortly;

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
```

**Time Complexity**: **O(N)**

**Space Complexity**: **O(1)**

## How to identify? ##

[Staircase](https://emre.me/coding-patterns/staircase) pattern is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving minimum / maximum steps, jumps, stairs, fibonacci numbers etc. to reach a target.

## Similar LeetCode Problems ##
* [LeetCode 62 - Unique Paths [*medium*]](https://leetcode.com/problems/unique-paths/)
* [LeetCode 91 - Decode Ways [*medium*]](https://leetcode.com/problems/decode-ways/)
* [LeetCode 509 - Fibonacci Number [*easy*]](https://leetcode.com/problems/fibonacci-number/)