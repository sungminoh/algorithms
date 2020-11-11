### [71. Simplify Path](https://leetcode.com/problems/simplify-path/description/)

[Description](https://leetcode.com/problems/simplify-path/description/)[Hints](https://leetcode.com/problems/simplify-path/hints/)[Submissions](https://leetcode.com/problems/simplify-path/submissions/)[Discuss](https://leetcode.com/problems/simplify-path/discuss/)[Solution](https://leetcode.com/problems/simplify-path/solution/)

[Pick One](https://leetcode.com/problems/random-one-question/)

------

Given an absolute path for a file (Unix-style), simplify it.

For example,
**path** = `"/home/"`, => `"/home"`
**path** = `"/a/./b/../../c/"`, => `"/c"`

[click to show corner cases.](https://leetcode.com/problems/simplify-path/description/#)

**Corner Cases:**

 

 

- Did you consider the case where **path** = `"/../"`?
  In this case, you should return `"/"`.
- Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.
  In this case, you should ignore redundant slashes and return `"/home/foo"`.