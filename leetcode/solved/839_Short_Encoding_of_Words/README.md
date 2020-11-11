### [839. Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/)

Medium

Given a list of words, we may encode it by writing a reference string `` S `` and a list of indexes `` A ``.

For example, if the list of words is `` ["time", "me", "bell"] ``, we can write it as `` S = "time#bell#" `` and `` indexes = [0, 2, 5] ``.

Then for each index, we will recover the word by reading from the reference string from that index until we reach a `` "#" `` character.

What is the length of the shortest reference string S possible that encodes the given words?

__Example:__

<strong>Input:</strong> words = ["time", "me", "bell"]
    <strong>Output:</strong> 10
    <strong>Explanation:</strong> S = <code>"time#bell#" and indexes = [0, 2, 5</code>].

 

__Note:__

1.   `` 1 <= words.length <= 2000 ``.
2.   `` 1 <= words[i].length <= 7 ``.
3.   Each word has only lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 25,648 | 12,914 | 50.4% |