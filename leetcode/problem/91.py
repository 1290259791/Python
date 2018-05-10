class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s) == 0 or s[0] == '0' or int(s) % 10 == 0:
            return 0
        if int(s) < 10:
            return 1
        try:
            s = s.lstrip(0)
        except Exception:
            s = s
        s = list(s)
        n = len(s)
        dp = [0] * n
        if '0' < s[0] <= '9':
            dp[0] = 1
        if s[0] + s[1] > '26':
            dp[1] = 1
        elif s[0] + s[1] == '10' or s[0] + s[1] == '20':
            dp[1] = 1
        else:
            dp[1] = 2
        for i in range(2, n):
            if s[i] == '0' and s[i - 1] + s[i] > '27':
                dp[i] = dp[i - 2] + 1
            else:
                dp[i] = dp[i - 2] + 2
        return dp[-1]


solution = Solution()
print(solution.numDecodings('100'))
