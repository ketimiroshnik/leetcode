# 167. Two Sum II - Input Array Is Sorted

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        x + y = target
        """
        n = len(numbers)
        j = n - 1
        # На каждом шаге i ищем минимальный j (i < j)  что numbers[i] + numbers[j] >= target
        # заметим, что если numbers[i] + numbers[j] >= target, то и numbers[i+1] + numbers[j] >= target так как numbers[i+1] >= numbers[i]
        for i in range(n):
            if numbers[i] + numbers[n-1] < target:
                # даже самое большое число не подошло
                continue
            if j <= i:
                # тогда конец так как мы знаем, что numbers[i] + numbers[i] >= target
                # тогда и при всех i < j  numbers[i] + numbers[j] > target
                return [-1, -1]

            # пробуем уменьшить j
            while numbers[i] + numbers[j-1] >= target and j-1 > i:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]