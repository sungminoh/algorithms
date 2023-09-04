### [319. Bulb Switcher](https://leetcode.com/problems/bulb-switcher/?envType=daily-question&envId=2023-04-27)

Medium

There are `` n `` bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the <code>i<sup>th</sup></code> round, you toggle every `` i `` bulb. For the <code>n<sup>th</sup></code> round, you only toggle the last bulb.

Return _the number of bulbs that are on after `` n `` rounds_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg" style="width: 421px; height: 321px;"/>

```
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
```

<strong class="example">Example 2:</strong>

```
Input: n = 0
Output: 0
```

<strong class="example">Example 3:</strong>

```
Input: n = 1
Output: 1
```

 

__Constraints:__

*   <code>0 <= n <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 380,489 | 199,963 | 52.6% |