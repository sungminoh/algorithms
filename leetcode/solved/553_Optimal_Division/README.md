### [553. Optimal Division](https://leetcode.com/problems/optimal-division/)

Medium

Given a list of __positive integers__, the adjacent integers will perform the float division. For example, \[2,3,4\] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the __maximum__ result, and return the corresponding expression in string format. __Your expression should NOT contain redundant parenthesis.__

__Example:__  

```
<b>Input:</b> [1000,100,10,2]
<b>Output:</b> "1000/(100/10/2)"
<b>Explanation:</b>
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/(<b>(</b>100/10<b>)</b>/2)" are redundant, <br/>since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
```

__Note:__

1.   The length of the input array is \[1, 10\].
2.   Elements in the given array will be in range \[2, 1000\].
3.   There is only one optimal division for each test case.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 43,298 | 24,448 | 56.5% |