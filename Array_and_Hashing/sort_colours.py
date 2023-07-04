'''
75. Sort Colors Medium

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize three pointers
        left = 0  # Points to the position where the next 0 should be placed
        right = len(nums) - 1  # Points to the position where the next 2 should be placed
        current = 0  # Used for iteration
        
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:
                current += 1

