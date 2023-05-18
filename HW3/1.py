# Алгоритм заключется в следующем: мы создаем новый список и вставляем туда объекты из начально данного списка,
# а потом сравниваем, если этот список и его перевернутая версия равны.
# сложность O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new = []
        while head is not None:
            new.append(head.val)
            head = head.next
        return new == new[::-1]
