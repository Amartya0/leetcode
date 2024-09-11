'''
6. Zigzag Conversion
Solved
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of empty strings for all rows
        rows = [''] * numRows
        current_row = 0
        direction = -1  # This will be used to change direction

        for char in s:
            rows[current_row] += char

            # Change direction if we are at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            # Move to the next row
            current_row += direction

        # Combine all rows into one final string
        return ''.join(rows)


def main():
    s = "PAYPALISHIRING"
    sol = Solution()
    print(sol.convert(s, 3))  # "PAHNAPLSIIGYIR"
    print(sol.convert(s, 4))  # "PINALSIGYAHRPI"


if __name__ == '__main__':
    main()
