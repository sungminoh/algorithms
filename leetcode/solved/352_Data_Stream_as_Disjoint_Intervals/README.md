### [352. Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

Hard

Given a data stream input of non-negative integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

```
[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
```

 

__Follow up:__

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 80,360 | 38,439 | 47.8% |