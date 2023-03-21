### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)

Medium

You are given a __0-indexed__ array of integers `` nums `` of length `` n ``. You are initially positioned at `` nums[0] ``.

Each element `` nums[i] `` represents the maximum length of a forward jump from index `` i ``. In other words, if you are at `` nums[i] ``, you can jump to any `` nums[i + j] `` where:

*   `` 0 <= j <= nums[i] `` and
*   `` i + j < n ``

Return _the minimum number of jumps to reach _`` nums[n - 1] ``. The test cases are generated such that you can reach `` nums[n - 1] ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2,3,0,1,4]
Output: 2
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   `` 0 <= nums[i] <= 1000 ``
*   It's guaranteed that you can reach `` nums[n - 1] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,164,490 | 861,573 | 39.8% |