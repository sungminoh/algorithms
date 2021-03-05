### [1629. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)

Hard

Given a string `` num `` representing __the digits__ of a very large integer and an integer `` k ``.

You are allowed to swap any two adjacent digits of the integer __at most__ `` k `` times.

Return _the minimum integer_ you can obtain also as a string.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg" style="width: 500px; height: 40px;"/>

```
Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
```

__Example 2:__

```
Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
```

__Example 3:__

```
Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.
```

__Example 4:__

```
Input: num = "22", k = 22
Output: "22"
```

__Example 5:__

```
Input: num = "9438957234785635408", k = 23
Output: "0345989723478563548"
```

 

__Constraints:__

*   `` 1 <= num.length <= 30000 ``
*   `` num `` contains __digits__ only and doesn't have __leading zeros__.
*   `` 1 <= k <= 10^9 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 14,762 | 5,401 | 36.6% |