### [755. Reach a Number](https://leetcode.com/problems/reach-a-number/)

Medium

You are standing at position `` 0 `` on an infinite number line. There is a goal at position `` target ``.

On each move, you can either go left or right. During the _n_-th move (starting from 1), you take _n_ steps.

Return the minimum number of steps required to reach the destination.

__Example 1:__  

```
<b>Input:</b> target = 3
<b>Output:</b> 2
<b>Explanation:</b>
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```

__Example 2:__  

```
<b>Input:</b> target = 2
<b>Output:</b> 3
<b>Explanation:</b>
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```

__Note:__  
<li><code>target</code> will be a non-zero integer in the range <code>[-10^9, 10^9]</code>.</li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 49,096 | 17,095 | 34.8% |