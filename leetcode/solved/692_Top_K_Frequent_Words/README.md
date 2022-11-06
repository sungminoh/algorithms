### [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

Medium

Given an array of strings `` words `` and an integer `` k ``, return _the _`` k ``_ most frequent strings_.

Return the answer __sorted__ by __the frequency__ from highest to lowest. Sort the words with the same frequency by their __lexicographical order__.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

<strong class="example">Example 2:</strong>

```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

 

__Constraints:__

*   `` 1 <= words.length <= 500 ``
*   `` 1 <= words[i].length <= 10 ``
*   `` words[i] `` consists of lowercase English letters.
*   `` k `` is in the range <code>[1, The number of <strong>unique</strong> words[i]]</code>

 

__Follow-up:__ Could you solve it in `` O(n log(k)) `` time and `` O(n) `` extra space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 881,293 | 501,096 | 56.9% |