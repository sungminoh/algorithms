### [853. Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/description/?envType=daily-question&envId=2024-06-18)

Medium

You have `` n `` jobs and `` m `` workers. You are given three arrays: `` difficulty ``, `` profit ``, and `` worker `` where:

*   `` difficulty[i] `` and `` profit[i] `` are the difficulty and the profit of the <code>i<sup>th</sup></code> job, and
*   `` worker[j] `` is the ability of <code>j<sup>th</sup></code> worker (i.e., the <code>j<sup>th</sup></code> worker can only complete a job with difficulty at most `` worker[j] ``).

Every worker can be assigned __at most one job__, but one job can be __completed multiple times__.

*   For example, if three workers attempt the same job that pays `` $1 ``, then the total profit will be `` $3 ``. If a worker cannot complete any job, their profit is `` $0 ``.

Return the maximum profit we can achieve after assigning the workers to the jobs.

 

<strong class="example">Example 1:</strong>

```
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
```

<strong class="example">Example 2:</strong>

```
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
```

 

__Constraints:__

*   `` n == difficulty.length ``
*   `` n == profit.length ``
*   `` m == worker.length ``
*   <code>1 <= n, m <= 10<sup>4</sup></code>
*   <code>1 <= difficulty[i], profit[i], worker[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 364,089 | 203,448 | 55.9% |