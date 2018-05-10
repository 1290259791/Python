class Solution:

    def myPow(self, x, n):
        """
        求 x 的 n 次幂
        使用递归的方法,每次缩小2的倍数
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:   # n小于0
            return 1 / self.myPow(x, -n)
        if n & 1:   # 是否是奇数
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)
