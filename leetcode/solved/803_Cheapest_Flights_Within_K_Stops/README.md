### [803. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Medium

There are `` n `` cities connected by `` m `` flights. Each flight starts from city `` u  ``and arrives at `` v `` with a price `` w ``.

Now given all the cities and flights, together with starting city `` src `` and the destination `` dst ``, your task is to find the cheapest price from `` src `` to `` dst `` with up to `` k `` stops. If there is no such route, output `` -1 ``.

<strong>Example 1:</strong>
<strong>Input:</strong> 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
    <strong>Output:</strong> 200
    <strong>Explanation:</strong> 
    The graph looks like this:
    <img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height:180px; width:246px"/>
    
    The cheapest price from city 0 to city <code>2</code> with at most 1 stop costs 200, as marked red in the picture.

<strong>Example 2:</strong>
<strong>Input:</strong> 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
    <strong>Output:</strong> 500
    <strong>Explanation:</strong> 
    The graph looks like this:
    <img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height:180px; width:246px"/>
    
    The cheapest price from city 0 to city <code>2</code> with at most 0 stop costs 500, as marked blue in the picture.

__Note:__

*   The number of nodes `` n `` will be in range `` [1, 100] ``, with nodes labeled from `` 0 `` to `` n 
````  - 1 ``.
*   The size of `` flights `` will be in range `` [0, n * (n - 1) / 2] ``.
*   The format of each flight will be `` (src,  
```` dst 
```` , price) ``.
*   The price of each flight will be in the range `` [1, 10000] ``.
*   `` k `` is in the range of `` [0, n - 1] ``.
*   There will not be any duplicated flights or self cycles.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 197,274 | 73,800 | 37.4% |