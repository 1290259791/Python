class Solution:
    def uniquePaths(self, m, n):
        """
        题目:不同路径
        解法:动态规划
        将第一行和第一列的路径方法为1
        依次从左向右累加方法.
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[0] * m for j in range(n)]
        print(result)
        # 第一行,只有一种走法,从左边来
        for i in range(m):
            result[0][i] = 1
        # 第一列
        for j in range(n):
            result[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]

solution = Solution()
print(solution.uniquePaths(7,3))



