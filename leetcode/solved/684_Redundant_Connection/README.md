### [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

Medium

In this problem, a tree is an __undirected__ graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `` edges ``. Each element of `` edges `` is a pair `` [u, v] `` with `` u < v ``, that represents an __undirected__ edge connecting nodes `` u `` and `` v ``.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge `` [u, v] `` should be in the same format, with `` u < v ``.

__Example 1:__  

```
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given undirected graph will be like this:
  1
 / \
2 - 3
```

__Example 2:__  

```
<b>Input:</b> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<b>Output:</b> [1,4]
<b>Explanation:</b> The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
```

__Note:__  
<li>The size of the input 2D-array will be between 3 and 1000.</li><li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>

  

<b><font color="red">Update (2017-09-26):</font></b>  
We have overhauled the problem description + test cases and specified clearly the graph is an ___undirected___ graph. For the ___directed___ graph follow up please see __[Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/description/)__). We apologize for any inconvenience caused.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 173,385 | 99,759 | 57.5% |