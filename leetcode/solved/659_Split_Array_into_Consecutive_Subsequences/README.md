### [659. Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

Medium

Given an array `` nums `` sorted in ascending order, return `` true `` if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

__Example 1:__

```
<b>Input:</b> [1,2,3,3,4,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

```

__Example 2:__

```
<b>Input:</b> [1,2,3,3,4,4,5,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

```

__Example 3:__

```
<b>Input:</b> [1,2,3,4,4,5]
<b>Output:</b> False
```

 

__Constraints:__

*   `` 1 <= nums.length <= 10000 ``

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 100,767 | 43,975 | 43.6% |