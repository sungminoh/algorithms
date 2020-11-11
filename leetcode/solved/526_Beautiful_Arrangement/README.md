### [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

Medium

Suppose you have __N__ integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these __N__ numbers successfully if one of the following is true for the i<sub>th</sub> position (1 <= i <= N) in this array:

1.   The number at the i<sub>th</sub> position is divisible by __i__.
2.   __i__ is divisible by the number at the i<sub>th</sub> position.

 

Now given N, how many beautiful arrangements can you construct?

__Example 1:__

```
<b>Input:</b> 2
<b>Output:</b> 2
<b>Explanation:</b> 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
```

 

__Note:__

1.   __N__ is a positive integer and will not exceed 15.

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 85,085 | 48,833 | 57.4% |