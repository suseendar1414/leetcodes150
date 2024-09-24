# Given the beginning of a singly linked list head, reverse the list, 
# and return the new beginning of the list.

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# head = [0,1,2,3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optional import for type hints
from typing import Optional

class Solution:
    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev pointer forward
            current = next_node       # Move current pointer forward
        return prev

# Helper function to convert a Python list into a linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
input_list = [1, 2, 3, 4, 5]  # Define your input list here
head = list_to_linkedlist(input_list)  # Convert Python list to linked list

print("Original Linked List:")
print_linkedlist(head)  # Print original linked list

solution = Solution()  # Create an instance of Solution
result = solution.revList(head)  # Reverse the linked list

print("Reversed Linked List:")
print_linkedlist(result)  # Print reversed linked list



