class Solution:
    def climbStairs(self, n):
        """
        题目:爬楼梯
        解法:动态规划
        思路:
        知道爬1台阶和2台阶的步数,
        剩下就是叠加 n = n-1 + n-2的步数
        :type n: int
        :rtype: int
        """
        if n <3:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


solution = Solution()
print(solution.climbStairs(0))
