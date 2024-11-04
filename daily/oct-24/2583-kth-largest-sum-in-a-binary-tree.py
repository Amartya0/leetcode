'''
2583. Kth Largest Sum in a Binary Tree
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
'''


import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert_from_list(self, lst):
        root = TreeNode(lst[0])
        cl = [root]
        i = 1
        while (i < len(lst)):
            nl = []
            for node in cl:
                if i+1 < len(lst):
                    node.left = TreeNode(lst[i])
                    nl.append(node.left)
                    node.right = TreeNode(lst[i+1])
                    nl.append(node.right)
                    i += 2
                elif i < len(lst):
                    node.left = TreeNode(lst[i])
                    nl.append(node.left)
                    i += 1
            cl = nl

        self.root = root

    def print_tree(self):
        cl = [self.root]
        while cl:
            nl = []
            for node in cl:
                print(node.val, end=' ')
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            print()
            cl = nl


class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        cl = [root]
        mh = []

        while cl:
            nl = []
            ls = 0
            for node in cl:
                if node.val:
                    ls += node.val
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)

            cl = nl

            if len(mh) < k:
                heapq.heappush(mh, ls)
            elif ls > mh[0]:
                heapq.heapreplace(mh, ls)

        return mh[0] if len(mh) >= k else -1


def main():
    tree = Tree()
    tree.insert_from_list([5, 8, 9, 2, 1, 3, 7, 4, 6])
    # tree.print_tree()
    k = 2
    sol = Solution()
    print(sol.kthLargestLevelSum(tree.root, k))

    tree = Tree()
    tree.insert_from_list([1, 2, None, 3])
    k = 1
    print(sol.kthLargestLevelSum(tree.root, k))


if __name__ == '__main__':
    main()
