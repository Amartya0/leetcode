'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the 
original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(s))
        print(Counter(t))
        return Counter(s) == Counter(t)

        # same approach but without using library and using array instead of dictionary

        # n = len(s)
        # m = len(t)

        # if n != m:
        #     return False

        # char_bank = [0]*26

        # for i in range(m):
        #     if s[i] == t[i]:
        #         continue
        #     char_bank[ord(s[i])-97] += 1
        #     char_bank[ord(t[i])-97] -= 1

        # for num in char_bank:
        #     if num != 0:
        #         return False

        # return True


def main():
    print(Solution().isAnagram("anagram", "nagaram"))  # expected: True


if __name__ == '__main__':
    main()
