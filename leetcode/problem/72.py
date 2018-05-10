class Solution:
    def minDistance(self, word1, word2):
        """
        题目:编辑距离
        解法:动态规划

        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:  # 当len2字符串为空
                    dp[i][j] = j
                elif j == 0:  # 当len1字符串为空
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  # word1的i-1字符和 word2j-1字符相同
                    dp[i][j] = dp[i - 1][j - 1]
                else:  # 不相同就从添加删除替换最小的操作中选一个加1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

solution = Solution()
print(solution.minDistance(word1="intention", word2="execution"))
