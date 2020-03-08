---
title: "Tarjan's Algorithm: Strongly Connected Components"
header:
  image: https://cdn.emre.me/2020-03-07-tarjans-algorithm-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/ubQDHALqKiM)"
categories:
  - algorithms
tags:
  - algorithms
  - graphs
toc: true
toc_sticky: true
---

**Tarjan's algorithm**[<sup>1</sup>](#references)<sup>, </sup>[<sup>2</sup>](#references) which runs in *linear time* is an algorithm in [Graph Theory](https://emre.me/data-structures/graphs/) for finding the **strongly connected components** of a [directed graph](https://emre.me/data-structures/graphs/#directed-or-undirected).

## Bridges and Articulation Points ##

**Bridges** and **Articulation Points** are important in [Graph Theory](https://emre.me/data-structures/graphs/) because in real-world situations, they often hint *weak points*, *bottleneck* or *vulnerabilities* in the graph. Therefore, it is important to be able to quickly *find* and *detect* **where** and **when** they occur.

### Bridge ###
A [Bridge](https://en.wikipedia.org/wiki/Bridge_(graph_theory)) (or **cut-edge**) in [graph theory](https://emre.me/data-structures/graphs/) is any **edge** in a graph *whose removal increases the number of connected components*. 

![Bridge in Graph Theory](https://cdn.emre.me/2020-03-07-bridge.png)

Lines with the *red color* are **bridges** because if you remove any of them, the graph is *divided into two components*.

### Articulation Point ###
An [Articulation Point](https://en.wikipedia.org/wiki/Biconnected_component) (or **cut-vertex**) is any **node** in a graph *whose removal increases the number of connected components*.

![Articulation Point in Graph Theory](https://cdn.emre.me/2020-03-07-articulation-point.png)

Nodes marked with *orange color* are **articulation points** because if you remove any of them, graph is *devided into two components*.


## Tarjan's Algorithm ##
[Tarjan's Algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) provides a very effective way to find these **bridges** and **articulation points** in linear time. We can explain this algorithm in **3** steps:

### Steps ###
**1-** Start at **any** *node* and do a [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/) traversal, labeling nodes with an *increasing* `id` value as you go.

![DFS Lebeling](https://cdn.emre.me/2020-03-07-dfs-traversal.gif)

**2-** Keep track the `id` of *each* node and the *smallest* [low link](#what-is-low-link) value.

#### What is Low Link? ####
**Low Link Value** of a node is defined as the smallest `id` reachable from that node when doing a [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), including itself.

Initially, all [low link](#what-is-low-link) values can be initialized to the each node `id`.

![Low Link Initial](https://cdn.emre.me/2020-03-07-low-link1.png)

If we inspect *node 1* and *node 2*, we will notice that **there exist a path** going from *node 1* and *node 2* to *node 0*.

So, we should update both *node 1* and *node 2* [low link](#what-is-low-link) values to **0**.

![Low Link 0-1-2](https://cdn.emre.me/2020-03-07-low-link2.png)

However, *node 3*, *node 4* and *node 5* are already at their optimal [low link](#what-is-low-link) value because there are **no other node** they can reach with a smaller `id`.

![Low Link 3-4-5](https://cdn.emre.me/2020-03-07-low-link3.png)

For *node 6*, *node 7* and *node 8*, **there is a path** from *node 6*, *node 7* and *node 8* to *node 5*.

So, we should update *node 6*, *node 7* and *node 8* [low link](#what-is-low-link) values to **5**.

![Low Link 6-7-8](https://cdn.emre.me/2020-03-07-low-link4.png)


**3-** During the [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), bridges will be found where the `id` of node your edge is coming from is **less than** the [low link](#what-is-low-link) value of the node your edge is going to.

![Is Bridge?](https://cdn.emre.me/2020-03-07-is-bridge.png)

## Problem: Critical Connections in a Network ##
{% capture notice %}
[**LeetCode 1192 - Critical Connections in a Network** [*hard*]](https://leetcode.com/problems/critical-connections-in-a-network/)

There are `n` servers numbered from **0** to **n-1** connected by undirected server-to-server connections forming a network where `connections[i] = [a, b]` represents a connection between servers **a** and **b**. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

**Example 1:**

![Critical Connections](https://cdn.emre.me/2020-03-07-critical-connections.png)


`Input: n = 4, connections = [[0, 1], [1, 2], [2, 0], [1, 3]]`

`Output: [[1, 3]]`

`Explanation: [[3, 1]] is also accepted.`

**Constraints:**

- 1 <= `n` <= 10<sup>5</sup>
- `n-1` <= `connections.length` <= 10<sup>5</sup>
- `connections[i][0] != connections[i][1]`
- There are no repeated connections.


{% endcapture %}

<div class="notice--info">
  {{ notice | markdownify }}
</div>


## References
1. Wikipedia, *[Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)*
2. Wikipedia, *[Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)*
3. YouTube, *[William Fiset - Bridges and Articulation points - Graph Theory](https://www.youtube.com/watch?v=aZXi1unBdJA)*