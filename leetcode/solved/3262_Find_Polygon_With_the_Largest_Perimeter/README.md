### [3262. Find Polygon With the Largest Perimeter](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15)

Medium

You are given an array of __positive__ integers `` nums `` of length `` n ``.

A __polygon__ is a closed plane figure that has at least `` 3 `` sides. The __longest side__ of a polygon is __smaller__ than the sum of its other sides.

Conversely, if you have `` k `` (`` k >= 3 ``) __positive__ real numbers <code>a<sub>1</sub></code>, <code>a<sub>2</sub></code>, <code>a<sub>3</sub></code>, ..., <code>a<sub>k</sub></code> where <code>a<sub>1</sub> <= a<sub>2</sub> <= a<sub>3</sub> <= ... <= a<sub>k</sub></code> __and__ <code>a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub> + ... + a<sub>k-1</sub> > a<sub>k</sub></code>, then there __always__ exists a polygon with `` k `` sides whose lengths are <code>a<sub>1</sub></code>, <code>a<sub>2</sub></code>, <code>a<sub>3</sub></code>, ..., <code>a<sub>k</sub></code>.

The __perimeter__ of a polygon is the sum of lengths of its sides.

Return _the __largest__ possible __perimeter__ of a __polygon__ whose sides can be formed from_ `` nums ``, _or_ `` -1 `` _if it is not possible to create a polygon_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
```

 

__Constraints:__

*   <code>3 <= n <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 187,786 | 124,006 | 66.0% |