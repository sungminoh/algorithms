### [552. Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/)

Hard

Given a positive integer __n__, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10<sup>9</sup> + 7.

A student attendance record is a string that only contains the following three characters:

1.   __'A'__ : Absent. 
2.   __'L'__ : Late.
3.    __'P'__ : Present. 

A record is regarded as rewardable if it doesn't contain __more than one 'A' (absent)__ or __more than two continuous 'L' (late)__.

__Example 1:__  

```
<b>Input:</b> n = 2
<b>Output:</b> 8 
<b>Explanation:</b>
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
```

__Note:__The value of __n__ won't exceed 100,000.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 71,111 | 26,292 | 37.0% |