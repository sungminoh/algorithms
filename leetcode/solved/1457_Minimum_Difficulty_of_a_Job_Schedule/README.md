### [1457. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/?envType=daily-question&envId=2023-12-29)

Hard

You want to schedule a list of jobs in `` d `` days. Jobs are dependent (i.e To work on the <code>i<sup>th</sup></code> job, you have to finish all the jobs `` j `` where `` 0 <= j < i ``).

You have to finish __at least__ one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `` d `` days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array `` jobDifficulty `` and an integer `` d ``. The difficulty of the <code>i<sup>th</sup></code> job is `` jobDifficulty[i] ``.

Return _the minimum difficulty of a job schedule_. If you cannot find a schedule for the jobs return `` -1 ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/untitled.png" style="width: 365px; height: 370px;"/>

```
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
```

<strong class="example">Example 2:</strong>

```
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
```

<strong class="example">Example 3:</strong>

```
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
```

 

__Constraints:__

*   `` 1 <= jobDifficulty.length <= 300 ``
*   `` 0 <= jobDifficulty[i] <= 1000 ``
*   `` 1 <= d <= 10 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 315,671 | 188,391 | 59.7% |