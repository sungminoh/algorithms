### [1814. Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

Medium

You are given a __0-indexed__ integer array `` nums `` and an integer `` k ``.

You are initially standing at index `` 0 ``. In one move, you can jump at most `` k `` steps forward without going outside the boundaries of the array. That is, you can jump from index `` i `` to any index in the range `` [i + 1, min(n - 1, i + k)] `` __inclusive__.

You want to reach the last index of the array (index `` n - 1 ``). Your __score__ is the __sum__ of all `` nums[j] `` for each index `` j `` you visited in the array.

Return _the __maximum score__ you can get_.

 

__Example 1:__

```
Input: nums = [<u>1</u>,<u>-1</u>,-2,<u>4</u>,-7,<u>3</u>], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
```

__Example 2:__

```
Input: nums = [<u>10</u>,-5,-2,<u>4</u>,0,<u>3</u>], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
```

__Example 3:__

```
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
```

 

__Constraints:__

*   <code>1 <= nums.length, k <= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 187,336 | 86,899 | 46.4% |