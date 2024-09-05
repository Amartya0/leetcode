'''
189. Rotate Array
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''


def circularArrayRotationRight(nums, k):
    # return nums[-k:] + nums[:-k]

    # n= len(nums)
    # k=k%n
    # temp1 = nums[n-k:]
    # temp2 = nums[:n-k]
    # for i in range(n):
    #     if i < k:
    #         nums[i]=temp1[i]
    #     else:
    #         nums[i]=temp2[i-k]

    n = len(nums)
    k = k % n
    if k == 0:
        return nums
    elif k <= n//2 + 1:
        temp1 = nums[n-k:]
        for i in range(n-k, 0, -1):
            nums[i+k-1] = nums[i-1]
        for i in range(k):
            nums[i] = temp1[i]
    else:
        temp1 = nums[:n-k]
        for i in range(k):
            nums[i] = nums[i+n-k]
        print(nums, temp1)
        for i in range(n-k):
            nums[i+k] = temp1[i]

    return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    nums = circularArrayRotationRight(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
