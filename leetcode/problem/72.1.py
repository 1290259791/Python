class Solution:
    def minDistance(self, word1, word2):
        """
        题目:编辑距离
        解法:动态规划
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = i
        for j in range(n):
            dp[j][0] = j
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + (
                    0 if word1[j - 1] == word2[i - 1] else 1)
        return dp[-1][-1]


solution = Solution()
print(solution.minDistance(word1="intention", word2="execution"))