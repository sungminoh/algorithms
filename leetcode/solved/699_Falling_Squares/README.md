### [699. Falling Squares](https://leetcode.com/problems/falling-squares/)

Hard

There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array `` positions `` where <code>positions[i] = [left<sub>i</sub>, sideLength<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> square with a side length of <code>sideLength<sub>i</sub></code> that is dropped with its left edge aligned with X-coordinate <code>left<sub>i</sub></code>.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands __on the top side of another square__ or __on the X-axis__. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the __height of the current tallest stack of squares__.

Return _an integer array _`` ans ``_ where _`` ans[i] ``_ represents the height described above after dropping the _<code>i<sup>th</sup></code>_ square_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg" style="width: 500px; height: 505px;"/>

```
Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].
```

<strong class="example">Example 2:</strong>

```
Input: positions = [[100,100],[200,100]]
Output: [100,100]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.
```

 

__Constraints:__

*   `` 1 <= positions.length <= 1000 ``
*   <code>1 <= left<sub>i</sub> <= 10<sup>8</sup></code>
*   <code>1 <= sideLength<sub>i</sub> <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 49,418 | 21,955 | 44.4% |