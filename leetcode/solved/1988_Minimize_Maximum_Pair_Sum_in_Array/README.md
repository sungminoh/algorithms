### [1988. Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17)

Medium

The __pair sum__ of a pair `` (a,b) `` is equal to `` a + b ``. The __maximum pair sum__ is the largest __pair sum__ in a list of pairs.

*   For example, if we have pairs `` (1,5) ``, `` (2,3) ``, and `` (4,4) ``, the __maximum pair sum__ would be `` max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 ``.

Given an array `` nums `` of __even__ length `` n ``, pair up the elements of `` nums `` into `` n / 2 `` pairs such that:

*   Each element of `` nums `` is in __exactly one__ pair, and
*   The __maximum pair sum __is __minimized__.

Return _the minimized __maximum pair sum__ after optimally pairing up the elements_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   `` n `` is __even__.
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 204,298 | 166,587 | 81.5% |