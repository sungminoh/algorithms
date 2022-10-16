### [1896. Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)

Hard

You are given two __0-indexed__ integer arrays `` nums `` and `` multipliers ``__ __of size `` n `` and `` m `` respectively, where `` n >= m ``.

You begin with a score of `` 0 ``. You want to perform __exactly__ `` m `` operations. On the <code>i<sup>th</sup></code> operation (__0-indexed__) you will:

*   Choose one integer `` x `` from __either the start or the end __of the array `` nums ``.
*   Add `` multipliers[i] * x `` to your score. 
    
    *   Note that `` multipliers[0] `` corresponds to the first operation, `` multipliers[1] `` to the second operation, and so on.
    
    
    
*   Remove `` x `` from `` nums ``.

Return _the __maximum__ score after performing _`` m `` _operations._

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,<u>3</u>], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,<u>2</u>], adding 2 * 2 = 4 to the score.
- Choose from the end, [<u>1</u>], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [<u>-5</u>,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [<u>-3</u>,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [<u>-3</u>,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,<u>1</u>], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,<u>7</u>], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
```

 

__Constraints:__

*   `` n == nums.length ``
*   `` m == multipliers.length ``
*   `` 1 <= m <= 300 ``
*   <code>m <= n <= 10<sup>5</sup></code>``   ``
*   `` -1000 <= nums[i], multipliers[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 235,659 | 85,420 | 36.2% |