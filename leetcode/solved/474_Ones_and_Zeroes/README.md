### [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

Medium

You are given an array of binary strings `` strs `` and two integers `` m `` and `` n ``.

Return _the size of the largest subset of `` strs `` such that there are __at most__ _`` m ``_ _`` 0 ``_'s and _`` n ``_ _`` 1 ``_'s in the subset_.

A set `` x `` is a __subset__ of a set `` y `` if all elements of `` x `` are also elements of `` y ``.

 

__Example 1:__

```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
```

__Example 2:__

```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
<b>Explanation:</b> The largest subset is {"0", "1"}, so the answer is 2.
```

 

__Constraints:__

*   `` 1 <= strs.length <= 600 ``
*   `` 1 <= strs[i].length <= 100 ``
*   `` strs[i] `` consists only of digits `` '0' `` and `` '1' ``.
*   `` 1 <= m, n <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 185,684 | 81,153 | 43.7% |