'''
962. Maximum Width Ramp
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104
'''


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        #! Brainchild
        # n = len(nums)
        # max_right = [0]*n
        # max_right[n-1] = nums[n-1]
        # for i in range(n-2,-1,-1):
        #     max_right[i] = max(nums[i],max_right[i+1])

        # result = 0
        # left = 0
        # for i in range(n):
        #     while nums[left] > max_right[i]:
        #         left += 1
        #     result = max(result,i-left)

        # return result

        n = len(nums)
        result = 0
        stack = []

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                temp = stack.pop()
                result = max(result, j - temp)
                if temp == 0:
                    return result
        return result


def main():
    print(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]))  # 4


if __name__ == '__main__':
    main()
