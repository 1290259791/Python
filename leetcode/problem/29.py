class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend < 0 and divisor < 0:
            flag = 1
        elif divisor > 0 and dividend > 0:
            flag = 1
        else:
            flag = -1

        sum = abs(dividend) // abs(divisor)
        sum *= flag
        if sum > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return sum


solution = Solution()
print(solution.divide(2147483647, 2))
