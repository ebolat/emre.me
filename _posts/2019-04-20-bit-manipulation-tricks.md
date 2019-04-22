---
title: "Bit Manipulation Tricks"
header:
  image: https://cdn.emre.me/2019-04-20-bit-manipulation-tricks-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/MaDXpqp1vM0)"
categories:
  - computer-science
tags:
  - binary-numbers
  - bitwise-operators
toc: true
toc_sticky: true
---

If programming is a craft, then it is best learned by imitation and lots of practice. These bit manipulation techniques are little programming tricks that manipulate integers in a smart and efficient manner like a master craftsman.

## Check if the integer is *even* or *odd* ##

This is a well known bit trick among embedded systems programmers.

```python
if (num & 1) == 0:
    # num is EVEN
else:
    # num is ODD
```

An integer is *odd* if and only if the **least significant bit (LSB)** is **1**. By AND-ing given number (*num*) by **1**, we are eliminating all bits other than **LSB**.
After this operation, if the result is **0**, that means **LSB** is **0** and the number is *even*. Otherwise, it is *odd*.

Lets try it with 54;

```
   0011 0110  (binary of 54)
   0000 0001  (binary of 1)
& -----------
   0000 0000  --> 0, so 54 is EVEN       
```

And lets try it with an odd number, 37

```
   0010 0101  (binary of 37)
   0000 0001  (binary of 1)
& -----------
   0000 0001  --> 1, so 37 is ODD
```
