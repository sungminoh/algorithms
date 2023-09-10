### [1621. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/?envType=daily-question&envId=2023-05-06)

Medium

You are given an array of integers `` nums `` and an integer `` target ``.

Return _the number of __non-empty__ subsequences of _`` nums ``_ such that the sum of the minimum and maximum element on it is less or equal to _`` target ``. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
```

<strong class="example">Example 2:</strong>

```
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
```

<strong class="example">Example 3:</strong>

```
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>6</sup></code>
*   <code>1 <= target <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 235,999 | 104,208 | 44.2% |