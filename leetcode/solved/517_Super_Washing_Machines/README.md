### [517. Super Washing Machines](https://leetcode.com/problems/super-washing-machines/)

Hard

You have __n__ super washing machines on a line. Initially, each washing machine has some dresses or is empty. 

For each __move__, you could choose __any m__ (1 ≤ m ≤ n) washing machines, and pass __one dress__ of each washing machine to one of its adjacent washing machines __ at the same time __. 

Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the __minimum number of moves__ to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

__Example1__

```
<b>Input:</b> [1,0,5]

<b>Output:</b> 3

<b>Explanation:</b> 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   
```

__Example2__

```
<b>Input:</b> [0,3,0]

<b>Output:</b> 2

<b>Explanation:</b> 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
```

__Example3__

```
<b>Input:</b> [0,2,0]

<b>Output:</b> -1

<b>Explanation:</b> 
It's impossible to make all the three washing machines have the same number of dresses. 
```

__Note:__  

1.   The range of n is \[1, 10000\].
2.   The range of dresses number in a super washing machine is \[0, 1e5\].

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 45,854 | 17,592 | 38.4% |