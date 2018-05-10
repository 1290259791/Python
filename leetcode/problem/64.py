class Solution:
    def minPathSum(self, grid):
        """
        题目:最小路径和
        解法:动态规划
        从左上开始向右下
        :type grid: List[List[int]]
        :rtype: int
        """
        width = grid[0].__len__()
        high = grid.__len__()
        result = [[0 for i in range(width)] for i in range(high)]
        sum = 0
        for i in range(width):
            sum += grid[0][i]
            result[0][i] = sum
        sum = 0
        for j in range(high):
            sum += grid[j][0]
            result[j][0] = sum

        for i in range(1, width):
            for j in range(1, high):
                result[j][i] = min(result[j-1][i], result[j][i-1]) + grid[j][i]
        return result[high-1][width-1]

solution = Solution()
print(solution.minPathSum([[1,2,5],[3,2,1]]))
