---
title: "Greedy Algorithms"
header:
  image: https://cdn.emre.me/2019-09-11-greedy-algorithms-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/Wc8k-KryEPM)"
categories:
  - algorithms
tags:
  - python
  - greedy
  - algorithms
toc: true
toc_sticky: true
---

A greedy algorithm, as the name suggests, **always makes the choice that seems to be the best at that moment**. This means that it makes a *locally-optimal* choice in the hope that this choice will lead to a *globally-optimal* solution.

They never look backwards at what they've done to see if they could *optimise* **globally**. This is the main difference between [Greedy](https://en.wikipedia.org/wiki/Greedy_algorithm) and [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/).

## Limitations of Greedy Algorithms ##
Sometimes *greedy algorithm* fails to find the **optimal** solution because it does *not* consider *all available data* and make choices which *seems best at that moment*.

A famous example for this limitation is searching the largest path in a tree.

![Greedy Algorithm - Searching Largest Path](https://cdn.emre.me/2019-09-11-greedy-search-path.gif){: .align-center}
<figure>
  <figcaption>Greedy Algorithm for searching the <b>largest</b> path in a tree</figcaption>
</figure>

The **greedy algorithm** fails to solve this problem because it makes decisions *purely* based on what the best answer at the time is: at **each** step it did choose the **largest** number and solve the problem as **7** -> **12** -> **6** -> **9**. Total is: **34**.

But obviously, this is **not** the optimal solution. Correct solution to this problem is, **7** -> **3** -> **1** -> **99**. Total is: **110**.

## Minimum Coin Change Problem ##
A good example to understand Greedy Algorithms better is; *the minimum coin change problem*.

In this problem, the aim is to find the *minimum number of coins* with particular value which *add up* to a given amount of money. These types of optimization problems is often solved by [Dynamic Programming](https://emre.me/algorithms/dynamic-programming/) or [Greedy Algorithms](https://en.wikipedia.org/wiki/Greedy_algorithm).

Say you're a cashier in [Istanbul](https://en.wikipedia.org/wiki/Istanbul) and need to give someone **2 lira (₺) and 67 kuruş (kr)** using as *few* coins[<sup>1</sup>](#references) as possible. How would you do it?

For reference, this is the denomination of each coin in **Turkey**:

```python
[1 kr, 5 kr, 10 kr, 25 kr, 50 kr, ₺1 (100 kr)]
```

![Turkish Coins](https://cdn.emre.me/2019-09-11-turkish-coins.jpg){: .align-center}

For returning **2 lira (₺) and 67 kuruş (kr)**, you'd take the highest-value coin you could. *A* **lira**, *another* **lira**, then *a* **50 kr**, *a* **10 kr**, *a* **5 kr** and finally *two* **1 kr**. That's a **greedy algorithm**, because you're always *greedily* choosing the coin that covers the *biggest* portion of the remaining amount.

### Implementation ###

```python
denominations = [1, 5, 10, 25, 50, 100]
# 100kr is ₺1


def return_change(change, denominations):
    to_give_back = [0] * len(denominations)

    # starting with the largest coin, goes through denominations list
    # and also keeps track of the counter, pos.
    for pos, coin in enumerate(reversed(denominations)):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back


print(return_change(267, denominations))
# returns [2, 1, 0, 1, 1, 2]
# 2x ₺1 (100 kr), 1x 50kr, 0x 25kr, 1x 10kr, 1x 5kr, 2x 1kr = 267kr = ₺2.67
```

The *runtime* of this algorithm is dominated by the **2** loops, thus it is **O(n<sup>2</sup>)**.

## References ##
1. Wikipedia, *[Coins of Turkey](https://en.wikipedia.org/wiki/Coins_of_Turkey)*

