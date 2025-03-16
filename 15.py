# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool

        Follow up: Could you do it in O(n) time and O(1) space?
        """
        if head is None:
            return True
        d = dict()
        # словарь где к каждой цифре мы напишем список индексов где она встречается
        for i in range(0, 10):
            d[i] = list()
        now = head
        i = 0
        while now is not None:
            d[now.val].append(i)
            i += 1
            now = now.next
        n = i

        # в отдельности проверим на палиндромность каждую цифру
        for digit in range(0, 10):
            k = len(d[digit])
            # сравниваем на симметричность индексы с двух концов
            for i in range(k // 2):
                if d[digit][i] != n - 1 - d[digit][-i-1]:
                    return False
            # если нечет кол-во индексов, то проверим центральный отдельно
            if k % 2 == 1:
                if n % 2 == 0:
                    return False
                if d[digit][k//2] != n // 2:
                    return False
        return True