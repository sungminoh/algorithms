### [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/description/?envType=daily-question&envId=2024-08-13)

Medium

Given a collection of candidate numbers (`` candidates ``) and a target number (`` target ``), find all unique combinations in `` candidates `` where the candidate numbers sum to `` target ``.

Each number in `` candidates `` may only be used __once__ in the combination.

__Note:__ The solution set must not contain duplicate combinations.

 

<strong class="example">Example 1:</strong>

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

<strong class="example">Example 2:</strong>

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

 

__Constraints:__

*   `` 1 <= candidates.length <= 100 ``
*   `` 1 <= candidates[i] <= 50 ``
*   `` 1 <= target <= 30 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,143,062 | 1,213,695 | 56.6% |