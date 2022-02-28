### [1794. Minimize Deviation in Array](https://leetcode.com/problems/minimize-deviation-in-array/)

Hard

You are given an array `` nums `` of `` n `` positive integers.

You can perform two types of operations on any element of the array any number of times:

*   If the element is __even__, __divide__ it by `` 2 ``.	
    
    *   For example, if the array is `` [1,2,3,4] ``, then you can do this operation on the last element, and the array will be <code>[1,2,3,<u>2</u>].</code>
    
    
    
*   If the element is __odd__, __multiply__ it by `` 2 ``.	
    
    *   For example, if the array is `` [1,2,3,4] ``, then you can do this operation on the first element, and the array will be <code>[<u>2</u>,2,3,4].</code>
    
    
    

The __deviation__ of the array is the __maximum difference__ between any two elements in the array.

Return _the __minimum deviation__ the array can have after performing some number of operations._

 

__Example 1:__

```
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,<u>2</u>], then to [<u>2</u>,2,3,2], then the deviation will be 3 - 2 = 1.
```

__Example 2:__

```
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,<u>2</u>,5,<u>5</u>,3], then the deviation will be 5 - 2 = 3.
```

__Example 3:__

```
Input: nums = [2,10,8]
Output: 3
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>2 <= n <= 10<sup><span style="font-size: 10.8333px;">5</span></sup></code>
*   <code>1 <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 79,731 | 41,857 | 52.5% |