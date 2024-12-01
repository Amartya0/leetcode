'''
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the 
next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is 
not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x: int = 0, next: 'ListNode' = None):
        self.val = x
        self.next = next

    def arrayToListWithCycle(self, arr: list[int], pos: int = -1) -> 'ListNode':
        head = ListNode(arr[0])
        current = head
        cycle = ListNode()  # dummy node to keep track where to add cycle
        if pos == 0:
            cycle = head

        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
            if i == pos:
                cycle = current
        if pos != -1:
            current.next = cycle
        return head


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


def main():
    array = [3, 2, 0, -4]
    head = ListNode().arrayToListWithCycle(array, 2)  # True
    # head = ListNode().arrayToListWithCycle(array)  # False
    print(Solution().hasCycle(head))


if __name__ == '__main__':
    main()
