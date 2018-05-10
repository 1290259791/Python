class Solution:
    def numDistinct(self, s, t):
        """
        题目:不同子序列
        解法:动态规划
        思路:f(i,j)表示S 中的前 i 个字符,和 T 中的前 j 个字符
        当 s[i]!=t[j]时 f(i,j)=f(i-1,j)
        当 s[i]==t[j]时 f(i,j)=f(i-1,j)+f(i-1,j-1)
        :type s: str
        :type t: str
        :rtype: int
        s 在子序列中 t 出现的个数
        """
        len1, len2 = len(s), len(t)
        dp = [0] * (len2 + 1)
        dp[0] = 1
        for i in range(1, len1 + 1):
            for j in range(len2, 0, -1):
                dp[j] += dp[j - 1] if t[j - 1] == s[i - 1] else 0
        return dp[-1]

solution = Solution()
solution.numDistinct(s="babgbag", t = "bag")
