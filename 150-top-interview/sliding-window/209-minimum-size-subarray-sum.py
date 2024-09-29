'''
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0  # Left pointer for the sliding window
        current_sum = 0  # To store the current sum of the sliding window
        # Initialize to infinity, to track the minimum length of subarray
        min_length = float('inf')

        for right in range(n):  # Iterate through the array using the right pointer
            current_sum += nums[right]  # Add the current element to the sum

            # While the current sum is greater than or equal to target, shrink the window
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                # Remove the leftmost element from the sum
                current_sum -= nums[left]
                left += 1  # Move the left pointer to shrink the window

        # If we never found a valid subarray, return 0; otherwise, return the minimum length
        return min_length if min_length != float('inf') else 0

# Test cases to validate the solution


def main():
    solution = Solution()
    print(solution.minSubArrayLen(11, [1, 2, 3, 4, 5]))
    # Expected output: 3 (subarray [3, 4, 5])

    # print(solution.minSubArrayLen(4, [1, 4, 4]))
    # # Expected output: 1 (subarray [4])

    # print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    # # Expected output: 0 (no valid subarray)


if __name__ == '__main__':
    main()
