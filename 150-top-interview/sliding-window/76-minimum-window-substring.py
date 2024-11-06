'''
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0)+1

        left = 0
        matched_chars = 0
        required_chars = len(target_count)
        window_count = {}
        result_range = []
        first_result = True

        for right in range(len(s)):
            current_char = s[right]
            window_count[current_char] = window_count.get(current_char, 0) + 1

            if current_char in target_count and window_count[current_char] == target_count[current_char]:
                matched_chars += 1

            while matched_chars == required_chars:
                if first_result:
                    result_range = [left, right]
                    first_result = False
                elif right - left < result_range[1] - result_range[0]:
                    result_range = [left, right]

                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    matched_chars -= 1

                left += 1

        return s[result_range[0]:result_range[1]+1] if not first_result else ""


def main():
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))


if __name__ == '__main__':
    main()
