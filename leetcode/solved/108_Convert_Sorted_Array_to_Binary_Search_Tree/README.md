### [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

Easy

Given an integer array `` nums `` where the elements are sorted in __ascending order__, convert _it to a __height-balanced__ binary search tree_.

A __height-balanced__ binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;"/>

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;"/>
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;"/>

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` is sorted in a __strictly increasing__ order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,244,459 | 850,838 | 68.4% |