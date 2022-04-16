### [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

Hard

Given an array `` nums `` which consists of non-negative integers and an integer `` m ``, you can split the array into `` m `` non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these `` m `` subarrays.

 

__Example 1:__

```
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

__Example 2:__

```
Input: nums = [1,2,3,4,5], m = 2
Output: 9
```

__Example 3:__

```
Input: nums = [1,4,4], m = 3
Output: 4
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   <code>0 <= nums[i] <= 10<sup>6</sup></code>
*   `` 1 <= m <= min(50, nums.length) ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 393,612 | 204,541 | 52.0% |