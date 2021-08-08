### [1829. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

Easy

You are assigned to put some amount of boxes onto __one truck__. You are given a 2D array `` boxTypes ``, where <code>boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]</code>:

*   <code>numberOfBoxes<sub>i</sub></code> is the number of boxes of type `` i ``.
*   <code>numberOfUnitsPerBox<sub>i</sub></code><sub> </sub>is the number of units in each box of the type `` i ``.

You are also given an integer `` truckSize ``, which is the __maximum__ number of __boxes__ that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `` truckSize ``.

Return _the __maximum__ total number of __units__ that can be put on the truck._

 

__Example 1:__

```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```

__Example 2:__

```
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
```

 

__Constraints:__

*   `` 1 <= boxTypes.length <= 1000 ``
*   <code>1 <= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> <= 1000</code>
*   <code>1 <= truckSize <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 91,384 | 66,217 | 72.5% |