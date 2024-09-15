'''
2419. Longest Subarray With Maximum Bitwise AND
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_value = max(nums)
        result = 0
        temp = 0
        for num in nums:
            if num == max_value:
                temp += 1
            else:
                result = max(result, temp)
                temp = 0

        result = max(result, temp)

        return result


def main():
    nums1 = [1, 2, 3, 3, 2, 2]
    print(Solution().longestSubarray(nums1))  # 2
    nums2 = [1, 2, 3, 4]
    print(Solution().longestSubarray(nums2))  # 1


if __name__ == '__main__':
    main()