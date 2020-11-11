### [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

Hard

Given a set of _non-overlapping_ intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

__Example 1:__

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

__Example 2:__

<strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = <code>[4,8]</code>
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
    <strong>Explanation:</strong> Because the new interval <code>[4,8]</code> overlaps with <code>[3,5],[6,7],[8,10]</code>.

__NOTE:__ input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 773,481 | 259,889 | 33.6% |