'''
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        key = strs[0]
        for token in strs[1:]:
            while not token.startswith(key):
                key = key[:-1]
                if not key:
                    return ""

        return key


def main():
    strs1 = ["flower", "flow", "flight"]  # "fl"
    strs2 = ["dog", "race-car", "car"]  # ""
    strs3 = ["interspace", "interstellar", "interstate"]  # "inters"
    sol = Solution()
    print(sol.longestCommonPrefix(strs1))
    print(sol.longestCommonPrefix(strs2))
    print(sol.longestCommonPrefix(strs3))


if __name__ == '__main__':
    main()
