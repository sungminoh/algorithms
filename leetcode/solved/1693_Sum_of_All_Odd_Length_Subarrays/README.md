### [1693. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

Easy

Given an array of positive integers `` arr ``, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return _the sum of all odd-length subarrays of _`` arr ``.

 

__Example 1:__

```
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

__Example 2:__

```
Input: arr = [1,2]
Output: 3
<b>Explanation: </b>There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

__Example 3:__

```
Input: arr = [10,11,12]
Output: 66
```

 

__Constraints:__

*   `` 1 <= arr.length <= 100 ``
*   `` 1 <= arr[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 52,596 | 42,926 | 81.6% |