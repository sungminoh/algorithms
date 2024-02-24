### [2107. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2023-11-16)

Medium

Given an array of strings `` nums `` containing `` n `` __unique__ binary strings each of length `` n ``, return _a binary string of length _`` n ``_ that __does not appear__ in _`` nums ``_. If there are multiple answers, you may return __any__ of them_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
```

<strong class="example">Example 2:</strong>

```
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
```

<strong class="example">Example 3:</strong>

```
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```

 

__Constraints:__

*   `` n == nums.length ``
*   `` 1 <= n <= 16 ``
*   `` nums[i].length == n ``
*   `` nums[i]  ``is either `` '0' `` or `` '1' ``.
*   All the strings of `` nums `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 175,399 | 130,691 | 74.5% |