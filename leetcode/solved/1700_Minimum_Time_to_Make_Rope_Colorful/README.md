### [1700. Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/?envType=daily-question&envId=2023-12-27)

Medium

Alice has `` n `` balloons arranged on a rope. You are given a __0-indexed__ string `` colors `` where `` colors[i] `` is the color of the <code>i<sup>th</sup></code> balloon.

Alice wants the rope to be __colorful__. She does not want __two consecutive balloons__ to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it __colorful__. You are given a __0-indexed__ integer array `` neededTime `` where `` neededTime[i] `` is the time (in seconds) that Bob needs to remove the <code>i<sup>th</sup></code> balloon from the rope.

Return _the __minimum time__ Bob needs to make the rope __colorful___.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;"/>

```
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;"/>

```
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;"/>

```
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
```

 

__Constraints:__

*   `` n == colors.length == neededTime.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= neededTime[i] <= 10<sup>4</sup></code>
*   `` colors `` contains only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 389,286 | 249,047 | 64.0% |