'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
'''

# Assuming ListNode and TreeNode are already defined as provided earlier


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, head: ListNode, node: TreeNode) -> bool:
        if not head:
            return True
        if not node:
            return False
        if head.val != node.val:
            return False
        return self.dfs(head.next, node.left) or self.dfs(head.next, node.right)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        if self.dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def create_binary_tree(values):
    """Helper function to create a binary tree from a list of values."""
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kid = 1
    for i in range(len(values)):
        if nodes[i] is not None:
            if kid < len(values):
                nodes[i].left = nodes[kid]
                kid += 1
            if kid < len(values):
                nodes[i].right = nodes[kid]
                kid += 1
    return nodes[0]


def main():
    # Example 1: Linked list [4, 2, 8], Tree [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    linked_list_values = [1, 4, 2, 6]
    binary_tree_values = [1, 4, 4, None, 2, 2, None,
                          1, None, 6, 8, None, None, None, None, 1, 3]

    head = create_linked_list(linked_list_values)
    root = create_binary_tree(binary_tree_values)

    solution = Solution()
    result = solution.isSubPath(head, root)

    print("Is the linked list a downward path in the binary tree?\n  ->", result)


if __name__ == "__main__":
    main()
