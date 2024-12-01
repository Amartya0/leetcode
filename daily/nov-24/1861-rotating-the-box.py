'''
1861. Rotating the Box
You are given an m x n matrix of characters boxGrid representing a side-view of a box. 
Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to 
gravity. Each stone falls down until it lands on an obstacle, another stone, or the 
bottom of the box. Gravity does not affect the obstacles' positions, and the inertia 
from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the 
bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 
Example 1:
Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 
Constraints:
m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
'''


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        for row in box:
            n = len(row)
            write_idx = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    write_idx = j - 1
                elif row[j] == '#':
                    row[j] = '.'
                    row[write_idx] = '#'
                    write_idx -= 1

        m, n = len(box), len(box[0])
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        return rotated


def main():
    print(Solution().rotateTheBox([["#", ".", "#"]]))
    # [["."], ["#"], ["#"]]

    print(Solution().rotateTheBox(
        [["#", ".", "*", "."], ["#", "#", "*", "."]]))
    # [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]

    print(Solution().rotateTheBox([["#", "#", "*", ".", "*", "."],
          ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]))
    # [[".","#","#"],[".","#","#"],["#","#","*"],["#","*","."],["#",".","*"],["#",".","."]]


if __name__ == '__main__':
    main()