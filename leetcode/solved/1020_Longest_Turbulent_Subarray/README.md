### [1020. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)

Medium

Given an integer array `` arr ``, return _the length of a maximum size turbulent subarray of_ `` arr ``.

A subarray is __turbulent__ if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `` [arr[i], arr[i + 1], ..., arr[j]] `` of `` arr `` is said to be turbulent if and only if:

*   For `` i <= k < j ``:	
    
    *   `` arr[k] > arr[k + 1] `` when `` k `` is odd, and
    *   `` arr[k] < arr[k + 1] `` when `` k `` is even.
    
    
    
*   Or, for `` i <= k < j ``:	
    
    *   `` arr[k] > arr[k + 1] `` when `` k `` is even, and
    *   `` arr[k] < arr[k + 1] `` when `` k `` is odd.
    
    
    

 

__Example 1:__

```
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```

__Example 2:__

```
Input: arr = [4,8,12,16]
Output: 2
```

__Example 3:__

```
Input: arr = [100]
Output: 1
```

 

__Constraints:__

*   <code>1 <= arr.length <= 4 * 10<sup>4</sup></code>
*   <code>0 <= arr[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 138,248 | 65,697 | 47.5% |