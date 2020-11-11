### [793. Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/)

Medium

In a string composed of `` 'L' ``, `` 'R' ``, and `` 'X' `` characters, like `` "RXXLRXRXL" ``, a move consists of either replacing one occurrence of `` "XL" `` with `` "LX" ``, or replacing one occurrence of `` "RX" `` with `` "XR" ``. Given the starting string `` start `` and the ending string `` end ``, return `` True `` if and only if there exists a sequence of moves to transform one string to the other.

 

__Example 1:__

```
Input: start = "X", end = "L"
Output: false
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```

__Example 2:__

```
Input: start = "LLR", end = "RRL"
Output: false
```

__Example 3:__

```
Input: start = "XLLR", end = "LXLX"
Output: false
```

 

__Constraints:__

*   <code>1 <= start.length <= 10<sup>4</sup></code>
*   `` start.length == end.length ``
*   Both `` start `` and `` end `` will only consist of characters in `` 'L' ``, `` 'R' ``, and `` 'X' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 81,792 | 28,497 | 34.8% |