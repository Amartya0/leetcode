'''
3217. Delete Nodes From Linked List Present in Array
Solved
Medium
Topics
Companies
Hint
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        if head == None or len(nums) == 0:
            return head

        # Step 1: Convert nums to a set for O(1) lookup
        num_set = set(nums)

        # Step 2: Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Step 3: Traverse the list and remove nodes with values in nums
        while current and current.next:
            if current.next.val in num_set:
                # Bypass the node with a value in nums
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        # Step 4: Return the modified list starting from dummy.next
        return dummy.next


# For demonstration purpose only

# Helper function to convert a list to a linked list
def build_linked_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Main function
def main():
    nums = [1, 3, 6]  # The list of values to remove
    linked_list_values = [1, 2, 3, 4, 1, 2, 1, 2]  # The linked list input

    # Step 1: Convert input list to linked list
    head = build_linked_list(linked_list_values)

    # Step 2: Create a Solution object and call modifiedList
    solution = Solution()
    modified_head = solution.modifiedList(nums, head)

    # Step 3: Convert the modified linked list back to a list and print it
    while modified_head:
        print(modified_head.val, end=" ")
        modified_head = modified_head.next
    print()


if __name__ == "__main__":
    main()
