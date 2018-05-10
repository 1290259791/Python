class Solution:

    def myPow(self, x, n):
        """
        求 x 的 n 次幂
        使用递归的方法,每次缩小2的倍数
        :type x: float
        :type n: int
        :rtype: float
        """
        def fun(x,n):
            result = 1
            while n:
                if n & 1:
                    result *= x
                n >>= 1
                x *= x
            return result
        return fun(x,n)


solution = Solution()
print(solution.myPow(123, 3))