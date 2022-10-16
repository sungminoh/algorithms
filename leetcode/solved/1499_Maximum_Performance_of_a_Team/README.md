### [1499. Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

Hard

You are given two integers `` n `` and `` k `` and two integer arrays `` speed `` and `` efficiency `` both of length `` n ``. There are `` n `` engineers numbered from `` 1 `` to `` n ``. `` speed[i] `` and `` efficiency[i] `` represent the speed and efficiency of the <code>i<sup>th</sup></code> engineer respectively.

Choose __at most__ `` k `` different engineers out of the `` n `` engineers to form a team with the maximum __performance__.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return _the maximum performance of this team_. Since the answer can be a huge number, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
```

<strong class="example">Example 2:</strong>

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
```

<strong class="example">Example 3:</strong>

```
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
```

 

__Constraints:__

*   <code>1 <= k <= n <= 10<sup>5</sup></code>
*   `` speed.length == n ``
*   `` efficiency.length == n ``
*   <code>1 <= speed[i] <= 10<sup>5</sup></code>
*   <code>1 <= efficiency[i] <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 166,892 | 81,706 | 49.0% |