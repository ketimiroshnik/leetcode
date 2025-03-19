# 2. Add Two Numbers


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        up = 0
        head = ListNode(-1)
        last = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                x = l2.val + up
                up = int(x > 9)
                x = x % 10
                l2 = l2.next
                node = ListNode(x)
                last.next = node
                last = node
                continue
            if l2 is None:
                x = l1.val + up
                up = int(x > 9)
                x = x % 10
                l1 = l1.next
                node = ListNode(x)
                last.next = node
                last = node
                continue

            x = l1.val + l2.val + up
            up = int(x > 9)
            x = x % 10
            l1 = l1.next
            l2 = l2.next
            node = ListNode(x)
            last.next = node
            last = node
        if up:
            node = ListNode(1)
            last.next = node
        return head.next



