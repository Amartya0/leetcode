'''
2563. Count the Number of Fair Pairs
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:
1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
'''


from bisect import bisect_right


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 1):
            min_val = lower - nums[i] - 1
            max_val = upper - nums[i]

            right_idx = bisect_right(nums, max_val, i + 1)
            left_idx = bisect_right(nums, min_val, i + 1)

            count += right_idx - left_idx

        return count


def main():
    print(Solution().countFairPairs([1, 7, 9, 2, 5], 11, 11))


if __name__ == '__main__':
    main()
