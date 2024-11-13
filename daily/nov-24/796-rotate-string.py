'''
796. Rotate String
Solved
Easy
Topics
Companies
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

'''

#! BrainChild
# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         n = len(s)
#         m = len(goal)

#         if m != n:
#             return False

#         k = m//5 + 2
#         for i in range(1, k):
#             s1 = ''.join([s[m-i:], s[:m-i]])
#             s2 = ''.join([s[m-(i+k):], s[:m-(i+k)]])
#             s3 = ''.join([s[m-(i+2*k):], s[:m-(i+2*k)]])
#             s4 = ''.join([s[m-(i+3*k):], s[:m-(i+3*k)]])
#             s5 = ''.join([s[m-(i+4*k):], s[:m-(i+4*k)]])
#             if goal == s1 or goal == s2 or goal == s3 or goal == s4 or goal == s5:
#                 return True

#         return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


def main():
    print(Solution().rotateString('abcde', 'cdeab'))


if __name__ == '__main__':
    main()
