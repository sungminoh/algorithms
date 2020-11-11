### [875. Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/)

Medium

Let's call any (contiguous) subarray B (of A) a _mountain_ if the following properties hold:

*   `` B.length >= 3 ``
*   There exists some `` 0 < i < B.length - 1 `` such that `` B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1] ``

(Note that B could be any subarray of A, including the entire array A.)

Given an array `` A `` of integers, return the length of the longest _mountain_. 

Return `` 0 `` if there is no mountain.

__Example 1:__

```
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
```

__Example 2:__

```
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
```

__Note:__

1.   `` 0 <= A.length <= 10000 ``
2.   `` 0 <= A[i] <= 10000 ``

__Follow up:__

*   Can you solve it using only one pass?
*   Can you solve it in `` O(1) `` space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 101,352 | 38,035 | 37.5% |