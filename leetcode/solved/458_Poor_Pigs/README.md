### [458. Poor Pigs](https://leetcode.com/problems/poor-pigs/ls)

Hard

There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.

 

__General case: __

If there are `` n `` buckets and a pig drinking poison will die within `` m `` minutes, how many pigs (`` x ``) you need to figure out the __poisonous__ bucket within `` p `` minutes? There is exactly one bucket with poison.

 

__Note:__

1.   A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
2.   After a pig has instantly finished drinking buckets, there has to be a __cool down time__ of _m _minutes. During this time, only observation is allowed and no feedings at all.
3.   Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 40,151 | 19,159 | 47.7% |