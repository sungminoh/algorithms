### [981. Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)

Easy

You are given an array of `` n `` strings `` strs ``, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

*   For example, `` strs = ["abc", "bce", "cae"] `` can be arranged as follows:

```
abc
bce
cae
```

You want to __delete__ the columns that are __not sorted lexicographically__. In the above example (__0-indexed__), columns 0 (`` 'a' ``, `` 'b' ``, `` 'c' ``) and 2 (`` 'c' ``, `` 'e' ``, `` 'e' ``) are sorted, while column 1 (`` 'b' ``, `` 'c' ``, `` 'a' ``) is not, so you would delete column 1.

Return _the number of columns that you will delete_.

 

<strong class="example">Example 1:</strong>

```
Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
```

<strong class="example">Example 2:</strong>

```
Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
```

<strong class="example">Example 3:</strong>

```
Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
```

 

__Constraints:__

*   `` n == strs.length ``
*   `` 1 <= n <= 100 ``
*   `` 1 <= strs[i].length <= 1000 ``
*   `` strs[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 224,539 | 167,980 | 74.8% |