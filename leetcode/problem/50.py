class Solution:

    def myPow(self, x, n):
        """
        求 x 的 n 次幂
        使用递归的方法,每次缩小2的倍数
        二分法解决
        使用了闭包
        :type x: float
        :type n: int
        :rtype: float
        """

        def fun(x, n):
            if not n:
                return 1
            if n == 1:
                return x
            if n & 1:
                return fun(x * x, n // 2) * x
            else:
                return fun(x * x, n // 2)

        if n < 0:
            return 1/fun(x,abs(n))
        else:
            return fun(x, n)


solution = Solution()
print(solution.myPow(0.000123, 123456))

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
"""
