'''

MEDIUM
 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

'''

class Solution:
    def threeSum(self, integers):
        """
        :type integers: List[int]
        :rtype: List[List[int]]
        """
        integers.sort()
        result = []
        for index in range(len(integers)):
            if integers[index] > 0:
                break
            if index > 0 and integers[index] == integers[index - 1]:
                continue
            left, right = index + 1, len(integers) - 1
            while left < right:
                if integers[left] + integers[right] < 0 - integers[index]:
                    left += 1
                elif integers[left] + integers[right] > 0 - integers[index]:
                    right -= 1
                else:
                    result.append([integers[index], integers[left], integers[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two integers.
                    while integers[left] == integers[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result