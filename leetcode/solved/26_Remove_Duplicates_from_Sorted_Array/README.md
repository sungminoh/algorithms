### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Easy

Given an integer array `` nums `` sorted in __non-decreasing order__, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">__in-place__</a> such that each unique element appears only __once__. The __relative order__ of the elements should be kept the __same__.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the __first part__ of the array `` nums ``. More formally, if there are `` k `` elements after removing the duplicates, then the first `` k `` elements of `` nums `` should hold the final result. It does not matter what you leave beyond the first `` k `` elements.

Return `` k ``_ after placing the final result in the first _`` k ``_ slots of _`` nums ``.

Do __not__ allocate extra space for another array. You must do this by __modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>__ with O(1) extra memory.

__Custom Judge:__

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be __accepted__.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

<strong class="example">Example 2:</strong>

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

 

__Constraints:__

*   <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
*   `` -100 <= nums[i] <= 100 ``
*   `` nums `` is sorted in __non-decreasing__ order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 5,142,579 | 2,615,659 | 50.9% |