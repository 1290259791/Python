class Solution:
    def minimumTotal(self, triangle):
        """
        题目:三角形最小路径和
        解法:动态规划
        创建一个一维数组
        将一维数组赋值为倒数第一行
        一维数组更新为,倒数第二行加上倒数第一行 j+1,j 中最小的一个
        依次叠加
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1):
                if i == n-1:
                    dp[j] = triangle[i][j]
                else:
                    dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]