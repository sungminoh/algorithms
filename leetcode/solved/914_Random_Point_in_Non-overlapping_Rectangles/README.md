### [914. Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/)

Medium

Given a list of __non-overlapping__ axis-aligned rectangles `` rects ``, write a function `` pick `` which randomly and uniformily picks an __integer point__ in the space covered by the rectangles.

Note:

1.   An __integer point__ is a point that has integer coordinates. 
2.   A point on the perimeter of a rectangle is __included__ in the space covered by the rectangles. 
3.   `` i ``th rectangle = `` rects[i] `` = `` [x1,y1,x2,y2] ``, where `` [x1, y1] `` are the integer coordinates of the bottom-left corner, and `` [x2, y2] `` are the integer coordinates of the top-right corner.
4.   length and width of each rectangle does not exceed `` 2000 ``.
5.   `` 1 <= rects.length <= 100 ``
6.   `` pick `` return a point as an array of integer coordinates `` [p_x, p_y] ``
7.   `` pick `` is called at most `` 10000 `` times.

<div>
<p><strong>Example 1:</strong></p>
```
Input: 
<span id="example-input-1-1">["Solution","pick","pick","pick"]
</span><span id="example-input-1-2">[[[[1,1,5,5]]],[],[],[]]</span>
Output: 
<span id="example-output-1">[null,[4,1],[4,1],[3,3]]</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: 
<span id="example-input-2-1">["Solution","pick","pick","pick","pick","pick"]
</span><span id="example-input-2-2">[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]</span>
Output: 
<span id="example-output-2">[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]</span>
```
</div>
<div>
<p><strong>Explanation of Input Syntax:</strong></p>
<p>The input is two lists: the subroutines called and their arguments. <code>Solution</code>'s constructor has one argument, the array of rectangles <code>rects</code>. <code>pick</code> has no arguments. Arguments are always wrapped with a list, even if there aren't any.</p>
</div>
</div>

<div>
<div> </div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 31,659 | 11,841 | 37.4% |