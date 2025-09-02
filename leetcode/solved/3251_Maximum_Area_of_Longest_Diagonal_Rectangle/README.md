### [3251. Maximum Area of Longest Diagonal Rectangle](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26)

Easy

You are given a 2D __0-indexed __integer array `` dimensions ``.

For all indices `` i ``, `` 0 <= i < dimensions.length ``, `` dimensions[i][0] `` represents the length and `` dimensions[i][1] `` represents the width of the rectangle<span style="font-size: 13.3333px;"> `` i ``</span>.

Return _the __area__ of the rectangle having the __longest__ diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the __maximum__ area._

 

<strong class="example">Example 1:</strong>

```
Input: dimensions = [[9,3],[8,6]]
Output: 48
Explanation: 
For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈<!-- notionvc: 882cf44c-3b17-428e-9c65-9940810216f1 --> 9.487.
For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.
```

<strong class="example">Example 2:</strong>

```
Input: dimensions = [[3,4],[4,3]]
Output: 12
Explanation: Length of diagonal is the same for both which is 5, so maximum area = 12.
```

 

__Constraints:__

<ul><li><code>1 <= dimensions.length <= 100</code></li><li><code><font face="monospace">dimensions[i].length == 2</font></code></li><li><code><font face="monospace">1 <= dimensions[i][0], dimensions[i][1] <= 100</font></code></li></ul>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 378,326 | 173,285 | 45.8% |