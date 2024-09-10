'''
2807. Insert Greatest Common Divisors in Linked List
Solved
Medium
Topics
Companies
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:


Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gcd(self, num1: int, num2: int) -> int:
        if num2 > num1:
            temp = num2
            num2 = num1
            num1 = temp
        if num2 != 0:
            return self.gcd(num2, num1 % num2)
        else:
            return num1

    def insertGreatestCommonDivisors(self, head: list[ListNode]) -> list[ListNode]:
        start = head
        while (head and head.next):
            newNode = ListNode(self.gcd(head.val, head.next.val), head.next)
            head.next = newNode
            head = newNode.next
        return start


class Helper:
    def arrayToListNode(self, array: list[int]) -> ListNode:
        if not array:
            return None
        head = ListNode(array[0])
        dummy = head
        for i in array[1:]:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head

    def printLinkedList(self, head: ListNode) -> None:
        while head:
            print(head.val, end="->")
            head = head.next
        print("NULL")


def main():
    numbers = [18, 6, 10, 3]
    head = Helper().arrayToListNode(numbers)
    Helper().printLinkedList(head)
    modHead = Solution().insertGreatestCommonDivisors(head)
    Helper().printLinkedList(modHead)


if __name__ == '__main__':
    main()
