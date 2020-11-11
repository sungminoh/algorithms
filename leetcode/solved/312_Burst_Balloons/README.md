### [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/description/)

[**Description](https://leetcode.com/problems/burst-balloons/description/)[**Hints](https://leetcode.com/problems/burst-balloons/hints/)[**Submissions](https://leetcode.com/problems/burst-balloons/submissions/)[**Discuss](https://leetcode.com/problems/burst-balloons/discuss/)[**Solution](https://leetcode.com/problems/burst-balloons/solution/)

[**Discuss](https://discuss.leetcode.com/category/392)[**Pick One](https://leetcode.com/problems/random-one-question/)

------

Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a number on it represented by array `nums`. You are asked to burst all the balloons. If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right`are adjacent indices of `i`. After the burst, the `left` and `right` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

**Note:** 
(1) You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
(2) 0 ≤ `n` ≤ 500, 0 ≤ `nums[i]` ≤ 100

**Example:**

Given `[3, 1, 5, 8]`

Return `167`

```
    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

```

**Credits:**
Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.