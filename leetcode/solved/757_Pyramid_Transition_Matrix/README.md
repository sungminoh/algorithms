### [757. Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/)

Medium

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block `` C `` on top of two adjacent blocks of colors `` A `` and `` B ``, if and only if `` ABC `` is an allowed triple.

We start with a bottom row of `` bottom ``, represented as a single string. We also start with a list of allowed triples `` allowed ``. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

__Example 1:__

```
<b>Input:</b> bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
<b>Output:</b> true
<b>Explanation:</b>
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
```

 

__Example 2:__

```
<b>Input:</b> bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
<b>Output:</b> false
<b>Explanation:</b>
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
```

 

__Constraints:__

*   `` bottom `` will be a string with length in range `` [2, 8] ``.
*   `` allowed `` will have length in range `` [0, 200] ``.
*   Letters in all strings will be chosen from the set `` {'A', 'B', 'C', 'D', 'E', 'F', 'G'} ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 38,737 | 21,244 | 54.8% |