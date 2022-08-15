### [458. Poor Pigs](https://leetcode.com/problems/poor-pigs/)

Hard

There are `` buckets `` buckets of liquid, where __exactly one__ of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have `` minutesToTest `` minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

1.   Choose some live pigs to feed.
2.   For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
3.   Wait for `` minutesToDie `` minutes. You may __not__ feed any other pigs during this time.
4.   After `` minutesToDie `` minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
5.   Repeat this process until you run out of time.

Given `` buckets ``, `` minutesToDie ``, and `` minutesToTest ``, return _the __minimum__ number of pigs needed to figure out which bucket is poisonous within the allotted time_.

 

__Example 1:__

```Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
Output: 5
```

__Example 2:__

```Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
Output: 2
```

__Example 3:__

```Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
Output: 2
```

 

__Constraints:__

*   `` 1 <= buckets <= 1000 ``
*   `` 1 <= minutesToDie <= minutesToTest <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 104,712 | 69,586 | 66.5% |