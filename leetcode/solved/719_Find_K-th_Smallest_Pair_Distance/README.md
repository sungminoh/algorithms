### [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14)

Hard

The __distance of a pair__ of integers `` a `` and `` b `` is defined as the absolute difference between `` a `` and `` b ``.

Given an integer array `` nums `` and an integer `` k ``, return _the_ <code>k<sup>th</sup></code> _smallest __distance among all the pairs___ `` nums[i] `` _and_ `` nums[j] `` _where_ `` 0 <= i < j < nums.length ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1<sup>st</sup> smallest distance pair is (1,1), and its distance is 0.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,1,1], k = 2
Output: 0
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,6,1], k = 3
Output: 5
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>2 <= n <= 10<sup>4</sup></code>
*   <code>0 <= nums[i] <= 10<sup>6</sup></code>
*   `` 1 <= k <= n * (n - 1) / 2 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 411,698 | 186,911 | 45.4% |