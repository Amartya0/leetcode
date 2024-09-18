'''
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''

#! chatGpt
# from functools import cmp_to_key
# class Solution:
#     def compare(self, x, y):
#         if x + y > y + x:
#             return -1
#         elif x + y < y + x:
#             return 1
#         else:
#             return 0

#     def largestNumber(self, nums: list[int]) -> str:
#         nums_str = list(map(str, nums))
#         nums_str.sort(key=cmp_to_key(self.compare))
#         result = ''.join(nums_str)
#         if result[0] == '0':
#             return "0"
#         return result


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))
        # Sort based on the string repeated 10 times, in reverse order
        # This works because our constraints are 0 <= nums[i] <= 10^9; so the maximum length of a number is 10
        nums.sort(key=lambda x: x * 10, reverse=True)
        result = ''.join(nums)
        '''
        Example Walkthrough:
            For the list [3, 30, 34, 5, 9]:
                3 * 10 = "3333333333"
                30 * 10 = "3030303030"
                34 * 10 = "3434343434"
                5 * 10 = "5555555555"
                9 * 10 = "9999999999"
            When sorted in descending order, the result is ["9", "5", "34", "3", "30"].
            Concatenating these gives "9534330", which is the correct largest number.
        '''
        if result[0] == '0':
            return "0"
        return result


def main():
    print(Solution().largestNumber([10, 2]))  # 210
    print(Solution().largestNumber([3, 30, 34, 5, 9]))  # 9534330
    print(Solution().largestNumber([1, 0, 0, 0]))  # 1
    print(Solution().largestNumber([0, 0, 0]))  # 0


if __name__ == '__main__':
    main()
