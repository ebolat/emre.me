---
title: "Coding Patterns: K-way Merge"
header:
  image: https://cdn.emre.me/2019-11-22-k-way-merge-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/k5w21D7PgMk)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/) and [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers) patterns and today, we will introduce [K-way Merge](https://emre.me/coding-patterns/k-way-merge) pattern which is very useful to solve the problems whenever we are given **K** sorted arrays, we can use a [Heap](https://emre.me/data-structures/heaps/) to efficiently perform a *sorted traversal* of *all* the elements of *all* arrays. 

We can push the **smallest** (*first*) element of each sorted array in a [Min Heap](https://emre.me/data-structures/heaps/#min_heapify-and-build_min_heap) to get the overall minimum. While inserting elements to the [Min Heap](https://emre.me/data-structures/heaps/#min_heapify-and-build_min_heap) we keep track of which array the element came from. 

We can also remove the **top** element from the [heap](https://emre.me/data-structures/heaps/) to get the *smallest* element and push the next element from the same array, to which this *smallest* element belonged, to the [heap](https://emre.me/data-structures/heaps/). We can repeat this process to make a sorted traversal of all elements.

## Problem: Merge K Sorted Lists ##
{% capture notice %}
[**LeetCode 23 - Merge k Sorted Lists** [*hard*]](https://leetcode.com/problems/merge-k-sorted-lists/)

Merge **k** sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**

```python
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### K-way Merge Solution ###

We need to find the **smallest** element of **all** the input lists. To do so, we have to compare only the **smallest** element of all the lists first. Once we have the *smallest* element, we can put it in the merged list.

Following a similar pattern, we can then find the *next smallest* element of all the lists to add it to the merged list.

1. We can push the **smallest** (*first*) element of each sorted array in a [Min Heap](https://emre.me/data-structures/heaps/#min_heapify-and-build_min_heap) to get the overall minimum.
2. After this, we can take out the **smallest** (top) element from the [heap](https://emre.me/data-structures/heaps/) and add it to the merged list.
3. After removing the **smallest** element from the [heap](https://emre.me/data-structures/heaps/), we can insert the *next* element of the same list into the [heap](https://emre.me/data-structures/heaps/).
4. We can repeat steps **2** and **3** to populate the merged list in sorted order.


```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeExtension(ListNode):
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = ListNodeExtension.__lt__
        min_heap = []
        for root in lists:
            if root is not None:
                heappush(min_heap, root)

        head = tail = ListNode(0)
        while min_heap:
            tail.next = heappop(min_heap)
            tail = tail.next
            if tail.next:
                heappush(min_heap, tail.next)

        return head.next
```

**Time Complexity**: **O(N log K)** where **N** is the total number of elements in all the **K** input arrays.

**Space Complexity**: **O(K)**

## How to identify? ##
If the problem giving **K** sorted arrays and asks us to perform a *sorted traversal* of *all* the elements of *all* arrays, we need to think about [K-way Merge](https://emre.me/coding-patterns/k-way-merge) pattern.

While solving the problems, we are going to use [Heap](https://emre.me/data-structures/heaps/) data structure to keep track of all elements in **K** arrays.

## Similar LeetCode Problems ##
* [LeetCode 4 - Median of Two Sorted Arrays [*hard*]](https://leetcode.com/problems/median-of-two-sorted-arrays/)