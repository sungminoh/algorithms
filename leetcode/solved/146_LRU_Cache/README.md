### [146. LRU Cache](https://leetcode.com/problems/lru-cache/description/)

Medium

Design a data structure that follows the constraints of a __<a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a>__.

Implement the `` LRUCache `` class:

*   `` LRUCache(int capacity) `` Initialize the LRU cache with __positive__ size `` capacity ``.
*   `` int get(int key) `` Return the value of the `` key `` if the key exists, otherwise return `` -1 ``.
*   `` void put(int key, int value) `` Update the value of the `` key `` if the `` key `` exists. Otherwise, add the `` key-value `` pair to the cache. If the number of keys exceeds the `` capacity `` from this operation, __evict__ the least recently used key.

The functions `` get `` and `` put `` must each run in `` O(1) `` average time complexity.

 

<strong class="example">Example 1:</strong>

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

 

__Constraints:__

*   `` 1 <= capacity <= 3000 ``
*   <code>0 <= key <= 10<sup>4</sup></code>
*   <code>0 <= value <= 10<sup>5</sup></code>
*   At most <code>2 * 10<sup>5</sup></code> calls will be made to `` get `` and `` put ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,831,823 | 1,628,176 | 42.5% |