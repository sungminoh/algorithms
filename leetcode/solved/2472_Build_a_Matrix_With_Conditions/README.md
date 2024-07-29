### [2472. Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/description/?envType=daily-question&envId=2024-07-21)

Hard

You are given a __positive__ integer `` k ``. You are also given:

*   a 2D integer array `` rowConditions `` of size `` n `` where <code>rowConditions[i] = [above<sub>i</sub>, below<sub>i</sub>]</code>, and
*   a 2D integer array `` colConditions `` of size `` m `` where <code>colConditions[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>.

The two arrays contain integers from `` 1 `` to `` k ``.

You have to build a `` k x k `` matrix that contains each of the numbers from `` 1 `` to `` k `` __exactly once__. The remaining cells should have the value `` 0 ``.

The matrix should also satisfy the following conditions:

*   The number <code>above<sub>i</sub></code> should appear in a __row__ that is strictly __above__ the row at which the number <code>below<sub>i</sub></code> appears for all `` i `` from `` 0 `` to `` n - 1 ``.
*   The number <code>left<sub>i</sub></code> should appear in a __column__ that is strictly __left__ of the column at which the number <code>right<sub>i</sub></code> appears for all `` i `` from `` 0 `` to `` m - 1 ``.

Return ___any__ matrix that satisfies the conditions_. If no answer exists, return an empty matrix.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png" style="width: 211px; height: 211px;"/>

```
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row <u>1</u>, and number 2 is in row <u>2</u>, so 1 is above 2 in the matrix.
- Number 3 is in row <u>0</u>, and number 2 is in row <u>2</u>, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column <u>1</u>, and number 1 is in column <u>2</u>, so 2 is left of 1 in the matrix.
- Number 3 is in column <u>0</u>, and number 2 is in column <u>1</u>, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
```

<strong class="example">Example 2:</strong>

```
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
```

 

__Constraints:__

*   `` 2 <= k <= 400 ``
*   <code>1 <= rowConditions.length, colConditions.length <= 10<sup>4</sup></code>
*   `` rowConditions[i].length == colConditions[i].length == 2 ``
*   <code>1 <= above<sub>i</sub>, below<sub>i</sub>, left<sub>i</sub>, right<sub>i</sub> <= k</code>
*   <code>above<sub>i</sub> != below<sub>i</sub></code>
*   <code>left<sub>i</sub> != right<sub>i</sub></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 112,723 | 89,720 | 79.6% |