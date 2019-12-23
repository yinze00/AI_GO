from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def swap(ptr1: ListNode, ptr2: ListNode):
            temp = ptr1.val
            ptr1.val = ptr2.val
            ptr2.val = temp
        