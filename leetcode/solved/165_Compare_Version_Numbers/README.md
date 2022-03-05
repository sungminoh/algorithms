### [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)

Medium

Given two version numbers, `` version1 `` and `` version2 ``, compare them.

Version numbers consist of __one or more revisions__ joined by a dot `` '.' ``. Each revision consists of __digits__ and may contain leading __zeros__. Every revision contains __at least one character__. Revisions are __0-indexed from left to right__, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example `` 2.5.33 `` and `` 0.1 `` are valid version numbers.

To compare version numbers, compare their revisions in __left-to-right order__. Revisions are compared using their __integer value ignoring any leading zeros__. This means that revisions `` 1 `` and `` 001 `` are considered __equal__. If a version number does not specify a revision at an index, then __treat the revision as `` 0 ``__. For example, version `` 1.0 `` is less than version `` 1.1 `` because their revision 0s are the same, but their revision 1s are `` 0 `` and `` 1 `` respectively, and `` 0 < 1 ``.

_Return the following:_

*   If `` version1 < version2 ``, return `` -1 ``.
*   If `` version1 > version2 ``, return `` 1 ``.
*   Otherwise, return `` 0 ``.

 

__Example 1:__

```
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
```

__Example 2:__

```
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
```

__Example 3:__

```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
```

 

__Constraints:__

*   `` 1 <= version1.length, version2.length <= 500 ``
*   `` version1 `` and `` version2 `` only contain digits and `` '.' ``.
*   `` version1 `` and `` version2 `` __are valid version numbers__.
*   All the given revisions in `` version1 `` and `` version2 `` can be stored in a __32-bit integer__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 899,024 | 308,176 | 34.3% |