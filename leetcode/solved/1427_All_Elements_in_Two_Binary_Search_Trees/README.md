### [1427. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

Medium

Given two binary search trees `` root1 `` and `` root2 ``, return _a list containing all the integers from both trees sorted in __ascending__ order_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png" style="width: 457px; height: 207px;"/>

```
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e5-.png" style="width: 352px; height: 197px;"/>

```
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
```

 

__Constraints:__

*   The number of nodes in each tree is in the range `` [0, 5000] ``.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 193,280 | 153,864 | 79.6% |