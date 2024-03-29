### [1184. Car Pooling](https://leetcode.com/problems/car-pooling/)

Medium

There is a car with `` capacity `` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `` capacity `` and an array `` trips `` where <code>trips[i] = [numPassengers<sub>i</sub>, from<sub>i</sub>, to<sub>i</sub>]</code> indicates that the <code>i<sup>th</sup></code> trip has <code>numPassengers<sub>i</sub></code> passengers and the locations to pick them up and drop them off are <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `` true ``_ if it is possible to pick up and drop off all passengers for all the given trips, or _`` false ``_ otherwise_.

 

__Example 1:__

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

__Example 2:__

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

 

__Constraints:__

*   `` 1 <= trips.length <= 1000 ``
*   `` trips[i].length == 3 ``
*   <code>1 <= numPassengers<sub>i</sub> <= 100</code>
*   <code>0 <= from<sub>i</sub> < to<sub>i</sub> <= 1000</code>
*   <code>1 <= capacity <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 232,944 | 137,005 | 58.8% |