'''
55. Jump Game
Solved
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                return True
        return False


# For demonstration purposes only

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 3, 1, 1, 4], True),   # Expected output: True
        ([3, 2, 1, 0, 4], False),  # Expected output: False
        ([2, 0, 2, 0, 1], True),   # Expected output: True
        ([0], True),               # Expected output: True (Only one element)
        ([1, 1, 1, 1, 1], True),   # Expected output: True
        ([1, 2, 3], True),         # Expected output: True
        ([1, 2, 0, 0, 4], False)   # Expected output: False
    ]

    # Run test cases
    for nums, expected in test_cases:
        result = solution.canJump(nums)
        print(f"Input: {nums}, Can jump: {result}, Expected: {
              expected}, Test {'Passed' if result == expected else 'Failed'}")


if __name__ == "__main__":
    main()
