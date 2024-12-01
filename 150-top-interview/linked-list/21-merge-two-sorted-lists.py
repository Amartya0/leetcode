'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes 
of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListBuilder:
    def fromArray(self, values):
        head = ListNode()
        current = head
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return head.next

    def toArray(self, head):
        current = head
        result = []
        while current:
            result.append(current.val)
            current = current.next
        return result

    def print(self, head):
        while head:
            print(head.val, end='->')
            head = head.next
        print('None')


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_head = ListNode()
        result = new_head

        while list1 and list2:
            if list1.val < list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next

        if list1:
            new_head.next = list1
        else:
            new_head.next = list2

        return result.next


def main():
    builder = ListBuilder()
    solution = Solution()

    list1 = builder.fromArray([1, 2, 4])
    list2 = builder.fromArray([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    builder.print(result)
    # [1, 1, 2, 3, 4, 4]

    list1 = builder.fromArray([])
    list2 = builder.fromArray([])
    result = solution.mergeTwoLists(list1, list2)
    builder.print(result)
    # []

    list1 = builder.fromArray([])
    list2 = builder.fromArray([0])
    result = solution.mergeTwoLists(list1, list2)
    builder.print(result)
    # [0]


if __name__ == '__main__':
    main()
