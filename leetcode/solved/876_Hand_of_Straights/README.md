### [876. Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

Medium

Alice has a `` hand `` of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size `` W ``, and consists of `` W `` consecutive cards.

Return `` true `` if and only if she can.

 

__Example 1:__

<strong>Input: </strong>hand = [1,2,3,6,2,3,4,7,8], W = 3
    <strong>Output: </strong>true
    <strong>Explanation:</strong> Alice's hand can be rearranged as <code>[1,2,3],[2,3,4],[6,7,8]</code>.

__Example 2:__

<strong>Input: </strong>hand = [1,2,3,4,5], W = 4
    <strong>Output: </strong>false
    <strong>Explanation:</strong> Alice's hand can't be rearranged into groups of <code>4</code>.

 

__Constraints:__

*   `` 1 <= hand.length <= 10000 ``
*   `` 0 <= hand[i] <= 10^9 ``
*   `` 1 <= W <= hand.length ``

__Note:__ This question is the same as 1296: <https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 99,536 | 54,315 | 54.6% |