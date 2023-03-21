### [1580. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)

Easy

Given the array `` nums `` consisting of `` 2n `` elements in the form <code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code>.

_Return the array in the form_ <code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code>.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 then the answer is [2,3,5,4,1,7].
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
```

 

__Constraints:__

*   `` 1 <= n <= 500 ``
*   `` nums.length == 2n ``
*   `` 1 <= nums[i] <= 10^3 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 571,800 | 509,121 | 89.0% |