'''
1574. Shortest Subarray to be Removed to Make Array Sorted
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements 
in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

 
Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after 
that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we 
need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:
1 <= arr.length <= 105
0 <= arr[i] <= 109
'''

from bisect import bisect_left


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        elif n == 2:
            return 0 if arr[0] <= arr[1] else 1

        l, r = 0, n - 1
        l_done, r_done = False, False
        l_val, r_val = arr[0], arr[-1]

        for i in range(1, n):
            l_curr, r_curr = arr[i], arr[n - i - 1]

            if not l_done and l_curr < l_val:
                l = i - 1
                l_done = True
            if not r_done and r_curr > r_val:
                r = n - i
                r_done = True
            if l_done and r_done:
                break
            l_val, r_val = l_curr, r_curr

        if not l_done or l >= r:
            return 0

        res = max(l + 1, n - r)
        i = 0
        while i <= l and r < n:
            while r < n and arr[r] < arr[i]:
                r += 1
            res = max(i + 1 + (n - r), res)
            i += 1
        return n - res


def main():
    print(Solution().findLengthOfShortestSubarray([1, 3, 2, 4]))  # 1
    print(Solution().findLengthOfShortestSubarray(
        [1, 2, 3, 10, 4, 2, 3, 5]))  # 3


if __name__ == '__main__':
    main()
