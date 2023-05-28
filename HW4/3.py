class Solution:
    def tribonacci(self, n: int) -> int:

        t0, t1, t2 = 0, 1, 1

        # если n меньше или равно 2, то возвращаем соответствующее начальное значение
        if n == 0:
            return t0
        elif n == 1 or n == 2:
            return t1

        # вычисляем последующие значения последовательности
        # исходя из того, что последующее число равно сумме двух предыдуших
        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn
        return tn
