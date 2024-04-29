### [1000. Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/)

Hard

You are given an array of `` n `` strings `` strs ``, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have `` strs = ["abcdef","uvwxyz"] `` and deletion indices `` {0, 2, 3} ``, then the final array after deletions is `` ["bef", "vyz"] ``.

Suppose we chose a set of deletion indices `` answer `` such that after deletions, the final array has __every string (row) in lexicographic__ order. (i.e., `` (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]) ``, and `` (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]) ``, and so on). Return _the minimum possible value of_ `` answer.length ``.

 

<strong class="example">Example 1:</strong>

```
Input: strs = ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]).
Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic order.
```

<strong class="example">Example 2:</strong>

```
Input: strs = ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row will not be lexicographically sorted.
```

<strong class="example">Example 3:</strong>

```
Input: strs = ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.
```

 

__Constraints:__

*   `` n == strs.length ``
*   `` 1 <= n <= 100 ``
*   `` 1 <= strs[i].length <= 100 ``
*   `` strs[i] `` consists of lowercase English letters.

*    

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 24,630 | 14,249 | 57.9% |