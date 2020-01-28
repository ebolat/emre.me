---
title: "Coding Patterns: Longest Common Substring/Subsequence (DP)"
header:
  image: https://cdn.emre.me/2020-01-27-longest-common-substring-subsequence-header-image.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/photos/flight-seagull-sequence-bird-1179587/)"
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

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/), [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers), [K-way Merge](https://emre.me/coding-patterns/k-way-merge), [0/1 Knapsack](https://emre.me/coding-patterns/knapsack), [Topological Sort](https://emre.me/coding-patterns/topological-sort), [Bitwise XOR](https://emre.me/coding-patterns/bitwise-xor), [Staircase](https://emre.me/coding-patterns/staircase) and [Palindromes](https://emre.me/coding-patterns/palindromes) patterns and today, we will introduce [Longest Common Substring / Subsequence](https://emre.me/coding-patterns/longest-common-substring-subsequence) pattern which is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving *longest* / *shortest* *common* *strings*, *substrings*, *subsequences* etc.

If you need to refresh your knowledge of [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/), you may want to check it before diving into more advanced problems.

## Problem: Longest Common Subsequence ##
{% capture notice %}
[**LeetCode 1143 - Longest Common Subsequence** [*medium*]](https://leetcode.com/problems/longest-common-subsequence/)

Given two strings `text1` and `text2`, return the length of their *longest common subsequence*.

A common subsequence of two strings is a subsequence that is common to both strings. If there is no common subsequence, return 0.

**Example 1:**

**Input:** text1 = "abcde", text2 = "ace" 

**Output:** 3  

**Explanation:** The longest common subsequence is "ace" and its length is 3.

**Example 2:**

**Input:** text1 = "abc", text2 = "abc"

**Output:** 3

**Explanation:** The longest common subsequence is "abc" and its length is 3.

**Example 3:**

**Input:** text1 = "abc", text2 = "def"

**Output:** 0

**Explanation:** There is no such common subsequence, so the result is 0.
 
**Constraints:**

1 <= text1.length <= 1000

1 <= text2.length <= 1000

The input strings consist of lowercase English characters only.

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Brute Force Solution ###

> A [subsequence](https://en.wikipedia.org/wiki/Subsequence) of a string is a *new* string generated from the *original* string with some characters (can be none) deleted without changing the relative order of the remaining characters. (eg, *"ace"* is a subsequence of *"abcde"* while *"aec"* is **not**).

As a **brute force** solution, we can try all subsequences of `text1` and `text2` to find the longest one.

* if the characters `text1[i]` matches `text2[j]`, we can recursively match the others.
* if the characters `text1[i]` and `text2[j]` does **not** match, we will make two recursive calls by skipping one character from each string.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequence_recursive(text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.longestCommonSubsequence_recursive(text1, text2, i + 1, j + 1)

        return max(self.longestCommonSubsequence_recursive(text1, text2, i + 1, j),
                   self.longestCommonSubsequence_recursive(text1, text2, i, j + 1))
```
**Time Complexity**: **O(2<sup>N+M</sup>)** where **N** and **M** are the lengths of two input strings.

**Space Complexity**: **O(N + M)** which is used to store the recursion stack.

### Top-down Dynamic Programming with Memoization ###

We can use a two-dimensional array to store the already solved subproblems.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.longestCommonSubsequence_recursive(memo, text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, memo, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j] == -1:
            if text1[i] == text2[j]:
                memo[i][j] = 1 + self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j + 1)
            else:
                memo[i][j] = max(self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j),
                                 self.longestCommonSubsequence_recursive(memo, text1, text2, i, j + 1))
        return memo[i][j]
```
**Time Complexity**: **O(N * M)** where **N** and **M** are the lengths of two input strings.

**Space Complexity**: **O(N * M)**

### Bottom-up Dynamic Programming with Tabulation ###

Lets create our two dimensional array in a bottom-up fashion.

* if the characters `text1[i]` matches `text2[j]`, the length of the common subsequence would be one plus the length of the common subsequence until the `i-1` and `j-1` indexes.
* if the characters `text1[i]` and `text2[j]` does **not** match, we take the longest sequence by skipping one character either from **i<sup>th</sup>** string or **j<sup>th</sup>** character from respective strings.

Our overall algorithm is;

```python
if text1[i] == text2[j]:
    memo[i][j] = 1 + memo[i - 1][j - 1]
else:
    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
```

and the solution is;

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        max_length = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

                max_length = max(max_length, memo[i][j])
        return max_length
```
**Time Complexity**: **O(N * M)** where **N** and **M** are the lengths of two input strings.

**Space Complexity**: **O(N * M)**

## How to identify? ##

[Longest Common Substring / Subsequence](https://emre.me/coding-patterns/longest-common-substring-subsequence) pattern is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving *longest* / *shortest* *common* *strings*, *substrings*, *subsequences* etc.

## Similar LeetCode Problems ##
* [LeetCode 72 - Edit Distance [*hard*]](https://leetcode.com/problems/edit-distance/)
* [LeetCode 97 - Interleaving String [*hard*]](https://leetcode.com/problems/interleaving-string/)
* [LeetCode 300 - Longest Increasing Subsequence [*medium*]](https://leetcode.com/problems/longest-increasing-subsequence/)
* [LeetCode 1092 - Shortest Common Supersequence [*hard*]](https://leetcode.com/problems/shortest-common-supersequence/)

