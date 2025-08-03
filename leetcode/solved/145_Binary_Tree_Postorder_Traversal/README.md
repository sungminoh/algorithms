### [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-25)

Easy

Given the `` root `` of a binary tree, return _the postorder traversal of its nodes' values_.

 

<strong class="example">Example 1:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,null,2,3]</span></p>
<p><strong>Output:</strong> <span class="example-io">[3,2,1]</span></p>
<p><strong>Explanation:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;"/></p>
</div>

<strong class="example">Example 2:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>
<p><strong>Output:</strong> <span class="example-io">[4,6,7,5,2,9,8,3,1]</span></p>
<p><strong>Explanation:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/tree_2.png" style="width: 350px; height: 286px;"/></p>
</div>

<strong class="example">Example 3:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = []</span></p>
<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<strong class="example">Example 4:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1]</span></p>
<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

 

__Constraints:__

*   The number of the nodes in the tree is in the range `` [0, 100] ``.
*   `` -100 <= Node.val <= 100 ``

 
__Follow up:__ Recursive solution is trivial, could you do it iteratively?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,986,120 | 1,471,441 | 74.1% |