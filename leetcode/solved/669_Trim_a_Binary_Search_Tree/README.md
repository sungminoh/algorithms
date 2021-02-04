### [669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)

Medium

Given the `` root `` of a binary search tree and the lowest and highest boundaries as `` low `` and `` high ``, trim the tree so that all its elements lies in `` [low, high] ``. Trimming the tree should __not__ change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a __unique answer__.

Return _the root of the trimmed binary search tree_. Note that the root may change depending on the given bounds.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="width: 450px; height: 126px;"/>

```
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="width: 450px; height: 277px;"/>

```
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
```

__Example 3:__

```
Input: root = [1], low = 1, high = 2
Output: [1]
```

__Example 4:__

```
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
```

__Example 5:__

```
Input: root = [1,null,2], low = 2, high = 4
Output: [2]
```

 

__Constraints:__

*   The number of nodes in the tree in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>0 <= Node.val <= 10<sup>4</sup></code>
*   The value of each node in the tree is __unique__.
*   `` root `` is guaranteed to be a valid binary search tree.
*   <code>0 <= low <= high <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 227,761 | 147,064 | 64.6% |