### [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

Medium

There are `` n `` cities. Some of them are connected, while some are not. If city `` a `` is connected directly with city `` b ``, and city `` b `` is connected directly with city `` c ``, then city `` a `` is connected indirectly with city `` c ``.

A __province__ is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `` n x n `` matrix `` isConnected `` where `` isConnected[i][j] = 1 `` if the <code>i<sup>th</sup></code> city and the <code>j<sup>th</sup></code> city are directly connected, and `` isConnected[i][j] = 0 `` otherwise.

Return _the total number of __provinces___.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;"/>

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;"/>

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

 

__Constraints:__

*   `` 1 <= n <= 200 ``
*   `` n == isConnected.length ``
*   `` n == isConnected[i].length ``
*   `` isConnected[i][j] `` is `` 1 `` or `` 0 ``.
*   `` isConnected[i][i] == 1 ``
*   `` isConnected[i][j] == isConnected[j][i] ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,323,400 | 875,873 | 66.2% |