### [1121. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/description/?envType=daily-question&envId=2024-02-03)

Medium

Given an integer array `` arr ``, partition the array into (contiguous) subarrays of length __at most__ `` k ``. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return _the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a __32-bit__ integer._

 

<strong class="example">Example 1:</strong>

```
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
```

<strong class="example">Example 2:</strong>

```
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
```

<strong class="example">Example 3:</strong>

```
Input: arr = [1], k = 1
Output: 1
```

 

__Constraints:__

*   `` 1 <= arr.length <= 500 ``
*   <code>0 <= arr[i] <= 10<sup>9</sup></code>
*   `` 1 <= k <= arr.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 222,756 | 170,389 | 76.5% |