class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        题目:不同路径的走法
        解法:动态规划
        注意:
        当[0][0]就不能走的时候,直接返回0
        其余当遇到数组中为1的时候,这个位置的方法为0
        创造的数组,多一行多一列
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width = len(obstacleGrid[0])
        height = len(obstacleGrid)
        if obstacleGrid[0][0]:  # 判断第一个就不能走
            return 0

        dp = [[0] * (width + 1) for i in range(height + 1)]
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if i == 1 and j == 1:   # 起始位置方法为1
                    dp[i][j] = 1
                else:
                    if obstacleGrid[i - 1][j - 1] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


solution = Solution()
print(solution.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
