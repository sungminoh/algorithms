### [547. Friend Circles](https://leetcode.com/problems/friend-circles/)

Medium

There are __N__ students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a __direct__ friend of B, and B is a __direct__ friend of C, then A is an __indirect__ friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a __N\*N__ matrix __M__ representing the friend relationship between students in the class. If M\[i\]\[j\] = 1, then the i<sub>th</sub> and j<sub>th</sub> students are __direct__ friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

__Example 1:__  

```
<b>Input:</b> 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
<b>Output:</b> 2
<b>Explanation:</b>The 0<sub>th</sub> and 1<sub>st</sub> students are direct friends, so they are in a friend circle. <br/>The 2<sub>nd</sub> student himself is in a friend circle. So return 2.
```

__Example 2:__  

```
<b>Input:</b> 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
<b>Output:</b> 1
<b>Explanation:</b>The 0<sub>th</sub> and 1<sub>st</sub> students are direct friends, the 1<sub>st</sub> and 2<sub>nd</sub> students are direct friends, <br/>so the 0<sub>th</sub> and 2<sub>nd</sub> students are indirect friends. All of them are in the same friend circle, so return 1.
```

__Note:__  

1.   N is in range \[1,200\].
2.   M\[i\]\[i\] = 1 for all students.
3.   If M\[i\]\[j\] = 1, then M\[j\]\[i\] = 1.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 270,183 | 156,084 | 57.8% |