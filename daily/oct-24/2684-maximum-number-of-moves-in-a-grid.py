'''
2684. Maximum Number of Moves in a Grid
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value 
of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106
'''


class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = [[0] * col for _ in range(row)]
        answer = 0

        for col_index in range(col-2, -1, -1):
            for row_index in range(row-1, -1, -1):
                temp1, temp2, temp3 = 0, 0, 0
                if row_index == 0:
                    if grid[row_index][col_index] < grid[row_index][col_index+1]:
                        temp2 = result[row_index][col_index+1] + 1
                    if grid[row_index][col_index] < grid[row_index+1][col_index+1]:
                        temp3 = result[row_index+1][col_index+1] + 1
                elif row_index == row - 1:
                    if grid[row_index][col_index] < grid[row_index-1][col_index+1]:
                        temp1 = result[row_index-1][col_index+1]+1
                    if grid[row_index][col_index] < grid[row_index][col_index+1]:
                        temp2 = result[row_index][col_index+1] + 1
                else:
                    if grid[row_index][col_index] < grid[row_index-1][col_index+1]:
                        temp1 = result[row_index-1][col_index+1]+1
                    if grid[row_index][col_index] < grid[row_index][col_index+1]:
                        temp2 = result[row_index][col_index+1] + 1
                    if grid[row_index][col_index] < grid[row_index+1][col_index+1]:
                        temp3 = result[row_index+1][col_index+1] + 1
                result[row_index][col_index] = max(temp1, temp2, temp3)
                if col_index == 0:
                    answer = max(answer, result[row_index][col_index])

        return answer


def main():
    sol = Solution()
    print(sol.maxMoves(
        [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))  # 3
    print(sol.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))  # 0


if __name__ == '__main__':
    main()
