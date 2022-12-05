# проверяем содержатся ли элементы камней в элементах ювелирных камней
# O(n)
def numJewelsInStones(jewels, stones):
    counter = 0  # вводим счетчик
    for i in stones:  # для каждого элемента в камнях
        if i in jewels:  # если елемент в камнях содержится в списке ювелирных камней
            counter += 1  # то добавляем его в счетчик

    return counter  # возвращаем счетчик


print(numJewelsInStones('Aa', 'AaAA'))
