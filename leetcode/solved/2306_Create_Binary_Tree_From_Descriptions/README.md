### [2306. Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2024-07-15)

Medium

You are given a 2D integer array `` descriptions `` where <code>descriptions[i] = [parent<sub>i</sub>, child<sub>i</sub>, isLeft<sub>i</sub>]</code> indicates that <code>parent<sub>i</sub></code> is the __parent__ of <code>child<sub>i</sub></code> in a __binary__ tree of __unique__ values. Furthermore,

*   If <code>isLeft<sub>i</sub> == 1</code>, then <code>child<sub>i</sub></code> is the left child of <code>parent<sub>i</sub></code>.
*   If <code>isLeft<sub>i</sub> == 0</code>, then <code>child<sub>i</sub></code> is the right child of <code>parent<sub>i</sub></code>.

Construct the binary tree described by `` descriptions `` and return _its __root___.

The test cases will be generated such that the binary tree is __valid__.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png" style="width: 300px; height: 236px;"/>

```
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png" style="width: 131px; height: 300px;"/>

```
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
```

 

__Constraints:__

*   <code>1 <= descriptions.length <= 10<sup>4</sup></code>
*   `` descriptions[i].length == 3 ``
*   <code>1 <= parent<sub>i</sub>, child<sub>i</sub> <= 10<sup>5</sup></code>
*   <code>0 <= isLeft<sub>i</sub> <= 1</code>
*   The binary tree described by `` descriptions `` is valid.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 183,533 | 150,134 | 81.8% |