'''
3254. Find the Power of K-Size Subarrays I
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.

Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]

Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]

 
Constraints:
1 <= n == nums.length <= 500
1 <= nums[i] <= 105
1 <= k <= n
'''


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        ans = []
        l, r = 0, 1
        n = len(nums)

        while r < n:
            if nums[r] - nums[r-1] != 1:
                while l < r and l + k - 1 < n:
                    ans.append(-1)
                    l += 1
                l = r
            elif r - l == k - 1:
                ans.append(nums[r])
                l += 1

            r += 1
        return ans


def main():
    print(Solution().resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
    # [3,4,-1,-1,-1]
    print(Solution().resultsArray([2, 2, 2, 2, 2], 4))
    # [-1,-1]


if __name__ == '__main__':
    main()