class Solution:
    def minimumTotal(self, triangle):
        """
        题目:三角形最小路径和
        解法:动态规划
        从倒数第二行开始,
        倒数第二行加上倒数第一行 [i][j+1],[i][j] 中最小的一个
        倒数第三行加上倒数第二行累加的
        :type triangle: List[List[int]]
        :rtype: int
        """
        h = len(triangle) - 2
        for i in range(h, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j + 1], triangle[i + 1][j])
        return triangle[0][0]


solution = Solution()
print(solution.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
