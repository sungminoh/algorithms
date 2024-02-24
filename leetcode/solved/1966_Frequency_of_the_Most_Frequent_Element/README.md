### [1966. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/?envType=daily-question&envId=2023-11-18)

Medium

The __frequency__ of an element is the number of times it occurs in an array.

You are given an integer array `` nums `` and an integer `` k ``. In one operation, you can choose an index of `` nums `` and increment the element at that index by `` 1 ``.

Return _the __maximum possible frequency__ of an element after performing __at most__ _`` k ``_ operations_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [3,9,6], k = 2
Output: 1
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>
*   <code>1 <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 280,395 | 127,367 | 45.4% |