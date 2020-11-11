### [915. Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/)

Medium

Given the radius and x-y positions of the center of a circle, write a function `` randPoint `` which generates a uniform random point in the circle.

Note:

1.   input and output values are in <a href="https://www.webopedia.com/TERM/F/floating_point_number.html" target="_blank">floating-point</a>.
2.   radius and x-y position of the center of the circle is passed into the class constructor.
3.   a point on the circumference of the circle is considered to be in the circle.
4.   `` randPoint `` returns a size 2 array containing x-position and y-position of the random point, in that order.

<div>
<p><strong>Example 1:</strong></p>
```
Input: 
<span id="example-input-1-1">["Solution","randPoint","randPoint","randPoint"]
</span><span id="example-input-1-2">[[1,0,0],[],[],[]]</span>
Output: <span id="example-output-1">[null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: 
<span id="example-input-2-1">["Solution","randPoint","randPoint","randPoint"]
</span><span id="example-input-2-2">[[10,5,-7.5],[],[],[]]</span>
Output: <span id="example-output-2">[null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]</span>
```
</div>
<p><strong>Explanation of Input Syntax:</strong></p>
<p>The input is two lists: the subroutines called and their arguments. <code>Solution</code>'s constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. <code>randPoint</code> has no arguments. Arguments are always wrapped with a list, even if there aren't any.</p>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 25,861 | 9,940 | 38.4% |