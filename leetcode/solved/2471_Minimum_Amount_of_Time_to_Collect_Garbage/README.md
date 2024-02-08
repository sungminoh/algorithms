### [2471. Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/?envType=daily-question&envId=2023-11-20)

Medium

You are given a __0-indexed__ array of strings `` garbage `` where `` garbage[i] `` represents the assortment of garbage at the <code>i<sup>th</sup></code> house. `` garbage[i] `` consists only of the characters `` 'M' ``, `` 'P' `` and `` 'G' `` representing one unit of metal, paper and glass garbage respectively. Picking up __one__ unit of any type of garbage takes `` 1 `` minute.

You are also given a __0-indexed__ integer array `` travel `` where `` travel[i] `` is the number of minutes needed to go from house `` i `` to house `` i + 1 ``.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house `` 0 `` and must visit each house __in order__; however, they do __not__ need to visit every house.

Only __one__ garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks __cannot__ do anything.

Return_ the __minimum__ number of minutes needed to pick up all the garbage._

 

<strong class="example">Example 1:</strong>

```
Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
Output: 21
Explanation:
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
```

<strong class="example">Example 2:</strong>

```
Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
Output: 37
Explanation:
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.
```

 

__Constraints:__

*   <code>2 <= garbage.length <= 10<sup>5</sup></code>
*   `` garbage[i] `` consists of only the letters `` 'M' ``, `` 'P' ``, and `` 'G' ``.
*   `` 1 <= garbage[i].length <= 10 ``
*   `` travel.length == garbage.length - 1 ``
*   `` 1 <= travel[i] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 141,407 | 121,426 | 85.9% |