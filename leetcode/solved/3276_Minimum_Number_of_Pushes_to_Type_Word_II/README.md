### [3276. Minimum Number of Pushes to Type Word II](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2024-08-06)

Medium

You are given a string `` word `` containing lowercase English letters.

Telephone keypads have keys mapped with __distinct__ collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `` 2 `` is mapped with `` ["a","b","c"] ``, we need to push the key one time to type `` "a" ``, two times to type `` "b" ``, and three times to type `` "c" `` _._

It is allowed to remap the keys numbered `` 2 `` to `` 9 `` to __distinct__ collections of letters. The keys can be remapped to __any__ amount of letters, but each letter __must__ be mapped to __exactly__ one key. You need to find the __minimum__ number of times the keys will be pushed to type the string `` word ``.

Return _the __minimum__ number of pushes needed to type _`` word `` _after remapping the keys_.

An example mapping of letters to keys on a telephone keypad is given below. Note that `` 1 ``, `` * ``, `` # ``, and `` 0 `` do __not__ map to any letters.

<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png" style="width: 329px; height: 313px;"/>

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png" style="width: 329px; height: 313px;"/>

```
Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2024/08/20/edited.png" style="width: 329px; height: 313px;"/>

```
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png" style="width: 329px; height: 313px;"/>

```
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.
```

 

__Constraints:__

*   <code>1 <= word.length <= 10<sup>5</sup></code>
*   `` word `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 217,309 | 175,292 | 80.7% |