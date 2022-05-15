### [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)

Medium

Design an iterator that supports the `` peek `` operation on an existing iterator in addition to the `` hasNext `` and the `` next `` operations.

Implement the `` PeekingIterator `` class:

*   `` PeekingIterator(Iterator<int> nums) `` Initializes the object with the given integer iterator `` iterator ``.
*   `` int next() `` Returns the next element in the array and moves the pointer to the next element.
*   `` boolean hasNext() `` Returns `` true `` if there are still elements in the array.
*   `` int peek() `` Returns the next element in the array __without__ moving the pointer.

__Note:__ Each language may have a different implementation of the constructor and `` Iterator ``, but they all support the `` int next() `` and `` boolean hasNext() `` functions.

 

__Example 1:__

```
Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [<u>1</u>,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,<u>2</u>,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,<u>2</u>,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,<u>3</u>]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   `` 1 <= nums[i] <= 1000 ``
*   All the calls to `` next `` and `` peek `` are valid.
*   At most `` 1000 `` calls will be made to `` next ``, `` hasNext ``, and `` peek ``.

 
__Follow up:__ How would you extend your design to be generic and work with all types, not just integer?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 333,290 | 191,971 | 57.6% |