### [436. Find Right Interval](https://leetcode.com/problems/find-right-interval/)

Medium

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

__Note:__

1.   You may assume the interval's end point is always bigger than its start point.
2.   You may assume none of these intervals have the same start point.

 

__Example 1:__

```
<b>Input:</b> [ [1,2] ]

<b>Output:</b> [-1]

<b>Explanation:</b> There is only one interval in the collection, so it outputs -1.
```

 

__Example 2:__

```
<b>Input:</b> [ [3,4], [2,3], [1,2] ]

<b>Output:</b> [-1, 0, 1]

<b>Explanation:</b> There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
```

 

__Example 3:__

```
<b>Input:</b> [ [1,4], [2,3], [3,4] ]

<b>Output:</b> [-1, 2, -1]

<b>Explanation:</b> There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
```

__NOTE:__ input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 74,909 | 33,443 | 44.6% |