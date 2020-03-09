---
title: "Coding Patterns: Depth First Search (DFS)"
header:
  image: https://cdn.emre.me/2019-11-14-depth-first-search-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/KLuI1al8z9c)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/) and [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/) patterns and today, we will introduce [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/) pattern which is very useful to solve the problems involving traversal of a tree.

We will be using recursion (or we can also use a [Stack](https://emre.me/data-structures/stacks-and-queues/#stacks) for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be **O(H)**, where **H** is the *maximum height* of the tree.

## Problem: Path Sum ##
{% capture notice %}
[**LeetCode 112 - Path Sum** [*easy*]](https://leetcode.com/problems/path-sum/)

Given a binary tree and a sum, determine if the tree has a *root-to-leaf* path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and sum = 22,

```python
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return `true`, as there exist a *root-to-leaf* path 5 -> 4 -> 11 -> 2 which sum is **22**.

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Depth First Search Solution ###

As we are trying to search for a **root-to-leaf** path, we can use the [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/) technique to solve this problem.

To recursively traverse a binary tree in a DFS fashion, we can start from the `root` and at every step, make two recursive calls one for the `root.left` and one for the `root.right` child by subtracting the value of the current node from the given number: `sum - root.val`.

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.val == sum and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```
**Time Complexity**: **O(N)** where **`N`** is the total number of nodes in the [tree](https://emre.me/data-structures/binary-tree/).

**Space Complexity**: **O(N)**, this space will be used to store the recursion stack. The worst case will happen when the given tree is a [linked list](https://emre.me/data-structures/linked-lists/) (i.e. *every* node has only *one* child)

## How to identify? ##

This approach is quite useful when dealing with the problems involving traversal of a tree.

When the problem asks the traversal of a tree, you should think about [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/) pattern and using it in combination with a recursive approach.

## Similar LeetCode Problems ##
* [LeetCode 110 - Balanced Binary Tree [*easy*]](https://leetcode.com/problems/balanced-binary-tree/)
* [LeetCode 113 - Path Sum II [*medium*]](https://leetcode.com/problems/path-sum-ii/)
* [LeetCode 129 - Sum Root to Leaf Numbers [*medium*]](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
* [LeetCode 200 - Number of Islands [*medium*]](https://leetcode.com/problems/number-of-islands/)
* [LeetCode 257 - Binary Tree Paths [*easy*]](https://leetcode.com/problems/binary-tree-paths/)
* [LeetCode 437 - Path Sum III [*easy*]](https://leetcode.com/problems/path-sum-iii/)