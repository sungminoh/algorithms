### [1503. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/)

Hard

A chef has collected data on the `` satisfaction `` level of his `` n `` dishes. Chef can cook any dish in 1 unit of time.

__Like-time coefficient__ of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. `` time[i] * satisfaction[i] ``.

Return _the maximum sum of __like-time coefficient__ that the chef can obtain after dishes preparation_.

Dishes can be prepared in __any __order and the chef can discard some dishes to get this maximum value.

 

<strong class="example">Example 1:</strong>

```
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.
```

<strong class="example">Example 2:</strong>

```
Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
```

<strong class="example">Example 3:</strong>

```
Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.
```

 

__Constraints:__

*   `` n == satisfaction.length ``
*   `` 1 <= n <= 500 ``
*   `` -1000 <= satisfaction[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 143,763 | 110,608 | 76.9% |