---
title: "Coding Patterns: Topological Sort (Graph)"
header:
  image: https://cdn.emre.me/2019-11-30-topological-sort-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/TIT-oE5quKE)"
categories:
  - coding-patterns
tags:
  - algorithms
  - python
  - graphs
toc: true
toc_sticky: true
---

In **[Coding Patterns](https://emre.me/categories/#coding-patterns)** series, we will try to *recognize* common patterns *underlying* behind each algorithm question, using real examples from [Leetcode](https://leetcode.com/).

Previous posts were about [Sliding Window](https://emre.me/coding-patterns/sliding-window/), [Two Pointers](https://emre.me/coding-patterns/two-pointers/), [Fast & Slow Pointers](https://emre.me/coding-patterns/fast-slow-pointers/), [Merge Intervals](https://emre.me/coding-patterns/merge-intervals/), [Cyclic Sort](https://emre.me/coding-patterns/cyclic-sort/), [In-place Reversal of a Linked List](https://emre.me/coding-patterns/in-place-reversal-of-a-linked-list/), [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/), [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), [Two Heaps](https://emre.me/coding-patterns/two-heaps/), [Subsets](https://emre.me/coding-patterns/subsets/), [Modified Binary Search](https://emre.me/coding-patterns/modified-binary-search/), [Top K Numbers](https://emre.me/coding-patterns/top-k-numbers), [K-way Merge](https://emre.me/coding-patterns/k-way-merge) and [0/1 Knapsack](https://emre.me/coding-patterns/knapsack) patterns and today, we will introduce [Topological Sort](https://emre.me/coding-patterns/topological-sort) pattern which is very useful for finding a linear ordering of elements that have dependencies on each other.

## Problem: Course Schedule ##
{% capture notice %}
[**LeetCode 207 - Course Schedule** [*medium*]](https://leetcode.com/problems/course-schedule/)

There are a total of **n** courses you have to take, labeled from **0** to **n - 1**.

Some courses may have prerequisites, for example to take course **0** you have to first take course **1**, which is expressed as a pair: **[0, 1]**

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**Example 1:**

```python
Input: 2, [[1, 0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```python
Input: 2, [[1, 0], [0, 1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 
             you should also have finished course 1. So it is impossible.
```

**Note:**

 - The input **prerequisites** is a graph represented by a list of **edges**, not adjacency matrices. Read more about how a [graph](https://emre.me/data-structures/graphs/) is represented.
 - You may assume that there are no duplicate **edges** in the input **prerequisites**.

{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>

### Topological Sort Solution ###

The aim of [topological sort](https://en.wikipedia.org/wiki/Topological_sorting) is to provide a partial ordering among the *[vertices](https://emre.me/data-structures/graphs/#vertex)* of the [graph](https://emre.me/data-structures/graphs/) such that if there is an *[edge](https://emre.me/data-structures/graphs/#edge)* from `U` to `V` then `U <= V`, which means, `U` comes before `V` in the ordering.

1. **Source:** Any node that has *no incoming edge* and has *only outgoing edges* is called a **source**.
2. **Sink:** Any node that has *only incoming edges* and *no outgoing edge* is called a **sink**.
3. Topological ordering *starts* with one of the **sources** and *ends* at one of the **sinks**.
4. A topological ordering is possible only when the graph has no [directed cycles](https://emre.me/data-structures/graphs/#directed-or-undirected), i.e. if the graph is a [Directed Acyclic Graph (DAG)](https://emre.me/data-structures/graphs/#cyclic-or-acyclic). If the graph has a **cycle**, some vertices will have *cyclic dependencies* which makes it **impossible** to find a linear ordering among vertices.

To find the [topological sort](https://en.wikipedia.org/wiki/Topological_sorting) of a [graph](https://emre.me/data-structures/graphs/) we can *traverse* the graph in a [Breadth First Search (BFS)](https://emre.me/coding-patterns/breadth-first-search/) way.

**a. Initialization**

We will store the graph in [Adjacency Lists](https://emre.me/data-structures/graphs/#adjacency-list), which means each parent [vertex](https://emre.me/data-structures/graphs/#vertex) will have a list containing all of its children. We will do this using a [Hash Table](https://emre.me/data-structures/hash-tables/) where the `key` will be the *parent vertex number* and the `value` will be a [List](https://emre.me/data-structures/lists/) containing *children vertices*.

To find the sources, we will keep a [Hash Table](https://emre.me/data-structures/hash-tables/) to count the in-degrees (count of incoming edges of each vertex). Any vertex with **0** in-degree will be a **source**.

**b. Build the graph and find in-degrees of all vertices**

We will build the graph from the input and populate the in-degrees [Hash Table](https://emre.me/data-structures/hash-tables/).

**c. Find all sources**

All vertices with **0** in-degrees will be our sources and we will store them in a [Queue](https://emre.me/data-structures/stacks-and-queues/#queues).

**d. Sort**

For each source:
- Add it to the sorted list.
- Get all of its children from the [graph](https://emre.me/data-structures/graphs/).
- Decrement the in-degree of each child by **1**.
- If a child’s in-degree becomes **0**, add it to the sources [Queue](https://emre.me/data-structures/stacks-and-queues/#queues).

Repeat these steps, until the source [Queue](https://emre.me/data-structures/stacks-and-queues/#queues) is empty.

```python
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list = []

        if numCourses <= 0:
            return False

        # a. Initialization
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        in_degree = {i: 0 for i in range(numCourses)}  # count of incoming edges

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            in_degree[child] += 1

        # c. Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. Sort
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if sorted_list does not contain all the courses, there is a cyclic dependency between courses
        # scheduling is not possible if there is a cyclic dependency
        return len(sorted_list) == numCourses
```

**Time Complexity**: **O(V + E)** where **V** is the total number of courses and **E** is the total number of `prerequisites`.

**Space Complexity**: **O(V + E)** since we are storing all of the `prerequisites` for each course in an [adjacency list](https://emre.me/data-structures/graphs/#adjacency-list).

## How to identify? ##

[Topological Sort](https://emre.me/coding-patterns/topological-sort) pattern is very useful for finding a linear ordering of elements that have dependencies on each other.

Scheduling or grouping problems which have dependencies between items are good examples to the problems that can be solved with using this technique.

## Similar LeetCode Problems ##
* [LeetCode 210 - Course Schedule II [*medium*]](https://leetcode.com/problems/course-schedule-ii/)
* [LeetCode 269 - Alien Dictionary [*hard*] [*premium*]](https://leetcode.com/problems/alien-dictionary/)