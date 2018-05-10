class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        w, h = len(matrix[0]) + 1, len(matrix) + 1
        dp = [[0] * w for _ in range(h)]
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i - 1][j - 1] is 1 and matrix[i - 1][j] is 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = 0
        print(dp)
        print(dp[-1][-1])
        return dp[-1][-1]


solution = Solution()
solution.maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
])
