### [2364. Longest Path With Different Adjacent Characters](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/)

Hard

You are given a __tree__ (i.e. a connected, undirected graph that has no cycles) __rooted__ at node `` 0 `` consisting of `` n `` nodes numbered from `` 0 `` to `` n - 1 ``. The tree is represented by a __0-indexed__ array `` parent `` of size `` n ``, where `` parent[i] `` is the parent of node `` i ``. Since node `` 0 `` is the root, `` parent[0] == -1 ``.

You are also given a string `` s `` of length `` n ``, where `` s[i] `` is the character assigned to node `` i ``.

Return _the length of the __longest path__ in the tree such that no pair of __adjacent__ nodes on the path have the same character assigned to them._

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png" style="width: 201px; height: 241px;"/>

```
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png" style="width: 201px; height: 221px;"/>

```
Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
```

 

__Constraints:__

*   `` n == parent.length == s.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   `` 0 <= parent[i] <= n - 1 `` for all `` i >= 1 ``
*   `` parent[0] == -1 ``
*   `` parent `` represents a valid tree.
*   `` s `` consists of only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 116,269 | 64,999 | 55.9% |