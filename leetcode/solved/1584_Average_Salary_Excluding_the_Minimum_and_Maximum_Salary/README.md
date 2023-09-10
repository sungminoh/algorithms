### [1584. Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/?envType=daily-question&envId=2023-05-01)

Easy

You are given an array of __unique__ integers `` salary `` where `` salary[i] `` is the salary of the <code>i<sup>th</sup></code> employee.

Return _the average salary of employees excluding the minimum and maximum salary_. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.

 

<strong class="example">Example 1:</strong>

```
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
```

<strong class="example">Example 2:</strong>

```
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
```

 

__Constraints:__

*   `` 3 <= salary.length <= 100 ``
*   <code>1000 <= salary[i] <= 10<sup>6</sup></code>
*   All the integers of `` salary `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 499,907 | 317,385 | 63.5% |