### [917. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

Medium

You are given an array `` people `` where `` people[i] `` is the weight of the <code>i<sup>th</sup></code> person, and an __infinite number of boats__ where each boat can carry a maximum weight of `` limit ``. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `` limit ``.

Return _the minimum number of boats to carry every given person_.

 

<strong class="example">Example 1:</strong>

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

<strong class="example">Example 2:</strong>

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

<strong class="example">Example 3:</strong>

```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

 

__Constraints:__

*   <code>1 <= people.length <= 5 * 10<sup>4</sup></code>
*   <code>1 <= people[i] <= limit <= 3 * 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 451,799 | 252,249 | 55.8% |