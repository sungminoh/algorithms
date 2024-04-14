### [779. Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/)

Hard

You are given an integer array `` arr ``.

We split `` arr `` into some number of __chunks__ (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return _the largest number of chunks we can make to sort the array_.

 

<strong class="example">Example 1:</strong>

```
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
```

<strong class="example">Example 2:</strong>

```
Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
```

 

__Constraints:__

*   `` 1 <= arr.length <= 2000 ``
*   <code>0 <= arr[i] <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 116,538 | 61,984 | 53.2% |