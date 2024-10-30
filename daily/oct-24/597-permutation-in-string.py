'''
567. Permutation in String
Solved
Medium
Topics
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1_map = {}
        s2_window_map = {}

        for i in s1:
            if i in s1_map:
                s1_map[i] += 1
            else:
                s1_map[i] = 1

        for i in s2[:s1_len]:
            if i in s2_window_map:
                s2_window_map[i] += 1
            else:
                s2_window_map[i] = 1

        for i in range(s1_len, s2_len):
            if s2_window_map == s1_map:
                return True
            else:
                if s2[i-s1_len] == s2[i]:
                    continue
                else:
                    if s2[i] in s2_window_map:
                        s2_window_map[s2[i]] += 1
                    else:
                        s2_window_map[s2[i]] = 1

                    if s2_window_map[s2[i-s1_len]] == 1:
                        s2_window_map.pop(s2[i-s1_len])
                    else:
                        s2_window_map[s2[i-s1_len]] -= 1

        if s2_window_map == s1_map:
            return True
        return False


def main():
    print(Solution().checkInclusion("adc", "dcda"))


if __name__ == '__main__':
    main()
