### [2413. Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=daily-question&envId=2023-04-25)

Medium

You have a set which contains all positive integers `` [1, 2, 3, 4, 5, ...] ``.

Implement the `` SmallestInfiniteSet `` class:

*   `` SmallestInfiniteSet() `` Initializes the __SmallestInfiniteSet__ object to contain __all__ positive integers.
*   `` int popSmallest() `` __Removes__ and returns the smallest integer contained in the infinite set.
*   `` void addBack(int num) `` __Adds__ a positive integer `` num `` back into the infinite set, if it is __not__ already in the infinite set.

 

<strong class="example">Example 1:</strong>

```
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
```

 

__Constraints:__

*   `` 1 <= num <= 1000 ``
*   At most `` 1000 `` calls will be made __in total__ to `` popSmallest `` and `` addBack ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 134,122 | 98,991 | 73.8% |