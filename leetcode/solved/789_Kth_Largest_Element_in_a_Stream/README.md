### [789. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12)

Easy

You are part of a university admissions office and need to keep track of the `` kth `` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `` k ``, maintains a stream of test scores and continuously returns the `` k ``th highest test score __after__ a new score has been submitted. More specifically, we are looking for the `` k ``th highest score in the sorted list of all scores.

Implement the `` KthLargest `` class:

*   `` KthLargest(int k, int[] nums) `` Initializes the object with the integer `` k `` and the stream of test scores `` nums ``.
*   `` int add(int val) `` Adds a new test score `` val `` to the stream and returns the element representing the <code>k<sup>th</sup></code> largest element in the pool of test scores so far.

 

<strong class="example">Example 1:</strong>

<div class="example-block">
<p><strong>Input:</strong><br/>
<span class="example-io">["KthLargest", "add", "add", "add", "add", "add"]<br/>
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]</span></p>
<p><strong>Output:</strong> <span class="example-io">[null, 4, 5, 5, 8, 8]</span></p>
<p><strong>Explanation:</strong></p>
<p>KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);<br/>
kthLargest.add(3); // return 4<br/>
kthLargest.add(5); // return 5<br/>
kthLargest.add(10); // return 5<br/>
kthLargest.add(9); // return 8<br/>
kthLargest.add(4); // return 8</p>
</div>

<strong class="example">Example 2:</strong>

<div class="example-block">
<p><strong>Input:</strong><br/>
<span class="example-io">["KthLargest", "add", "add", "add", "add"]<br/>
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]</span></p>
<p><strong>Output:</strong> <span class="example-io">[null, 7, 7, 7, 8]</span></p>
<p><strong>Explanation:</strong></p>
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);<br/>
kthLargest.add(2); // return 7<br/>
kthLargest.add(10); // return 7<br/>
kthLargest.add(9); // return 7<br/>
kthLargest.add(9); // return 8</div>

 

__Constraints:__

*   <code>0 <= nums.length <= 10<sup>4</sup></code>
*   `` 1 <= k <= nums.length + 1 ``
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= val <= 10<sup>4</sup></code>
*   At most <code>10<sup>4</sup></code> calls will be made to `` add ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,226,497 | 728,389 | 59.4% |