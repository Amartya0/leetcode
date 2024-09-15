'''
1371. Find the Longest Substring Containing Vowels in Even Counts
Solved
Medium
Topics
Companies
Hint
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        mask_map = {0: -1}
        max_len = 0
        current_mask = 0

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                current_mask ^= (1 << vowel_to_bit[char])

            if current_mask in mask_map:
                max_len = max(max_len, i - mask_map[current_mask])
            else:
                mask_map[current_mask] = i

        return max_len


def main():
    string = "leetcodeisgreat"
    print(Solution().findTheLongestSubstring(string))  # 5
    string = "eleetminicoworoep"
    print(Solution().findTheLongestSubstring(string))  # 13
    string = "bcbcbc"
    print(Solution().findTheLongestSubstring(string))  # 6


if __name__ == '__main__':
    main()
