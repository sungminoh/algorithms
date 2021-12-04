### [989. Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/)

Hard

You are given an integer array of unique positive integers `` nums ``. Consider the following graph:

*   There are `` nums.length `` nodes, labeled `` nums[0] `` to `` nums[nums.length - 1] ``,
*   There is an undirected edge between `` nums[i] `` and `` nums[j] `` if `` nums[i] `` and `` nums[j] `` share a common factor greater than `` 1 ``.

Return _the size of the largest connected component in the graph_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="width: 500px; height: 97px;"/>

```
Input: nums = [4,6,15,35]
Output: 4
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="width: 500px; height: 85px;"/>

```
Input: nums = [20,50,9,63]
Output: 2
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="width: 500px; height: 260px;"/>

```
Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
```

 

__Constraints:__

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>
*   All the values of `` nums `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 104,255 | 42,130 | 40.4% |