# 1004. Max Consecutive Ones III

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Запоминаем положение k+1 нуля. Затем когда приходит k+2, то мы берем отрезок строки начиная
        с первого символа после самого дальнего нуля в памяти и до текущего нуля не включая
        ___0(____0___0___)0 при k=2
        """
        # модифицируем изначальный массив для удобства
        nums = [0] + nums + [0]
        t = k + 1
        mas = [-1] * t
        count = 0
        i = 0
        # сначала считваем первый k+1 ноль
        while count != t:
            if nums[i] == 0:
                mas[count] = i
                count += 1
            i += 1
            if i == len(nums):
                break
        if count != t:
            # значит нулей в строке меньше чем k
            return len(nums) - 2

        # теперь обрабатываем следующие символы
        ans = i - 2
        for j in range(i, len(nums)):
            if nums[j] == 1:
                continue
            ans = max(ans, j - mas[count % t] - 1)
            mas[count % t] = j
            count += 1

        return ans







