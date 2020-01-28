---
title: "Coding Patterns: Palindromes (DP)"
header:
  image: https://cdn.emre.me/2020-01-22-palindromes-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/vgrIBxpKhwk)"
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

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/), [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers), [K-way Merge](https://emre.me/coding-patterns/k-way-merge), [0/1 Knapsack](https://emre.me/coding-patterns/knapsack), [Topological Sort](https://emre.me/coding-patterns/topological-sort), [Bitwise XOR](https://emre.me/coding-patterns/bitwise-xor) and [Staircase](https://emre.me/coding-patterns/staircase) patterns and today, we will introduce [Palindromes](https://emre.me/coding-patterns/palindromes) pattern which is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving **palindromes** and **palindromic** *strings*, *substrings*, *subsequences* etc.

If you need to refresh your knowledge of [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/), you may want to check it before diving into more advanced problems.

## Problem: Longest Palindromic Subsequence ##
{% capture notice %}
[**LeetCode 516 - Longest Palindromic Subsequence** [*medium*]](https://leetcode.com/problems/longest-palindromic-subsequence/)

Given a string **s**, find the longest [palindromic](https://en.wikipedia.org/wiki/Palindrome) subsequence's length in **s**. You may assume that the *maximum length* of **s** is **1000**.

**Example 1:**

**Input:** "bbbab"

**Output:** 4

One possible longest palindromic subsequence is "bbbb".

**Example 2:**

**Input:** "cbbd"

**Output:** 2

One possible longest palindromic subsequence is "bb".

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Brute Force Solution ###

> A **palindrome** is a *word*, *number*, *phrase*, or other sequence of characters which **reads the same backward as forward**, such as *madam*, *racecar*, or the number *10801*. 
> 
> Sentence-length palindromes may be written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as "*A man, a plan, a canal, Panama!*", "*Was it a car or a cat I saw?*" etc.[<sup>1</sup>](#references)

As a **brute force** solution, we can try all *subsequences* of the given *sequence*. Starting from the beginning and the end of the sequence;
* if the elements at the beginning and the end are the same, we can increment the counter by **2** and make a recursive call to remaining subsequences
* we will skip one element either from the beginning or from the end o make two recursive calls for the remaining subsequence

If the **first option** applies then it will give us the length of *Longest Palindromic Substring (**LPS**)*. 

Otherwise, the length of *Longest Palindromic Substring (**LPS**)* will be the maximum number returned by the *two* recursive calls from **the second option**.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseq_recursive(s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        # case 1: elements at the beginning and the end are the same
        if s[start] == s[end]:
            return 2 + self.longestPalindromeSubseq_recursive(s, start + 1, end - 1)

        # case 2: skip one element either from the beginning or the end
        subseq1 = self.longestPalindromeSubseq_recursive(s, start + 1, end)
        subseq2 = self.longestPalindromeSubseq_recursive(s, start, end - 1)

        return max(subseq1, subseq2)
```

**Time Complexity**: **O(2<sup>N</sup>)** because we are making **2** recursive calls in the same function.

**Space Complexity**: **O(N)** which is used to store the recursion stack.

### Top-down Dynamic Programming with Memoization ###

`start` and `end` are two changing values of our recursive function in the [Brute Force Solution](#brute-force-solution). So, we can store the results of all subsequences in a two-dimensional array to *memoize* them.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.longestPalindromeSubseq_recursive(memo, s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, memo, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        if memo[start][end] == -1:
            # case 1: elements at the beginning and the end are the same
            if s[start] == s[end]:
                memo[start][end] = 2 + self.longestPalindromeSubseq_recursive(memo, s, start + 1, end - 1)
            else:
                # case 2: skip one element either from the beginning or the end
                subseq1 = self.longestPalindromeSubseq_recursive(memo, s, start + 1, end)
                subseq2 = self.longestPalindromeSubseq_recursive(memo, s, start, end - 1)
                memo[start][end] = max(subseq1, subseq2)

        return memo[start][end]
```

**Time Complexity**: **O(N<sup>2</sup>)** because [memoization](https://emre.me/algorithms/dynamic-programming/#memoization) array, `memo[len(s)][len(s)]`. We will not have more than **N*N** subsequences.

**Space Complexity**: **O(N<sup>2</sup> + N)** == **O(N<sup>2</sup>)** because we used **N<sup>2</sup>** for [memoization](https://emre.me/algorithms/dynamic-programming/#memoization) array and **N** for recursive stack.

### Bottom-up Dynamic Programming with Tabulation ###

We can build our two-dimensional [memoization](https://emre.me/algorithms/dynamic-programming/#memoization) array in a bottom-up fashion, adding one element at a time.

* if the element at the `start` and the `end` is matching, the length of *Longest Palindromic Substring (**LPS**)* is 2 plus the length of **LPS** till `start+1` and `end-1`.
* if the element at the `start` does **not** match the element at the `end`, we will take the `max` of **LPS** by either skipping the element at `start` or `end`

So the overall algorith will be;

```python
if s[start] == s[end]:
    memo[start][end] = 2 + memo[start + 1][end - 1]
else:
    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])
```

and the solution;

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # every sequence with one element is a palindrome of length 1
        for i in range(len(s)):
            memo[i][i] = 1

        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                # case 1: elements at the beginning and the end are the same
                if s[start] == s[end]:
                    memo[start][end] = 2 + memo[start + 1][end - 1]
                else:  # case 2: skip one element either from the beginning or the end
                    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])

        return memo[0][len(s) - 1]
```

**Time Complexity**: **O(N<sup>2</sup>)**

**Space Complexity**: **O(N<sup>2</sup>)** where **N** is the input sequence.

## How to identify? ##

[Palindromes](https://emre.me/coding-patterns/palindromes) pattern is very useful to solve [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) problems involving **palindromes** and **palindromic** *strings*, *substrings*, *subsequences* etc.

## Similar LeetCode Problems ##
* [LeetCode 5 - Longest Palindromic Substring [*medium*]](https://leetcode.com/problems/longest-palindromic-substring/)
* [LeetCode 131 - Palindrome Partitioning [*medium*]](https://leetcode.com/problems/palindrome-partitioning/)
* [LeetCode 647 - Palindromic Substrings [*medium*]](https://leetcode.com/problems/palindromic-substrings/)
* [LeetCode 1216 - Valid Palindrome III [*hard*] [*premium*]](https://leetcode.com/problems/valid-palindrome-iii/)

## References ##
1. Wikipedia, *[Palindrome](https://en.wikipedia.org/wiki/Palindrome)* 