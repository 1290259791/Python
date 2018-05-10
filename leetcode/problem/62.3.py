class Solution:
    def uniquePaths(self, m, n):
        """
        解法:
        这个解法没理解....
        :type m: int
        :type n: int
        :rtype: int
        """
        def f(n):
            ret = 1
            for i in range(1, n+1):
                ret *= i
            return ret
        return f(m+n-2)//(f(m-1)*f(n-1))