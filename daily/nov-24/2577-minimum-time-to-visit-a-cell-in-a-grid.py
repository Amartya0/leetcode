'''
2577. Minimum Time to Visit a Cell In a Grid
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] 
represents the minimum time required to be able to visit the cell (row, col), which means you 
can visit the cell (row, col) only when the time you visit it is greater than or equal to 
grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any 
adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If 
you cannot visit the bottom-right cell, then return -1.

 

Example 1:
Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.

Example 2:
Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
 

Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0
'''

from heapq import heappop, heappush
from math import inf
from itertools import pairwise


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        distance = [[inf] * cols for _ in range(rows)]
        distance[0][0] = 0

        priority_queue = [(0, 0, 0)]
        directions = (-1, 0, 1, 0, -1)

        while priority_queue:
            time, row, col = heappop(priority_queue)
            if row == rows - 1 and col == cols - 1:
                return time

            for delta_row, delta_col in pairwise(directions):
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_time = time + 1
                    if new_time < grid[new_row][new_col]:
                        new_time = grid[new_row][new_col] + \
                            (grid[new_row][new_col] - new_time) % 2
                    if new_time < distance[new_row][new_col]:
                        distance[new_row][new_col] = new_time
                        heappush(priority_queue, (new_time, new_row, new_col))

        return -1


def main():
    print(Solution().minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]))
    # Output: 7
    print(Solution().minimumTime([[0, 2, 4], [3, 2, 1], [1, 0, 4]]))
    # Output: -1


if __name__ == '__main__':
    main()
