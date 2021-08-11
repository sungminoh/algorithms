### [1464. Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/)

Medium

You are given an integer array `` arr ``. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return _the minimum size of the set so that __at least__ half of the integers of the array are removed_.

 

__Example 1:__

```
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
```

__Example 2:__

```
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
```

__Example 3:__

```
Input: arr = [1,9]
Output: 1
```

__Example 4:__

```
Input: arr = [1000,1000,3,7]
Output: 1
```

__Example 5:__

```
Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
```

 

__Constraints:__

*   <code>1 <= arr.length <= 10<sup>5</sup></code>
*   `` arr.length `` is even.
*   <code>1 <= arr[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 104,346 | 71,383 | 68.4% |