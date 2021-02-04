### [198. House Robber](https://leetcode.com/problems/house-robber/)

Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and __it will automatically contact the police if two adjacent houses were broken into on the same night__.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight __without alerting the police__.

 

__Example 1:__

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

__Example 2:__

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

 

__Constraints:__

*   `` 0 <= nums.length <= 100 ``
*   `` 0 <= nums[i] <= 400 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,541,197 | 658,660 | 42.7% |