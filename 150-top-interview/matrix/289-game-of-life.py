'''
289. Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) 
or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where 
births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some 
cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would 
cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). 
How would you address these problems?
'''


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        DEAD_TO_LIVE = 3  # 0 -> 1
        LIVE_TO_DEAD = 2  # 1 -> 0

        # Helper function to count live neighbors
        def count_live_neighbors(x, y):
            live_neighbors = 0
            for i in range(max(0, x - 1), min(n, x + 2)):
                for j in range(max(0, y - 1), min(m, y + 2)):
                    if (i, j) != (x, y) and (board[i][j] == 1 or board[i][j] == LIVE_TO_DEAD):
                        live_neighbors += 1
            return live_neighbors

        # Handle single-row or single-column matrices
        flag = False

        if n == 1 and not flag:  # Single row
            for j in range(m):
                live_neighbors = count_live_neighbors(0, j)
                if board[0][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[0][j] = LIVE_TO_DEAD
                elif board[0][j] == 0 and live_neighbors == 3:
                    board[0][j] = DEAD_TO_LIVE

            flag = True

        elif m == 1 and not flag:  # Single column
            for i in range(n):
                live_neighbors = count_live_neighbors(i, 0)
                if board[i][0] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][0] = LIVE_TO_DEAD
                elif board[i][0] == 0 and live_neighbors == 3:
                    board[i][0] = DEAD_TO_LIVE
            flag = True

        # General case for m x n boards
        if not flag:
            for i in range(n):
                for j in range(m):
                    live_neighbors = count_live_neighbors(i, j)
                    if board[i][j] == 1:
                        if live_neighbors < 2 or live_neighbors > 3:
                            board[i][j] = LIVE_TO_DEAD
                    elif board[i][j] == 0 and live_neighbors == 3:
                        board[i][j] = DEAD_TO_LIVE

        for i in range(n):
            for j in range(m):
                if board[i][j] == LIVE_TO_DEAD:
                    board[i][j] = 0
                elif board[i][j] == DEAD_TO_LIVE:
                    board[i][j] = 1

        return


def main():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol = Solution()
    sol.gameOfLife(board)
    print(board)


if __name__ == '__main__':
    main()
