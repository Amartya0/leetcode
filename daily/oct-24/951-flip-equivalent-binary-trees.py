'''
951. Flip Equivalent Binary Trees
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
 

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# Helper class for creating a binary tree from a list of values and to visualize the tree.
class Tree:
    def __init__(self):
        self.root = None

    def printTree(self, root):
        current_level = [root]
        while current_level:
            next_level = []
            for node in current_level:
                print(node.val, end=" ")
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print()
            current_level = next_level

    def list_to_tree(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        nodes = [root]
        i = 1
        while i < len(values):
            node = nodes.pop(0)
            if values[i] is not None:
                node.left = TreeNode(values[i])
                nodes.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                nodes.append(node.right)
            i += 1
        return root


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))


def main():
    tree = Tree()
    root1 = tree.list_to_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8])
    root2 = tree.list_to_tree(
        [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])

    sol = Solution()
    print(sol.flipEquiv(root1, root2))  # True


if __name__ == '__main__':
    main()
