# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None:
            return True

        # Найдем середину списка с помощью метода "slow and fast pointers"
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Развернем вторую половину списка
        # у нас будет slow.next == None
        before = None
        now = slow
        while now is not None:
            next_now = now.next
            now.next = before
            before = now
            now = next_now

        tail = before  # Последний элемент списка

        # Проверяем на палиндромность
        begin = head
        end = tail
        while end is not None:  # Проверяем, что end не None (если end None, то мы дошли до середины)
            if begin.val != end.val:
                return False
            begin = begin.next
            end = end.next

        return True



"""
Идея метода "slow and fast pointers"
Метод "slow and fast pointers" используется для нахождения середины связного списка за один проход. 
Основная идея заключается в том, что один указатель (slow) движется по списку с обычной скоростью (один шаг за итерацию), 
а другой указатель (fast) движется в два раза быстрее (два шага за итерацию). 
Когда быстрый указатель достигает конца списка, медленный указатель будет находиться в середине.

Результат:
Когда fast достигает конца списка, slow оказывается на середине списка.
Если список имеет четное количество элементов, slow будет указывать на начало второй половины списка.
Если список имеет нечетное количество элементов, slow будет указывать на центральный элемент.
"""