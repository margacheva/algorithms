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
        ptr = head #дублируем список
        s = '' #создаем пустую строку
        while ptr != None: #проходимся по списку
            s += str(ptr.val)#добавляем элементы в строку
            ptr = ptr.next #переходим к следующему элементу
        return int(s, 2) #используем встроенную функцию переводу в десятичную систему счисления и указываем,
        # в какой системе находится число