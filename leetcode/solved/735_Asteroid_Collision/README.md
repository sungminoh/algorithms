### [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

Medium

We are given an array `` asteroids `` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

__Example 1:__  

```
<b>Input:</b> 
asteroids = [5, 10, -5]
<b>Output:</b> [5, 10]
<b>Explanation:</b> 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
```

__Example 2:__  

```
<b>Input:</b> 
asteroids = [8, -8]
<b>Output:</b> []
<b>Explanation:</b> 
The 8 and -8 collide exploding each other.
```

__Example 3:__  

```
<b>Input:</b> 
asteroids = [10, 2, -5]
<b>Output:</b> [10]
<b>Explanation:</b> 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
```

__Example 4:__  

```
<b>Input:</b> 
asteroids = [-2, -1, 1, 2]
<b>Output:</b> [-2, -1, 1, 2]
<b>Explanation:</b> 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
```

__Note:__<li>The length of <code>asteroids</code> will be at most <code>10000</code>.</li><li>Each asteroid will be a non-zero integer in the range <code>[-1000, 1000].</code>.</li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 160,275 | 65,839 | 41.1% |