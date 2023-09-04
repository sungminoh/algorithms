### [1528. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=daily-question&envId=2023-04-17)

Easy

There are `` n `` kids with candies. You are given an integer array `` candies ``, where each `` candies[i] `` represents the number of candies the <code>i<sup>th</sup></code> kid has, and an integer `` extraCandies ``, denoting the number of extra candies that you have.

Return _a boolean array _`` result ``_ of length _`` n ``_, where _`` result[i] ``_ is _`` true ``_ if, after giving the _<code>i<sup>th</sup></code>_ kid all the _`` extraCandies ``_, they will have the __greatest__ number of candies among all the kids__, or _`` false ``_ otherwise_.

Note that __multiple__ kids can have the __greatest__ number of candies.

 

<strong class="example">Example 1:</strong>

```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

<strong class="example">Example 2:</strong>

```
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
```

<strong class="example">Example 3:</strong>

```
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

 

__Constraints:__

*   `` n == candies.length ``
*   `` 2 <= n <= 100 ``
*   `` 1 <= candies[i] <= 100 ``
*   `` 1 <= extraCandies <= 50 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 676,790 | 592,454 | 87.5% |