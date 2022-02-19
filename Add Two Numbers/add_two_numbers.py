# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        if self.val == other.val and self.next == other.next:
            return True
        else:
            return False


class Solution:
    def create_list_node(self, input: Optional[ListNode]) -> Optional[ListNode]:
        list_node = None
        last = None
        for val in input:
            if list_node is None:
                list_node = ListNode(val)
            else:
                if last is None:
                    last = ListNode(val)
                    list_node.next = last
                else:
                    val_res = ListNode(val)
                    last.next = val_res
                    last = val_res
        return list_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = []

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0    

            carry, val = divmod(val_1 + val_2 + carry, 10)
            res.append(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.create_list_node(res)
