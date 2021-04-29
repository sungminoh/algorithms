### [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)

Medium

You are given a nested list of integers `` nestedList ``. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `` NestedIterator `` class:

*   `` NestedIterator(List<NestedInteger> nestedList) `` Initializes the iterator with the nested list `` nestedList ``.
*   `` int next() `` Returns the next integer in the nested list.
*   `` boolean hasNext() `` Returns `` true `` if there are still some integers in the nested list and `` false `` otherwise.

 

__Example 1:__

```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```

__Example 2:__

```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```

 

__Constraints:__

*   `` 1 <= nestedList.length <= 500 ``
*   The values of the integers in the nested list is in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 403,234 | 225,673 | 56.0% |