'''
214. Shortest Palindrome
Solved
Hard
Topics
Companies
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''


class Solution:
    def computeLPS(self, pattern: str) -> list:
        # LPS (Longest Prefix Suffix) Array Construction for KMP algorithm
        n = len(pattern)
        lps = [0] * n
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev_s = s[::-1]
        combined = s + "#" + rev_s
        lps = self.computeLPS(combined)

        # Length of the longest palindromic prefix
        longest_palindrome_prefix_len = lps[-1]

        # Add the non-palindromic part of the reverse string to the front
        non_palindrome_suffix = rev_s[:len(s) - longest_palindrome_prefix_len]

        return non_palindrome_suffix + s


def main():
    print(Solution().shortestPalindrome("aacecaaa"))
    print(Solution().shortestPalindrome("abcd"))


if __name__ == '__main__':
    main()
