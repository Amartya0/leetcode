'''
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        answer = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                answer.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in range(right, left-1, -1):
                answer.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top-1, -1):
                answer.append(matrix[i][left])
            left += 1
            if right < left:
                break

        if top <= bottom:
            for i in range(top, bottom+1):
                answer.append(matrix[i][left])

        if left <= right:
            for i in range(left, right+1):
                answer.append(matrix[top][i])

        return answer


def main():
    print(Solution().spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


if __name__ == '__main__':
    main()
