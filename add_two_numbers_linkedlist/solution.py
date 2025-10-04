"""
Add Two Numbers — Problem Description

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

Constraints:
- The two numbers do not contain any leading zero, except the number 0 itself.
- Lists can be of different lengths.

Example:
  Input:  l1 = [2,4,3], l2 = [5,6,4]
  Output: [7,0,8]  # because 342 + 465 = 807
"""

from typing import Optional, Iterable, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Add two numbers represented by reversed linked lists.

    Uses a dummy head and iterates while either list has nodes or there is a carry.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        l1_val = l1.val if l1 is not None else 0
        l2_val = l2.val if l2 is not None else 0
        column_sum = l1_val + l2_val + carry
        carry = column_sum // 10
        current.next = ListNode(column_sum % 10)
        current = current.next
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    return dummy_head.next


def build_list(values: Iterable[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    summed = add_two_numbers(l1, l2)
    print(to_list(summed))  # Expected: [7, 0, 8]


