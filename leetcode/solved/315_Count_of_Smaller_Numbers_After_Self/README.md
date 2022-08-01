### [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

Hard

You are given an integer array `` nums `` and you have to return a new `` counts `` array. The `` counts `` array has the property where `` counts[i] `` is the number of smaller elements to the right of `` nums[i] ``.

 

__Example 1:__

```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is only <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
```

__Example 2:__

```
Input: nums = [-1]
Output: [0]
```

__Example 3:__

```
Input: nums = [-1,-1]
Output: [0,0]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 628,075 | 269,493 | 42.9% |