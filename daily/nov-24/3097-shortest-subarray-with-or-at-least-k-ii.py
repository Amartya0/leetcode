'''
3097. Shortest Subarray With OR at Least K II
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Subarray:
A subarray is a contiguous non-empty sequence of elements within an array.
 

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

 
Constraints:
1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
'''


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 1

        n = len(nums)
        min_length = float('inf')
        current_or = 0
        left = 0

        bit_count = [0] * 32

        def add_to_bit_count(num):
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1

        def remove_from_bit_count(num):
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] -= 1

        def recompute_current_or():
            result = 0
            for i in range(32):
                if bit_count[i] > 0:
                    result |= (1 << i)
            return result

        for right in range(n):
            add_to_bit_count(nums[right])
            current_or |= nums[right]

            while current_or >= k:
                min_length = min(min_length, right - left + 1)
                remove_from_bit_count(nums[left])
                left += 1
                current_or = recompute_current_or()

        return min_length if min_length != float('inf') else -1


def main():
    print(Solution().minimumSubarrayLength([1, 2, 32, 21], 55))
    print(32 | 21 | 2)


if __name__ == '__main__':
    main()
