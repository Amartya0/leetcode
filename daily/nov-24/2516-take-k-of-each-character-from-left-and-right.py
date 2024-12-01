'''
2516. Take K of Each Character From Left and Right
You are given a string s consisting of the characters 'a', 'b', and 'c' and a 
non-negative integer k. Each minute, you may take either the leftmost character of s, 
or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each 
character, or return -1 if it is not possible to take k of each character.

 
Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = Counter(s)
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1

        n = len(s)
        required = {'a': count['a'] - k,
                    'b': count['b'] - k, 'c': count['c'] - k}
        current = {'a': 0, 'b': 0, 'c': 0}
        max_len = 0
        left = 0

        for right in range(n):
            current[s[right]] += 1

            while current['a'] > required['a'] or current['b'] > required['b'] or current['c'] > required['c']:
                current[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return n - max_len


def main():
    print(Solution().takeCharacters("aabaaaacaabc", 2))
    # Output: 8
    print(Solution().takeCharacters("a", 1))
    # Output: -1


if __name__ == '__main__':
    main()
