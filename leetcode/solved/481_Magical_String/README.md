### [481. Magical String](https://leetcode.com/problems/magical-string/)

Medium

A magical string __S__ consists of only '1' and '2' and obeys the following rules:

The string __S__ is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string __S__ itself.

The first few elements of string __S__ is the following:__S__ = "1221121221221121122……"

If we group the consecutive '1's and '2's in __S__, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the __S__ itself. 

Given an integer N as input, return the number of '1's in the first N number in the magical string __S__.

__Note:__N will not exceed 100,000.

__Example 1:__  

```
<b>Input:</b> 6
<b>Output:</b> 3
<b>Explanation:</b> The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 45,955 | 21,707 | 47.2% |