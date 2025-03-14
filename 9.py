# 206. Reverse Linked List


class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head

        before = None
        now = head

        while now is not None:
            new = now.next
            now.next = before
            before = now
            now = new
        return before



