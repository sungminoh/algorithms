### [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/)

Hard

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the __minimum length__ of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

 

__Example 1:__

```
<b>Input:</b> [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<b>Output:</b> [[1,1],[2,0],[4,2],[3,3],[2,4]]
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/erect_the_fence_1.png" style="width: 100%; max-width: 320px"/>
```

__Example 2:__

```
<b>Input:</b> [[1,2],[2,2],[4,2]]
<b>Output:</b> [[1,2],[2,2],[4,2]]
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/erect_the_fence_2.png" style="width: 100%; max-width: 320px"/>
Even you only have trees in a line, you need to use rope to enclose them. 
```

 

__Note:__

1.   All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
2.   All input integers will range from 0 to 100.
3.   The garden has at least one tree.
4.   All coordinates are distinct.
5.   Input points have __NO__ order. No order required for output.
6.   input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 28,193 | 10,197 | 36.2% |