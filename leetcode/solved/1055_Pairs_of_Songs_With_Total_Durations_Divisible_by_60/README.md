### [1055. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

Medium

You are given a list of songs where the <code>i<sup>th</sup></code> song has a duration of `` time[i] `` seconds.

Return _the number of pairs of songs for which their total duration in seconds is divisible by_ `` 60 ``. Formally, we want the number of indices `` i ``, `` j `` such that `` i < j `` with `` (time[i] + time[j]) % 60 == 0 ``.

 

__Example 1:__

```
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

__Example 2:__

```
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
```

 

__Constraints:__

*   <code>1 <= time.length <= 6 * 10<sup>4</sup></code>
*   `` 1 <= time[i] <= 500 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 326,998 | 176,083 | 53.8% |