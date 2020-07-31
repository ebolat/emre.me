---
title: "Dynamic Programming"
header:
  image: https://cdn.emre.me/2019-09-07-dynamic-programming-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/GfmIT_pseDQ)"
categories:
  - algorithms
tags:
  - python
  - dynamic-programming
  - algorithms
toc: true
toc_sticky: true
---

*Dynamic programming* is all about breaking down an **optimization problem** into **simpler sub-problems**, and **storing** the solution to each sub-problem so that each sub-problem is **solved only once**.

This method was developed by [Richard Bellman](https://en.wikipedia.org/wiki/Richard_E._Bellman) in the **1950s**. He explained the reasoning behind the name "*Dynamic Programming*" in his autobiography[<sup>1</sup>](#references) and the main reason was: "*to pick a term that didn’t sound like mathematical research*". 

He wrote that the *Secretary of Defense* at the time was biased against research. So he picked “*programming*”, which sounded less like *research*. He also wanted to get across the idea that it was multistage, so he picked “*dynamic*”. The final name was also hard to use in a negative way, even for a Congressman!

## Sub-problems ##
We said that, it is all about *breaking down* the original problem into **simpler** *sub-problems*. But what is a **sub-problem**?

For example lets think about a simple mathematical calculation:

```
3 + 7 + 8 + 1 + 5 + 2 + 3 + 7 + 8 + 8 + 8 + 1 = 61
```

We can divide it into sub-problems;

```
3 + 7 = 10
8 + 1 = 9
5 + 2 = 7
3 + 7 ---> We already calcualted it! It's 10.
8 + 8 = 16
8 + 1 ---> We already calcualted it! It's 9.
```

In **Dynamic Programming (DP)**, we are storing the solutions of sub-problems so that we do not need to recalculate it later. This is called [Memoization](#memoization).

By finding the solutions for **every single sub-problem**, we can solve the **original** problem itself.

## Memoization ##
[Memoization](#memoization) refers to the technique of *caching* and *reusing* previously computed results. It is a **top-down approach** where we just start by solving the problem in a *natural manner* and storing the solutions of the sub-problems *along the way*.

Suppose that we want to find the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) at a particular index of the sequence. So `fibonacci(n)` = *n*<sup>th</sup> element in the **Fibonacci sequence**.

This problem is normally solved with [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) algorithm. There are **3** main parts in this technique:

1. **Divide** - divide the problem into smaller *sub-problems* of the same type
2. **Conquer** - solve the sub-problems *recursively*
3. **Combine** - combine all the sub-problems *to create a solution to the original problem*

Lets define a function which will be responsible for calculating each of the **Fibonacci numbers** up to some defined limit **n**. 

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

This first naive solution **recursively** calculates *each* number in the sequence *from scratch*. This method has **O(2<sup>n</sup>)** time complexity, which is really bad runetime. For example, calculating `fibonacci(40)` will take **more than a minute!**

This also happens to be a good example of the **danger of naive recursive functions**.

The main idea behind **Memoization** was to re-use already calculated sub-problem results in order to solve the original problem.

![Recursion Tree](https://cdn.emre.me/2019-09-07-fibonacci-number.png){: .align-center}

As you can see in the **recursion tree**, the same sub-problems occured more than once. For example `fib(3)` is occuring **twice**, `fib(2)` is occuring **3** times etc. 

So, despite calculating the result of the **same problem**, again and again, we can *store* the results once and *use them again whenever needed*.

Let's write the same code but this time by storing the terms we have already calculated.

```python
memo = {0: 0, 1: 1}

def fibonacci_memoization(n):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]
```

By not computing the full *recusrive tree* on each iteration, we've essentially reduced the running time for `fibonacci(40)` from **more than a minute** to **almost instant**. But we are sacrificing **memory** for the **speed**. Dynamic programming basically trades **time** with **memory**.

## Tabulation ##

The other way we could have solved the [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) problem was by starting from the **bottom** i.e., start by calculating the *2*<sup>nd</sup> term and then *3*<sup>rd</sup> and so on and finally calculating the *higher terms on the top of these*, by using these values. This **bottom-up approach** is called [Tabulation](#tabulation).

```python
def fibonacci_tabulation(n):
    if n == 0:
        return n

	# pre-initialize array
    f = [0] * (n + 1)
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
```

## Memoization vs Tabulation ##

Generally speaking, [memoization](#memoization) is easier to code than [tabulation](#tabulation). We can write a *memoriser* wrapper function that automatically does it for us. With [tabulation](#tabulation), we have to come up with an *ordering*.

Also, [memoization](#memoization) is indeed the natural way of solving a problem, so coding is easier in [memoization](#memoization) when we deal with a complex problem. Coming up with a specific order while dealing with lot of conditions might be difficult in the [tabulation](#tabulation).

What is more, think about a case when we don't need to find the solutions of all the subproblems. In that case, we would prefer to use the [memoization](#memoization) instead.

[Tabulation](#tabulation) is *faster*, as you already know the order and dimensions of the table. [Memoization](#memoization) is *slower*, because you are creating the table on the fly. Generally, [memoization](#memoization) is also slower than [tabulation](#tabulation) because of the large **recursive calls**.

In [memoization](#memoization), table does *not have to be fully computed*, it is just a **cache** while in [tabulation](#tabulation), table is *fully computed*.

If all sub-problems must be solved at least once, a **bottom-up** *tabulated* [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) algorithm usually outperforms a **top-down** *memoized* algorithm by a constant factor.

## References ##
1. Wikipedia, *[Eye of the Hurricane: An Autobiography](https://www.amazon.com/Hurricane-Autobiography-Richard-Ernest-Bellman/dp/997196600X)*, (1984, page 159)
2. Wikipedia, *[Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)*
3. Wikipedia, *[Memoization](https://en.wikipedia.org/wiki/Memoization)*