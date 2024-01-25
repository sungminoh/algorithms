### [943. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/?envType=daily-question&envId=2024-01-20)

Medium

Given an array of integers arr, find the sum of `` min(b) ``, where `` b `` ranges over every (contiguous) subarray of `` arr ``. Since the answer may be large, return the answer __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

<strong class="example">Example 2:</strong>

```
Input: arr = [11,81,94,43,3]
Output: 444
```

 

__Constraints:__

*   <code>1 <= arr.length <= 3 * 10<sup>4</sup></code>
*   <code>1 <= arr[i] <= 3 * 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 634,958 | 237,840 | 37.5% |