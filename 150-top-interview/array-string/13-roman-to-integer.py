'''
13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]

        return total

        # roman = {
        #     'I': 1, 'II': 2, 'III': 3, 'IV': 4,
        #             'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
        #             'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40,
        #             'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
        #             'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400,
        #             'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
        #             'M': 1000, 'MM': 2000, 'MMM': 3000
        # }

        # result = 0
        # i = len(s)
        # while (i >= 0):
        #     if s[i-2:i+1] in roman:
        #         result += roman[s[i-2:i+1]]
        #         print(s[i-2:i+1], result)
        #         i -= 3
        #     elif s[i-1:i+1] in roman:
        #         result += roman[s[i-1:i+1]]
        #         print(s[i-1:i+1], result)
        #         i -= 2
        #     else:
        #         result += roman[s[i]]
        #         print(s[i], result)
        #         i -= 1

        # return result


def main():
    s = "MCMXCIV"
    sol = Solution()
    result = sol.romanToInt(s)
    print(result)


if __name__ == '__main__':
    main()
