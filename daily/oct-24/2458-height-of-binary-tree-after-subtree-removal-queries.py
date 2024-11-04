'''
2458. Height of Binary Tree After Subtree Removal Queries
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array 
queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the 
value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 

Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).
Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val
'''


from collections import defaultdict


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
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        height = {}
        depth = {}
        max_depth_heights = defaultdict(list)

        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left_height = dfs(node.left, d + 1)
            right_height = dfs(node.right, d + 1)
            h = 1 + max(left_height, right_height)
            height[node.val] = h
            max_depth_heights[d].append(h)
            return h

        dfs(root, 0)

        for d, h_list in max_depth_heights.items():
            h_list.sort(reverse=True)
            max_depth_heights[d] = (
                h_list[0], h_list[1] if len(h_list) > 1 else -1)

        result = []
        for q in queries:
            node_height = height[q]
            node_depth = depth[q]

            max1, max2 = max_depth_heights[node_depth]
            if node_height == max1:
                new_tree_height = node_depth + max2
            else:
                new_tree_height = node_depth + max1

            result.append(new_tree_height)

        return result


def main():
    tree = Tree()
    root = tree.list_to_tree([5, 8, 9, 2, 1, 3, 7, 4, 6])
    # tree.printTree(root)
    queries = [3, 2, 4, 8]
    sol = Solution()
    result = sol.treeQueries(root, queries)
    print(result)

    tree = Tree()
    root = tree.list_to_tree(
        [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7])
    # tree.printTree(root)
    queries = [4]
    sol = Solution()
    result = sol.treeQueries(root, queries)
    print(result)


if __name__ == '__main__':
    main()
