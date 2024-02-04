### [1395. Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2023-12-03)

Easy

On a 2D plane, there are `` n `` points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return _the __minimum time__ in seconds to visit all the points in the order given by _`` points ``.

You can move according to these rules:

*   In `` 1 `` second, you can either:	
    
    *   move vertically by one unit,
    *   move horizontally by one unit, or
    *   move diagonally `` sqrt(2) `` units (in other words, move one unit vertically then one unit horizontally in `` 1 `` second).
    
    
    
*   You have to visit the points in the same order as they appear in the array.
*   You are allowed to pass through points that appear later in the order, but these do not count as visits.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;"/>

```
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```

<strong class="example">Example 2:</strong>

```
Input: points = [[3,2],[-2,2]]
Output: 5
```

 

__Constraints:__

*   `` points.length == n ``
*   `` 1 <= n <= 100 ``
*   `` points[i].length == 2 ``
*   `` -1000 <= points[i][0], points[i][1] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 270,324 | 223,066 | 82.5% |