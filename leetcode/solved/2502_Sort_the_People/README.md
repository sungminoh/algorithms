### [2502. Sort the People](https://leetcode.com/problems/sort-the-people/description/?envType=daily-question&envId=2024-07-22)

Easy

You are given an array of strings `` names ``, and an array `` heights `` that consists of __distinct__ positive integers. Both arrays are of length `` n ``.

For each index `` i ``, `` names[i] `` and `` heights[i] `` denote the name and height of the <code>i<sup>th</sup></code> person.

Return `` names ``_ sorted in __descending__ order by the people's heights_.

 

<strong class="example">Example 1:</strong>

```
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
```

<strong class="example">Example 2:</strong>

```
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
```

 

__Constraints:__

*   `` n == names.length == heights.length ``
*   <code>1 <= n <= 10<sup>3</sup></code>
*   `` 1 <= names[i].length <= 20 ``
*   <code>1 <= heights[i] <= 10<sup>5</sup></code>
*   `` names[i] `` consists of lower and upper case English letters.
*   All the values of `` heights `` are distinct.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 344,837 | 293,355 | 85.1% |