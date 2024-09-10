'''
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n

        prefix_suffix_temp = 1
        for i in range(n):
            result[i] *= prefix_suffix_temp
            prefix_suffix_temp *= nums[i]

        prefix_suffix_temp = 1
        for i in range(n-1, -1, -1):
            result[i] *= prefix_suffix_temp
            prefix_suffix_temp *= nums[i]

        return result


def main():
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]


if __name__ == '__main__':
    main()
