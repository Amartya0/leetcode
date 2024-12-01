'''
862. Shortest Subarray with Sum at Least K
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a 
sum of at least k. If there is no such subarray, return -1.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''
from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dq = deque()
        min_length = float('inf')
        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_length if min_length != float('inf') else -1


def main():
    print(Solution().shortestSubarray([1], 1))  # 1
    print(Solution().shortestSubarray([1, 2], 4))  # -1
    print(Solution().shortestSubarray([2, -1, 2], 3))  # 3


if __name__ == '__main__':
    main()
