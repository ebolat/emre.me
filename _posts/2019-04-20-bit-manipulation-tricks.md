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

Please note that, If you are not familiar with binary system and/or bitwise operators, I recommend that you read [Binary Computation and Bitwise Operators](https://emre.me/computer-science/binary-computation-and-bitwise-operators/) post first.

## Check if the integer is *even* or *odd* ##

This is a well known bit trick among embedded systems programmers.

```python
def even_or_odd_checker(num: int) -> str:
    if (num & 1) == 0:
        return f"{num} is EVEN"
    else:
        return f"{num} is ODD"
```

An integer is *odd* if and only if the **least significant bit (LSB)** is **1**. By using AND (`&`) operator between given number (*num*) and **1**, we are eliminating all bits other than **LSB**.
After this operation, if the result is **0**, that means **LSB** is **0** and the number is *even*. Otherwise, it is *odd*.

Let's try it with 54;

```
   0011 0110  (binary of 54)
   0000 0001  (binary of 1)
& -----------
   0000 0000  --> 0, so 54 is EVEN       
```

And let's try it with an odd number, 37;

```
   0010 0101  (binary of 37)
   0000 0001  (binary of 1)
& -----------
   0000 0001  --> 1, so 37 is ODD
```

## Test if the *n-th* bit is set ##

This bit trick uses the same logic with the previous one to check if n-th bit is set or not.

```python
def check_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        return f"{num} = {bin(num)} (binary) and {n}th bit is set"
    else:
        return f"{num} = {bin(num)} (binary) and {n}th bit is NOT set"
```

Left shift (`<<`) finds the correct position of the bit which we want to test

```
1         0000 0001
1 << 1    0000 0010
1 << 2    0000 0100
1 << 3    0000 1000
1 << 4    0001 0000
1 << 5    0010 0000
and so on...
```

If the result after this AND (`&`) operation is **0**, then checked bit is **0**, otherwise that bit was set.

Let's try with 175 and check if 5<sup>th</sup> bit is set;

```
   1010 1111  (binary of 175)  
   0010 0000  (1 << 5)
& -----------
   0010 0000 --> 5th bit is set
```

## Set the *n-th* bit if it is not already set ##

We are going to use *left shift* trick that we learn previously.

```python
def set_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is ALREADY set"
    else:
        set_nth_bit_result = num | (1 << n)
        return f"{n}th bit is set ({bin(num)} is changed to {bin(set_nth_bit_result)})"
```

If the result of `num | (1 << n)` operation sets the targeted bit.

Suppose we have 113 and trying the 2<sup>nd</sup> bit.

```
   0111 0001   (binary of 113)
   0000 0100   (1 << 2)
| -----------
   0111 0101  --> 2nd bit is set
```

## Unset *n-th* bit if it is not already unset ##

```python
def unset_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        unset_nth_bit_result = num & ~(1 << n)
        return f"{n}th bit is unset ({bin(num)} is changed to {bin(unset_nth_bit_result)})"
    else:
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is ALREADY unset"
```

Most important part of this trick is `num & ~(1 << n)` operation. It turns all bits on except the targetted one.

One's complement operator (`~`);

```
~1           1111 1110
~(1 << 1)    1111 1101
~(1 << 2)    1111 1011
~(1 << 3)    1111 0111
~(1 << 4)    1110 1111
~(1 << 5)    1101 1111
and so on...
```

By using the AND (`&`) operator with *Left shifted One's complement*, we are eliminating the targetted bit.

Supporse that we want to unset 4<sup>th</sup> bit of 83;

```
   0101 0011   (binary of 83)
   1110 1111   ~(1 << 4)
& -----------
   0100 0011  --> 4th bit is unset
```


