### [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

Medium

Given an `` n x n `` `` matrix `` where each of the rows and columns is sorted in ascending order, return _the_ <code>k<sup>th</sup></code> _smallest element in the matrix_.

Note that it is the <code>k<sup>th</sup></code> smallest element __in the sorted order__, not the <code>k<sup>th</sup></code> __distinct__ element.

You must find a solution with a memory complexity better than <code>O(n<sup>2</sup>)</code>.

 

__Example 1:__

```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,<u>13</u>,15], and the 8<sup>th</sup> smallest number is 13
```

__Example 2:__

```
Input: matrix = [[-5]], k = 1
Output: -5
```

 

__Constraints:__

*   `` n == matrix.length == matrix[i].length ``
*   `` 1 <= n <= 300 ``
*   <code>-10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup></code>
*   All the rows and columns of `` matrix `` are __guaranteed__ to be sorted in __non-decreasing order__.
*   <code>1 <= k <= n<sup>2</sup></code>

 

__Follow up:__

*   Could you solve the problem with a constant memory (i.e., `` O(1) `` memory complexity)?
*   Could you solve the problem in `` O(n) `` time complexity? The solution may be too advanced for an interview but you may find reading <a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a> fun.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 780,764 | 479,149 | 61.4% |