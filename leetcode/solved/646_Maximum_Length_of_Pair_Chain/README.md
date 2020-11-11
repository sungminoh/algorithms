### [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

Medium

You are given `` n `` pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair `` (c, d) `` can follow another pair `` (a, b) `` if and only if `` b < c ``. Chain of pairs can be formed in this fashion. 

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

__Example 1:__  

```
<b>Input:</b> [[1,2], [2,3], [3,4]]
<b>Output:</b> 2
<b>Explanation:</b> The longest chain is [1,2] -> [3,4]
```

__Note:__  

1.   The number of given pairs will be in the range \[1, 1000\].

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 109,221 | 56,135 | 51.4% |