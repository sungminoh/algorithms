### [958. Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)

Easy

Given an array of integers `` nums ``, half of the integers in `` nums `` are __odd__, and the other half are __even__.

Sort the array so that whenever `` nums[i] `` is odd, `` i `` is __odd__, and whenever `` nums[i] `` is even, `` i `` is __even__.

Return _any answer array that satisfies this condition_.

 

__Example 1:__

```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

__Example 2:__

```
Input: nums = [2,3]
Output: [2,3]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 2 * 10<sup>4</sup></code>
*   `` nums.length `` is even.
*   Half of the integers in `` nums `` are even.
*   `` 0 <= nums[i] <= 1000 ``

 

__Follow Up:__ Could you solve it in-place?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 235,642 | 166,336 | 70.6% |