### [335. Self Crossing](https://leetcode.com/problems/self-crossing/)

Hard

You are given an array _x_ of `` n `` positive numbers. You start at point `` (0,0) `` and moves `` x[0] `` metres to the north, then `` x[1] `` metres to the west, `` x[2] `` metres to the south, `` x[3] `` metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with `` O(1) `` extra space to determine, if your path crosses itself, or not.

 

__Example 1:__

<strong>┌───┐
    │   │
    └───┼──>
        │
    
    Input: </strong>[2,1,1,2]
    <strong>Output: </strong>true

__Example 2:__

<strong>┌──────┐
    │      │
    │
    │
    └────────────>
    
    Input:</strong> [1,2,3,4]
    <strong>Output: </strong>false 

__Example 3:__

<strong>┌───┐
    │   │
    └───┼>
    
    Input:</strong> [1,1,1,1]
    <strong>Output:</strong> true 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,942 | 23,461 | 28.3% |