---
title: "Coding Patterns: Two Pointers"
header:
  image: https://cdn.emre.me/2019-10-21-two-pointers-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/YEWvMidcKkg)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous post was about [Sliding Window](https://emre.me/coding-patterns/sliding-window/) pattern and today, we will introduce [Two Pointers](https://emre.me/coding-patterns/two-pointers/) pattern which is very useful to solve problems with [sorted](https://emre.me/algorithms/sorting-algorithms/) [arrays](https://emre.me/data-structures/lists/) (or [Linked Lists](https://emre.me/data-structures/linked-lists/)) which involve a set of pair elements, or a triplet or even a subarray.

## Problem: Pair with Target Sum ##
{% capture notice %}
[**LeetCode 1 - Two Sum** [*easy*]](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the **two** numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**

**Given nums** = [2, 7, 11, 15], **target** = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return **[0, 1]**.
{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Two Pointers Solution ###
With using the [Two Pointers](https://emre.me/coding-patterns/two-pointers/) pattern, and *Pointer 1* pointing to the beginning of the array and *Pointer 2* pointing to the end of the array, we will check if the numbers pointed by the pointers add up to the target sum. If they do, we have found our pair. If not, we should do one of these things:

* If the sum is *bigger* than the target sum, this means that we need a *smaller* sum so, we are going to *decrement* the *Pointer 2* (end-pointer).
* If the sum is *smaller* than the target sum, this means that we need a *bigger* sum so, we are going to *increment* the *Pointer 1* (start-pointer).

![Two Pointers](https://cdn.emre.me/2019-10-21-two-pointers.png){: .align-center}

Please note that, this solution only works if we are working with **sorted arrays**!
 
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]

        if target > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]
```

**Time Complexity**: **O(N)** where **`N`** is the number of elements in the input array (**`nums`**).

**Space Complexity**: **O(1)**, algorithm runs in constant space.

### An Alternative Solution ###
Instead of using the [Two Pointers Solution](#two-pointers-solution), we can use a [HashTable](https://emre.me/data-structures/hash-tables/) to solve the problem.

We are searching the array for **2** items, **`x`** and **`y`** where **`x + y = target`**. This means that, during our iteration when we are at number **`x`**, we are looking for a **`y`** (which is equivalent to **`target - x`**, basic maths!).

If we found a **`target - x`** value in **HashTable**, we found our pair! If not, we will insert **`x`** into the **HashTable**, so that we can search for it later.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}  # to store numbers and their indices
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        else:
            numlist[nums[i]] = i
    return [-1, -1]
```

**Time Complexity**: **O(N)** where **`N`** is the number of elements in the input array (**`nums`**).

**Space Complexity**: **O(N)**, in the worst case, we will be pushing **N** numbers to **HashMap**.

## How to identify? ##
So we want to be able to identify the problems that [Two Pointers](https://emre.me/coding-patterns/two-pointers/) pattern works.

* The problem involve [sorted](https://emre.me/algorithms/sorting-algorithms/) [arrays](https://emre.me/data-structures/lists/) (or [Linked Lists](https://emre.me/data-structures/linked-lists/)), a set of pair elements, or a triplet or even a subarray.
* There is a *target* value to match or duplicates to be *removed*.

Most of these type of problems can be solved in **O(N)** *time complexity* and **O(1)** or **O(N)** *space complexity*.

## Similar LeetCode Problems ##
* [LeetCode 15 - 3Sum [*medium*]](https://leetcode.com/problems/3sum/)
* [LeetCode 16 - 3Sum Closest [*medium*]](https://leetcode.com/problems/3sum-closest/)
* [LeetCode 26 - Remove Duplicates from Sorted Array [*easy*]](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
* [LeetCode 27 - Remove Element [*easy*]](https://leetcode.com/problems/remove-element/)
* [LeetCode 259 - 3Sum Smaller [*medium*] [*premium*]](https://leetcode.com/problems/3sum-smaller)
* [LeetCode 713 - Subarray Product Less Than K [*medium*]](https://leetcode.com/problems/subarray-product-less-than-k/)
* [LeetCode 977 - Squares of a Sorted Array [*easy*]](https://leetcode.com/problems/squares-of-a-sorted-array/)