### [1787. Sum of Absolute Differences in a Sorted Array](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/?envType=daily-question&envId=2023-11-25)

Medium

You are given an integer array `` nums `` sorted in __non-decreasing__ order.

Build and return _an integer array _`` result ``_ with the same length as _`` nums ``_ such that _`` result[i] ``_ is equal to the __summation of absolute differences__ between _`` nums[i] ``_ and all the other elements in the array._

In other words, `` result[i] `` is equal to `` sum(|nums[i]-nums[j]|) `` where `` 0 <= j < nums.length `` and `` j != i `` (__0-indexed__).

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= nums[i + 1] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 149,527 | 103,132 | 69.0% |