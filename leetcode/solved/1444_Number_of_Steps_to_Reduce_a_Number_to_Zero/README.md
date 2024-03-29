### [1444. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

Easy

Given an integer `` num ``, return _the number of steps to reduce it to zero_.

In one step, if the current number is even, you have to divide it by `` 2 ``, otherwise, you have to subtract `` 1 `` from it.

 

__Example 1:__

```
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
```

__Example 2:__

```
Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
```

__Example 3:__

```
Input: num = 123
Output: 12
```

 

__Constraints:__

*   <code>0 <= num <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 374,942 | 322,498 | 86.0% |