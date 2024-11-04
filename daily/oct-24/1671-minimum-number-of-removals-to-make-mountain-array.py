'''
1671. Minimum Number of Removals to Make Mountain Array
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
'''


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        mountain_scores = [0] * n

        lis = [1] * n
        lis_start = 0

        lds = [1] * n
        lds_end = 0

        for i in range(1, n):
            lis_temp = [0]
            lds_temp = [0]

            for j in range(i):
                if nums[j] < nums[i]:
                    lis_temp.append(lis[j])

                if nums[-(j + 1)] < nums[-(i + 1)]:
                    lds_temp.append(lds[-(j + 1)])

            lis[i] = max(lis_temp) + 1
            mountain_scores[i] += lis[i]
            if lis_start == 0 and lis[i] > 1:
                lis_start = i

            lds[-(i + 1)] = max(lds_temp) + 1
            mountain_scores[-(i + 1)] += lds[-(i + 1)]
            if lds_end == 0 and lds[-(i + 1)] > 1:
                lds_end = n - (i + 1)

        return n - max(mountain_scores[lis_start:lds_end + 1]) + 1


def main():
    print(Solution().minimumMountainRemovals([1, 3, 1]))  # 0
    print(Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))  # 3


if __name__ == '__main__':
    main()
