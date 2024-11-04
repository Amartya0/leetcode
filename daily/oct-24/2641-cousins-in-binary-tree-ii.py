'''
2641. Cousins in Binary Tree II
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104
'''

# Definition for a binary tree node.


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
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        # We are considering the root node as level 0 and its children as level 1 and so on.
        # As all values of level 0 and level 1 are 0, we can start from level 2.
        # We will keep track of the nodes of the previous level and the current level.
        # From all nodes of current level, we will calculate the sum of their values.
        # From all nodes of previous level we will access their children which are the nodes of current level.
        # We are doing this so that we can have acces to a node as well as their sibling to update their values as required.

        previous_level = []
        root.val = 0
        if root.left:
            root.left.val = 0
            previous_level.append(root.left)
        if root.right:
            root.right.val = 0
            previous_level.append(root.right)

        current_level = []
        for node in previous_level:
            if node.left:
                current_level.append(node.left)
            if node.right:
                current_level.append(node.right)

        while current_level:
            next_level = []
            current_level_sum = 0
            # loop to calculate the sum of values of all nodes of current level
            for node in current_level:
                current_level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # loop to update the values of all nodes of current level accessed through previous level,
            # so that we can have access to a node as well as their sibling.
            for node in previous_level:
                value = current_level_sum
                value -= node.left.val if node.left else 0
                if node.right:
                    value -= node.right.val
                    node.right.val = value
                if node.left:
                    node.left.val = value

            # updating the previous level and current level for next iteration
            previous_level = current_level
            current_level = next_level

        return root


def main():
    values = [5, 4, 9, 1, 10, None, 7]
    root = TreeNode(values[0])
    tree = Tree()
    root = tree.list_to_tree(values)
    tree.printTree(root)
    tree.printTree(Solution().replaceValueInTree(root))


if __name__ == '__main__':
    main()
