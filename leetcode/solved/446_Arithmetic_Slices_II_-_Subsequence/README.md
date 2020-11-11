### [446. Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/ls)

Hard

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not arithmetic.

```
1, 1, 2, 5, 7
```


 


A zero-indexed array A consisting of N numbers is given. A __subsequence__ slice of that array is any sequence of integers (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) such that 0 ≤ P<sub>0</sub> < P<sub>1</sub> < ... < P<sub>k</sub> < N.

A __subsequence__ slice (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) of array A is called arithmetic if the sequence A\[P<sub>0</sub>\], A\[P<sub>1</sub>\], ..., A\[P<sub>k-1</sub>\], A\[P<sub>k</sub>\] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -2<sup>31</sup> and 2<sup>31</sup>-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 2<sup>31</sup>-1.


 


__Example:__

```
<b>Input:</b> [2, 4, 6, 8, 10]

<b>Output:</b> 7

<b>Explanation:</b>
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 68,862 | 22,689 | 32.9% |