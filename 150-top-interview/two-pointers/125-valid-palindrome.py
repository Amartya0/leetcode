'''
125. Valid Palindrome
Solved
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join([i for i in s if i.isalnum()])).lower()
        i = 0
        n = len(s)-1
        while i < n:
            if s[i] != s[n]:
                return False
            i += 1
            n -= 1
        return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))  # True
    s = "race a car"
    print(Solution().isPalindrome(s))  # False
    s = " "
    print(Solution().isPalindrome(s))  # True


if __name__ == '__main__':
    main()
