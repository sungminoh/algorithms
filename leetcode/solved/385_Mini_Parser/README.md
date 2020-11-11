### [385. Mini Parser](https://leetcode.com/problems/mini-parser/)

Medium

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

__Note:__You may assume that the string is well-formed:

*   String is non-empty.
*   String does not contain white spaces.
*   String contains only digits `` 0-9 ``, `` [ ``, `` - `` `` , ``, `` ] ``.

__Example 1:__

```
Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
```

__Example 2:__

```
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 109,339 | 36,197 | 33.1% |