### [1031. Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)

Easy

The __array-form__ of an integer `` num `` is an array representing its digits in left to right order.

*   For example, for `` num = 1321 ``, the array form is `` [1,3,2,1] ``.

Given `` num ``, the __array-form__ of an integer, and an integer `` k ``, return _the __array-form__ of the integer_ `` num + k ``.

 

<strong class="example">Example 1:</strong>

```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

<strong class="example">Example 2:</strong>

```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

<strong class="example">Example 3:</strong>

```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

 

__Constraints:__

*   <code>1 <= num.length <= 10<sup>4</sup></code>
*   `` 0 <= num[i] <= 9 ``
*   `` num `` does not contain any leading zeros except for the zero itself.
*   <code>1 <= k <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 470,103 | 221,418 | 47.1% |