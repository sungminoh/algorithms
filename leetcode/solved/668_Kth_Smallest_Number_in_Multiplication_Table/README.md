### [668. Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

Hard

Nearly everyone has used the <a href="https://en.wikipedia.org/wiki/Multiplication_table" target="_blank">Multiplication Table</a>. The multiplication table of size `` m x n `` is an integer matrix `` mat `` where `` mat[i][j] == i * j `` (__1-indexed__).

Given three integers `` m ``, `` n ``, and `` k ``, return _the _<code>k<sup>th</sup></code>_ smallest element in the _`` m x n ``_ multiplication table_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg" style="width: 500px; height: 254px;"/>

```
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5<sup>th</sup> smallest number is 3.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg" style="width: 493px; height: 293px;"/>

```
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6<sup>th</sup> smallest number is 6.
```

 

__Constraints:__

*   <code>1 <= m, n <= 3 * 10<sup>4</sup></code>
*   `` 1 <= k <= m * n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 88,295 | 44,609 | 50.5% |