'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # temp = []
        # max_len = 0
        # for i in s:
        #     if i not in temp:
        #         temp.append(i)
        #     else:
        #         max_len = max(max_len, len(temp))
        #         temp.append(i)
        #         temp = temp[temp.index(i)+1:]
        # max_len = max(max_len, len(temp))
        # return max_len

        max_len, left, right = 0, 0, 0
        for i in s:
            if i not in s[left:right]:
                right += 1
            else:
                max_len = max(max_len, right-left)
                right += 1
                left += s[left:right].index(i) + 1
        max_len = max(max_len, right-left)
        return max_len


def main():
    print(Solution().lengthOfLongestSubstring("aabaab!bb"))
    # Expected output: 3


if __name__ == '__main__':
    main()
