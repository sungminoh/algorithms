### [2257. Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/)

Hard

You have `` n `` flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two __0-indexed__ integer arrays `` plantTime `` and `` growTime ``, of length `` n `` each:

*   `` plantTime[i] `` is the number of __full days__ it takes you to __plant__ the <code>i<sup>th</sup></code> seed. Every day, you can work on planting exactly one seed. You __do not__ have to work on planting the same seed on consecutive days, but the planting of a seed is not complete __until__ you have worked `` plantTime[i] `` days on planting it in total.
*   `` growTime[i] `` is the number of __full days__ it takes the <code>i<sup>th</sup></code> seed to grow after being completely planted. __After__ the last day of its growth, the flower __blooms__ and stays bloomed forever.

From the beginning of day `` 0 ``, you can plant the seeds in __any__ order.

Return _the __earliest__ possible day where __all__ seeds are blooming_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/1.png" style="width: 453px; height: 149px;"/>

```
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0<sup>th</sup> seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1<sup>st</sup> seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2<sup>nd</sup> seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/2.png" style="width: 454px; height: 184px;"/>

```
Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 1, plant the 0<sup>th</sup> seed. The seed grows for 2 full days and blooms on day 4.
On days 0 and 3, plant the 1<sup>st</sup> seed. The seed grows for 1 full day and blooms on day 5.
On days 2, 4, and 5, plant the 2<sup>nd</sup> seed. The seed grows for 2 full days and blooms on day 8.
On days 6 and 7, plant the 3<sup>rd</sup> seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.
```

<strong class="example">Example 3:</strong>

```
Input: plantTime = [1], growTime = [1]
Output: 2
Explanation: On day 0, plant the 0<sup>th</sup> seed. The seed grows for 1 full day and blooms on day 2.
Thus, on day 2, all the seeds are blooming.
```

 

__Constraints:__

*   `` n == plantTime.length == growTime.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= plantTime[i], growTime[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 58,268 | 43,761 | 75.1% |