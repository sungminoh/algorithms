### [772. Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/)

Medium

Given a `` n * n `` matrix `` grid `` of `` 0's `` and `` 1's `` only. We want to represent the `` grid `` with a Quad-Tree.

Return _the root of the Quad-Tree_ representing the `` grid ``.

Notice that you can assign the value of a node to __True__ or __False__ when `` isLeaf `` is __False__, and both are __accepted__ in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

*   `` val ``: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
*   `` isLeaf ``: True if the node is leaf node on the tree or False if the node has the four children.

```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

We can construct a Quad-Tree from a two-dimensional area using the following steps:

1.   If the current grid has the same value (i.e all `` 1's `` or all `` 0's ``) set `` isLeaf `` True and set `` val `` to the value of the grid and set the four children to Null and stop.
2.   If the current grid has different values, set `` isLeaf `` to False and set `` val `` to any value and divide the current grid into four sub-grids as shown in the photo.
3.   Recurse for each of the children with the proper sub-grid.

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="width: 777px; height: 181px;"/>

If you want to know more about the Quad-Tree, you can refer to the [wiki](https://en.wikipedia.org/wiki/Quadtree).

__Quad-Tree format:__

The output represents the serialized format of a Quad-Tree using level order traversal, where `` null `` signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list `` [isLeaf, val] ``.

If the value of `` isLeaf `` or `` val `` is True we represent it as __1__ in the list `` [isLeaf, val] `` and if the value of `` isLeaf `` or `` val `` is False we represent it as __0__.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/grid1.png" style="width: 777px; height: 99px;"/>

```
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.
```
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e1tree.png" style="width: 777px; height: 186px;"/>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" style="width: 777px; height: 343px;"/>

```
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:
```
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" style="width: 777px; height: 328px;"/>


__Example 3:__

```
<strong>Input:</strong> grid = [[1,1],[1,1]]
<strong>Output:</strong> [[1,1]]
```

__Example 4:__

```
<strong>Input:</strong> grid = [[0]]
<strong>Output:</strong> [[1,0]]
```

__Example 5:__

```
<strong>Input:</strong> grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
<strong>Output:</strong> [[0,1],[1,1],[1,0],[1,0],[1,1]]
```

 

__Constraints:__

*   `` n == grid.length == grid[i].length ``
*   `` n == 2^x `` where `` 0 <= x <= 6 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 33,839 | 20,610 | 60.9% |