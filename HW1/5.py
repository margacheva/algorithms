# Алгоритм заключается в том, что мы записываем в счетчик,
# пока не найдем закрытую пару скобок
# сложность O(n)
def removeOuterParentheses(s):
    counter = 0  # создаем счетчик
    result = []  # создаем список для записи в результат
    for e in s:  # для каждого элемента в данной строке
        if e == ')':  # если элемент равен закрытой скобке
            counter -= 1  # вычитаем единицу из счетчика
        if counter > 0:  # если при итерации счетчик больше нуля
            result.append(e)  # в список добавляем этот элемент
        if e == '(':  # если элемент равен открытой скобке
            counter += 1  # добавляем в счетчик единицу
    return ''.join(result)  # возвращаем строку


print(removeOuterParentheses('(())'))
