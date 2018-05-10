class Solution:

    def longestPalindrome(self, s):
        """
        题目:最长回文字符串子序列
        解法:动态规划
        s[i,j] 是回文 s[i+1,j-1]也是回文,分解为子问题
        状态转移方程:
        1. p[i,j]=p[i+1,j-1]+2 if s[i]==s[j]
        2. p[i,j]=0 if s[i]!=s[j]
        :type s: str
        :rtype: str
        """
        n = len(s)
        left = 0    # 记录最长子串开始位置
        leng = 0    # 记录长度
        result = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            result[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[j] == s[i]:
                    result[i][j] = result[i + 1][j - 1] + 2
                else:
                    result[i][j] = max(result[i + 1][j], result[i][j - 1])
                if leng < result[i][j]:

                    leng = result[i][j]
                    left = i
        print(result)
        print(result[0][n-1])
        result = result[0][n-1]
        return s[left:left + result]



solutino = Solution()
print(solutino.longestPalindrome("BBABCBCAB"))
