'''
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

 

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row_0_need_zero = False
        col_0_need_zero = False

        for i in range(n):
            if matrix[i][0] == 0:
                col_0_need_zero = True
                break
        for j in range(m):
            if matrix[0][j] == 0:
                row_0_need_zero = True
                break

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_0_need_zero:
            for j in range(m):
                matrix[0][j] = 0
        if col_0_need_zero:
            for i in range(n):
                matrix[i][0] = 0


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
