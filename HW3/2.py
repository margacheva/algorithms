# Алгоритм заключается в следующем:
# мы конвертируем данный список в строку и при помощи встроенной функции пересчитываем число
# в десятичную систему счисления
# сложность O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head is not None:
            s += str(head.val)
            head = head.next
        return int(s, 2)
