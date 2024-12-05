### [650. 2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19)

Medium

There is only one character `` 'A' `` on the screen of a notepad. You can perform one of two operations on this notepad for each step:

*   Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
*   Paste: You can paste the characters which are copied last time.

Given an integer `` n ``, return _the minimum number of operations to get the character_ `` 'A' `` _exactly_ `` n `` _times on the screen_.

 

<strong class="example">Example 1:</strong>

```
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
```

<strong class="example">Example 2:</strong>

```
Input: n = 1
Output: 0
```

 

__Constraints:__

*   `` 1 <= n <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 444,675 | 265,002 | 59.6% |