### [494. Target Sum](https://leetcode.com/problems/target-sum/)

Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols `` + `` and `` - ``. For each integer, you should choose one from `` + `` and `` - `` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S. 

__Example 1:__  

```
<b>Input:</b> nums is [1, 1, 1, 1, 1], S is 3. 
<b>Output:</b> 5
<b>Explanation:</b> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

__Note:__  

1.   The length of the given array is positive and will not exceed 20. 
2.   The sum of elements in the given array will not exceed 1000.
3.   Your output answer is guaranteed to be fitted in a 32-bit integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 326,833 | 152,065 | 46.5% |