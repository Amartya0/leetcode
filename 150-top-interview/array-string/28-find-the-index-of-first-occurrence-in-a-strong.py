'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Brute force solution with built-in functions
        # return haystack.find(needle)

        # Brute force solution manually
        # m = len(needle)

        # if haystack == needle:
        #     return 0

        # for i in range(len(haystack)-m):
        #     if haystack[i:i+m] == needle:
        #         return i

        # return -1

        # KMP algorithm
        n, m = len(haystack), len(needle)

        if m == 0:
            return 0  # Special case: empty needle

        lps = self.computeLPSArray(needle)  # Preprocess the pattern
        # print(lps)
        i = 0  # index for haystack
        j = 0  # index for needle

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == m:
                return i - j  # Found the pattern at index i-j
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1  # Pattern not found

    def computeLPSArray(self, needle: str) -> list:
        m = len(needle)
        lps = [0] * m  # Create the LPS array of length m
        length = 0  # Length of the previous longest prefix suffix
        i = 1

        # Build the LPS array
        while i < m:
            if needle[i] == needle[length]:
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


def main():
    # haystack = "a"
    # needle = "a"

    # haystack = "hello"
    # needle = "ll"

    haystack = "mississippi"
    needle = "not"

    solution = Solution()
    print(solution.strStr(haystack, needle))


if __name__ == '__main__':
    main()
