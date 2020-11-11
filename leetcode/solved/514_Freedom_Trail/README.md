### [514. Freedom Trail](https://leetcode.com/problems/freedom-trail/)

Hard

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string __ring__, which represents the code engraved on the outer ring and another string __key__, which represents the keyword needs to be spelled. You need to find the __minimum__ number of steps in order to spell all the characters in the keyword.

Initially, the first character of the __ring__ is aligned at 12:00 direction. You need to spell all the characters in the string __key__ one by one by rotating the ring clockwise or anticlockwise to make each character of the string __key__ aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character __key\[i\]__:

1.   You can rotate the __ring__ clockwise or anticlockwise __one place__, which counts as 1 step. The final purpose of the rotation is to align one of the string __ring's__ characters at the 12:00 direction, where this character must equal to the character __key\[i\]__.
2.   If the character __key\[i\]__ has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

__Example:__

<center><img src="https://assets.leetcode.com/uploads/2018/10/22/ring.jpg" style="width: 26%;"/></center>


 


```
<b>Input:</b> ring = "godding", key = "gd"
<b>Output:</b> 4
<b>Explanation:</b>
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
```

__Note:__

1.   Length of both ring and __key__ will be in range 1 to 100.
2.   There are only lowercase letters in both strings and might be some duplcate characters in both strings.
3.   It's guaranteed that string __key__ could always be spelled by rotating the string __ring__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 46,286 | 20,578 | 44.5% |