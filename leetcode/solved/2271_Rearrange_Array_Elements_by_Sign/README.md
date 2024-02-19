### [2271. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14)

Medium

You are given a __0-indexed__ integer array `` nums `` of __even__ length consisting of an __equal__ number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

1.   Every __consecutive pair__ of integers have __opposite signs__.
2.   For all integers with the same sign, the __order__ in which they were present in `` nums `` is __preserved__.
3.   The rearranged array begins with a positive integer.

Return _the modified array after rearranging the elements to satisfy the aforementioned conditions_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
```

<strong class="example">Example 2:</strong>

```
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
```

 

__Constraints:__

*   <code>2 <= nums.length <= 2 * 10<sup>5</sup></code>
*   `` nums.length `` is __even__
*   <code>1 <= |nums[i]| <= 10<sup>5</sup></code>
*   `` nums `` consists of __equal__ number of positive and negative integers.

 
It is not required to do the modifications in-place.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 353,239 | 296,461 | 83.9% |