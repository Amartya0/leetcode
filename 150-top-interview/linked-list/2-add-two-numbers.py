'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each
of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        temp = self
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def arrayToList(self, arr: list[int]) -> 'ListNode':
        # Forward reference in the return type hint as <ListNode> is defined within the same class
        # Alternatively, in Python 3.9 and later, you can enable the use of the current class name without quotes by adding the following import:
        # from __future__ import annotations

        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = ListNode()
        ans = temp
        carry = 0
        while l1 and l2:
            key = carry + l1.val + l2.val
            carry = key // 10
            temp.next = ListNode(val=key % 10)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            if carry == 0:
                temp.next = l1
                return ans.next
            key = carry + l1.val
            carry = key // 10
            temp.next = ListNode(val=key % 10)
            temp = temp.next
            l1 = l1.next

        while l2:
            if carry == 0:
                temp.next = l2
                return ans.next
            key = carry + l2.val
            carry = key // 10
            temp.next = ListNode(val=key % 10)
            temp = temp.next
            l2 = l2.next

        temp.next = ListNode(val=carry) if carry != 0 else None

        return ans.next


def main():
    l1_arr = [9, 9, 9, 9, 9, 9, 9]
    l2_arr = [9, 9, 9, 9]

    l1 = ListNode().arrayToList(l1_arr)
    l2 = ListNode().arrayToList(l2_arr)

    ans = Solution().addTwoNumbers(l1, l2)
    print("l1:  ", end="")
    l1.printList()
    print("l2:  ", end="")
    l2.printList()
    print("ans: ", end="")
    ans.printList()


if __name__ == '__main__':
    main()
