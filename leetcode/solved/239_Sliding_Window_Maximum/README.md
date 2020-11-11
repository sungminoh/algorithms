### [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

Hard

Given an array _nums_, there is a sliding window of size _k_ which is moving from the very left of the array to the very right. You can only see the _k_ numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

__Follow up:__  
Could you solve it in linear time?

__Example:__

<strong>Input:</strong> <em>nums</em> = [1,3,-1,-3,5,3,6,7], and <em>k</em> = 3
    <strong>Output: </strong><code>[3,3,5,5,6,7] 
    <strong>Explanation: 
    </strong></code>
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       <strong>3</strong>
     1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
     1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
     1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
     1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
     1  3  -1  -3  5 [3  6  7]      <strong>7</strong>

 

__Constraints:__

*   `` 1 <= nums.length <= 10^5 ``
*   `` -10^4 <= nums[i] <= 10^4 ``
*   `` 1 <= k <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 615,229 | 260,725 | 42.4% |