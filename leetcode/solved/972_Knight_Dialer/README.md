### [972. Knight Dialer](https://leetcode.com/problems/knight-dialer/description/?envType=daily-question&envId=2023-11-27)

Medium

The chess knight has a __unique movement__, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an __L__). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="width: 402px; height: 402px;"/>

We have a chess knight and a phone pad as shown below, the knight __can only stand on a numeric cell__ (i.e. blue cell).

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="width: 242px; height: 322px;"/>

Given an integer `` n ``, return how many distinct phone numbers of length `` n `` we can dial.

You are allowed to place the knight __on any numeric cell__ initially and then you should perform `` n - 1 `` jumps to dial a number of length `` n ``. All jumps should be __valid__ knight jumps.

As the answer may be very large, __return the answer modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
```

<strong class="example">Example 2:</strong>

```
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
```

<strong class="example">Example 3:</strong>

```
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
```

 

__Constraints:__

*   `` 1 <= n <= 5000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 279,350 | 167,001 | 59.8% |