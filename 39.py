# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        node1 = list1
        node2 = list2

        if node1.val < node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next

        ans = head

        while node1 is not None or node2 is not None:
            if node1 is None:
                head.next = node2
                head = node2
                node2 = node2.next
                continue
            if node2 is None:
                head.next = node1
                head = node1
                node1 = node1.next
                continue

            if node1.val < node2.val:
                head.next = node1
                head = node1
                node1 = node1.next
            else:
                head.next = node2
                head = node2
                node2 = node2.next
        return ans



