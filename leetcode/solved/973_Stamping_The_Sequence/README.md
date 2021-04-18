### [973. Stamping The Sequence](https://leetcode.com/problems/stamping-the-sequence/)

Hard

You want to form a `` target `` string of __lowercase letters__.

At the beginning, your sequence is `` target.length `` `` '?' `` marks.  You also have a `` stamp `` of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to `` 10 * target.length `` turns.

For example, if the initial sequence is 

<font face="monospace">"?????"</font>

, and your stamp is `` "abc" ``,  then you may make 

<font face="monospace">"abc??", "?abc?", "??abc" </font>

in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is 

<font face="monospace">"ababc"</font>

, and the stamp is `` "abc" ``, then we could return the answer `` [0, 2] ``, corresponding to the moves 

<font face="monospace">"?????" -> "abc??" -> "ababc"</font>

.

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within `` 10 * target.length `` moves.  Any answers specifying more than this number of moves will not be accepted.

 

__Example 1:__

```
Input: stamp = <span id="example-input-1-1">"abc"</span>, target = <span id="example-input-1-2">"ababc"</span>
Output: <span id="example-output-1">[0,2]</span>
([1,0,2] would also be accepted as an answer, as well as some other answers.)
```

<div>
<p><strong>Example 2:</strong></p>
```
Input: stamp = <span id="example-input-2-1">"</span><span id="example-input-2-2">abca</span><span>"</span>, target = <span id="example-input-2-2">"</span><span>aabcaca"</span>
Output: <span id="example-output-2">[3,0,1]</span>
```
<div>
<p> </p>
<p><strong>Note:</strong></p>
</div>
</div>

1.   `` 1 <= stamp.length <= target.length <= 1000 ``
2.   `` stamp `` and `` target `` only contain lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 41,095 | 21,940 | 53.4% |