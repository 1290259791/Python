class Solution:
    def minPathSum(self, grid):
        """
        从左上循环到右下
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        height = len(grid)  # 宽
        width = len(grid[0])    # 高
        for m in range(1, width):   # 将第一行宽求出来,防止数组溢出
            grid[0][m] += grid[0][m-1]
        for n in range(1, height):
            grid[n][0] += grid[n-1][0]
        for m in range(1, height):
            for n in range(1, width):
                grid[m][n] += min(grid[m][n-1], grid[m-1][n])   # 将最短的路径叠加
        return grid[-1][-1]


solution = Solution()
print(solution.minPathSum([[1,2,5],[3,2,1]]))