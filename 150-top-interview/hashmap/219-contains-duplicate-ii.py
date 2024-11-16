'''
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i 
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #! brainchild
        # if k == 0:
        #     return False

        # maps = {}
        # for i in range(min(k, len(nums))):
        #     if nums[i] in maps:
        #         return True
        #     maps[nums[i]] = i

        # for i in range(k, len(nums)):
        #     if nums[i] in maps:
        #         return True
        #     del maps[nums[i - k]]
        #     maps[nums[i]] = i

        # return False

        maps = {}
        for i in range(len(nums)):
            if nums[i] in maps and i - maps[nums[i]] <= k:
                return True
            maps[nums[i]] = i
        return False


def main():
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    # Output: true

    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    # Output: true

    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
    # Output: false


if __name__ == '__main__':
    main()
