'''

HARD
 
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cleaning up the array
        for indx in range(len(nums)):
            if nums[indx] <= 0 or nums[indx] > len(nums):
                nums[indx] = len(nums) + 1
        
        # placing our marker to see what numbers have been accounted for
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num - 1] >= 0:
                nums[num - 1] *= -1
        
        # final step for getting the answer
        for indx in range(len(nums)):
            if nums[indx] > 0:
                return indx + 1
        
        return len(nums) + 1
