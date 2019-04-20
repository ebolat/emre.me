---
title: "Binary Computation and Bitwise Operators"
header:
  image: https://cdn.emre.me/2019-04-15-binary-computation-and-bitwise-operators-header-image.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/h3sAF1cVURw)"
categories:
  - computer-science
tags:
  - basics
  - binary-numbers
  - bitwise-operators
---

If binary code is something only computers can understand, why should you learn about it?

As developers, we have our user friendly [programming languages](https://en.wikipedia.org/wiki/List_of_programming_languages) to give instructions to computers but they are still translated into binary code for computers to be able to interpret them and run your programs.
 
Binary code is the most fundamental concept underlying programming and [Computer Science](https://emre.me/categories/#computer-science). But, how does binary work then? How can a complex computer program consist of only **1**’s and **0**’s?

## How does the binary number system works? ##

To be able to understand the [binary number system](https://en.wikipedia.org/wiki/Binary_number), we need to take a closer look to the [decimal number system](https://en.wikipedia.org/wiki/Decimal) which we learn in elementary school and still using everyday.
Many numeral systems of ancient civilisations use ten and its powers for representing numbers, probably because there are ten fingers on two hands and people started counting by using their fingers.[<sup>1</sup>](#references)

In the decimal system, each digit in a certain number represents the **1**’s, the **10**’s, the **100**’s, and so on, starting from the right hand side.

![Decimal Number - 123](https://cdn.emre.me/2019-04-15-binary-numbers-123.png){: .align-center}

So, with the number *123*, for example, we have a *3* representing the **1**’s, a *2* representing the **10**’s, and finally a *1* to represent the **100**’s and total of them are **123**.

We are starting from 10 to the power of 0 and increasing the powers while moving to left 1, 2, 3 and so on.

In the **binary system**, instead of using powers of 10, **we use powers of 2**.

![Binary Number - 0111 1011](https://cdn.emre.me/2019-04-15-binary-numbers-01111011.png){: .align-center}

In the binary system, each digit in a certain number represents **1**’s, **2**’s, **4**’s, **8**’s, **16**’s, **32**’s, **64**’s, **128**’s, **256**’s and so on, starting from the right hand side.

## What about negative numbers? ##

Computers use a method called *Two's Complement* [<sup>2</sup>](#references) to represent negative numbers. Also this method can be more effective when performing mathematical operations like adding and subtracting.

In this method, the **bit** at the far left side of the bit pattern is **the most significant bit** or **MSB** is used to indicate *positive* or *negative* numbers. 

Positive numbers always start with a **0** and the remaining bits are used to store the actual size of the number.

Four-bit, positive, two's complement numbers would be 0000 = 0, 0001 = 1, up to 0111 = 7. The smallest positive number is the smallest binary value.

![4-bit Positive Binary Numbers](https://cdn.emre.me/2019-04-15-four-bit-positive-binary-numbers.png){: .align-center}

Negative numbers always start with a **1** and the remaining bits are used to store the actual size of the number. The biggest negative number is the largest binary value. (*e.g.* **1111** is **-1**)

![4-bit Negative Binary Numbers](https://cdn.emre.me/2019-04-15-four-bit-negative-binary-numbers.png){: .align-center}

## Steps to convert a positive binary number to its negative value ##

Following these steps will convert a positive binary number to its negative value by using *Two's Complement for negative numbers* method.



1. Find the *positive* binary value for the *negative* number you want to represent.
2. Add a **0** to the front of the number, to indicate that it is *positive*.
3. Invert or find the complement of each bit in the number.
4. Add **1** to this number.

[Ben Eater](https://www.youtube.com/channel/UCS0N5baNlQWJCUrhCEo8WlA) is explaining these steps very clearly in his [YouTube Channel](https://www.youtube.com/channel/UCS0N5baNlQWJCUrhCEo8WlA). 

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4qH4unVtJkE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Even though we do need a few more digits than we did with the decimal system, the binary system is just as good as the decimal system for displaying numbers.

Well, in fact, we are not limited to numbers, different types of information can also be represented in binary code, too! 

To be able to represent **text in binary code**, we can use simple numbers to represent the different letters in the alphabet. So, *A* could be **1**, *B* could be **2**, and so on.

Also, *images* and *graphics* displayed on your screen consists of pixels and each pixel in an image has **a numerical value** that determines the color it should display. This means that, we can represent images and graphics with binary code.

## Bitwise Operators ##



### References ###

1. Wikipedia, *[Origin of the Decimal Number System](https://en.wikipedia.org/wiki/Decimal#Origin)*
2. Wikipedia, *[Two's complement](https://en.wikipedia.org/wiki/Two%27s_complement)*

