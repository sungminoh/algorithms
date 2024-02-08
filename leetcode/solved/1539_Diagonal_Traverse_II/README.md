### [1539. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/description/?envType=daily-question&envId=2023-11-22)

Medium

Given a 2D integer array `` nums ``, return _all elements of _`` nums ``_ in diagonal order as shown in the below images_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png" style="width: 158px; height: 143px;"/>

```
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png" style="width: 230px; height: 177px;"/>

```
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i].length <= 10<sup>5</sup></code>
*   <code>1 <= sum(nums[i].length) <= 10<sup>5</sup></code>
*   <code>1 <= nums[i][j] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 220,272 | 124,758 | 56.6% |