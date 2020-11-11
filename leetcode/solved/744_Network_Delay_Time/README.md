### [744. Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Medium

There are `` N `` network nodes, labelled `` 1 `` to `` N ``.

Given `` times ``, a list of travel times as __directed__ edges `` times[i] = (u, v, w) ``, where `` u `` is the source node, `` v `` is the target node, and `` w `` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `` K ``. How long will it take for all nodes to receive the signal? If it is impossible, return `` -1 ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 200px; height: 220px;"/>

```
Input: times = <span id="example-input-1-1">[[2,1,1],[2,3,1],[3,4,1]]</span>, N = <span id="example-input-1-2">4</span>, K = <span id="example-input-1-3">2</span>
Output: <span id="example-output-1">2</span>
```

 

__Note:__

1.   `` N `` will be in the range `` [1, 100] ``.
2.   `` K `` will be in the range `` [1, N] ``.
3.   The length of `` times `` will be in the range `` [1, 6000] ``.
4.   All edges `` times[i] = (u, v, w) `` will have `` 1 <= u, v <= N `` and `` 0 <= w <= 100 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 244,451 | 110,009 | 45.0% |