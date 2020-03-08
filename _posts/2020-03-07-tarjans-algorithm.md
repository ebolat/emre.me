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
1. Start at **any** *node* and do a [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/) traversal, labeling nodes with an *increasing* `id` value as you go.

![DFS Lebeling](https://cdn.emre.me/2020-03-07-dfs.gif)

2. Keep track the `id` of *each* node and the *smallest* [low link](#what-is-low-link) value.
3. During the [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), bridges will be found where the `id` of node your edge is coming from is **less than** the [low link](#what-is-low-link) value of the node your edge is going to.

### What is Low Link? ###
**Low Link Value** of a node is defined as the smallest `id` reachable from that node when doing a [Depth First Search (DFS)](https://emre.me/coding-patterns/depth-first-search/), including itself.


=============== TO BE CONTINUE ==================

## References
1. Wikipedia, *[Robert Tarjan](https://en.wikipedia.org/wiki/Robert_Tarjan)*
2. Wikipedia, *[Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)*
3. YouTube, *[William Fiset - Bridges and Articulation points - Algorithm | Graph Theory](https://www.youtube.com/watch?v=aZXi1unBdJA)*