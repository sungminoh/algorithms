### [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

Medium

Given an array of __distinct__ integers `` nums `` and a target integer `` target ``, return _the number of possible combinations that add up to_ `` target ``.

The test cases are generated so that the answer can fit in a __32-bit__ integer.

 

__Example 1:__

```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

__Example 2:__

```
Input: nums = [9], target = 3
Output: 0
```

 

__Constraints:__

*   `` 1 <= nums.length <= 200 ``
*   `` 1 <= nums[i] <= 1000 ``
*   All the elements of `` nums `` are __unique__.
*   `` 1 <= target <= 1000 ``

 

__Follow up:__ What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 611,765 | 317,029 | 51.8% |