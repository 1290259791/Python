class Solution:
    def mySqrt(self, x):
        """
        开根号操作
        没有看懂,以后会看懂吗????
        :type x: int
        :rtype: int
        """
        y = 12
        while not -0.1 < y ** 2 - x < 0.1:
            y = (y + x / y) / 2
        return int(y)


solution = Solution()
print(solution.mySqrt(146))
