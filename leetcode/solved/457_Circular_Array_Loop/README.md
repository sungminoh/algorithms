### [457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/)

Medium

You are given a __circular__ array `` nums `` of positive and negative integers. If a number _k_ at an index is positive, then move forward _k_ steps. Conversely, if it's negative (-_k_), move backward _k_ steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in `` nums ``. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

 

__Example 1:__

```
<b>Input:</b> [2,-1,1,2,2]
<b>Output:</b> true
<b>Explanation:</b> There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
```

__Example 2:__

```
<b>Input:</b> [-1,2]
<b>Output:</b> false
<b>Explanation:</b> The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
```

__Example 3:__

```
<b>Input:</b> [-2,1,-1,-2,-2]
<b>Output:</b> false
<b>Explanation:</b> The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
```

 

__Note:__

1.   -1000 ≤ nums\[i\] ≤ 1000
2.   nums\[i\] ≠ 0
3.   1 ≤ nums.length ≤ 5000

 

__Follow up:__

Could you solve it in __O(n)__ time complexity and __O(1)__ extra space complexity?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 105,895 | 30,575 | 28.9% |