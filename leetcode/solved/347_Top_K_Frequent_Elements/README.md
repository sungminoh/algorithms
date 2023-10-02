### [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/?envType=daily-question&envId=2023-05-22)

Medium

Given an integer array `` nums `` and an integer `` k ``, return _the_ `` k `` _most frequent elements_. You may return the answer in __any order__.

 

<strong class="example">Example 1:</strong>

```Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

<strong class="example">Example 2:</strong>

```Input: nums = [1], k = 1
Output: [1]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` k `` is in the range `` [1, the number of unique elements in the array] ``.
*   It is __guaranteed__ that the answer is __unique__.

 

__Follow up:__ Your algorithm's time complexity must be better than `` O(n log n) ``, where n is the array's size.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,686,569 | 1,695,657 | 63.1% |