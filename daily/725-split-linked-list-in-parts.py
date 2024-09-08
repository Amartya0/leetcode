'''
725. Split Linked List in Parts
Solved
Medium
Topics
Companies
Hint
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:

        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next
        length_of_sublists = count//k
        additional = count % k

        result = []
        current = head
        for _ in range(k):
            temphead = current
            part_length = length_of_sublists + (1 if additional > _ else 0)
            for _ in range(part_length-1):
                if current:
                    current = current.next
            if current:
                temp = current.next
                current.next = None
                current = temp
            result.append(temphead)

        return result


def print_linked_list(head: ListNode):
    """Helper function to print the linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def build_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def main():
    # Test case 1
    # values = [1, 2, 3]
    # k = 5
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    head = build_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    # Create a solution object
    solution = Solution()

    # Split the list
    parts = solution.splitListToParts(head, k)

    # Print the result
    print(f"Split into {k} parts:")
    for i, part in enumerate(parts):
        print(f"Part {i + 1}:")
        print_linked_list(part)


if __name__ == "__main__":
    main()
