### [1604. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16)

Medium

Given an array of integers `` arr `` and an integer `` k ``. Find the _least number of unique integers_ after removing __exactly__ `` k `` elements__.__

 

<strong class="example">Example 1:</strong>

```
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```

<strong class="example">Example 2:</strong>

```
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```

 

__Constraints:__

*   `` 1 <= arr.length <= 10^5 ``
*   `` 1 <= arr[i] <= 10^9 ``
*   `` 0 <= k <= arr.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 367,573 | 230,500 | 62.7% |