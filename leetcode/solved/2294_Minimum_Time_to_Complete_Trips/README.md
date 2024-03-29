### [2294. Minimum Time to Complete Trips](https://leetcode.com/problems/minimum-time-to-complete-trips/)

Medium

You are given an array `` time `` where `` time[i] `` denotes the time taken by the <code>i<sup>th</sup></code> bus to complete __one trip__.

Each bus can make multiple trips __successively__; that is, the next trip can start __immediately after__ completing the current trip. Also, each bus operates __independently__; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `` totalTrips ``, which denotes the number of trips all buses should make __in total__. Return _the __minimum time__ required for all buses to complete __at least__ _`` totalTrips ``_ trips_.

 

<strong class="example">Example 1:</strong>

```
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.
```

<strong class="example">Example 2:</strong>

```
Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.
```

 

__Constraints:__

*   <code>1 <= time.length <= 10<sup>5</sup></code>
*   <code>1 <= time[i], totalTrips <= 10<sup>7</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 242,403 | 95,054 | 39.2% |