### [502. IPO](https://leetcode.com/problems/ipo/)

Hard

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most __k__ distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most __k__ distinct projects. 

You are given several projects. For each project __i__, it has a pure profit __P<sub>i</sub>__ and a minimum capital of __C<sub>i</sub>__ is needed to start the corresponding project. Initially, you have __W__ capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most __k__ distinct projects from given projects to maximize your final capital, and output your final maximized capital.

__Example 1:__  

```
<b>Input:</b> k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

<b>Output:</b> 4

<b>Explanation:</b> Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
```

__Note:__  

1.   You may assume all numbers in the input are non-negative integers.
2.   The length of Profits array and Capital array will not exceed 50,000.
3.   The answer is guaranteed to fit in a 32-bit signed integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 48,024 | 19,593 | 40.8% |