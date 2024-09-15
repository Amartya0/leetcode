'''
2326. Spiral Matrix IV
Medium
Topics
Companies
Hint
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.



Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: [ListNode]) -> list[list[int]]:
        matrix = [[-1]*n for _ in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1
        while head:
            for i in range(left, right+1):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
            top += 1
            for i in range(top, bottom+1):
                if head:
                    matrix[i][right] = head.val
                    head = head.next
            right -= 1
            for i in range(right, left-1, -1):
                if head:
                    matrix[bottom][i] = head.val
                    head = head.next
            bottom -= 1
            for i in range(bottom, top-1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
            left += 1

        return matrix

# For showing result only


def create_linked_list(arr):
    pre = ListNode()
    current = pre
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return pre.next

# Main function to test the implementation


def main():
    # Test case 1
    m, n = 3, 5
    arr = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    head = create_linked_list(arr)
    result = Solution().spiralMatrix(m, n, head)
    print("Test Case 1 Result:")
    for row in result:
        print(row)

    # Test case 2
    m, n = 1, 4
    arr = [0, 1, 2]
    head = create_linked_list(arr)
    result = Solution().spiralMatrix(m, n, head)
    print("Test Case 2 Result:")
    for row in result:
        print(row)


# Run the main function
if __name__ == "__main__":
    main()
