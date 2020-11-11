### [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)

Medium

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any __one__ of them.

Two trees are duplicate if they have the same structure with same node values.

__Example 1: __

```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
```

The following are two duplicate subtrees:

```
      2
     /
    4
```

and

```
    4
```


Therefore, you need to return above trees' root in the form of a list.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 123,773 | 61,695 | 49.8% |