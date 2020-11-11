### [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)

Hard

Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache.

Implement the `` LFUCache `` class:

*   `` LFUCache(int capacity) `` Initializes the object with the `` capacity `` of the data structure.
*   `` int get(int key) `` Gets the value of the `` key `` if the `` key `` exists in the cache. Otherwise, returns `` -1 ``.
*   `` void put(int key, int value) `` Sets or inserts the value if the `` key `` is not already present. When the cache reaches its `` capacity ``, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), __the least recently__ used `` key `` would be evicted.

__Notice that__ the number of times an item is used is the number of calls to the `` get `` and `` put `` functions for that item since it was inserted. This number is set to zero when the item is removed.

__Follow up:__  
Could you do both operations in __O(1)__ time complexity?

 

__Example 1:__

```
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // return 1
lFUCache.put(3, 3);   // evicts key 2
lFUCache.get(2);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.put(4, 4);   // evicts key 1.
lFUCache.get(1);      // return -1 (not found)
lFUCache.get(3);      // return 3
lFUCache.get(4);      // return 4

```

 

__Constraints:__

*   <code>0 <= capacity, key, value <= 10<sup>4</sup></code>
*   At most <code>10<sup>5</sup></code> calls will be made to `` get `` and `` put ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 240,824 | 84,097 | 34.9% |