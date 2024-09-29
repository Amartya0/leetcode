'''
15. 3Sum
Attempted
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array
        result = []  # To store the list of triplets that sum up to 0
        n = len(nums)  # Length of the input array

        # Find the first positive number's index (if any), and only run up to n-2 or that index
        first_positive_index = n  # Assume no positive numbers
        for i in range(n):
            if nums[i] > 0:
                first_positive_index = i
                break

        # Iterate over the array from 0 to min(first_positive_index, n-2)
        for major_index in range(min(first_positive_index, n-2)):
            # Skip duplicates for the first element to avoid repeating the same triplet
            if major_index > 0 and nums[major_index] == nums[major_index-1]:
                continue

            # Initialize two pointers: one starting from the next element, and one from the end of the array
            left = major_index + 1
            right = n - 1

            # Continue while the left pointer is less than the right pointer
            while left < right:
                current_sum = nums[major_index] + \
                    nums[left] + nums[right]  # Calculate the sum

                if current_sum > 0:  # If sum is greater than zero, move the right pointer left to decrease the sum
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif current_sum < 0:  # If sum is less than zero, move the left pointer right to increase the sum
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:  # If the sum is zero, we've found a valid triplet
                    result.append([nums[major_index], nums[left], nums[right]])

                    # Skip duplicates for both left and right pointers after finding a valid triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


# Test cases to validate the solution
def main():

    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # Expected output: [[-1,-1,2],[-1,0,1]]

    print(Solution().threeSum([0, 1, 1]))  # Expected output: []


# Entry point for running the script
if __name__ == '__main__':
    main()
