### [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/)

Easy

You have a set of integers `` s ``, which originally contains all the numbers from `` 1 `` to `` n ``. Unfortunately, due to some error, one of the numbers in `` s `` got duplicated to another number in the set, which results in __repetition of one__ number and __loss of another__ number.

You are given an integer array `` nums `` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return _them in the form of an array_.

 

<strong class="example">Example 1:</strong>

```Input: nums = [1,2,2,4]
Output: [2,3]
```

<strong class="example">Example 2:</strong>

```Input: nums = [1,1]
Output: [1,2]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>4</sup></code>
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 580,319 | 249,475 | 43.0% |