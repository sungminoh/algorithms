### [1447. Jump Game IV](https://leetcode.com/problems/jump-game-iv/)

Hard

Given an array of integers `` arr ``, you are initially positioned at the first index of the array.

In one step you can jump from index `` i `` to index:

*   `` i + 1 `` where: `` i + 1 < arr.length ``.
*   `` i - 1 `` where: `` i - 1 >= 0 ``.
*   `` j `` where: `` arr[i] == arr[j] `` and `` i != j ``.

Return _the minimum number of steps_ to reach the __last index__ of the array.

Notice that you can not jump outside of the array at any time.

 

__Example 1:__

```
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
```

__Example 2:__

```
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
```

__Example 3:__

```
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
```

__Example 4:__

```
Input: arr = [6,1,9]
Output: 2
```

__Example 5:__

```
Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
```

 

__Constraints:__

*   <code>1 <= arr.length <= 5 * 10<sup>4</sup></code>
*   <code>-10<sup>8</sup> <= arr[i] <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 88,145 | 37,152 | 42.1% |