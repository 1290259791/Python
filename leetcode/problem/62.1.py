class Solution:
    def uniquePaths(self, m, n):
        """
        题目:不同路径
        解法:动态规划
        和1不同的是多了一行和一列0
        不同考虑过届问题
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in range(m+1)]
        dp[1][1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not (i == 1 and j == 1):
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[-1][-1]

solution = Solution()
print(solution.uniquePaths(7,3))
