### [1352. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/?envType=daily-question&envId=2024-01-06)

Hard

We have `` n `` jobs, where every job is scheduled to be done from `` startTime[i] `` to `` endTime[i] ``, obtaining a profit of `` profit[i] ``.

You're given the `` startTime ``, `` endTime `` and `` profit `` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `` X `` you will be able to start another job that starts at time `` X ``.

 

<strong class="example">Example 1:</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png" style="width: 380px; height: 154px;"/></strong>

```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
```

<strong class="example">Example 2:</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png" style="width: 600px; height: 112px;"/> </strong>

```
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
```

<strong class="example">Example 3:</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png" style="width: 400px; height: 112px;"/></strong>

```
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
```

 

__Constraints:__

*   <code>1 <= startTime.length == endTime.length == profit.length <= 5 * 10<sup>4</sup></code>
*   <code>1 <= startTime[i] < endTime[i] <= 10<sup>9</sup></code>
*   <code>1 <= profit[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 521,358 | 285,781 | 54.8% |