'''
1072. Flip Columns For Maximum Number of Equal Rows
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column 
(i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 
Example 1:
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
'''

from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        pattern_count = Counter()

        for row in matrix:
            term0 = row[0]
            base_pattern = tuple(x ^ term0 for x in row)
            pattern_count[base_pattern] += 1

        return max(pattern_count.values())


def main():
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]))
    # Output: 1
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
    # Output: 2
    print(Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))

    # Output: 2
if __name__ == '__main__':
    main()