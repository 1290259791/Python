class Solution:
    def climbStairs(self, n):
        """
        题目:爬楼梯
        解法:动态规划
        思路:
        n[0] = 1
        n[1] = 2
        然后用交换方法
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b
