### [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/?envType=daily-question&envId=2024-01-31)

Medium

Given an array of integers `` temperatures `` represents the daily temperatures, return _an array_ `` answer `` _such that_ `` answer[i] `` _is the number of days you have to wait after the_ <code>i<sup>th</sup></code> _day to get a warmer temperature_. If there is no future day for which this is possible, keep `` answer[i] == 0 `` instead.

 

<strong class="example">Example 1:</strong>

```Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

<strong class="example">Example 2:</strong>

```Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

<strong class="example">Example 3:</strong>

```Input: temperatures = [30,60,90]
Output: [1,1,0]
```

 

__Constraints:__

*   <code>1 <= temperatures.length <= 10<sup>5</sup></code>
*   `` 30 <= temperatures[i] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,347,596 | 889,141 | 66.0% |