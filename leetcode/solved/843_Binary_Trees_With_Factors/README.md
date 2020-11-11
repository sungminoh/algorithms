### [843. Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/)

Medium

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer __modulo 10 \*\* 9 + 7__.

__Example 1:__

<strong>Input:</strong> A = [2, 4]
    <strong>Output:</strong> 3
    <strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code>

__Example 2:__

<strong>Input:</strong> A = [2, 4, 5, 10]
    <strong>Output:</strong> <code>7</code>
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.

 

__Note:__

1.   `` 1 <= A.length <= 1000 ``.
2.   `` 2 <= A[i] <= 10 ^ 9 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 30,700 | 10,826 | 35.3% |