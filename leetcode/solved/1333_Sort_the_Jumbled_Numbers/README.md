### [1333. Sort the Jumbled Numbers](https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24)

Medium

You are given a __0-indexed__ integer array `` mapping `` which represents the mapping rule of a shuffled decimal system. `` mapping[i] = j `` means digit `` i `` should be mapped to digit `` j `` in this system.

The __mapped value__ of an integer is the new integer obtained by replacing each occurrence of digit `` i `` in the integer with `` mapping[i] `` for all `` 0 <= i <= 9 ``.

You are also given another integer array `` nums ``. Return _the array _`` nums ``_ sorted in __non-decreasing__ order based on the __mapped values__ of its elements._

__Notes:__

*   Elements with the same mapped values should appear in the __same relative order__ as in the input.
*   The elements of `` nums `` should only be sorted based on their mapped values and __not be replaced__ by them.

 

<strong class="example">Example 1:</strong>

```
Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]
Explanation: 
Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].
```

<strong class="example">Example 2:</strong>

```
Input: mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
Output: [123,456,789]
Explanation: 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].
```

 

__Constraints:__

*   `` mapping.length == 10 ``
*   `` 0 <= mapping[i] <= 9 ``
*   All the values of `` mapping[i] `` are __unique__.
*   <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
*   <code>0 <= nums[i] < 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 237,150 | 142,935 | 60.3% |