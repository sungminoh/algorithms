### [2244. Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03)

Medium

Anti-theft security devices are activated inside a bank. You are given a __0-indexed__ binary string array `` bank `` representing the floor plan of the bank, which is an `` m x n `` 2D matrix. `` bank[i] `` represents the <code>i<sup>th</sup></code> row, consisting of `` '0' ``s and `` '1' ``s. `` '0' `` means the cell is empty, while`` '1' `` means the cell has a security device.

There is __one__ laser beam between any __two__ security devices __if both__ conditions are met:

*   The two devices are located on two __different rows__: <code>r<sub>1</sub></code> and <code>r<sub>2</sub></code>, where <code>r<sub>1</sub> < r<sub>2</sub></code>.
*   For __each__ row `` i `` where <code>r<sub>1</sub> < i < r<sub>2</sub></code>, there are __no security devices__ in the <code>i<sup>th</sup></code> row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return _the total number of laser beams in the bank_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg" style="width: 400px; height: 368px;"/>

```
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0<sup>th</sup> row with any on the 3<sup>rd</sup> row.
This is because the 2<sup>nd</sup> row contains security devices, which breaks the second condition.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg" style="width: 244px; height: 325px;"/>

```
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
```

 

__Constraints:__

*   `` m == bank.length ``
*   `` n == bank[i].length ``
*   `` 1 <= m, n <= 500 ``
*   `` bank[i][j] `` is either `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 224,484 | 192,792 | 85.9% |