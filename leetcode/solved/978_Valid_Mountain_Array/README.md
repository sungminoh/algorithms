### [978. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)

Easy

Given an array of integers `` arr ``, return _`` true `` if and only if it is a valid mountain array_.

Recall that arr is a mountain array if and only if:

*   `` arr.length >= 3 ``
*   There exists some `` i `` with `` 0 < i < arr.length - 1 `` such that:	
    
    *   `` arr[0] < arr[1] < ... < arr[i - 1] < arr[i]  ``
    *   `` arr[i] > arr[i + 1] > ... > arr[arr.length - 1] ``
    
    
    

<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500"/>

 

__Example 1:__

```Input: arr = [2,1]
Output: false
```

__Example 2:__

```Input: arr = [3,5,5]
Output: false
```

__Example 3:__

```Input: arr = [0,3,2,1]
Output: true
```

 

__Constraints:__

*   <code>1 <= arr.length <= 10<sup>4</sup></code>
*   <code>0 <= arr[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 802,403 | 272,130 | 33.9% |