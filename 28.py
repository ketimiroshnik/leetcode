# 19. Remove Nth Node From End of List

# solve it with only one pass


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # идея: запускаем сначала fast и затем slow на расстояним n-1, далее они шагают вместе
        # когда fast будет на последнем элементе, то slow будет на искомом
        fast = head
        for _ in range(n - 1):
            fast = fast.next
        before_slow = None
        slow = head
        while fast.next is not None:
            fast = fast.next
            before_slow = slow
            slow = slow.next
        if before_slow is None:
            return head.next
        before_slow.next = slow.next
        return head



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
print(s.removeNthFromEnd(head, 2))


