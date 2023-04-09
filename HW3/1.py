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
        new = []#созадем список
        cur = head#создаем переменную, которая показывает, где мы находимся сейчас
        while cur is not None: #проходимся по списку
            new.append(cur.val) #добавляем каждый элемент в новый список
            cur = cur.next #меняе местонахождение на следующий элемент
        return new == new[::-1] #проверяе если списки равны